"""
Python Training - File 15: Web Requests

This file covers:
- Making HTTP requests with requests library
- GET and POST requests
- Handling responses
- Working with APIs
- Error handling in web requests
- Practical examples
"""

import requests
import json

# Basic GET request
print("Basic GET request:")
try:
    response = requests.get("https://httpbin.org/get")
    print(f"Status code: {response.status_code}")
    print(f"Response type: {type(response.json())}")
    print(f"URL: {response.json()['url']}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# GET request with parameters
print(f"\nGET request with parameters:")
params = {
    "q": "python",
    "page": 1,
    "per_page": 5
}
try:
    response = requests.get("https://httpbin.org/get", params=params)
    print(f"Full URL: {response.url}")
    print(f"Status: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# POST request with JSON data
print(f"\nPOST request with JSON:")
data = {
    "title": "Python Training",
    "body": "Learning to make HTTP requests",
    "userId": 1
}
try:
    response = requests.post("https://httpbin.org/post", json=data)
    print(f"Status: {response.status_code}")
    response_data = response.json()
    print(f"Sent data: {response_data['json']}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# Working with real API (JSONPlaceholder)
print(f"\nWorking with JSONPlaceholder API:")

# GET request to retrieve data
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        post = response.json()
        print(f"Post title: {post['title']}")
        print(f"Post body: {post['body'][:50]}...")  # First 50 chars
    else:
        print(f"Failed to retrieve post: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# GET request for multiple items
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"_limit": 3})
    if response.status_code == 200:
        posts = response.json()
        print(f"\nFirst 3 posts:")
        for i, post in enumerate(posts, 1):
            print(f"  {i}. {post['title'][:30]}...")
    else:
        print(f"Failed to retrieve posts: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# POST request to create data
print(f"\nPOST request to create data:")
new_post = {
    "title": "My New Post",
    "body": "This post was created via API",
    "userId": 1
}
try:
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
    if response.status_code == 201:  # 201 means created
        created_post = response.json()
        print(f"Created post ID: {created_post['id']}")
        print(f"Post title: {created_post['title']}")
    else:
        print(f"Failed to create post: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# Adding headers to requests
print(f"\nRequest with custom headers:")
headers = {
    "User-Agent": "Python Training App",
    "Accept": "application/json",
    "Authorization": "Bearer fake-token"  # This is just for demonstration
}
try:
    response = requests.get("https://httpbin.org/headers", headers=headers)
    if response.status_code == 200:
        received_headers = response.json()["headers"]
        print("Headers sent by client:")
        for key, value in received_headers.items():
            print(f"  {key}: {value}")
    else:
        print(f"Failed to get headers: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# Handling different response formats
print(f"\nHandling different response formats:")

# JSON response
try:
    response = requests.get("https://httpbin.org/json")
    if response.status_code == 200:
        json_data = response.json()
        print(f"JSON response: {type(json_data)}")
except requests.exceptions.RequestException as e:
    print(f"JSON request failed: {e}")

# Text response
try:
    response = requests.get("https://httpbin.org/html")
    if response.status_code == 200:
        print(f"Text response length: {len(response.text)} characters")
        print(f"Content type: {response.headers['Content-Type']}")
except requests.exceptions.RequestException as e:
    print(f"Text request failed: {e}")

# Working with query parameters and URL building
print(f"\nWorking with query parameters:")

base_url = "https://httpbin.org/get"
params = {
    "search": "python tutorial",
    "category": "programming",
    "sort": "date",
    "order": "desc"
}

try:
    response = requests.get(base_url, params=params)
    print(f"Built URL: {response.url}")
    print(f"Status: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

# Error handling in web requests
print(f"\nError handling:")

def safe_request(url, timeout=5):
    """Make a request with comprehensive error handling"""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"General Request Error: {e}")
    return None

# Test error handling with various URLs
test_urls = [
    "https://httpbin.org/status/404",  # 404 error
    "https://httpbin.org/delay/10",    # This will timeout
    "https://invalid-url-example-12345.com"  # Invalid domain
]

for url in test_urls:
    print(f"\nTesting: {url}")
    response = safe_request(url, timeout=3)
    if response:
        print(f"Success: {response.status_code}")
    else:
        print("Request failed as expected")

# Working with sessions (for maintaining cookies, etc.)
print(f"\nUsing sessions:")
try:
    session = requests.Session()
    session.headers.update({"User-Agent": "Python Training Session"})
    
    # First request
    response1 = session.get("https://httpbin.org/headers")
    print(f"First request headers: {response1.json()['headers']['User-Agent']}")
    
    # Second request using same session
    response2 = session.get("https://httpbin.org/cookies/set/session_id/abc123")
    print(f"Second request status: {response2.status_code}")
    
    # Third request to see if cookies are maintained
    response3 = session.get("https://httpbin.org/cookies")
    cookies = response3.json().get("cookies", {})
    print(f"Cookies in session: {cookies}")
    
    session.close()
except requests.exceptions.RequestException as e:
    print(f"Session request failed: {e}")

# Practical example: Fetching and processing API data
print(f"\nPractical example - GitHub user data:")

def get_github_user_info(username):
    """Fetch and display GitHub user information"""
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 200:
            user_data = response.json()
            return {
                "name": user_data.get("name", "N/A"),
                "public_repos": user_data.get("public_repos", 0),
                "followers": user_data.get("followers", 0),
                "following": user_data.get("following", 0),
                "bio": user_data.get("bio", "No bio available")
            }
        else:
            print(f"GitHub API returned status: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GitHub data: {e}")
        return None

# Get info for a popular user (using a well-known username)
github_info = get_github_user_info("octocat")
if github_info:
    print(f"GitHub User Info:")
    print(f"  Name: {github_info['name']}")
    print(f"  Public Repos: {github_info['public_repos']}")
    print(f"  Followers: {github_info['followers']}")
    print(f"  Following: {github_info['following']}")
    print(f"  Bio: {github_info['bio'][:60]}...")

# Practical example: API data processing pipeline
print(f"\nAPI data processing pipeline:")

def fetch_and_process_posts(user_id=None):
    """Fetch posts and process them"""
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        if user_id:
            url += f"?userId={user_id}"
        
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            
            # Process: count posts, find longest title
            total_posts = len(posts)
            longest_title = max(posts, key=lambda p: len(p['title']))
            
            return {
                "total_posts": total_posts,
                "longest_title": longest_title['title'],
                "longest_title_length": len(longest_title['title'])
            }
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error in pipeline: {e}")
        return None

# Process posts
result = fetch_and_process_posts()
if result:
    print(f"Total posts: {result['total_posts']}")
    print(f"Longest title: '{result['longest_title'][:30]}...'")
    print(f"Longest title length: {result['longest_title_length']}")

# Timeout and retry logic
print(f"\nTimeout and retry example:")
import time

def request_with_retry(url, max_retries=3, timeout=5):
    """Make request with retry logic"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
                time.sleep(1)  # Wait 1 second before retrying
            else:
                print("Max retries reached")
                raise

try:
    response = request_with_retry("https://httpbin.org/delay/2", timeout=3)
    print("Request successful")
except requests.exceptions.RequestException:
    print("Request ultimately failed after retries")

print("\nWeb requests completed!")