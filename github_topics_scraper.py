# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:41:24 2021

@author: Abhishek
"""

# importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import math
#from tqdm.notebook import tqdm #(for Jupyter notebook)
from tqdm import tqdm   # for all other IDEs

def github_topics_scraper(detailed=False, records=True):
    
    # checking for the correct data type
    if type(detailed)!= bool:
        raise Exception("Expected boolean input for argument 'detailed' but got{}".format(type(detailed)))
    if type(records) != int:
        if type(records)==bool:
            pass
        else:
            raise Exception("Expected integer or boolean input for the argument 'records' but got{}".format(type(records)))
     
    print('Scrapping GitHub topics{}...'.format(' in detail' if detailed==True else ''))
    
    # creating variables
    page_content=''  # to store page content
    start = 1            # 'start' - GitHub topics pages start from 1 & go till 6
    end = math.ceil(records/30) if type(records)==int else (1 if records==True else 6 )
    # 'end' calculates how many pages to load based on the required no of records
    
    while start<=end:
        url = 'https://github.com/topics?page={}'.format(start) # creating URL for the specific page
        r =requests.get(url)
        if r.status_code != 200:    #failed to load the page
            start-=1                #reloading the page once again by decrementing the the start value
        else:
            page_content += '\n' + r.text
        start+=1
    soup = BeautifulSoup(page_content,'html.parser')

    # extracting topic titles
    topic_ptags = soup.find_all('p',{'class':'f3 lh-condensed mb-0 mt-1 Link--primary'}, limit=records)
    topics =[]
    for tag in topic_ptags:
        topics.append(tag.text)
        
    # extracting description
    descr_ptags =soup.find_all('p',{'class':'f5 color-text-secondary mb-0 mt-1'}, limit=records)
    topic_descs =[]
    for tag in descr_ptags:
        topic_descs.append(tag.text.strip())
        
    # extracting topic urls
    topic_url_tags =soup.find_all('a',{'class':'d-flex no-underline'}, limit=records)
    topic_urls =[]
    for tag in topic_url_tags:
        topic_urls.append('https://github.com' + tag['href'])
        
    # creating a dictionary to store the scraped data
    topics_dict = {
        'Topics': topics,
        'Description': topic_descs,
        'Topic_URL': topic_urls
    }
    
    if records>len(topics):
        print('There are only {} topics present on GitHub'.format(len(topics)))

    # if want detailed data, this will execute
    if detailed:
        # creating progress bar using tqdm
        pbar = tqdm(total=len(topic_urls))
                
        # creating another dictionary to strore the data of popular repositories & their details
        pop_repo_details ={'Popular_Repository':[],'PR_Username':[],'PR_URL':[],'Stars':[],
                       'Forks':[],'Commits':[],'Last_committed':[]}
        
        # scraping popular repo name, username & URL (popularity - based on star counts)
        i=0
        while i<len(topic_urls):   # topic_urls -> scraped already, utilizing to scrape remaining data
            url = topic_urls[i] + '?o=desc&s=stars'  # creating url based on the topic
            r =requests.get(url)
            if r.status_code !=200:    # failed to load the page
                i-=1                   # loading once again
            else:     
                pr_soup1 = BeautifulSoup(r.text,'html.parser')  # creating beautiful soup object
                
                # popular repo name, usernam and URL, loacted in a-tag of first h3-tag
                h3_tags = pr_soup1.find_all('h3',{'class':'f3 color-text-secondary text-normal lh-condensed'}, limit=1)
                atags = h3_tags[0].find_all('a')
                
                # extracting popular repo name, usernam and URL
                pop_repo_name = atags[1].text.strip()               # repo name
                pr_username = atags[0].text.strip()                 # repo username
                pr_url ='https://github.com' + atags[1]['href']     # repo URL     

                # scraping number of stars, forked count, total commits and last committed time using pr_url
                r =requests.get(pr_url)
                if r.status_code != 200:
                    i-=1
                else:
                    pr_soup2 =BeautifulSoup(r.text, 'html.parser')

                    # locating tags for star counts, forks counts, commits and last committed time
                    star_atags = pr_soup2.find_all('a',{'class':'social-count js-social-count'})
                    forks_atags =pr_soup2.find_all('a',{'class':'social-count'})
                    commit_span_tags = pr_soup2.find_all('span',{'class':'d-none d-sm-inline'})
                    last_commit_atag =pr_soup2.find_all('a',{'class':'Link--secondary ml-2'})

                    # extracting star counts, forks counts, commits and last committed time
                    stars = int(star_atags[0]['aria-label'].split()[0])
                    forks = int(forks_atags[1]['aria-label'].split()[0])
                    commits = int(commit_span_tags[1].strong.text.replace(',', '')) if len(commit_span_tags)==2 else int(commit_span_tags[0].strong.text.replace(',', ''))
                    last_updated = last_commit_atag[0].find_all('relative-time')[0]['datetime'] if len(last_commit_atag)>=1 else None

                    # appending scraped data for popular repository to the dictionary
                    pop_repo_details['Popular_Repository'].append(pop_repo_name)
                    pop_repo_details['PR_Username'].append(pr_username)
                    pop_repo_details['PR_URL'].append(pr_url)
                    pop_repo_details['Stars'].append(stars)
                    pop_repo_details['Forks'].append(forks)
                    pop_repo_details['Commits'].append(commits)
                    pop_repo_details['Last_committed'].append(last_updated)
                    
                    pbar.update(1) # updating the progress bar
            i+=1    # loading next page
            
        # closing the progress bar once completed
        pbar.close()
           
        # merging the dictionaries "topics_dict" and "pop_repo_details"
        topics_dict.update(pop_repo_details)
        
    print('Scrapping completed successfully!!!')
    
    # creating a dataframe of the scraped data
    return pd.DataFrame(topics_dict)

df = github_topics_scraper(True, False)
#df.to_csv('GitHub_topics_detailed.csv')
