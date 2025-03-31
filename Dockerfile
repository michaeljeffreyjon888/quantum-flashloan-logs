FROM public.ecr.aws/docker/library/python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt || true
CMD ["python", "quantum_live_arbitrage.py"]


