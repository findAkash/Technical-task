FROM python:3.9.0

#set the working directory inside the container
WORKDIR /app

# Install Git
RUN apt-get update && apt-get install -y git

# Install OpenGL libraries
RUN apt-get install -y libgl1-mesa-glx

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Command to run the FastAPI application
CMD ["fasapi", "run"]
