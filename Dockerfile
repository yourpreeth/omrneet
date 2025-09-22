# Use official Python image
FROM python:3.9-slim

WORKDIR /app
COPY backend/ ./backend/
RUN pip install fastapi uvicorn

EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
