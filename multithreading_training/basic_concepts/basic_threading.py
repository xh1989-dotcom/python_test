"""
Python Multithreading - Basic Concepts

This module introduces the fundamental concepts of multithreading in Python.
It covers creating threads, starting them, and understanding basic thread behavior.
"""

import threading
import time


def basic_thread_example():
    """
    Basic example showing how to create and start a thread
    """
    def worker_function(name, duration):
        print(f"Thread {name} starting")
        time.sleep(duration)
        print(f"Thread {name} finished")
    
    # Create threads
    thread1 = threading.Thread(target=worker_function, args=("Worker-1", 2))
    thread2 = threading.Thread(target=worker_function, args=("Worker-2", 3))
    
    # Start threads
    thread1.start()
    thread2.start()
    
    # Wait for threads to complete
    thread1.join()
    thread2.join()
    
    print("Both threads completed")


def thread_with_return_value():
    """
    Example showing how to get return values from threads
    """
    result = [None]  # Use a list to store result (mutable)
    
    def worker_with_result():
        time.sleep(1)
        result[0] = "Result from thread"
    
    thread = threading.Thread(target=worker_with_result)
    thread.start()
    thread.join()
    
    return result[0]


def daemon_thread_example():
    """
    Example demonstrating daemon threads
    Daemon threads are background threads that automatically terminate when the main program exits
    """
    def background_task():
        while True:  # This would run forever, but daemon threads stop when main thread ends
            print("Background task running...")
            time.sleep(1)
    
    daemon_thread = threading.Thread(target=background_task)
    daemon_thread.daemon = True  # Set as daemon thread
    daemon_thread.start()
    
    print("Main thread sleeping...")
    time.sleep(3)
    print("Main thread ending...")


if __name__ == "__main__":
    print("=== Basic Thread Example ===")
    basic_thread_example()
    
    print("\n=== Thread with Return Value ===")
    result = thread_with_return_value()
    print(f"Returned value: {result}")
    
    print("\n=== Daemon Thread Example ===")
    daemon_thread_example()
    print("Program ending")