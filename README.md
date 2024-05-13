**Code Structure**

```
The microservice is organized into three main files:

1. main.py
This file is responsible for initiating and running the microservice.

2. api.py
The api.py file contains all the API endpoint definitions and related logic. Each endpoint handles a specific HTTP request and performs the necessary operations.

3. config.py
config.py stores configuration settings for the microservice. These settings include details such as host, port, database connection parameters, and any other environment-specific configurations.
```

**We can test the microservice in two different way**

`Without docker follow these steps`

1. **Create a Virtual Environment and Activate It**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install the Requirements**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the service**
   ```bash
   fastapi dev # (to the service in development environment)
   fastapi run # (to run the service in production environment)
   ```

`Or directly run service through docker`
**Install docker if not installed already**
reference for proper instruction (https://docs.docker.com/engine/install/)

**Run through docker by containerising it**

```bash (need to be in project directory)
docker-compose up #(first it might take time because it will build the contrainer including all the depencies, model)

docker-compose up -d #(to run it in background)

docker-compose up --build #(whenever we make any changes in the code we have to trigger the docker that to build image instead of using old image)

docker-compose down #(to end the service)
```

**Testing**
Once the service is running, we can test the API endpoints using tools like cURL, Postman, or any HTTP client.

The endpoint for testing is (http://localhost:8000/api/segment-image)

We can use fastapi docs to test --- http://localhost:8000/docs#/default/segment_image_api_segment_image_post

Add image that need to be processed, multiple images can be added and tested.

The processed image will be stored in the folder named "generated"  in same project directory.
