import requests
from bs4 import BeautifulSoup
import random
import string
import time
from pprint import pp as pp
from cookie_test import get_session_cookies
def get_search_results(term):
    session = requests.Session()  # Use a session to persist cookies
    r = session.post("https://banweb.canton.edu/StudentRegistrationSsb/ssb/term/search?mode=search", data='term=202509&studyPath=&studyPathText=&startDatepicker=&endDatepicker=')
    jessionid= r.cookies['JSESSIONID']
    
    search_url = "https://banweb.canton.edu/StudentRegistrationSsb/ssb/searchResults/searchResults"
    # jessionid = 'A15272E27F9B4F85354C2CF2D3E644A1'
    search_headers = {
        "Cookie": f"JSESSIONID={jessionid}",
    }
    search_params = {
        "txt_term": term,
        "startDatepicker": "",
        "endDatepicker": "",
        "pageOffset": "0",
        "pageMaxSize": "20",
        "sortColumn": "subjectDescription",
        "sortDirection": "asc"
    }

    try:
        session.get('https://banweb.canton.edu/StudentRegistrationSsb/ssb/classSearch/classSearch')
        search_response = session.get(search_url, headers=search_headers, params=search_params)
        search_response.raise_for_status()
        return search_response.json()  # Assuming the response is JSON
    except requests.exceptions.RequestException as e:
        print(f"Error fetching search results: {e}")
        return None


i = 1
while True:
    results = get_search_results("202509")
    print(f'Trying new request...#{i}')
    i+=1
    if results['totalCount'] != 0:
        break

if results:
    pp(results['totalCount'])
