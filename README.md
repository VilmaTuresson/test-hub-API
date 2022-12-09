# TestHub API

This is the API built for the TestHub application.
Link to deployed page LÄNK TILL API

## Table of contents
1. [Database](#database)
    - [Modules](#modules)

2. [USED TECHNOLOGY](#used-technology)
    - [Languages](#languages)
    - [Libraries & Tools](#libraries-tools)
    - [Frameworks](#frameworks)

3. [DEPLOYMENT](#deployment)
    - [Creating Heroku App](#creating-heroku-app)
    - [Connecting to GitHub](#connecting-gitHub)

4. [TESTING](#testing)
    - [Manual Testing](#manual-testing)

5. [Credits](#credits)


## Database

### Models

**Profiles**

Fields in the Profile model:

- Owner, One-to-one field connected to User
- Created_at, Date-time field set with auto-now-add as true
- Updated_at, Date-time field set with auto-now as true
- Username, Text field with a max length of 255 characters
- Profile_img, Image field set with a default URL, linked at Cloudinary

**Comments**

Fields in the Comments model:

- Owner, set with foreign-key connected to User
- Post, set with foreign-key connected to Post
- Created_at, Date-time field set with auto-now-add as true
- Content, Text field with a max length of 500 characters

**Followers**

Fields in the Followers model:

- Owner, set with foreign-key connected to User with a related name of “following”
- Followed, set with foreign-key connected to User with a related name of “followed”
- Created_at, Date-time field set with auto-now-add as true

**Likes**

Fields in the Followers model:

- Owner, set with foreign-key connected to User
- Post, set with foreign-key connected to Post with a related name of “likes”
- Created_at, Date-time field set with auto-now-add as true

**Posts**

Fields in the Followers model:

- Owner, set with foreign-key connected to User
- Created_at, Date-time field set with auto-now-add as true
- Updated_at, Date-time field set with auto-now as true
- Title, Char field with a max length of 255 characters
- Content, Text field with a max length of 2000 characters
- Image, Image field set with a default URL, linked at Cloudinary

## Used technologies

### Languages
- Python

### Frameworks 
- Django REST Framework was used to build the back-end API

### Libraries & Tools
- Cloudinary to store static files
- Git was used for version control via Gitpod terminal to push the code to GitHub
- GitHub was used as a remote repository to store project code
- Django AllAuth was used for user authentication
- Psycopg2 was used as a PostgreSQL database adapter for Python
- PostgreSQL – deployed project on Render uses a PostgreSQL database

## Deployment
 
**This project was deployed through Heroku using the following steps:**

**Creating Heroku App**
+ Log into Heroku
+ Select 'Create New App' from your dashboard
+ Choose an app name (if there has been an app made with that name, you will be informed and will need to choose an alternative)
+ Select the appropriate region based on your location
+ Click 'Create App'

**Connecting to GitHub**
+ From the dashboard, click the 'Deploy' tab towards the top of the screen
+ From here, locate 'Deployment Method' and choose 'GitHub'
+ From the search bar newly appeared, locate your repository by name
+ When you have located the correct repository, click 'Connect'


**Environment Variables**
+ Click the 'Settings' tab towards the top of the page
+ Locate the 'Config Vars' and click 'Reveal Config Vars'
+ Add the variables needed


**Heroku Postgres Database**
+ Go to the resources tab in Heroku.
+ In the Add-ons search bar look for Heroku Postgres & select it.
+ Choose the Hobby Dev-Free option in plans.
+ Click submit order form.
+ Go back to the build environment and install 2 more requirements:
  + ```pip3 install dj_databse_url```
  + ```pip3 install psycopg2```
  make sure to add these to the requirements file using ```pip3 freeze > requirements.txt```


## CREDITS
 
**Amy O'Shea**
- For the Heroku deployment process, taken from the README file of this repositiry
- [Amy O'Sheas repository](https://github.com/AmyOShea/MS4-ARTstop#deployment)
