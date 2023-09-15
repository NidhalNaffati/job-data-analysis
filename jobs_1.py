

import scrapy

class JobsSpider(scrapy.Spider):
    # Spider name
    name = "jobs"

    # List of starting URLs
    start_urls = [
        'https://tunisia.tanqeeb.com/s/jobs/jobs-in-tunisia'
    ]

    # Custom settings for the spider
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'COOKIES_ENABLED': True,
        'DOWNLOAD_DELAY': 1  # Set the delay to 1 second (or adjust as needed)
    }

    # Initialize the page count
    page_count = 0
    
    # Maximum number of pages to scrape
    max_pages = 50

    # Callback function that processes the response
    def parse(self, response):
        # Check if the response status is 403 (Forbidden)
        if response.status == 403:
            self.logger.warning("Received a 403 Forbidden response. You may be blocked. Check the website's terms of service.")
            return

        # Extract job information from each 'div.card-body' element
        for job in response.css('div.card-body'):
            yield {
                'location': job.css('p.h10 > span:nth-child(1)::text').get(),
                'jobTitle': job.css('h5::text').get(),
                'company': job.css('p.h10 > span:nth-child(2)::text').get(),
                'Add Date': job.css('p.h10 > span:nth-child(3)::text').get(),
            }
        
        # Increment the page count
        self.page_count += 1

        # Check if we have scraped 300 pages, and if not, follow pagination links
        if self.page_count < self.max_pages:
            yield from response.follow_all(css='li.page-item.active > a', callback=self.parse)

