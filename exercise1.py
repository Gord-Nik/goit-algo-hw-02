import string
from queue import Queue
import random
import time

queue = Queue()
request_id = 0

def generate_request():
    global request_id
    request_id += 1

    request_data = ''.join(random.sample(string.ascii_lowercase, 15))
    request = f"Request ID {request_id}: {request_data}"
    queue.put(request)
    print(f"Generated and added to queue: {request}")

def process_request():
    if queue.empty():
        print("Queue is empty")
    else:
        # Process the request by removing it from the queue
        request = queue.get()
        print(f"Processed request: {request}")

if __name__ == "__main__":
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(1)  # Add a delay of 1 second to simulate processing time
    except KeyboardInterrupt:
        print("Exiting program...")