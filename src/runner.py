thonimport json
import logging
from extractors.group_extractor import GroupExtractor
from extractors.member_extractor import MemberExtractor
from outputs.exporter import Exporter

# Set up basic logging
logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Starting Skool Scraper...")

    # Example URLs (can be loaded from config or arguments)
    group_url = "https://skool.com/group/xyz"
    member_url = "https://skool.com/member/abc"

    # Instantiate the extractors
    group_extractor = GroupExtractor(group_url)
    member_extractor = MemberExtractor(member_url)

    # Scrape group and member data
    group_data = group_extractor.extract_group_data()
    member_data = member_extractor.extract_member_data()

    # Example of how to use the exporter
    exporter = Exporter()

    # Export the data to JSON files
    exporter.export_to_json('group_data.json', group_data)
    exporter.export_to_json('member_data.json', member_data)

    logging.info("Scraping and export complete.")

if __name__ == "__main__":
    main()