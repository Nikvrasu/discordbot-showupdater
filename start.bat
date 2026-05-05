@echo off

echo Starting Docker Postgres...
docker start showtracker-db

echo Starting FastAPI...
start cmd /k "cd /d %~dp0 && venv\Scripts\activate && uvicorn api.main:app --reload"

echo Starting React frontend...
start cmd /k "cd /d %~dp0frontend && npm run dev"

echo All services started.