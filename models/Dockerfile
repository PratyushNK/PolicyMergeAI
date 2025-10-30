# Use official PyTorch CUDA image
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Set working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optional: Install Jupyter if you want notebook support
# RUN pip install notebook jupyterlab

# Copy your code into the container
COPY . /app

# Set default command
CMD ["bash"]
