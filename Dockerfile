# Use lightweight Python base image
FROM python:3.11-slim-bookworm

# Set environment variables
ENV OLLAMA_HOST="host.docker.internal:11434"
ENV JUPYTER_PORT=8888
ENV NB_USER=jovyan
ENV NB_UID=1000
ENV HOME=/home/$NB_USER

# Create user with sudo privileges
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    curl git build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create work directory
RUN mkdir /work && chown $NB_USER:$NB_USER /work
WORKDIR /work

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter Lab
RUN pip install jupyterlab

# Copy project files
COPY --chown=$NB_USER:$NB_USER . .

# Expose Jupyter port
EXPOSE $JUPYTER_PORT

# Switch to user
USER $NB_USER

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s \
    CMD curl -f http://localhost:$JUPYTER_PORT || exit 1

# Start Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]