FROM python:3.9

WORKDIR /app

# Install Jupyter
#RUN pip install jupyter
RUN pip install jupyterlab

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set the OpenAI API key as an environment variable
#ENV OPENAI_API_KEY="API_KEY"

EXPOSE 8888

# JupyterLab server is started on port 8888 and the browser is disabled to allow access from outside the container
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
