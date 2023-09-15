
import scrapy

# Define a Scrapy spider class named 'jobsSpider'
class jobsSpider(scrapy.Spider):
    # Set the name of the spider
    name = "jobs"

    # Define the starting URLs for the spider
    start_urls = [
        "https://www.farojob.net/jobs"
    ]

    # Initialize a page counter
    page_counter = 0

    # Maximum number of pages to scrape
    max_pages = 50

    # Callback function to process the web page's response
    def parse(self, response):
        # Check if the response status is 403 (Forbidden)
        if response.status == 403:
            self.logger.warning("Received a 403 Forbidden response. You may be blocked. Check the website's terms of service.")
            return
            
            
        # Increment the page counter
        self.page_counter += 1

        # Extract job information from each 'article.loadmore-item' element
        for job in response.css('article.loadmore-item'):
            yield {
                'location': job.css('div.loop-item-content > p > span.job-location > a > em::text').get(),
                'jobTitle': job.css(' div.loop-item-content > h2 > a::text').get(),
                'company': job.css('div.loop-item-content > p > span.job-company > a::text').get(),
                'Add Date': job.css('div.loop-item-content > p > span.job-date > time > span::text').get(),
            }
        
        # Follow pagination links to continue scraping other pages, but stop if we've reached the maximum number of pages
        if self.page_counter < self.max_pages:
            yield from response.follow_all(css='div.pagination.list-center > a.next.page-numbers', callback=self.parse)

