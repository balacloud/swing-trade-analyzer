#!/bin/bash
# Swing Trade Analyzer - Start Script
# Usage: ./start.sh [backend|frontend|all]

PROJECT_DIR="/Users/balajik/projects/swing-trade-analyzer"

start_backend() {
    echo "Starting backend..."
    cd "$PROJECT_DIR/backend"
    source venv/bin/activate
    python backend.py &
    echo "Backend started (PID: $!)"
}

start_frontend() {
    echo "Starting frontend..."
    cd "$PROJECT_DIR/frontend"
    npm start &
    echo "Frontend starting..."
}

case "${1:-all}" in
    backend)
        start_backend
        ;;
    frontend)
        start_frontend
        ;;
    all)
        start_backend
        sleep 2
        start_frontend
        ;;
    *)
        echo "Usage: ./start.sh [backend|frontend|all]"
        exit 1
        ;;
esac

echo "Done. Use ./stop.sh to stop services."
