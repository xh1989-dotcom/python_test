"""
Python Multithreading Training - Test Suite

This module tests the multithreading examples to ensure they work correctly.
"""

import sys
import os
import time

# Add the training directories to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'basic_concepts'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'thread_synchronization'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'advanced_patterns'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'exercises'))

def test_basic_threading():
    """Test basic threading concepts"""
    print("Testing basic threading concepts...")
    
    # Import and run basic threading example
    try:
        from basic_concepts.basic_threading import basic_thread_example, thread_with_return_value, daemon_thread_example
        
        print("Running basic_thread_example...")
        basic_thread_example()
        
        print("Running thread_with_return_value...")
        result = thread_with_return_value()
        assert result == "Result from thread", f"Expected 'Result from thread', got {result}"
        
        print("Running daemon_thread_example...")
        daemon_thread_example()
        
        print("Basic threading tests passed!")
        return True
    except Exception as e:
        print(f"Basic threading tests failed: {e}")
        return False


def test_thread_synchronization():
    """Test thread synchronization concepts"""
    print("\nTesting thread synchronization concepts...")
    
    try:
        from thread_synchronization.thread_sync import lock_example, rlock_example, semaphore_example, condition_example, event_example
        
        print("Running lock_example...")
        lock_example()
        
        print("Running rlock_example...")
        rlock_example()
        
        print("Running semaphore_example...")
        semaphore_example()
        
        print("Running condition_example...")
        condition_example()
        
        print("Running event_example...")
        event_example()
        
        print("Thread synchronization tests passed!")
        return True
    except Exception as e:
        print(f"Thread synchronization tests failed: {e}")
        return False


def test_advanced_patterns():
    """Test advanced multithreading patterns"""
    print("\nTesting advanced multithreading patterns...")
    
    try:
        from advanced_patterns.advanced_patterns import thread_pool_example, producer_consumer_with_queue, thread_safe_counter, barrier_example
        
        print("Running thread_pool_example...")
        thread_pool_example()
        
        print("Running producer_consumer_with_queue...")
        producer_consumer_with_queue()
        
        print("Running thread_safe_counter...")
        thread_safe_counter()
        
        print("Running barrier_example...")
        barrier_example()
        
        print("Advanced patterns tests passed!")
        return True
    except Exception as e:
        print(f"Advanced patterns tests failed: {e}")
        return False


def test_exercises():
    """Test exercise templates"""
    print("\nTesting exercise templates...")
    
    try:
        from exercises.exercises import run_all_exercises
        print("Running exercise templates...")
        run_all_exercises()  # This won't complete the exercises, just run the template
        
        print("Exercise template tests passed!")
        return True
    except Exception as e:
        print(f"Exercise template tests failed: {e}")
        return False


def test_solutions():
    """Test exercise solutions"""
    print("\nTesting exercise solutions...")
    
    try:
        from exercises.solutions import run_all_solutions
        print("Running exercise solutions...")
        run_all_solutions()
        
        print("Solution tests passed!")
        return True
    except Exception as e:
        print(f"Solution tests failed: {e}")
        return False


def main():
    """Run all tests"""
    print("Starting Python Multithreading Training Test Suite\n")
    
    all_tests = [
        test_basic_threading,
        test_thread_synchronization,
        test_advanced_patterns,
        test_exercises,
        test_solutions
    ]
    
    passed = 0
    total = len(all_tests)
    
    for test_func in all_tests:
        if test_func():
            passed += 1
    
    print(f"\nTest Results: {passed}/{total} test modules passed")
    
    if passed == total:
        print("All tests passed! The training materials are working correctly.")
    else:
        print("Some tests failed. Please check the implementations.")


if __name__ == "__main__":
    main()