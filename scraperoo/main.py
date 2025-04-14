import requests
import time
import random
import string


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


steps = [
    "https://banweb.canton.edu/StudentRegistrationSsb/ssb/selfServiceMenu/data",
    "https://banweb.canton.edu/StudentRegistrationSsb/ssb/menu?type=Personal",
    "https://banweb.canton.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?searchTerm=&offset=1&max=10&_=1744659190021",
    "https://banweb.canton.edu/StudentRegistrationSsb/ssb/term/search?mode=search?",
]
post = ["https://banweb.canton.edu/StudentRegistrationSsb/ssb/term/search?mode=search"]

steps2 = [
    "https://banweb.canton.edu/StudentRegistrationSsb/ssb/selfServiceMenu/data",
    "https://banweb.canton.edu/StudentRegistrationSsb/ssb/menu?type=Personal",
    "https://banweb.canton.edu/StudentRegistrationSsb/ssb/classSearch/resetDataForm",
    "https://banweb.canton.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202509&startDatepicker=&endDatepicker=&uniqueSessionId=cl06f1744659190170&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc",
]

form_data = {
    "term": "202509",
    "studyPath": "",
    "studyPathText": "",
    "startDatepicker": "",
    "endDatepicker": "",
    "uniqueSessionId": "cl06f1744659190170",
}
with requests.Session() as s:
    for i in steps:
        r = s.get(i)
        print(s.cookies)
    # rp = s.post(
    #     url=post,
    #     data=form_data,
    # )
    print(s.cookies)
    for i in steps2:
        r = s.get(i)
        print(s.cookies)
    print(r.content)
