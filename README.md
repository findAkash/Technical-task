---

# Microservice for Image Segmentation

This microservice provides APIs for image segmentation using FastAPI.

## Code Structure

The microservice is organized into three main files:

1. **main.py**: Responsible for initiating and running the microservice.
2. **api.py**: Contains all the API endpoint definitions and related logic.
3. **config.py**: Stores configuration settings for the microservice.

## Testing the Microservice

### Without Docker

1. **Create a Virtual Environment and Activate It**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install the Requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Service**
   ```bash
   fastapi dev  # Development environment
   fastapi run  # Production environment
   ```

### With Docker

1. **Install Docker** (if not installed already)  
   Refer to the official Docker documentation for installation instructions: [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)

2. **Run the Service through Docker**
   ```bash
   docker-compose up  # Build and run the container (initial run)
   docker-compose up -d  # Run the container in detached mode (background)
   docker-compose up --build  # Rebuild the container with changes
   docker-compose down  # Stop the service
   ```

## Testing API Endpoints

Once the service is running, you can test the API endpoints using tools like cURL, Postman, or any HTTP client.

### FastAPI Docs
You can also use FastAPI's built-in documentation tool to test the endpoints.  
Access the documentation at: [http://localhost:8000/docs](http://localhost:8000/docs)

#### Endpoint for Image Segmentation
- **POST**: `/api/segment-image`

Add images that need to be processed, and multiple images can be added and tested simultaneously.  
The processed images will be stored in the `generated` folder in the project directory.

---
