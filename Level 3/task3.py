from googlesearch import search
import requests

def scrape_emails_from_search(search_term, num_results):
    query = f"{search_term} email"
    emails = []

    for index, url in enumerate(search(query, num_results=num_results), start=1):
        if index > num_results:
            break

        try:
            response = requests.get(url)
            text = response.text
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails += re.findall(email_regex, text)
        except requests.exceptions.RequestException:
            continue

    return emails

# Example usage:
search_term = input("Enter a search term: ")
num_results = int(input("Enter the number of search results to scrape: "))

scraped_emails = scrape_emails_from_search(search_term, num_results)
print(scraped_emails)