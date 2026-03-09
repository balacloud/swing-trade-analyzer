#!/bin/bash
# Swing Trade Analyzer - Start Script
# Usage: ./start.sh [backend|frontend|all]

PROJECT_DIR="/Users/balajik/projects/swing-trade-analyzer"

kill_port() {
    local port=$1
    local pids
    pids=$(lsof -ti:"$port" 2>/dev/null)
    if [ -n "$pids" ]; then
        echo "  Port $port in use — killing existing process(es)..."
        echo "$pids" | xargs kill -9 2>/dev/null
        sleep 1
    fi
}

start_backend() {
    echo "Starting backend..."
    pkill -f "python backend.py" 2>/dev/null
    kill_port 5001
    cd "$PROJECT_DIR/backend"
    source venv/bin/activate
    python backend.py &
    echo "Backend started (PID: $!)"
}

start_frontend() {
    echo "Starting frontend..."
    pkill -f "react-scripts start" 2>/dev/null
    kill_port 3000
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
