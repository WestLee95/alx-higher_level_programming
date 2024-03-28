#!/usr/bin/python3
from urllib.request import urlopen
import sys

def get_request_id(url):
  with urlopen(url) as response:
    headers = response.headers
    if 'X-Request-Id' in headers:
      return headers['X-Request-Id']
    else:
      return None

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)
    url = sys.argv[1]

  request_id = get_request_id(url)

  if request_id:
    print(f"X-Request-Id: {request_id}")
  else:
    print("X-Request-Id not found in response headers.")
