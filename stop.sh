#!/bin/bash
# Swing Trade Analyzer - Stop Script
# Usage: ./stop.sh [backend|frontend|all]

kill_port() {
    local port=$1
    local pids
    pids=$(lsof -ti:"$port" 2>/dev/null)
    if [ -n "$pids" ]; then
        echo "$pids" | xargs kill -9 2>/dev/null
    fi
}

stop_backend() {
    echo "Stopping backend..."
    pkill -f "python backend.py" 2>/dev/null
    kill_port 5001
    echo "Backend stopped"
}

stop_frontend() {
    echo "Stopping frontend..."
    pkill -f "react-scripts start" 2>/dev/null
    kill_port 3000
    echo "Frontend stopped"
}

case "${1:-all}" in
    backend)
        stop_backend
        ;;
    frontend)
        stop_frontend
        ;;
    all)
        stop_backend
        stop_frontend
        ;;
    *)
        echo "Usage: ./stop.sh [backend|frontend|all]"
        exit 1
        ;;
esac
