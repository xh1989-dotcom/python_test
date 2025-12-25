"""
Python Multithreading - Exercises

This module contains practical exercises for multithreading training.
Each exercise builds on the concepts learned in previous modules.
"""

import threading
import time
import queue
import random
from concurrent.futures import ThreadPoolExecutor


def exercise_1_simple_counter():
    """
    Exercise 1: Create a thread-safe counter
    Multiple threads will increment a shared counter.
    Use locks to ensure thread safety.
    
    TODO: Complete the implementation
    """
    print("Exercise 1: Thread-Safe Counter")
    
    # TODO: Implement a thread-safe counter class
    # Hint: Use threading.Lock() to protect the shared resource
    class ThreadSafeCounter:
        def __init__(self):
            # TODO: Initialize counter and lock
            pass
        
        def increment(self):
            # TODO: Implement thread-safe increment
            pass
        
        def get_value(self):
            # TODO: Implement thread-safe getter
            pass
    
    # TODO: Create counter instance and multiple threads that increment it
    # TODO: Verify the final count is correct after all threads complete


def exercise_2_producer_consumer():
    """
    Exercise 2: Producer-Consumer with Queue
    Implement a producer that generates numbers and a consumer that processes them.
    
    TODO: Complete the implementation
    """
    print("\nExercise 2: Producer-Consumer")
    
    # TODO: Create a thread-safe queue
    # TODO: Implement producer function that puts numbers 1-10 into the queue
    # TODO: Implement consumer function that processes numbers from the queue
    # TODO: Start both threads and wait for completion
    # TODO: Use poison pill pattern to signal completion


def exercise_3_thread_pool():
    """
    Exercise 3: Calculate factorials using ThreadPoolExecutor
    Calculate factorials of numbers 5-10 in parallel.
    
    TODO: Complete the implementation
    """
    print("\nExercise 3: Thread Pool Factorial Calculator")
    
    def factorial(n):
        """Calculate factorial of n"""
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    # TODO: Use ThreadPoolExecutor to calculate factorials of [5, 6, 7, 8, 9, 10] in parallel
    # TODO: Print the results in the format "Factorial of X is Y"


def exercise_4_banking_system():
    """
    Exercise 4: Thread-Safe Banking System
    Implement a simple banking system with thread-safe operations.
    
    TODO: Complete the implementation
    """
    print("\nExercise 4: Thread-Safe Banking System")
    
    # TODO: Implement a BankAccount class with thread-safe deposit and withdraw methods
    # TODO: Handle insufficient funds properly
    # TODO: Use appropriate synchronization primitives
    class BankAccount:
        def __init__(self, initial_balance=0):
            # TODO: Initialize account with lock and balance
            pass
        
        def deposit(self, amount):
            # TODO: Implement thread-safe deposit
            pass
        
        def withdraw(self, amount):
            # TODO: Implement thread-safe withdrawal with insufficient funds check
            pass
        
        def get_balance(self):
            # TODO: Implement thread-safe balance getter
            pass
    
    # TODO: Test the banking system with multiple threads performing deposits and withdrawals


def exercise_5_web_scraper():
    """
    Exercise 5: Concurrent Web Scraper
    Create a simple web scraper that fetches multiple URLs concurrently.
    (For this exercise, we'll simulate web requests with time.sleep)
    
    TODO: Complete the implementation
    """
    print("\nExercise 5: Concurrent Web Scraper Simulation")
    
    def fetch_url(url):
        """Simulate fetching a URL by sleeping for a random time"""
        sleep_time = random.uniform(0.5, 2.0)
        time.sleep(sleep_time)
        return f"Content from {url} (fetched in {sleep_time:.2f}s)"
    
    urls = [
        "http://example.com/page1",
        "http://example.com/page2",
        "http://example.com/page3",
        "http://example.com/page4",
        "http://example.com/page5"
    ]
    
    # TODO: Use ThreadPoolExecutor to fetch all URLs concurrently
    # TODO: Print the results as they complete
    # TODO: Time the total execution and compare with sequential execution


def exercise_6_race_condition_fix():
    """
    Exercise 6: Fix the Race Condition
    The following code has a race condition. Fix it using appropriate synchronization.
    
    TODO: Complete the implementation
    """
    print("\nExercise 6: Fix Race Condition")
    
    # This code has a race condition - fix it!
    shared_list = []
    
    def add_items(start, end):
        for i in range(start, end):
            # TODO: Fix the race condition here
            shared_list.append(i)
    
    # Create threads that add items to the shared list
    threads = []
    for i in range(5):
        start = i * 10
        end = (i + 1) * 10
        t = threading.Thread(target=add_items, args=(start, end))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"Final list length: {len(shared_list)}")
    print(f"Expected length: 50")
    print(f"Correct: {len(shared_list) == 50}")


def run_all_exercises():
    """
    Run all exercises (without completing the TODOs)
    """
    exercise_1_simple_counter()
    exercise_2_producer_consumer()
    exercise_3_thread_pool()
    exercise_4_banking_system()
    exercise_5_web_scraper()
    exercise_6_race_condition_fix()


if __name__ == "__main__":
    print("Python Multithreading Training - Exercises")
    print("Complete the TODO implementations in each exercise")
    run_all_exercises()