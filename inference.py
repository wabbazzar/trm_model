"""
Inference module for TRM (Tiny Recursive Model)
Handles model loading and prediction for ARC-AGI tasks
"""
import sys
import os
import torch
import json
from typing import Dict, List, Tuple, Any
import numpy as np

# Add the TinyRecursiveModels to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'TinyRecursiveModels'))

from models.recursive_reasoning.trm import TinyRecursiveReasoningModel_ACTV1
from omegaconf import OmegaConf


class TRMInference:
    """Wrapper for TRM model inference"""
    
    def __init__(self, checkpoint_path: str = None, device: str = "cpu"):
        """
        Initialize TRM model for inference
        
        Args:
            checkpoint_path: Path to model checkpoint (if None, uses random initialization)
            device: Device to run model on ('cpu', 'mps', or 'cuda')
        """
        self.device = device if torch.backends.mps.is_available() and device == "mps" else "cpu"
        print(f"Using device: {self.device}")
        
        # Load config
        config_path = os.path.join(os.path.dirname(__file__), 
                                   'TinyRecursiveModels/config/arch/trm.yaml')
        self.config = OmegaConf.load(config_path)
        
        # Set model parameters for ARC-AGI
        model_config = {
            'batch_size': 1,
            'seq_len': 900,  # 30x30 grid max
            'puzzle_emb_ndim': self.config.puzzle_emb_ndim,
            'num_puzzle_identifiers': 1000,
            'vocab_size': 11,  # 0-9 colors + padding
            'H_cycles': self.config.H_cycles,
            'L_cycles': self.config.L_cycles,
            'H_layers': self.config.H_layers,
            'L_layers': self.config.L_layers,
            'hidden_size': self.config.hidden_size,
            'expansion': self.config.expansion,
            'num_heads': self.config.num_heads,
            'pos_encodings': self.config.pos_encodings,
            'rms_norm_eps': 1e-5,
            'rope_theta': 10000.0,
            'halt_max_steps': self.config.halt_max_steps,
            'halt_exploration_prob': self.config.halt_exploration_prob,
            'forward_dtype': 'float32',  # Use float32 for CPU/MPS compatibility
            'mlp_t': self.config.mlp_t,
            'puzzle_emb_len': self.config.puzzle_emb_len,
            'no_ACT_continue': self.config.no_ACT_continue,
        }
        
        # Initialize model
        self.model = TinyRecursiveReasoningModel_ACTV1(model_config)
        self.model.eval()
        
        # Load checkpoint if provided
        if checkpoint_path and os.path.exists(checkpoint_path):
            print(f"Loading checkpoint from {checkpoint_path}")
            checkpoint = torch.load(checkpoint_path, map_location=self.device)
            self.model.load_state_dict(checkpoint['model_state_dict'])
        else:
            print("⚠️  Using randomly initialized model (no checkpoint provided)")
            print("   The model will not produce meaningful predictions until trained.")
        
        # Move model to device (keeping in float32 for CPU/MPS)
        self.model = self.model.to(self.device)
        
    def preprocess_grid(self, grid: List[List[int]]) -> torch.Tensor:
        """Convert a 2D grid to tensor format"""
        # Flatten grid
        flat = [cell for row in grid for cell in row]
        return torch.tensor(flat, dtype=torch.int32)
    
    def postprocess_output(self, output: torch.Tensor, height: int, width: int) -> List[List[int]]:
        """Convert model output back to 2D grid"""
        # Get predictions
        preds = output.argmax(dim=-1).cpu().numpy()
        
        # Reshape to grid
        grid = []
        for i in range(height):
            row = preds[i * width:(i + 1) * width].tolist()
            grid.append(row)
        return grid
    
    def solve(self, task: Dict[str, Any], max_steps: int = 16, show_iterations: bool = False) -> Dict[str, Any]:
        """
        Solve an ARC-AGI task
        
        Args:
            task: ARC-AGI task dict with 'train' (demo pairs) and 'test' (test inputs)
            max_steps: Maximum recursive reasoning steps
            show_iterations: If True, return intermediate predictions
            
        Returns:
            Dict with 'predictions' and optionally 'iterations'
        """
        results = {'predictions': []}
        
        # Process each test input
        for test_idx, test_input in enumerate(task['test']):
            input_grid = test_input['input']
            height, width = len(input_grid), len(input_grid[0])
            
            # Prepare input
            input_tensor = self.preprocess_grid(input_grid)
            
            # Pad to seq_len
            seq_len = 900  # 30x30 max
            if len(input_tensor) < seq_len:
                input_tensor = torch.nn.functional.pad(
                    input_tensor, (0, seq_len - len(input_tensor)), value=0
                )
            else:
                input_tensor = input_tensor[:seq_len]
            
            # Create batch
            batch = {
                'inputs': input_tensor.unsqueeze(0).to(self.device),
                'puzzle_identifiers': torch.tensor([[test_idx]], dtype=torch.int32).to(self.device)
            }
            
            # Run inference with recursive steps
            iterations = []
            with torch.no_grad():
                carry = self.model.initial_carry(batch)
                
                for step in range(max_steps):
                    carry, outputs = self.model(carry, batch)
                    
                    if show_iterations:
                        pred_grid = self.postprocess_output(
                            outputs['logits'][0], height, width
                        )
                        iterations.append({
                            'step': step + 1,
                            'prediction': pred_grid
                        })
                    
                    # Check if halted
                    if carry.halted[0]:
                        break
                
                # Final prediction
                final_output = outputs['logits'][0][:height * width]
                final_grid = self.postprocess_output(final_output, height, width)
            
            result = {'prediction': final_grid}
            if show_iterations:
                result['iterations'] = iterations
            results['predictions'].append(result)
        
        return results


def load_arc_task(task_id: str, dataset_path: str = None) -> Dict[str, Any]:
    """
    Load an ARC-AGI task from the evaluation dataset
    
    Args:
        task_id: Task ID (e.g., "007bbfb7")
        dataset_path: Path to ARC-AGI challenges JSON
        
    Returns:
        Task dict with 'train' and 'test'
    """
    if dataset_path is None:
        dataset_path = os.path.join(
            os.path.dirname(__file__),
            'TinyRecursiveModels/kaggle/combined/arc-agi_evaluation_challenges.json'
        )
    
    with open(dataset_path, 'r') as f:
        data = json.load(f)
    
    if task_id not in data:
        raise ValueError(f"Task {task_id} not found in dataset")
    
    return data[task_id]


def get_sample_tasks(num_tasks: int = 5) -> List[Tuple[str, Dict[str, Any]]]:
    """Get sample tasks from the evaluation set"""
    dataset_path = os.path.join(
        os.path.dirname(__file__),
        'TinyRecursiveModels/kaggle/combined/arc-agi_evaluation_challenges.json'
    )
    
    with open(dataset_path, 'r') as f:
        data = json.load(f)
    
    task_ids = list(data.keys())[:num_tasks]
    return [(tid, data[tid]) for tid in task_ids]


if __name__ == "__main__":
    # Test inference
    print("Initializing TRM model...")
    model = TRMInference()
    
    print("\nLoading sample task...")
    task_id, task = get_sample_tasks(1)[0]
    print(f"Task ID: {task_id}")
    print(f"Training examples: {len(task['train'])}")
    print(f"Test inputs: {len(task['test'])}")
    
    print("\nRunning inference...")
    results = model.solve(task, max_steps=8, show_iterations=True)
    
    print("\nResults:")
    for i, result in enumerate(results['predictions']):
        print(f"\nTest {i+1}:")
        print(f"  Prediction shape: {len(result['prediction'])}x{len(result['prediction'][0])}")
        print(f"  Iterations: {len(result.get('iterations', []))}")

