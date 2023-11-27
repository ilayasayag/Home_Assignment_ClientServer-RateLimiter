import threading
import requests
import time
import random


def send_request(client_id, server_url, log, crashed):
    try:
        response = requests.get(f"{server_url}/?clientId={client_id}")
        log.append((client_id, response.status_code, time.time()))
    except requests.exceptions.RequestException:
        crashed.append(client_id)


def simulate_load(num_clients, request_rate, server_url, duration, log, crashed):
    start_time = time.time()
    while time.time() - start_time < duration:
        threads = []
        for i in range(num_clients):
            thread = threading.Thread(target=send_request, args=(i + 1, server_url, log, crashed))
            threads.append(thread)
            thread.start()
            time.sleep(1 / request_rate)
        for thread in threads:
            thread.join()


def write_summary(log, crashed, num_clients, request_rate, duration):
    status_200 = len([entry for entry in log if entry[1] == 200])
    status_503 = len([entry for entry in log if entry[1] == 503])
    crashes = len(crashed)
    summary = (f"For {num_clients} clients, request rate {request_rate} per second, "
               f"and duration {duration} seconds, the system got {len(log)} requests, "
               f"returned {status_200} status code 200, {status_503} status code 503, "
               f"and crashed {crashes} times.\n")

    with open("test_summary.txt", "a") as file:
        file.write(summary)
    print(summary)


def main():
    server_url = "http://127.0.0.1:5000"

    while True:
        num_clients = random.randint(1, 20)
        request_rate = random.randint(1, 10)
        duration = random.randint(1, 5)*60
        print("----------------------------------------------------------------------------------------")
        print(f"simulating {num_clients} clients with request rate of {request_rate} for {duration} min")

        log = []
        crashed = []
        simulate_load(num_clients, request_rate, server_url, duration, log, crashed)
        write_summary(log, crashed, num_clients, request_rate, duration)

        time.sleep(5)  # Short pause before next iteration


if __name__ == "__main__":
    main()
