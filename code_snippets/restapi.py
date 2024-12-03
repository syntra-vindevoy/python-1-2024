import requests


'''
GET: Retrieve data from the server.
POST: Send new data to the server.
PUT: Update existing data on the server.
DELETE: Remove data from the server.
'''

def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(f"Title: {post['title']}")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

def post_request(url):
    payload = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print('Resource created successfully')
        print(response.json())
    else:
        print(f"Failed to create resource: {response.status_code}")    

def put_request(url):
    payload = {
        'id': 1,
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.put(url, json=payload)
    if response.status_code == 200:
        print('Resource updated successfully')
        print(response.json())
    else:
        print(f"Failed to update resource: {response.status_code}")

def delete_request(url):
    response = requests.delete(url)
    if response.status_code == 200:
        print('Resource deleted successfully')
    else:
        print(f"Failed to delete resource: {response.status_code}")

def get_request_with_error_handling(url:str):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        for post in data:
            print(f"Title: {post['title']}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


def main():
    get_request('https://jsonplaceholder.typicode.com/posts')
    post_request('https://jsonplaceholder.typicode.com/posts')
    put_request('https://jsonplaceholder.typicode.com/posts/1')
    delete_request('https://jsonplaceholder.typicode.com/posts/1')
    get_request_with_error_handling('https://jsonplaceholder.typicode.com/posts')
    print("Requests completed.")

if __name__ == "__main__":
    main()