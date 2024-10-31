## University Residence Management API

### Project Description

This capstone project tasks students with designing and developing a RESTful API for managing a university's residence system. This system will enable students and administrators to interact with various aspects of residence life, such as:

* Room applications and assignments
* Maintenance requests and tracking
* Event announcements and management
* Resident communication and feedback
* Administrative oversight and reporting

The API will be built using Django REST Framework, leveraging advanced Python concepts and techniques.

### [Stage-1: Foundation and Planning ](https://github.com/ALU-BSE/Summative-Project-UniNest-API/blob/stage-1/README.md) 

1. **Project Setup:**
   * Create a new Django project in this repository (no redundant folders ) and install Django REST Framework.
   * Set up a virtual environment to manage project dependencies.
   * Create essential models for entities like `Resident`, `Room`, `Building`, and `MaintenanceRequest`.
   * Implement basic serializers and views for CRUD operations on these models.

2. **API Design and Documentation:**
   * Design a well-structured API, outlining endpoints and their functionalities.
   * Document the API comprehensively using Swagger or Redoc, including clear descriptions, request/response examples, and error handling guidelines.

3. **Asynchronous Programming Exploration:**
   * Research and identify potential API endpoints that could benefit from asynchronous execution (e.g., long-running tasks, background jobs).
   * Provide a written explanation of your findings, justifying your choices for potential asynchronous implementation.

### [Stage-2: Enhanced Functionality](https://github.com/ALU-BSE/Summative-Project-UniNest-API/blob/stage-2/README.md) 

1. **Authentication and Authorization:**

*  Implement basic authentication (username/password) using Django's built-in authentication system.
*  Implement session authentication for persistent logins.
*  Design and implement a basic authorization scheme to control access to API endpoints based on user roles (e.g., student, administrator).

2. **Pagination and Filtering:**

*  Implement pagination for endpoints that return large datasets (e.g., list of all residents).
*  Implement filtering capabilities to allow users to refine API requests based on specific criteria.

3. **Caching:**

*  Implement caching for frequently accessed read-only data to improve API performance.
*  Use Django's cache framework or a suitable third-party library.

### [Stage-3: Advanced Features and Security](https://github.com/ALU-BSE/Summative-Project-UniNest-API/blob/stage-3/README.md) 

1. **Personal Data Handling:**
   * Review and ensure the API adheres to best practices for handling personal data.
   * Implement appropriate data encryption and anonymization where necessary.
   * Address common security concerns related to personal data.

2. **User Authentication Service:**
   * Improve the authentication system for the API to use JSON Web Tokens.
   * Enhance the authentication system using Django OAuth Toolkit or a similar library.
   * Explore integrating with external authentication providers (e.g., Google, Facebook).

3. **Error Handling and Logging:**
   * Implement comprehensive error handling for all API requests.
   * Provide clear and informative error messages to users.
   * Set up proper logging to capture errors and exceptions for debugging and monitoring.

### [Stage-4: Testing and Refinement](https://github.com/ALU-BSE/Summative-Project-UniNest-API/blob/stage-4/README.md) 

1. **Unit Tests and Integration Tests:**
   * Write unit tests to verify the functionality of individual components (models, views, serializers).
   * Write integration tests to ensure seamless interaction between different parts of the API.
   * Use Python's `unittest` module or a similar testing framework.

2. **Deployment (Optional):**
   * If time and resources permit, deploy the API to a production-like environment.
   * Consider using a cloud platform (e.g., Heroku, AWS) or a local server setup.

3. **Documentation and Presentation:**
   * Finalize API documentation (Swagger) and ensure it's comprehensive and up-to-date
   * Prepare a presentation or demonstration to showcase the project, highlighting the challenges faced and the solutions implemented

## API Documentation Structure

### 1. **Introduction**
   - **Overview**: Briefly describe the API’s purpose and functionalities.
   - **Base URL**: Provide the base URL for the API (e.g., `https://api.universityresidence.com/v1`).
   - **Authentication**: Outline the authentication method used (e.g., JWT, OAuth).

### 2. **Authentication**
   - **Login Endpoint**:
     - **Method**: POST
     - **Endpoint**: `/auth/login`
     - **Request Body**:
       ```json
       {
         "username": "string",
         "password": "string"
       }
       ```
     - **Responses**:
       - **200 OK**: Successful login
       - **401 Unauthorized**: Invalid credentials

### 3. **Endpoints Overview**
Provide a list of available endpoints, grouped by resource:

#### 3.1. **Residents**
- **Create Resident**
  - **Method**: POST
  - **Endpoint**: `/residents/`
  - **Request Body**:
    ```json
    {
      "name": "string",
      "email": "string",
      "phone": "string",
      "room": "room_id"
    }
    ```
  - **Responses**:
    - **201 Created**: Resident created successfully
    - **400 Bad Request**: Validation errors

- **Retrieve Resident**
  - **Method**: GET
  - **Endpoint**: `/residents/{id}/`
  - **Responses**:
    - **200 OK**: Resident details
    - **404 Not Found**: Resident not found

- **Update Resident**
  - **Method**: PUT
  - **Endpoint**: `/residents/{id}/`
  - **Request Body**:
    ```json
    {
      "name": "string",
      "email": "string",
      "phone": "string",
      "room": "room_id"
    }
    ```
  - **Responses**:
    - **200 OK**: Resident updated successfully
    - **400 Bad Request**: Validation errors
    - **404 Not Found**: Resident not found

- **Delete Resident**
  - **Method**: DELETE
  - **Endpoint**: `/residents/{id}/`
  - **Responses**:
    - **204 No Content**: Successfully deleted
    - **404 Not Found**: Resident not found

#### 3.2. **Rooms**
- **List Rooms**
  - **Method**: GET
  - **Endpoint**: `/rooms/`
  - **Query Parameters**: `building`, `capacity`
  - **Responses**:
    - **200 OK**: List of rooms

- **Create Room**
  - **Method**: POST
  - **Endpoint**: `/rooms/`
  - **Request Body**:
    ```json
    {
      "room_number": "string",
      "capacity": "integer",
      "building": "building_id"
    }
    ```
  - **Responses**:
    - **201 Created**: Room created successfully

#### 3.3. **Maintenance Requests**
- **Create Maintenance Request**
  - **Method**: POST
  - **Endpoint**: `/maintenance_requests/`
  - **Request Body**:
    ```json
    {
      "description": "string",
      "resident": "resident_id",
      "status": "string"
    }
    ```
  - **Responses**:
    - **201 Created**: Maintenance request created successfully

- **Get Maintenance Request**
  - **Method**: GET
  - **Endpoint**: `/maintenance_requests/{id}/`
  - **Responses**:
    - **200 OK**: Maintenance request details

### 4. **Error Handling**
Document common error responses:
- **400 Bad Request**: Invalid request parameters.
- **401 Unauthorized**: Authentication required or failed.
- **404 Not Found**: Resource not found.
- **500 Internal Server Error**: Unexpected server error.

### 5. **Rate Limiting**
- Mention any rate limiting policies (e.g., maximum requests per minute).

### 6. **Examples**
Provide example requests and responses for key endpoints. For instance:
#### Example of Creating a Resident
**Request**:
```http
POST /residents/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+123456789",
  "room": "101"
}
```
**Response**:
```http
201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+123456789",
  "room": "101"
}
```

### 7. **Versioning**
Indicate the versioning strategy (e.g., versioning via URL path like `/v1/`).

### 8. **Additional Resources**
- Links to further documentation or user guides.
- Contact information for support or inquiries.

---

## Tools for Documentation
Consider using tools like:
- **Swagger/OpenAPI**: For interactive documentation.
- **Redoc**: To create beautiful documentation from OpenAPI specifications.
- **Postman**: To create and share API documentation easily.

### Example of Swagger/OpenAPI Configuration
```yaml
openapi: 3.0.0
info:
  title: University Residence Management API
  version: 1.0.0
paths:
  /residents/:
    post:
      summary: Create a new resident
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                email:
                  type: string
                phone:
                  type: string
                room:
                  type: integer
      responses:
        '201':
          description: Resident created successfully
        '400':
          description: Invalid input
```
