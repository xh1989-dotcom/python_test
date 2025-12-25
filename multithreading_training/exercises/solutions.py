"""
Python Multithreading - Exercise Solutions

This module contains solutions for the multithreading exercises.
"""

import threading
import time
import queue
import random
from concurrent.futures import ThreadPoolExecutor


def solution_1_simple_counter():
    """
    Solution 1: Create a thread-safe counter
    """
    print("Solution 1: Thread-Safe Counter")
    
    class ThreadSafeCounter:
        def __init__(self):
            self._value = 0
            self._lock = threading.Lock()
        
        def increment(self):
            with self._lock:
                self._value += 1
        
        def get_value(self):
            with self._lock:
                return self._value
    
    counter = ThreadSafeCounter()
    
    def worker():
        for _ in range(10000):
            counter.increment()
    
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"Final counter value: {counter.get_value()}")
    assert counter.get_value() == 50000, f"Expected 50000, got {counter.get_value()}"
    print("Solution 1 completed successfully!")


def solution_2_producer_consumer():
    """
    Solution 2: Producer-Consumer with Queue
    """
    print("\nSolution 2: Producer-Consumer")
    
    q = queue.Queue()
    
    def producer():
        for i in range(1, 11):
            print(f"Producing item {i}")
            q.put(i)
            time.sleep(0.1)
        q.put(None)  # Poison pill to signal completion
    
    def consumer():
        while True:
            item = q.get()
            if item is None:  # Poison pill received
                q.put(None)  # Put it back for other consumers if there were multiple
                break
            print(f"Consuming item {item}")
            time.sleep(0.2)
            q.task_done()
    
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()
    
    print("Solution 2 completed successfully!")


def solution_3_thread_pool():
    """
    Solution 3: Calculate factorials using ThreadPoolExecutor
    """
    print("\nSolution 3: Thread Pool Factorial Calculator")
    
    def factorial(n):
        """Calculate factorial of n"""
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    numbers = [5, 6, 7, 8, 9, 10]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(factorial, num): num for num in numbers}
        
        for future in futures:
            num = futures[future]
            result = future.result()
            print(f"Factorial of {num} is {result}")
    
    print("Solution 3 completed successfully!")


def solution_4_banking_system():
    """
    Solution 4: Thread-Safe Banking System
    """
    print("\nSolution 4: Thread-Safe Banking System")
    
    class BankAccount:
        def __init__(self, initial_balance=0):
            self._balance = initial_balance
            self._lock = threading.Lock()
        
        def deposit(self, amount):
            with self._lock:
                self._balance += amount
                print(f"Deposited {amount}, new balance: {self._balance}")
        
        def withdraw(self, amount):
            with self._lock:
                if self._balance >= amount:
                    self._balance -= amount
                    print(f"Withdrew {amount}, new balance: {self._balance}")
                    return True
                else:
                    print(f"Insufficient funds for withdrawal of {amount}, balance: {self._balance}")
                    return False
        
        def get_balance(self):
            with self._lock:
                return self._balance
    
    account = BankAccount(100)
    
    def deposit_worker():
        for _ in range(5):
            account.deposit(10)
            time.sleep(0.1)
    
    def withdraw_worker():
        for _ in range(5):
            account.withdraw(5)
            time.sleep(0.15)
    
    threads = []
    for _ in range(2):
        t = threading.Thread(target=deposit_worker)
        threads.append(t)
        t.start()
    
    for _ in range(2):
        t = threading.Thread(target=withdraw_worker)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"Final balance: {account.get_balance()}")
    print("Solution 4 completed successfully!")


def solution_5_web_scraper():
    """
    Solution 5: Concurrent Web Scraper
    """
    print("\nSolution 5: Concurrent Web Scraper Simulation")
    
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
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(fetch_url, url): url for url in urls}
        
        for future in futures:
            url = futures[future]
            result = future.result()
            print(result)
    
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f}s")
    print("Solution 5 completed successfully!")


def solution_6_race_condition_fix():
    """
    Solution 6: Fix the Race Condition
    """
    print("\nSolution 6: Fix Race Condition")
    
    shared_list = []
    lock = threading.Lock()
    
    def add_items(start, end):
        for i in range(start, end):
            with lock:  # Fix the race condition with a lock
                shared_list.append(i)
    
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
    
    # Verify the list contains all expected values
    expected = list(range(50))
    success = sorted(shared_list) == expected
    print(f"List contains correct values: {success}")
    print("Solution 6 completed successfully!")


def run_all_solutions():
    """
    Run all exercise solutions
    """
    solution_1_simple_counter()
    solution_2_producer_consumer()
    solution_3_thread_pool()
    solution_4_banking_system()
    solution_5_web_scraper()
    solution_6_race_condition_fix()


if __name__ == "__main__":
    print("Python Multithreading Training - Exercise Solutions")
    run_all_solutions()