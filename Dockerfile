# Use official lightweight base image
FROM python:3.10-slim 

# Copy application code there
COPY . /app/

# Set working directory
WORKDIR /app

# Install required dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libportaudio2 \
    portaudio19-dev \
    gcc \
    libc-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Expose the required port
EXPOSE 7860

# Start the code inside the docker container
CMD [ "sh", "-c", "python gradio_app.py" ]