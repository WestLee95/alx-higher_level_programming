#!/usr/bin/python3

import urllib.request
import sys

def fetch_url(url):
  try:
    with urllib.request.urlopen(url) as response:
      return response.read().decode('utf-8')
  except urllib.error.HTTPError as e:
    print("HTTP error:", e.code, e.reason)  # Print informative error message
    return None
  except urllib.error.URLError as e:
    print("URL error:", e.reason)
    return None

if __name__ == "__main__":
  # Get the URL from command-line arguments
  url = sys.argv[1]

  response_body = fetch_url(url)

  if response_body:
    print(response_body)  # Print the decoded response body
