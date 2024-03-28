#!/usr/bin/python3
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys

def send_post_request(url, email):
  """Sends a POST request with the email parameter and displays the response."""
  data = {'email': email}  # Create the data to be sent
  data = bytes(urlencode(data), encoding='utf-8')  # Encode data for POST request

  with urlopen(Request(url, data=data, method='POST')) as response:
    response_body = response.read().decode('utf-8')  # Decode response body
    print(response_body)

if __name__ == "__main__":
  # Get URL and email from command-line arguments (assuming basic validation)
  if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)
  url = sys.argv[1]
  email = sys.argv[2]

  send_post_request(url, email)
