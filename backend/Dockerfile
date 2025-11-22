FROM python:3.11-slim
WORKDIR /app
COPY backend/ ./backend
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy aiosqlite
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
