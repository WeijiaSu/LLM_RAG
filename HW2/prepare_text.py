from bs4 import BeautifulSoup
import requests

# Base URL
base_url = "https://en.stomics.tech/"

# Send a request to the website
response = requests.get(base_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract all text from the main page
    main_content = soup.get_text(separator="\n", strip=True)
    print("Main Page Content:")
    print(main_content)

    # Extract all links
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("http")]
    print("\nLinks Found:")
    for link in links:
        print(link)

    # Save main page content
    with open("main_page_content.txt", "w") as file:
        file.write(main_content)

    # Follow links and extract content
    for link in links:
        try:
            sub_response = requests.get(link)
            if sub_response.status_code == 200:
                sub_soup = BeautifulSoup(sub_response.content, "html.parser")
                sub_content = sub_soup.get_text(separator="\n", strip=True)
                with open(f"{link.split('/')[-1]}.txt", "w") as sub_file:
                    sub_file.write(sub_content)
        except Exception as e:
            print(f"Error fetching {link}: {e}")
