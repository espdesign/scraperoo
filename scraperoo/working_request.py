import requests
from pprint import pp as pp
from get_cookie_complex import get_cookies_complex


def get_search_results(term, jession_id):
    session = requests.Session()  # Use a session to persist cookies

    
    search_url = "https://banweb.canton.edu/StudentRegistrationSsb/ssb/searchResults/searchResults"

    # if request is failing you may try hardcoding a recent jesssion id token
    # jessionid = '3B1474723A22C62AFBC3946CD1DFA05B'
    search_headers = {
        "Cookie": f"JSESSIONID={jession_id}",
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

term = '202502'
jession_id = get_cookies_complex(term)
while True:
    results = get_search_results(term, jession_id)
    print(f'Trying new request...#{i}')
    i+=1
    if results['totalCount'] != 0:
        break

if results:
    pp(results)
