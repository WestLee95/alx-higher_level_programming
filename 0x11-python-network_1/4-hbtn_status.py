#!/usr/bin/python3
import requests

def fetch_status():
  """Fetches the status from the provided URL and displays the response body."""
  url = "https://alx-intranet.hbtn.io/status"
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    data = response.json()  # Assuming JSON response format
    print("Body response:")
    for key, value in data.items():
      print(f"\t- {key}: {value}$")  # Use '$' as line ending for readability
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  fetch_status()
