import requests
from bs4 import BeautifulSoup
import random
import string
import time
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

def get_search_results_with_token(term):
    """
    Fetches the sync token and then retrieves search results.
    """

    session = requests.Session()  # Use a session to persist cookies

    # 1. Fetch the page containing the token (you'll need to adjust this URL)
    token_url = "https://banweb.canton.edu/StudentRegistrationSsb/ssb/classSearch/classSearch"  # Adjust this URL to the page with the token
    try:
        token_response = session.get(token_url)
        token_response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching token page: {e}")
        return None

    # 2. Extract the sync token
    soup = BeautifulSoup(token_response.content, "html.parser")
    token_tag = soup.find("meta", {"name": "synchronizerToken"})
    if token_tag:
        token = token_tag["content"]
        print(f"Found sync token: {token}")
    else:
        print("Sync token not found")
        return None

    # 3. Construct and send the search results request
    search_url = "https://banweb.canton.edu/StudentRegistrationSsb/ssb/searchResults/searchResults"
    search_headers = {
        "Host": "banweb.canton.edu",
        "Cookie": "JSESSIONID=CE6B2DF79B8CDD5C6B27A9D3838A56E8",  # You might need to handle cookies more dynamically
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
        "Accept-Language": "en-US",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "X-Synchronizer-Token": token,  # Use the extracted token
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
        "uniqueSessionId": f"{create_unique_id()}",  # You might need to handle this dynamically too
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
while True:
    results = get_search_results_with_token("202509")
    if results['totalCount'] != 0:
        break

if results:
    pp(results['totalCount'])