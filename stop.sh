#!/bin/bash
# Swing Trade Analyzer - Stop Script
# Usage: ./stop.sh [backend|frontend|all]

stop_backend() {
    echo "Stopping backend..."
    pkill -f "python backend.py" 2>/dev/null && echo "Backend stopped" || echo "Backend not running"
}

stop_frontend() {
    echo "Stopping frontend..."
    pkill -f "react-scripts start" 2>/dev/null && echo "Frontend stopped" || echo "Frontend not running"
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
