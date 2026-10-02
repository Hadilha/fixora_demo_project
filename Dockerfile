# Intentionally weak Docker configuration for FIXORA demo only.
FROM python:3.8-slim

WORKDIR /app

ENV DEMO_ADMIN_PASSWORD="DEMO_ONLY_PASSWORD"

COPY requirements-runtime.txt .
RUN pip install --no-cache-dir -r requirements-runtime.txt

COPY . .

# Intentionally no non-root USER directive.
EXPOSE 5000
CMD ["python", "src/app.py"]
