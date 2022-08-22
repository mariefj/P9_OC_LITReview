# LITReview #

1.  [Description](#description)
2.  [Use](#use)
    1.  [setup](#setup)
    2.  [features](#features)

## 1. Description <a name="description"></a> ##

This app has been realized as part of a project of the course
'Application developer - Python' of OpenClassrooms.


The app allows a community of users to consult or request a book review on demand.
It has two main use cases: 
- People requesting reviews on a particular book or article
- People looking for interesting articles and books to read, based on the reviews of others

This app is built with Django. The database is a SQLite file : db.sqlite3

## 2. Use <a name="use"></a> ##

#### SETUP : <a name="setup"></a> ####

First, start by cloning the repository:

```
git clone git@github.com:mariefj/P9_OC_LITReview.git
```

- Access the project folder
```
cd P9_OC_LITReview
```

- Create a virtual environment
```
python -m venv env
```

- Enable the virtual environment
```
source env/bin/activate
```

- Install the python dependencies on the virtual environment
```
pip install -r requirements.txt
```

- Start
```
python manage.py runserver
```

- Open in browser the following address
```
http:/127.0.0.1:8000
```

#### FEATURES : <a name="features"></a> ####

This Django project contains 3 apps : authentication - feed - follow, which represent the main features.

##### Sign in or sign up #####
First, you can sign in with one of the current user, for example - pseudo : sarah + password : aqwzsx741 - or create a new account.
Some users are already created to fill the app with examples of reviews and tickets.

##### Navigate #####
You can navigate through the app using the navigation bar at the top right.

##### Home #####
At home page (Accueil), you will see all your tickets and reviews, and the ones of the people you follow.
The 2 top button allows you to create a ticket (ask for a review) or create a review.
You can also create a review for a user's ticket.

##### Posts #####
At posts page (Posts), you will see all your tickets and reviews. You can update or remove them.

##### Follows #####
At follows page (Abonnements), you can follow other users and see the ones you already follow and choose to unfollow them or not.
You also see the people following you.
