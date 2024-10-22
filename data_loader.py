import requests
from bs4 import BeautifulSoup

def fetch_courses(url):
    response = requests.get(url)
    
    # Debugging output
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content[:500])  # Print first 500 characters of content

    if response.status_code != 200:
        print("Failed to retrieve data.")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    courses = []
    
    # Update this selector based on the actual course structure in the HTML
    for course in soup.find_all('div', class_='course-item'):  # Change 'course-item' to the actual class name
        title = course.find('h3').text.strip() if course.find('h3') else 'No title found'
        description = course.find('p').text.strip() if course.find('p') else 'No description found'
        link = course.find('a')['href'] if course.find('a') else 'No link found'
        
        courses.append({'title': title, 'description': description, 'link': link})

    print("Fetched courses:", courses)  # Check what courses were extracted
    return courses
