import requests
from bs4 import BeautifulSoup

def fetch_about_us_info_and_save(url, output_file_path):
    # Make an HTTP request to the WebPage
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all text content from the page
        all_text = soup.get_text()

        # Clean and format the text as needed
        # removed white spaces 
        cleaned_text = ' '.join(all_text.split())

        # Save the cleaned and formatted text to a file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Add additional formatting to make the text more readable
            output_file.write(cleaned_text.replace('. ', '.\n\n'))

        print(f'The information has been saved to {output_file_path}')
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')

fetch_about_us_info_and_save('https://cognifyz.com/about-us/', 'output.txt')
