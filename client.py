import threading
import time
import random
import requests

stop_threads = False

def simulate_client(client_id, server_url):
    global stop_threads
    while not stop_threads:
        # Generate a random client identifier
        random_client_id = random.randint(1, client_id)
        # Send HTTP request to the server
        response = requests.get(f"{server_url}/?clientId={random_client_id}")
        print(f"Client {random_client_id}: Server responded with status code {response.status_code}")
        # Wait for a random time before sending the next request
        time.sleep(random.uniform(0.5, 2.0))

def main():
    global stop_threads
    server_url = "http://127.0.0.1:5000"
    client_count = int(input("Enter the number of HTTP clients to simulate: "))

    # Create threads for each client
    threads = []
    for i in range(client_count):
        thread = threading.Thread(target=simulate_client, args=(client_count, server_url))
        thread.start()
        threads.append(thread)

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        stop_threads = True
        for thread in threads:
            thread.join()
        print("all threads joined")

if __name__ == "__main__":
    main()
