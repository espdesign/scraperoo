import requests
from bs4 import BeautifulSoup  # If you need to parse HTML
import json  # If you need to parse JSON
import time
import random
import string
from pprint import pp as pp
def create_unique_id():
    # Simulating sessionStorage in a dictionary (you can replace this with actual storage in practice)
    session_storage = {}

    STORAGE = "xe.unique.session.storage.id"

    # Generate the random string
    random_str = "".join(random.choices(string.ascii_lowercase + string.digits, k=5))

    # Get current time in milliseconds
    now = int(time.time() * 1000)
    # Simulate the sessionStorage behavior
    if STORAGE not in session_storage:
        session_storage[STORAGE] = random_str + str(now)

    # Retrieve the stored ID
    
    stored = session_storage[STORAGE]
    return stored

def get_search_results(term):
    """
    Automates the process of getting search results, including header handling.
    """

    session = requests.Session()  # Use a session to persist cookies

    # 1. Initial Request (e.g., to the class search page)
    initial_url = "https://banweb.canton.edu/StudentRegistrationSsb/ssb/classSearch/classSearch"  # Adjust this URL
    try:
        initial_response = session.get(initial_url)
        initial_response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching initial page: {e}")
        return None

    # 2. Parse Initial Response (Example: Extracting a token)
    # This part depends heavily on the website's structure
    # Example using BeautifulSoup (if the token is in an HTML element):
    soup = BeautifulSoup(initial_response.content, "html.parser")
    token_tag = soup.find("meta", {"name": "synchronizerToken"})
    token_element = soup.find("input", {"name": "synchronizerToken"})  # Adjust this selector
    if token_tag:
        token = token_tag["name"]
        print(f"Found token: {token}")
    else:
        print("Token not found")
        return None

    # In this case, we don't have a token in the first request, so we will use the token provided.

    # 3. Construct Target Request (for search results)
    search_url = "https://banweb.canton.edu/StudentRegistrationSsb/ssb/searchResults/searchResults"
    search_headers = {
        "Host": "banweb.canton.edu",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
        "Accept-Language": "en-US",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Synchronizer-Token": token,  # Use the extracted or provided token
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://banweb.canton.edu/StudentRegistrationSsb/ssb/classSearch/classSearch",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }
    search_params = {
        "txt_term": term,
        "startDatepicker": "",
        "endDatepicker": "",
        "uniqueSessionId": f"{create_unique_id()}",  # This might also need to be dynamically obtained
        "pageOffset": "0",
        "pageMaxSize": "10",
        "sortColumn": "subjectDescription",
        "sortDirection": "asc"
    }

    try:
        search_response = session.get(search_url, headers=search_headers, params=search_params)
        search_response.raise_for_status()
        return search_response.json()  # Assuming the response is JSON
    except requests.exceptions.RequestException as e:
        print(f"Error fetching search results: {e}")
        return None

# Example usage
results = get_search_results("202505")
if results:
    pp(json.dumps(results, indent=2))  # Pretty print the JSON