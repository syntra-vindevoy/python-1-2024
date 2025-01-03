import requests

# URL to fetch JSON data
URL = "https://gutendex.com/books/"

# Fetch JSON data from the URL
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Check the structure of the JSON (optional to understand its structure better)
    # print(data)

    # Iterate over the "results" key from the JSON structure, assuming it holds a list of books
    if "results" in data:
        for book in data["results"]:
            # Example: Print book title and authors
            title = book.get("title", "No Title Available")
            authors = [author['name'] for author in book.get("authors", [])]  # Extract authors from nested structure
            print(f"Title: {title}")
            print(f"Authors: {', '.join(authors)}")
            print("-" * 50)
    else:
        print("No 'results' key found in the JSON data.")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
