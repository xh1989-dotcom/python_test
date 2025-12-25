"""
Python Multithreading - Thread Synchronization

This module covers different synchronization primitives in Python threading:
- Lock
- RLock (Reentrant Lock)
- Semaphore
- Condition
- Event
"""

import threading
import time
import random


def lock_example():
    """
    Example showing how to use Lock to prevent race conditions
    """
    counter = 0
    lock = threading.Lock()
    
    def increment():
        nonlocal counter
        for _ in range(100000):
            with lock:  # Acquire lock before modifying shared resource
                counter += 1
    
    # Create multiple threads that increment the counter
    threads = []
    for i in range(5):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    print(f"Final counter value: {counter}")


def rlock_example():
    """
    Example showing Reentrant Lock (RLock)
    RLock can be acquired multiple times by the same thread
    """
    class Counter:
        def __init__(self):
            self.value = 0
            self.lock = threading.RLock()
        
        def increment(self):
            with self.lock:
                self.value += 1
                self.double_value()  # This method also acquires the lock
        
        def double_value(self):
            with self.lock:
                self.value *= 2
    
    counter = Counter()
    
    def worker():
        for _ in range(1000):
            counter.increment()
    
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"Final counter value with RLock: {counter.value}")


def semaphore_example():
    """
    Example showing how to use Semaphore to limit access to resources
    """
    # Limit to 2 threads accessing the resource at the same time
    semaphore = threading.Semaphore(2)
    
    def access_resource(thread_id):
        print(f"Thread {thread_id} waiting to access resource")
        with semaphore:
            print(f"Thread {thread_id} got access to resource")
            time.sleep(random.uniform(1, 3))  # Simulate work
            print(f"Thread {thread_id} releasing resource")
    
    threads = []
    for i in range(5):
        t = threading.Thread(target=access_resource, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()


def condition_example():
    """
    Example showing how to use Condition for thread coordination
    Producer-Consumer pattern
    """
    buffer = []
    max_buffer_size = 3
    condition = threading.Condition()
    
    def producer():
        for i in range(5):
            with condition:
                while len(buffer) >= max_buffer_size:
                    print("Buffer full, producer waiting...")
                    condition.wait()  # Wait until buffer has space
                
                buffer.append(f"item-{i}")
                print(f"Produced: item-{i}, Buffer size: {len(buffer)}")
                condition.notify_all()  # Notify consumers
            
            time.sleep(0.1)  # Simulate production time
    
    def consumer(consumer_id):
        for _ in range(2):  # Each consumer gets 2 items
            with condition:
                while len(buffer) == 0:
                    print(f"Consumer {consumer_id} waiting for items...")
                    condition.wait()  # Wait until buffer has items
                
                item = buffer.pop(0)
                print(f"Consumer {consumer_id} consumed: {item}, Buffer size: {len(buffer)}")
                condition.notify_all()  # Notify producers
    
    # Start producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_threads = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]
    
    producer_thread.start()
    for t in consumer_threads:
        t.start()
    
    producer_thread.join()
    for t in consumer_threads:
        t.join()


def event_example():
    """
    Example showing how to use Event for thread signaling
    """
    event = threading.Event()
    
    def waiter():
        print("Waiter waiting for event...")
        event.wait()  # Wait until event is set
        print("Waiter received event!")
    
    def setter():
        time.sleep(2)  # Wait 2 seconds before setting event
        print("Setting event...")
        event.set()
    
    waiter_thread = threading.Thread(target=waiter)
    setter_thread = threading.Thread(target=setter)
    
    waiter_thread.start()
    setter_thread.start()
    
    waiter_thread.join()
    setter_thread.join()


if __name__ == "__main__":
    print("=== Lock Example ===")
    lock_example()
    
    print("\n=== RLock Example ===")
    rlock_example()
    
    print("\n=== Semaphore Example ===")
    semaphore_example()
    
    print("\n=== Condition Example ===")
    condition_example()
    
    print("\n=== Event Example ===")
    event_example()