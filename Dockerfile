# Ubuntu base image
FROM ubuntu:18.04

# Set env variable
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    python3-dev \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Clone Github repo
RUN git clone https://github.com/jackykang061233/youtube_summary.git /app

# Install Cython
RUN pip3 install Cython

# Set the working directory to the app directory
WORKDIR /app

# Install Python dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Run file
CMD ["python3", "main.py"]
