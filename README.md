# Python-Web-Scraping
Web Scraping Project: Mango Product Data Extraction
Overview:
This project is focused on scraping product details from Mango's online shop. Specifically, the details of a men's t-shirt product page are extracted. The primary challenge was dealing with dynamic content, such as color names, that weren't directly available in the page source but were fetched asynchronously via AJAX.

Key Features:
Scrapy Spider: Utilized the Scrapy framework to structure the web scraping tasks.
Dynamic Content Handling: Used Scrapy's capabilities to send HTTP requests and fetch data from AJAX endpoints.
Integration with Splash: As the website relies on JavaScript for rendering, the Scrapy Splash middleware was used to process JavaScript-heavy web pages.
Structured Output: The scraped data is structured into a defined JSON format, ensuring clarity and ease of use.
Data Points Extracted:
Product Name
Price
Colour
Available Sizes
Unavailable Sizes
Technical Stack:
Python: The primary language for scripting and data extraction.
Scrapy: A popular web-crawling and web scraping framework in Python.
Splash: A headless browser designed for web scraping and rendering, integrated with Scrapy for this project.
