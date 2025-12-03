# 1. Base Image: Use a lightweight Linux with Python 3.9 pre-installed
FROM python:3.9-slim

# 2. Work Directory: Create a folder inside the container named '/app'
WORKDIR /app

# 3. Dependencies: Copy local file -> Container filesystem
COPY requirements.txt .

# 4. Install: Run pip inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Code: Copy all other files (app.py) -> Container filesystem
COPY . .

# 6. Command: What to do when the container starts?
CMD ["python", "app.py"]h