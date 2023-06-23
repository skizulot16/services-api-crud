# Services API CRUD

This project provides APIs for performing CRUD operations on a services database. It includes login authentication, retrieving all services, adding a new service, and performing other CRUD operations using APIView in Django.

## APIs Provided

### Login Authentication

**Endpoint:** `/api/v1/login/`

- **Method:** `POST`
- **Description:** Authenticates a user.
- **Request Body:**
  - `username`: The username of the user.
  - `password`: The password of the user.
- **Response:**
  - `token`: The access token generated for the authenticated user.
- **Status Codes:**
  - `200 OK`: Successful authentication and token generation.
  - `401 Unauthorized`: Invalid credentials provided.

### Get All Services

**Endpoint:** `/api/v1/services/`

- **Method:** `GET`
- **Description:** Retrieves all services from the database.
- **Response:**
  - List of services with their details.
- **Status Code:**
  - `200 OK`: Successful retrieval of services.

### Add Service

**Endpoint:** `/api/v1/servicedetails/`

- **Method:** `POST`
- **Description:** Adds a new service to the database.
- **Request Body:**
  - `name`: The name of the service.
  - `time`: The time duration of the service.
  - `description`: The description of the service.
  - `price`: The price of the service.
  - `discount`: The discount applied to the service (optional).
- **Response:**
  - Details of the added service.
- **Status Codes:**
  - `201 Created`: Successful addition of the service.
  - `400 Bad Request`: Invalid data provided.

### Update Service

**Endpoint:** `/api/v1/servicedetails/{id}/`

- **Method:** `PUT`
- **Description:** Updates an existing service in the database.
- **Request Body:**
  - `name`: The updated name of the service.
  - `time`: The updated time duration of the service.
  - `description`: The updated description of the service.
  - `price`: The updated price of the service.
  - `discount`: The updated discount applied to the service.
- **Response:**
  - Details of the updated service.
- **Status Codes:**
  - `200 OK`: Successful update of the service.
  - `400 Bad Request`: Invalid data provided.
  - `404 Not Found`: Service with the specified ID not found.

### Delete Service

**Endpoint:** `/api/v1/servicedetails/{id}/`

- **Method:** `DELETE`
- **Description:** Deletes an existing service from the database.
- **Response:**
  - No content.
- **Status Codes:**
  - `204 No Content`: Successful deletion of the service.
  - `404 Not Found`: Service with the specified ID not found.

## Technologies Used

- Django
- Django REST Framework

Feel free to explore the APIs and perform CRUD operations on the services database.

