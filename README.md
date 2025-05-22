# Example Proxy Service

A FastAPI-based proxy service for handling session management.

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Service

To run the service, use the following command:
```bash
uvicorn proxy:app --reload
```

The service will be available at `http://localhost:8000`

## API Endpoints

- `GET /proxy/session`: Get a session ID from the remote service

## Environment Variables

Create a `.env` file in the project root and add your authentication token:
```
AUTH_TOKEN=your_token_here
``` 