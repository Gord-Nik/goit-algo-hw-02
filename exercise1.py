import string
from queue import Queue
import random

queue = Queue()


def generate_request():
    # Створення запиту
    request = ''.join(random.sample(string.ascii_lowercase, 15))
    queue.put(request)


def process_request():
    if queue.empty():
        print("Queue is empty")
    else:
        # Опрацювання запиту
        request = queue.get()
        print(request)

if __name__ == "__main__":
    while True:
        generate_request()
        process_request()
