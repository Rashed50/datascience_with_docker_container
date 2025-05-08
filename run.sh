#!/bin/bash

# Stop and remove existing container if it exists
docker rm -f pandas-container 2>/dev/null

# Build the image
docker build -t pandas-doc-img .

# Run the container
docker run --name pandas-container pandas-doc-img

# Copy output from container to host
docker cp pandas-container:/app/output.csv .
docker cp pandas-container:/app/plot.png .

# Optional: remove container after run
#docker rm pandas-container