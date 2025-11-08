thonimport requests
from bs4 import BeautifulSoup
import logging

class GroupExtractor:
    def __init__(self, url):
        self.url = url
        self.group_data = {}

    def fetch_group_page(self):
        try:
            logging.info(f"Fetching group page: {self.url}")
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch group page: {e}")
            return None

    def parse_group_data(self, page_html):
        soup = BeautifulSoup(page_html, 'html.parser')
        
        # Extract group details (example selectors)
        self.group_data = {
            "group_slug": soup.find('meta', {'name': 'group-slug'})['content'],
            "group_name": soup.find('h1', class_='group-name').text.strip(),
            "group_description": soup.find('div', class_='description').text.strip(),
            "group_total_members": int(soup.find('span', class_='member-count').text.strip())
        }

    def extract_group_data(self):
        page_html = self.fetch_group_page()
        if page_html:
            self.parse_group_data(page_html)
        return self.group_data