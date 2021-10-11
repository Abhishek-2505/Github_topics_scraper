# GitHub Topics Scraper : Project Overview



## Introduction:

*Web scraping* is the process of parsing and extracting data from the websites. It is very useful when we want to collect data from the websites for our work. 

GitHub is web-based version control and collaboration platform for software developers. It has a page https://github.com/topics where we can find different topics listed on GitHub.

I have built a scraper i.e., [Github_topics_scraper](https://github.com/Abhishek-2505/Github_topics_scraper/blob/main/github_topics_scraper.py) which scrapes the [GitHub Topics](https://github.com/topics) webpage. This scraper can return, either detailed or non-detailed data frame based on the user preferences. 

## github_topics_scraper() : The scraper function

<code>github_topics_scraper()</code>, the scraper function, takes two optional arguments, <code> detailed</code> and <code>records</code>.



We will create a function github_topics_scraper() which takes two optional arguments detailed and records. The argument “detailed” takes Boolean inputs(True / False) and returns all the columns if set to “True” otherwise returns the first three columns(Topics, Description, and Topic URL). The argument “records” takes either Boolean or integer inputs and returns the required number of records. It should be set to “False” to return all the records.
