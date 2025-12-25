"""
Python Multithreading - Advanced Patterns

This module covers advanced multithreading patterns:
- Thread Pool
- Producer-Consumer with Queue
- Thread-Safe Data Structures
- Future Pattern
"""

import threading
import time
import queue
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import requests


def thread_pool_example():
    """
    Example showing how to use ThreadPoolExecutor for managing a pool of threads
    """
    def worker_task(task_id):
        print(f"Task {task_id} starting")
        time.sleep(1)  # Simulate work
        result = f"Result from task {task_id}"
        print(f"Task {task_id} completed")
        return result
    
    # Using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the pool
        futures = [executor.submit(worker_task, i) for i in range(5)]
        
        # Get results as they complete
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(f"Received: {result}")


def producer_consumer_with_queue():
    """
    Producer-Consumer pattern using queue.Queue for thread-safe communication
    """
    task_queue = queue.Queue(maxsize=5)
    result_queue = queue.Queue()
    
    def producer(producer_id):
        for i in range(3):
            item = f"Producer-{producer_id}-Item-{i}"
            print(f"Producer {producer_id} producing: {item}")
            task_queue.put(item)
            time.sleep(0.5)
        
        # Send poison pill to signal completion
        task_queue.put(None)
        print(f"Producer {producer_id} finished")
    
    def consumer(consumer_id):
        while True:
            item = task_queue.get()  # Blocks until item is available
            if item is None:  # Poison pill received
                task_queue.put(None)  # Put it back for other consumers
                break
            
            print(f"Consumer {consumer_id} processing: {item}")
            time.sleep(1)  # Simulate processing time
            result = f"Processed-{item}"
            result_queue.put(result)
            task_queue.task_done()
        
        print(f"Consumer {consumer_id} finished")
    
    # Start producer and consumer threads
    threads = []
    
    # Start 2 producers
    for i in range(2):
        t = threading.Thread(target=producer, args=(i,))
        threads.append(t)
        t.start()
    
    # Start 3 consumers
    for i in range(3):
        t = threading.Thread(target=consumer, args=(i,))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    # Collect results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    print(f"Results: {results}")


def thread_safe_counter():
    """
    Example of creating a thread-safe counter class
    """
    class ThreadSafeCounter:
        def __init__(self):
            self._value = 0
            self._lock = threading.Lock()
        
        def increment(self):
            with self._lock:
                self._value += 1
        
        def decrement(self):
            with self._lock:
                self._value -= 1
        
        def get_value(self):
            with self._lock:
                return self._value
    
    counter = ThreadSafeCounter()
    
    def worker():
        for _ in range(100000):
            counter.increment()
    
    # Create multiple threads
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"Thread-safe counter final value: {counter.get_value()}")


def future_pattern_example():
    """
    Example showing the Future pattern with ThreadPoolExecutor
    """
    def download_url(url):
        try:
            response = requests.get(url, timeout=5)
            return f"Downloaded {len(response.content)} bytes from {url}"
        except Exception as e:
            return f"Error downloading {url}: {str(e)}"
    
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/3",
    ]
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit all tasks and get futures
        future_to_url = {executor.submit(download_url, url): url for url in urls}
        
        # Process completed futures as they finish
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                print(f"Completed: {result}")
            except Exception as exc:
                print(f"URL {url} generated an exception: {exc}")


def barrier_example():
    """
    Example showing how to use threading.Barrier for thread synchronization
    """
    barrier = threading.Barrier(3)  # Wait for 3 threads
    
    def worker(worker_id):
        print(f"Worker {worker_id} starting")
        time.sleep(random.uniform(0.5, 2))  # Simulate different start times
        print(f"Worker {worker_id} reached barrier")
        
        barrier.wait()  # Wait for all threads to reach this point
        
        print(f"Worker {worker_id} passed barrier")
    
    import random
    
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()


if __name__ == "__main__":
    print("=== Thread Pool Example ===")
    thread_pool_example()
    
    print("\n=== Producer-Consumer with Queue Example ===")
    producer_consumer_with_queue()
    
    print("\n=== Thread-Safe Counter Example ===")
    thread_safe_counter()
    
    print("\n=== Future Pattern Example ===")
    # Note: Skipping the future pattern example that requires internet access
    print("Future pattern example requires internet access, skipping...")
    
    print("\n=== Barrier Example ===")
    barrier_example()