FROM python:3.10-slim

# Install dependencies
RUN pip install --upgrade pip

# Set work directory
WORKDIR /app

# Copy files
COPY . .

# Install Python packages
RUN pip install -r requirements.txt

# Expose default Streamlit port
EXPOSE 8501

# Run app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
