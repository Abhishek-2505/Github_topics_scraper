# Github Topics Details -Web scraping : Project Overview

![](https://github.com/Abhishek-2505/Github-Topics-Details-Web-scraping/blob/main/images/web%20scraping%20pic.jpg)

## Introduction:

Web scraping is the process of parsing and extracting data from the websites. It is very useful when we want to collect data from the websites for our work. 

I'm going to scrap Github's topics page(https://github.com/topics) to know-
* Different topics present on Github.
* For each topics,
    * topic titles, description and topic URL.
    * popular repository.
    * And for each popular repositories-
        * username(created by).
        * number of stars
        * URL of the repository.
        * number of times forked.
        * number of times commited.
        * last commited time.

<h6>Required data format:</h6>

|Topics|Descripton|Topic_URL|Popular_Repository|Username|Repository_URL|Number_Of_Stars|Forked_Count|Total_commits|Last_Commited|
|--|--|--|--|--|--|--|--|--|--|
|3D|--descr--|https://github.com/topics/3d| three.js|mrdoob |https://github.com/mrdoob/three.js |73300| 28708|37892|2021-08-07T10:36:49Z|
|||||||||||

<h6>Resources used:</h6>
Python, Pandas, BeautifulSoup, Requests

