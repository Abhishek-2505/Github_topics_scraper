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

<h6>Resources used:</h6> Python, Pandas, BeautifulSoup, Requests

## Data Locating:

The pictures attached below shows where(tag) we can find the required data.

<i>Note: All the pictures attached below represent the data for the first row i.e for "3D" topic.</i>


Topics, Description and Topic_URL (Basic topics information) -
![](https://github.com/Abhishek-2505/Github-Topics-Details-Web-scraping/blob/main/images/Topic_info.jpg)

Popular_Repository, Username (Basic repository information)-
![](https://github.com/Abhishek-2505/Github-Topics-Details-Web-scraping/blob/main/images/Repository_info.jpg)

Number_Of_Stars(for each popular repository) -
![](https://github.com/Abhishek-2505/Github-Topics-Details-Web-scraping/blob/main/images/Stars.jpg)

Forked_Count(Number of times forked that repository) -
![](https://github.com/Abhishek-2505/Github-Topics-Details-Web-scraping/blob/main/images/Forks.jpg)

Total_Commits(Number of times commited) - 

![](https://github.com/Abhishek-2505/Github-Topics-Details-Web-scraping/blob/main/images/Commits.jpg)

Last_Commited(Time when last commited the repository) -
![](https://github.com/Abhishek-2505/Github-Topics-Details-Web-scraping/blob/main/images/Last_updated.jpg)


<h6>Required data:</h6>

Sample output:

![](https://github.com/Abhishek-2505/Github-Topics-Details-Web-scraping/blob/main/images/sample_output1.png)
![](https://github.com/Abhishek-2505/Github-Topics-Details-Web-scraping/blob/main/images/sample_output2.png)

To view complete data(.csv) files [click here](https://github.com/Abhishek-2505/Github-Topics-Details-Web-scraping/tree/main/Output%20CSVs).
