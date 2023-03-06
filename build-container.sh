# This will start the JupyterLab server inside the Docker container, which can be accessed
# by navigating to http://localhost:8888 in your web browser.

# Build the Docker image
docker build -t openai-demo .

# Run the Docker container
docker run -p 8888:8888 openai-demo
