import time
from class_data import Data
scraped_data = Data()

if __name__ == "__main__":
    while True:
        scraped = scraped_data.scrape(scraped_data._URL)
        extracted = scraped_data.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = scraped_data.read(extracted)
            if not row:
                scraped_data.store(extracted)
                scraped_data.send_email(message="Hey, new event was found!")
        time.sleep(2)
