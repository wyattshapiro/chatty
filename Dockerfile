# Use the official Python image as the base
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY ./chat.py /app/

# Copy the requirements and install the dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Set command for start up
CMD ["python3", "chat.py"]

