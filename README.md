# HTTP Request Simulation and Rate Limiting Project

This project consists of three main components designed to simulate HTTP requests, enforce rate limiting on a server, and conduct structured load testing. The components are as follows:

## 1. Server (`server.py`)

This script sets up a Flask web server to listen for incoming HTTP requests. It implements rate limiting logic, allowing no more than 5 requests per client within a 5-second window.

### Features
- **Rate Limiting**: Tracks the number of requests per client and enforces a limit of 5 requests every 5 seconds.
- **Thread Safety**: Uses a thread-safe mechanism for tracking requests.
- **Request Handling**: Returns HTTP 200 for valid requests and HTTP 503 when the rate limit is exceeded.

### Usage
Run the server using the command:
```bash python server.py ```bash


## 2. Client (`client.py`)

This script simulates multiple HTTP clients sending requests to the server. Each client runs on a separate thread and sends requests with a random client identifier.

### Features
- **Multi-threading**: Simulates multiple clients using threading.
- **Randomized Request Simulation**: Each client sends requests at random intervals.
- **Graceful Shutdown**: The script can be terminated with a key press, ensuring all threads are gracefully closed.

### Usage
Run the client simulation with the command:
```bash
python client.py
```bash


Enter the desired number of clients to simulate when prompted.

## 3. Tester (`tester.py`)

The `tester.py` script is used for structured load testing of the server. It varies the number of clients, request rates, and test durations, then logs the results.

### Features
- **Automated Load Testing**: Randomizes the number of clients and request rates for each test iteration.
- **Logging**: Records the number of requests, response codes, and crashes, then writes a summary to `test_summary.txt`.
- **Continuous Testing**: Runs tests in a loop with varying parameters.

### Usage
Run the load testing with the command:
```bash
python tester.py
```bash


The script will run indefinitely until manually stopped. Check `test_summary.txt` for test results.

## General Information

- **Language**: Python
- **Libraries**: Flask (for the server), Requests (for HTTP requests)
- **Setup**: Ensure Python is installed along with Flask and Requests libraries.
- **Repository Structure**:
  - `server.py`: The Flask server script.
  - `client.py`: The client simulation script.
  - `tester.py`: The load testing script.
  - `README.md`: This documentation file.

