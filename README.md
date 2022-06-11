# Obi I. - Shopify Backend Challenge 2022 - Logistics Company Webapp

### Demo Links

Hosted on Heroku: [https://shopify-challenge-2022-obi.herokuapp.com/](https://shopify-challenge-2022-obi.herokuapp.com/)

Deployed on Replit (server not automatically booting in replit enviornment when url is accessed): [https://6905385c-248c-4c2f-8c4a-c28ad949278e.id.repl.co](https://6905385c-248c-4c2f-8c4a-c28ad949278e.id.repl.co/)

## **What it Does**

This webapp is a simple demonstration of backend CRUD fundamentals. This was built as my submission for Shopify’s Fall 2022 Backend Intern Challenge and it allows a user to:

- Create inventories & shipments
- Assign inventories to shipments
- Edit & delete them
- View all of them in list view inside tables.

## How it works

The site is very simple - simply create the inventories and shipments you want using the forms on the right side of the screen and view them all in the tables on the left side

When creating a shipment, you can select multiple inventories to assign to it. 

Then finally view all the objects you’ve made and edited in the tables on the left and boom, you’ve successfully used the site to do some basic logistics management.

## How to Run Locally
1. Need the following installed globally on your computer
- pip
- pipenv
2. Actitvate the virtual environment
- Run `pipenv shell` in the folder of the repo
- Run `pipenv install -r requirements.txt`
3. Get the database up to speed (in case theres changes that havent been migrated - always wise to do on first boot up)
- `python manage.py makemigrations`
- `python manage.py migrate`
4. Run the local test local test server
- `python manage.py runserver`
