# quotesjs

Crawl and scrape data from HTML files. The htmls saved to pages/ directory/folder with the "foxdom" script. There are other alternatives for saving web pages, such as a FireFox extension called Save Page WE.

Scrap urls-s from the pages:
```
scrapy crawl url -a dir=pages -o urls.lll
```
The .lll extension programmed for headless .csv

Scrap data from pages
```
scrapy crawl page -a dir=pages -o quotes.csv
```

