# Quick Start Guide

Get the TRM demo running in 3 simple steps!

## Step 1: Start the Server

```bash
cd /Users/wesleybeckner/code/trm_model
./start_server.sh
```

Or manually:
```bash
source venv/bin/activate
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Step 2: Open Your Browser

Navigate to: **http://localhost:8000**

## Step 3: Try It Out!

1. Select a task from the dropdown menu
2. Click "Solve Puzzle"
3. Watch the recursive reasoning in action!

## What You'll See

- **Model Info**: 7M parameters, device, configuration
- **Training Examples**: Demonstrations of the puzzle rule
- **Test Inputs**: Puzzles to solve
- **Predictions**: Model's solutions (random for now, until trained)

## API Testing

Test the API directly with curl:

```bash
# Get model info
curl http://localhost:8000/api/model-info

# Get sample tasks
curl http://localhost:8000/api/examples

# Health check
curl http://localhost:8000/health
```

## Next Steps

- **Train a model**: See README.md for training instructions
- **Load weights**: Set `TRM_CHECKPOINT_PATH` environment variable
- **Explore API**: Visit http://localhost:8000/docs for interactive API docs

## Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

## Need Help?

- Check README.md for detailed documentation
- Review the troubleshooting section
- Ensure all dependencies are installed: `pip list`

