import requests

session = requests.Session()

# Set the JSESSIONID manually

# Now make the authenticated request
url = 'https://banweb.canton.edu/StudentRegistrationSsb/ssb/classSearch/classSearch'
response = session.get(url)

print(response.status_code)
print(response.text)