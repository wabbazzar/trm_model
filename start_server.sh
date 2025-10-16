#!/bin/bash
# Startup script for TRM Inference API

echo "🚀 Starting TRM Inference API..."
echo ""

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✓ Virtual environment activated"
else
    echo "✗ Virtual environment not found. Please run setup first."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $PYTHON_VERSION"

# Check PyTorch
TORCH_VERSION=$(python -c "import torch; print(torch.__version__)" 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "✓ PyTorch version: $TORCH_VERSION"
else
    echo "✗ PyTorch not found"
    exit 1
fi

echo ""
echo "📊 Model Configuration:"
echo "   - Parameters: ~7M"
echo "   - Device: CPU (or MPS if available)"
echo "   - Status: Random initialization (no checkpoint)"
echo ""
echo "⚠️  Note: Model needs training for meaningful predictions"
echo ""

# Set environment variables (optional)
# export TRM_CHECKPOINT_PATH=/path/to/checkpoint.pt
# export USE_MPS=true  # Set to true to use MPS on M-series Macs

# Start the server
echo "🌐 Starting server at http://localhost:8000"
echo "   Press Ctrl+C to stop"
echo ""

uvicorn app:app --host 0.0.0.0 --port 8000 --reload

