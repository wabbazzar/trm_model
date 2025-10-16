"""
FastAPI application for TRM inference
Serves the Tiny Recursive Model for ARC-AGI puzzle solving
"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import os
import json
from pathlib import Path

from inference import TRMInference, load_arc_task, get_sample_tasks


# Initialize FastAPI app
app = FastAPI(
    title="TRM Inference API",
    description="Tiny Recursive Model for ARC-AGI puzzle solving",
    version="1.0.0"
)

# Global model instance
model: Optional[TRMInference] = None


# Pydantic models for API
class GridInput(BaseModel):
    """2D grid input"""
    grid: List[List[int]] = Field(..., description="2D grid with integer values (0-9)")


class TrainExample(BaseModel):
    """Training example with input and output grids"""
    input: List[List[int]]
    output: List[List[int]]


class TestInput(BaseModel):
    """Test input (only input grid, no output)"""
    input: List[List[int]]


class ARCTask(BaseModel):
    """Complete ARC-AGI task"""
    train: List[TrainExample] = Field(..., description="Training examples showing the rule")
    test: List[TestInput] = Field(..., description="Test inputs to solve")


class SolveRequest(BaseModel):
    """Request to solve a puzzle"""
    task: ARCTask
    max_steps: int = Field(16, ge=1, le=32, description="Maximum recursive reasoning steps")
    show_iterations: bool = Field(False, description="Return intermediate predictions")


class SolveResponse(BaseModel):
    """Response with predictions"""
    predictions: List[Dict[str, Any]]
    message: str


class ModelInfo(BaseModel):
    """Model information"""
    name: str
    parameters: int
    config: Dict[str, Any]
    checkpoint_loaded: bool
    device: str


@app.on_event("startup")
async def startup_event():
    """Initialize model on startup"""
    global model
    try:
        checkpoint_path = os.environ.get("TRM_CHECKPOINT_PATH")
        device = "mps" if os.environ.get("USE_MPS", "false").lower() == "true" else "cpu"
        model = TRMInference(checkpoint_path=checkpoint_path, device=device)
        print("✓ Model loaded successfully")
    except Exception as e:
        print(f"✗ Error loading model: {e}")
        raise


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main HTML interface"""
    html_path = Path(__file__).parent / "static" / "index.html"
    if html_path.exists():
        return HTMLResponse(content=html_path.read_text())
    return HTMLResponse(content="<h1>TRM Inference API</h1><p>Web interface not found. Use /docs for API documentation.</p>")


@app.get("/api/model-info", response_model=ModelInfo)
async def get_model_info():
    """Get information about the loaded model"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    # Count parameters
    total_params = sum(p.numel() for p in model.model.parameters())
    
    return ModelInfo(
        name="Tiny Recursive Model (TRM)",
        parameters=total_params,
        config={
            "H_cycles": model.config.H_cycles,
            "L_cycles": model.config.L_cycles,
            "L_layers": model.config.L_layers,
            "hidden_size": model.config.hidden_size,
            "halt_max_steps": model.config.halt_max_steps,
        },
        checkpoint_loaded=False,  # We're using random init for now
        device=model.device
    )


@app.post("/api/solve", response_model=SolveResponse)
async def solve_puzzle(request: SolveRequest):
    """
    Solve an ARC-AGI puzzle using the TRM model
    
    The model will recursively reason about the task and provide predictions.
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Convert Pydantic models to dict
        task_dict = {
            'train': [{'input': ex.input, 'output': ex.output} for ex in request.task.train],
            'test': [{'input': inp.input} for inp in request.task.test]
        }
        
        # Run inference
        results = model.solve(
            task_dict,
            max_steps=request.max_steps,
            show_iterations=request.show_iterations
        )
        
        return SolveResponse(
            predictions=results['predictions'],
            message="✓ Inference completed successfully"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")


@app.get("/api/examples")
async def get_examples():
    """Get sample ARC-AGI tasks from the evaluation set"""
    try:
        samples = get_sample_tasks(num_tasks=5)
        examples = []
        
        for task_id, task in samples:
            examples.append({
                'id': task_id,
                'name': f"ARC-AGI Task {task_id}",
                'task': task,
                'num_train': len(task['train']),
                'num_test': len(task['test'])
            })
        
        return {"examples": examples}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading examples: {str(e)}")


@app.get("/api/task/{task_id}")
async def get_task(task_id: str):
    """Get a specific ARC-AGI task by ID"""
    try:
        task = load_arc_task(task_id)
        return {
            'id': task_id,
            'task': task
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading task: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


# Mount static files
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

