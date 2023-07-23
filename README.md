# Project Idea - The Scrub Hub 
Deployed Link - https://spring-glade-2620.fly.dev/projects/

> * Project Description 
Crowdfunding Site to refit old buses with plumbing & shower facilities for a mobile shower service for the homeless. 
We need the public to pledge / donate to having buses for funding to upgrading with plumbing facilities. 
Current objective is to get enough funding for 2 buses. 
Once these are up & going and also if this proves it self to be successful, further request for pledges / funding to fit more buses. 

> * Tech Utilized 
Back End Project utlising
> * Python | #DRF & deployed via FlyIO - https://fly.io/ || Back end URL - https://spring-glade-2620.fly.dev/projects/

![image](https://user-images.githubusercontent.com/113986306/232380163-b27008a8-5b7e-472d-becd-84c837167996.png)


# TARGET AUDIENCE - ALL / CHARITY ORGANISATIONS / VOLUNTEERS 
***Purpose***
To provide a Mobile Shower Service for the homeless people in Perth. 
This will be done by fitting old buses with hot shower facilities. 
***Requirements***
Amount to raise per bus - $20,000
Funding for bus to be fitted with showers & basins to be tapped into hot water. 

***Future State***
Funding for storage racks to be fitted 
Volunteer to pledge time or donations of clothing, toiletries.
Doctor Services 

## Features

SIMPLE SITE WITH LANDING PAGE, ABOUT US, PURPOSE, GOAL & MISSIONS
PROJECT SITE WITH 2 PROJECTS 
USERS CAN CREATE ACCOUNTS TO PLEDGE, ADD COMMENTS. 

### User Accounts

- [X] Username
- [X] Email Address
- [X] Password

### Project

- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
  - [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Create - ADDED 
  - [X] Retrieve - ADDED 
  - [ ] Update - TO BE IMPLEMENTED | CURRENTLY CODE IS UNDER CONSTRUCTION 
  - [ ] Destroy - TO BE IMPLEMENTED | CURRENTLY CODE IS UNDER CONSTRUCTION 
- Pledge
  - [X] Create - ADDED 
  - [X] Retrieve - ADDED 
  - [ ] Update - TO BE IMPLEMENTED | CURRENTLY CODE IS UNDER CONSTRUCTION  
  - [ ] Destroy - TO BE IMPLEMENTED | CURRENTLY CODE IS UNDER CONSTRUCTION 
- User
  - [X] Create - ADDED 
  - [X] Retrieve - ADDED 
  - [ ] Update - TO BE IMPLEMENTED | CURRENTLY CODE IS UNDER CONSTRUCTION 
  - [ ] Destroy - TO BE IMPLEMENTED | CURRENTLY CODE IS UNDER CONSTRUCTION 

### Implement suitable permissions

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Limit who can create | ADDED ONLY SUPERUSER / ADMIN ONLY FOR PROJECTS / PERMISSIONS TO BE REFINED
  - [ ] Limit who can retrieve | ALL CAN VIEW PROJECTS 
  - [X] Limit who can update | ADDED ONLY SUPERUSER / ADMIN ONLY FOR PROJECTS / PERMISSIONS TO BE REFINED
  - [X] Limit who can delete | ADDED ONLY SUPERUSER / ADMIN ONLY FOR PROJECTS / PERMISSIONS TO BE REFINED
- Pledge
  - [X] Limit who can create | ADDED 
  - [ ] Limit who can retrieve | NOT ADDED AS ALL CAN VIEW 
  - [X] Limit who can update | ADDED 
  - [X] Limit who can delete | ADDED 
- Users
  - [ ] Limit who can retrieve | TO BE IMPLEMENTED | CURRENTLY CODE IS UNDER CONSTRUCTION
  - [X] Limit who can update | ADDED 
  - [X] Limit who can delete | NOT ADDED AT THIS STAGE. UNSURE AS TO WHETHER USERS CAN DELETE THEIR OWN ACCOUNTS.

### Implement relevant status codes

- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404

### Handle failed requests gracefully 

- [X] 404 response returns JSON rather than text

### Use token authentication

- [X] impliment /api-token-auth/

## Additional features

- [X] {TOTAL PLEDGES 1}

{{ SUM OF ALL PLEDGES FOR EACH OF THE PROJECTS}}

- [X] {COMMENTS ON PROJECTS}

{{ ALLOWS THOSE LOGGED IN TO BE ABLE TO ADD COMMENTS TO THE PROJECTS}}

- [X] {FILTERS TO PLEDGES, COMMENTS & USERS}

{{ FILTERS TO PLEDGES, COMMENTS & USER }}

### External libraries used

- [X] django-filter - FILTERS -     'DEFAULT_FILTER_BACKENDS'
        'django_filters.rest_framework.DjangoFilterBackend',


## Part A Submission

- [ ] A link to the deployed project - https://spring-glade-2620.fly.dev/projects/
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Your refined API specification and Database Schema.

### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

1. Create User

```shell
curl --request POST \
  --url https://spring-glade-2620.fly.dev/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"email": "not@myemail.com",
	"password": "not-my-password"
}'
```

2. Sign in User

```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"password": "not-my-password"
}'
```

3. Create Project

```shell
curl --request POST \
  --url https://spring-glade-2620.fly.dev/projects/ \
  --header 'Authorization: Token 5b8c82ec35c8e8cb1fac24f8eb6d480a367f322a' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Donate a cat",
	"description": "Please help, we need a cat for she codes plus, our class lacks meows.",
	"goal": 1,
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": true,
	"date_created": "2023-01-28T05:53:46.113Z"
}'
```
