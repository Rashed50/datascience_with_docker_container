#!/bin/bash

# Stop and remove existing container if it exists
docker rm -f pandas-container2 2>/dev/null

# Build the image
docker build -t pandas-image2 .

# Run the container
docker run --name pandas-container2 pandas-image2

# Copy output from container to host
docker cp pandas-container2:/app/output.csv .

# Optional: remove container after run
docker rm pandas-container2