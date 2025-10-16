#!/usr/bin/env python3
"""
Verification script to check TRM setup
"""
import sys
import os

def check_python():
    """Check Python version"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python version {version.major}.{version.minor} (need 3.10+)")
        return False

def check_torch():
    """Check PyTorch installation"""
    try:
        import torch
        print(f"✓ PyTorch {torch.__version__}")
        return True
    except ImportError:
        print("✗ PyTorch not installed")
        return False

def check_numpy():
    """Check NumPy version"""
    try:
        import numpy as np
        version = np.__version__
        major = int(version.split('.')[0])
        if major < 2:
            print(f"✓ NumPy {version}")
            return True
        else:
            print(f"⚠ NumPy {version} (should be 1.x)")
            return False
    except ImportError:
        print("✗ NumPy not installed")
        return False

def check_fastapi():
    """Check FastAPI installation"""
    try:
        import fastapi
        print(f"✓ FastAPI {fastapi.__version__}")
        return True
    except ImportError:
        print("✗ FastAPI not installed")
        return False

def check_model():
    """Check if TRM model can be loaded"""
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'TinyRecursiveModels'))
        from models.recursive_reasoning.trm import TinyRecursiveReasoningModel_ACTV1
        print("✓ TRM model imports successfully")
        return True
    except Exception as e:
        print(f"✗ TRM model import failed: {e}")
        return False

def check_inference():
    """Check inference module"""
    try:
        from inference import TRMInference
        print("✓ Inference module loads")
        return True
    except Exception as e:
        print(f"✗ Inference module failed: {e}")
        return False

def check_app():
    """Check FastAPI app"""
    try:
        from app import app
        print("✓ FastAPI app loads")
        return True
    except Exception as e:
        print(f"✗ FastAPI app failed: {e}")
        return False

def check_dataset():
    """Check ARC-AGI dataset"""
    try:
        path = os.path.join(
            os.path.dirname(__file__),
            'TinyRecursiveModels/kaggle/combined/arc-agi_evaluation_challenges.json'
        )
        if os.path.exists(path):
            import json
            with open(path) as f:
                data = json.load(f)
            print(f"✓ ARC-AGI dataset ({len(data)} tasks)")
            return True
        else:
            print("✗ ARC-AGI dataset not found")
            return False
    except Exception as e:
        print(f"✗ Dataset check failed: {e}")
        return False

def main():
    print("=" * 50)
    print("TRM Setup Verification")
    print("=" * 50)
    print()
    
    checks = [
        ("Python Version", check_python),
        ("PyTorch", check_torch),
        ("NumPy", check_numpy),
        ("FastAPI", check_fastapi),
        ("TRM Model", check_model),
        ("Inference Module", check_inference),
        ("FastAPI App", check_app),
        ("ARC-AGI Dataset", check_dataset),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\nChecking {name}...")
        result = check_func()
        results.append(result)
    
    print()
    print("=" * 50)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✅ All checks passed ({passed}/{total})")
        print()
        print("Setup is complete! Start the server with:")
        print("  ./start_server.sh")
        print()
        print("Or:")
        print("  source venv/bin/activate")
        print("  uvicorn app:app --port 8000")
        return 0
    else:
        print(f"⚠️  {passed}/{total} checks passed")
        print()
        print("Please review the failed checks above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

