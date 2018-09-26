
# Scrapy Spider

**This scrapy spider was used to quickly scrape information and download links of around 900+ paid courses from the course website https://freetutorials.us worth more than $ 9000 .
The same code was then later slightly modified to scrape all the courses from https://www.freecoursesonline.me/.**

![Output Image](https://github.com/revantg/scraping_courses/raw/master/courses/cloud_flare.png)
The main challenge for scraping this website was that the website was using CloudFlare Protection against scraping and other DOS attacks which made the scraping borderline impossible with the naive website-scraping practices. Special Scrapy-Middlewares have been implemented to overcome this.

# Usage / Installation

## Architecture
```bash
.
├── courses
│   ├── cloud_flare.png
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── items.py
│   ├── items.pyc
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── items.cpython-36.pyc
│   │   ├── pipelines.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── settings.py
│   ├── settings.pyc
│   └── spiders
│       ├── freetutorials.py
│       ├── freetutorials.pyc
│       ├── __init__.py
│       ├── __init__.pyc
│       └── __pycache__
│           ├── freetutorials.cpython-36.pyc
│           └── __init__.cpython-36.pyc
├── courses_data.json
├── final_log.txt
├── log_final.txt
├── requirements.txt
└── scrapy.cfg

4 directories, 24 files
```
## Installation
This section will guide you through a series of steps to setup this project on your computer.

### Requirements

Make sure you have the following installed to proceed further into the installation process

 - Python 3.5 (or above)
 - Python Package Manager - ( PIP )
 - Git 

### Install Dependencies

All the dependencies and Packages have been conveniently bundles into a `'requirements.txt'` file for a smooth installation and have the Project Up and running on your machine with minimal effort and time.
Run the following commands from the terminal .

Get a complete copy of the project by cloning into a suitable directory

    git clone https://github.com/revantg/scraping_courses.git
  
 Install all the dependencies by running the command from the terminal.

    sudo pip install -r requirements.txt

## Usage

 - For running the spider run the following command from the terminal.
```
scrapy crawl freetutorials -o courses_data.json
```
This generates the following files

-  ```log_final.txt``` - Complete output of the scrapy spider
- ```courses_data.json``` - Scraped data of all the courses
## Output

This script generates data for a course in the following format
```json
[
    {
        "course_title": "Git a Web Developer Job: Mastering the Modern Workflow",
        "course_views": "38,406",
        "course_img": "https://udemy-images.udemy.com/course/240x135/818990_57c0_3.jpg",
        "course_desc": "Learn Git, GitHub, Node.js, NPM, Object-oriented JavaScript, ES6, webpack, Gulp, BEM and Job Interview Tips",
        "course_tags": "BEM",
        "course_link": "https://www.freetutorials.us/git-a-web-developer-job-mastering-the-modern-workflow-udemy-free-download-1/",
        "course_published": {
            "datetime-object": "2017-12-18 13:32:47",
            "formatted_date": "18 December 2017",
            "formatted_time": "13:32:47",
            "formatted_date_time": "18 December 2017 13:32:47",
            "iso_string": "2017-12-18T13:32:47+00:00"
        },
        "course_updated": {
            "datetime-object": "2018-06-26 15:53:13",
            "formatted_date": "26 June 2018",
            "formatted_time": "15:53:13",
            "formatted_date_time": "26 June 2018 15:53:13",
            "iso_string": "2018-06-26T15:53:13+00:00"
        },
        "course_size": "2.68GB",
        "course_category": "Development",
        "course_download_link": "https://www.freetutorials.us/wp-content/uploads/2017/12/FreeTutorials.Us-Udemy-git-a-web-developer-job-mastering-the-modern-workflow.torrent",
        "related_posts": [
            [
                "React JS \u2013 Mastering Redux",
                "https://www.freetutorials.us/react-js-mastering-redux-1/"
            ],
            [
                "The Complete JavaScript Course \u2013 Beginner to Professional",
                "https://www.freetutorials.us/the-complete-javascript-course-beginner-to-professional-3/"
            ],
            [
                "Node.js: The Complete Guide to Build RESTful APIs (2018)",
                "https://www.freetutorials.us/node-js-the-complete-guide-to-build-restful-apis-2018/"
            ],
            [
                "Complete Git and GitHub Masterclass : Beginner to Git Expert",
                "https://www.freetutorials.us/complete-git-and-github-masterclass-beginner-to-git-expert-1/"
            ]
        ],
        "udemy_link": "https://www.udemy.com/git-a-web-developer-job-mastering-the-modern-workflow/"
    }
]
```
with the following parameters
- ``course_title - Name of the course``
- ``course_views - Total number of users who viewed this course`` 
- ``course_img - Link to the course image``
- ``course_desc - Description of the course``
- ``course_tags - Tags for the course``
- ``course_published - Contains data about when the course was published``
- ``course_updated - Contains the data about when was the course updated last time``
- ``course_size - Size of the course``
- ``course_link - Link to the course on the website``
- ``course_category - Category to which the course belongs``
- ``course_download_link - Download link to the course. (.torrent or magnet)``
- ``related_posts - Similiar Courses``
- ``udemy_link - Link to the course on udemy``

# Technical Details


## Middlewares

```python
DOWNLOADER_MIDDLEWARES  =  {
# The priority of 560 is important, because we want this middleware to kick in just before the scrapy built-in `RetryMiddleware`.
'scrapy_cloudflare_middleware.middlewares.CloudFlareMiddleware':  560
}
```
## Items
```python
"course_title" : string
"course_views" : string of integer
"course_img" : link
"course_desc" : string
"course_tags" : list of strings
"course_published" :
	"datetime-object": datetime.datetime object
	"formatted_date" : date in format "%d %B %Y"
	"formatted_time" : time in format "%H:%M:%S"
	"formatted_date_time": date + time in format "%d %B %Y %H:%M:%S"
	"iso_string": ISO-8601 String of standard format "%Y-%M-%DT%H:%M:%S+%z"
"course_updated"
	"datetime-object": datetime.datetime object
	"formatted_date" : date in format "%d %B %Y"
	"formatted_time" : time in format "%H:%M:%S"
	"formatted_date_time": date + time in format "%d %B %Y %H:%M:%S"
	"iso_string": ISO-8601 String of standard format "%Y-%M-%DT%H:%M:%S+%z"
"course_size" : string
"course_link" : link
"course_category" : list of strings
"course_download_link" : magnet or a.torrent link
"related_posts" : list of courses in format [course_name, course_link]
"udemy_link" : link
```

## Pipelines
```python
ITEM_PIPELINES  =  {
'courses.pipelines.CoursesPipeline':  300,
}
```


