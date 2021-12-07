# GitHub Topics Scraper : Project Overview

###### You can find the explanation of this project [here](https://medium.com/@abhishekdundagi06/building-web-scraper-using-python-scraping-github-topics-in-one-go-b553a0bf58d).

## Introduction:

*Web scraping* is the process of parsing and extracting data from the websites. It is useful techinque when we want to collect data from the websites for our work. 

GitHub is web-based version control and collaboration platform for software developers. It has a page https://github.com/topics where we can find different topics listed on GitHub.

I have built a scraper i.e., [Github_topics_scraper](https://github.com/Abhishek-2505/Github_topics_scraper/blob/main/github_topics_scraper.py) which scrapes the [GitHub Topics](https://github.com/topics) webpage. This scraper can return, either detailed or non-detailed data frame based on the user preferences. 

## Tools Used:

Programming Language: Python

Python Packages: [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Requests](https://docs.python-requests.org/en/latest/), [Pandas](https://pandas.pydata.org/docs/), [Math](https://docs.python.org/3/library/math.html) and [tqdm](https://tqdm.github.io/).

## The scraper function : github_topics_scraper() 

<code>github_topics_scraper()</code>, the scraper function, takes two optional arguments, <code>detailed</code> and <code>records</code>.

* The argument <code>records</code> represents the number of records user want. It can take either Boolean(True/False) or integer inputs. It should be set to “False” to return all the possible records.

* The argument <code>detailed</code> takes Boolean(True/False) inputs and returns detailed data frame if set to "True" else returns non detailed data frame. 

By default the function returns non-detailed data frame with single record.

## Detailed v/s non-detailed data frames:

As mentioned above, the scraper function can return either detailed or non-detailed data frame. 
