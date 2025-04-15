import requests

def get_session_cookies(initial_url):
    """
    Fetches the initial URL and prints the cookies managed by the session.
    """
    session = requests.Session()

    try:
        response = session.get(initial_url, allow_redirects=True)  # Ensure redirects are followed
        response.raise_for_status()

        print("Initial URL:", initial_url)
        print("Response Status Code:", response.status_code)
        print("Session Cookies:", session.cookies.get_dict())  # Print the cookies

        return session.cookies.get_dict()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# # **CRITICAL: Replace with the correct initial URL**
# initial_url = "https://banweb.canton.edu/StudentRegistrationSsb/"  # <--- Example: Try the base URL

# cookies = get_session_cookies(initial_url)

# if cookies:
#     print("Cookies retrieved successfully!")
# else:
#     print("Failed to retrieve cookies.")