# SandboxCodingAssingment

# PEP Checker

PEP Checker is a full-stack application that allows users to search for Politically Exposed Persons (PEPs) using fuzzy matching. The project is built with FastAPI, React (TypeScript), and Docker.

## Features

- Fuzzy name matching using RapidFuzz
- View detailed PEP information including birth date and the date added to the PEP list
- REST API with automatic documentation via Swagger
- Clean and responsive frontend built with React and TypeScript
- Fully containerized with Docker and Docker Compose

## Tech Stack

**Backend**

- Python
- FastAPI
- SQLite
- SQLAlchemy
- RapidFuzz

**Frontend**

- React
- TypeScript

**DevOps**

- Docker
- Docker Compose

## Getting Started

### Prerequisites

- Docker installed on your machine

### Run the Application

1. Clone the repository

```bash
git clone https://github.com/Madsfredag/SandboxCodingAssignment.git
cd SandboxCodingAssignment
```

2. Start the application

```bash
docker-compose up --build
```

3. Access the app

   Frontend: http://localhost:3000

   API docs (Swagger): http://localhost:8000/docs

## Project Structure

```bash
SandboxCodingAssignment/
├── app/                    # Backend FastAPI app
│   ├── api/                # API routes
│   ├── core/               # App config
│   ├── db/                 # Models and database
│   ├── schemas/            # Pydantic models
│   ├── services/           # Business logic
│   └── main.py             # FastAPI entrypoint
├── pep-checker-frontend/   # React frontend
├── Dockerfile              # Backend Dockerfile
├── docker-compose.yml      # Docker Compose config
├── pep_list.xlsx           # Excel file with PEP data
├── pep.db                  # SQLite database file
├── requirements.txt        # Python dependencies
```

## API Endpoints

### `GET /pep/search?name=...`

Search for Politically Exposed Persons (PEPs) using fuzzy name matching.

- **Query Parameters:**
  - `name` (string): The name to search for (partial or full)
- **Response:**
  - Returns a list of PEPs with:
    - `name`: Full name
    - `score`: Match score (0–100)
    - `_links.self.href`: Link to the detailed view of the matched PEP

---

### `GET /pep/{id}`

Get detailed information for a single PEP by ID.

- **Path Parameters:**
  - `id` (integer): The unique identifier of the PEP
- **Response:**
  - `id`: PEP ID
  - `name`: Full name
  - `birth_date`: Date of birth (YYYY-MM-DD)
  - `added_date`: Date added to the PEP list (YYYY-MM-DD)
  - `_links.self.href`: Self-reference link

---

### `GET /pep/all`

Get a full list of all PEP names in the database.

- **Response:**
  - Array of strings containing PEP full names

## Rate Limiting Options and Benefits

To enhance the robustness and security of the API, rate limiting could be introduced. This helps prevent abuse, ensures fair usage, and protects the backend from overload. Two viable options for implementing rate limiting in this project would be:

### 1. slowapi

slowapi is a rate limiting library designed to work with FastAPI and Starlette applications. It is based on limits, a configurable backend-agnostic rate limiter.

**Benefits:**

- Easy to integrate with FastAPI using decorators or global middleware.
- Can limit requests by IP address, endpoint, or method.
- Supports multiple storage backends (memory, Redis, etc.).
- Works well for development or smaller-scale deployments.

**Improvement for this project:**

Using `slowapi`, the `/pep/search` endpoint could be limited to e.g. 30 requests per minute per user/IP to prevent brute-force scanning of the PEP list. This would improve the reliability of the service and reduce unnecessary load during public usage or demos.

---

### 2. API Gateway

An API Gateway sits in front of the backend services and can enforce policies like rate limiting, authentication, logging, and caching.

**Benefits:**

- Decouples infrastructure-level logic (like rate limits and security) from the application code.
- Centralized control over traffic limits and quotas.
- Suitable for public-facing or production-level APIs.
- Scales well and often integrates with authentication, monitoring, and analytics.

**Improvement for this project:**
Integrating an API Gateway would prepare the application for production use. It would allow flexible rate limits, protect against DoS attacks, and enable features like usage analytics, key-based access control, or geo-restrictions, all without modifying the FastAPI codebase.

## Storage Considerations

The project currently uses **SQLite**, a lightweight, file-based database. It is ideal for local development and small-scale applications due to its simplicity and zero-configuration setup.

For more demanding or production-grade environments, other database systems may be more appropriate:

### PostgreSQL

A powerful, open-source relational database commonly used in web applications.

- **Advantages:**

  - Full SQL support with advanced querying and indexing
  - Highly reliable and scalable
  - Strong community and ecosystem

- **Disadvantages:**
  - Requires more setup (e.g. containerized service or managed cloud instance)
  - Slightly more complex migrations compared to SQLite

### MySQL

Another widely adopted relational database, often used in traditional web stacks.

- **Advantages:**

  - Good performance, especially for read-heavy workloads
  - Easy to deploy in containerized environments
  - Broad hosting support

- **Disadvantages:**
  - Less advanced feature set than PostgreSQL
  - Slightly weaker support for complex queries or constraints

### MongoDB (NoSQL)

A document-based database for storing flexible, schema-less data.

- **Advantages:**

  - Highly flexible for varying data structures
  - Easy to scale horizontally
  - Efficient for rapid development of unstructured data

- **Disadvantages:**
  - Not ideal for relational queries or fuzzy text search
  - Would require changing the schema and data logic

### Summary

For production deployments, **PostgreSQL** is typically the recommended replacement for SQLite due to its robustness, scalability, and compatibility with ORMs like SQLAlchemy.
