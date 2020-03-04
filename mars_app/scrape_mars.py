from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    first_element = soup.select_one("ul.item_list li.slide")
    title = first_element.find("div",class_="content_title").get_text()
    
    paragraph = first_element.find("div",class_="article_teaser_body").get_text()
    print(title,paragraph)

   
    # Store data in a dictionary
    mars_data = {
        "title": title,
        "paragraph": paragraph
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
