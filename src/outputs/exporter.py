thonimport json
import logging

class Exporter:
    def __init__(self):
        pass

    def export_to_json(self, filename, data):
        try:
            logging.info(f"Exporting data to {filename}")
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            logging.error(f"Error exporting data to {filename}: {e}")