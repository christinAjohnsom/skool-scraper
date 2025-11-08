thonimport requests
from bs4 import BeautifulSoup
import logging

class MemberExtractor:
    def __init__(self, url):
        self.url = url
        self.member_data = {}

    def fetch_member_page(self):
        try:
            logging.info(f"Fetching member page: {self.url}")
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch member page: {e}")
            return None

    def parse_member_data(self, page_html):
        soup = BeautifulSoup(page_html, 'html.parser')
        
        # Extract member details (example selectors)
        self.member_data = {
            "member_first_name": soup.find('span', class_='first-name').text.strip(),
            "member_last_name": soup.find('span', class_='last-name').text.strip(),
            "member_bio": soup.find('div', class_='bio').text.strip(),
            "member_social_links": {
                "instagram": soup.find('a', {'href': 'instagram'}).get('href', ''),
                "youtube": soup.find('a', {'href': 'youtube'}).get('href', '')
            }
        }

    def extract_member_data(self):
        page_html = self.fetch_member_page()
        if page_html:
            self.parse_member_data(page_html)
        return self.member_data