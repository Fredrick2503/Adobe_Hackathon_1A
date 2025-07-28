FROM --platform=linux/amd64 python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirement.txt .

# Copy packages directory (should contain all wheel files)
#COPY packages/ /packages/

# Install packages from local wheelhouse

RUN pip install -r requirement.txt
# Copy application code
COPY . .

RUN mkdir -p input output

CMD ["python", "main.py"]