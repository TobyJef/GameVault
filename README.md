
# GameVault

Welcome to GameVault. Our aim is to provide a quality website and reliable shopping service for not only gamers but those shopping for their gaming obsessed friends and loved ones. GameVault offers a variety of Games, Consoles and Gaming Accessories.

Visitors to the GameVault website can search and browse our range of products. Or for those that know what they want, filter their product searches or jump straight to their preferred categories from the navbar. The navbar main categories are based on our supported console brand i.e Playstation, Nintendo etc, our shoppers are looking to purchase for, then further expanded into sub categories including consoles, game genres and accessories. Shoppers can add their purchases to the basket which relays a live cost total so they can keep track of their spending before checking out and purchasing their desired items. GameVault also provides our site browsers and customers the opportunity to sign up to our mailing list so they can recieve future communications from us regarding new game and console releases and sale events.

The live link to the GameVault website can be found here: *website link here*

- *Home page screen shot here*

This project, is for a fictitous video game business to consumer e-commerce site of my own design. It is designed to allow customers to browse a range of video game related stock, add their desired purchases to a basket and later check out and purchase the chosen products. Create and log into a customer account, and if they so desire sign up to the GameVault sites mailing list. It will also allow for the business owner to log into the website as the super user, to manage their stock inventory, descriptions and images.

## Contents

The Contents of this site include,

- A base html template, that handles the navbar and footer across all pages. Allowing for the ability to write once and reuse across the site by using block tags.

- The Home page, featuring our masthead image and the GameVault brand name, with site wide navbar and search box, that directs site visitors to the products they are searching for.

- Navbar, 

- Search box, 

- Profile page, is intended for the customer to view their orders

- Reigster, a page that allows users to register an account for the GameVault website.

- Log In, a page that sits along side Register in the navbar that allows users to log in.

- Log Out, This page allows users to log out. It is hidden on the navbar to those that have yet to register/log in to the GameVault website, then once signed in replaces the Register and Log In spots within the navbar.

- Shopping Basket, to store products that customers wish to purchase and displays a live running total.


## User Experience

### Strategy Plane

The primary site goal of GameVault, is to serve as a business to consumer website for a video game retailer. GameVault offers its customers a selection of video games and gaming accessories across all modern gaming consoles. Product inventory is categorised by console and sub categories such as genre. Customers can use the search bar to look for specific items and filter products searches further by price and rating. Products images are displayed to help customers, who may not be confident when shopping for gaming related products to make the correct purchase for a friend or loved one. A basket with a live total is displayed to show the current total to help ensure customers towards sensible spending. Something that can be helpful for those who struggle with impulsive online purchases. 

### Scope Plane

 Agile Planning

 - A Kanban board was created to help breakdown individual Epics and User Stories tasks

*Kanban board screen shot*
*EPICS*
*User Stories*

## Skeleton Plane

To assist with the creation of the GameVault website, I have used the Boutique Ado walkthrough project from The Code Institute as the foundation for GameVault.

## Surface Plane

To assist with the creation of the GameVault website, I have used the Boutique Ado walkthrough project from The Code Institute, for the layout of buttons and menus.
But have chosen my own colour schemes and text styles.

## Business Plan

Website: GameVault.com (Placeholder)

- Mission Statement:

GameVault aims to provide gamers and those shopping for their gamer obsessed loved one an easy to use all in one platform for purchasing the latest video games, consoles and accessories. Supporting all the major console platforms and competitively priced against our competitors such as Game, GameStop and Amazon to name a few. While GameVault is currently in its infancy, our product range only currently focuses on selling physical copies of video games, and can not be as great as our competition. However we desire to eventually grow and expand our product ranges and customer base and then cater to those looking to purchase digital copies of games, PC games, gaming merchandise, toys, collectibles and trading cards. We also aim to allow our customers set up pre-orders and get GameVault into the second hand video game market and offer to competition to the likes of eBay and Cex.

- Target Market: 

Casual and hardcore gamers, collectors, and gaming enthusiasts focusing mainly on the UK market but offering international shipping and delivery to Europe and North America.

- Business Objectives:

Establish a foothold within the UK gaming retail market, last vauled in 2023 at £7.82b up 4.4% from 2022. As per the report published April 2024 from 
[UK Interactive Entertainment](https://ukie.org.uk/news/2024/04/2023VideoGameIndustryValuation).

We aim to do this via the GameVault website (*Insert live link here*) and also through using store fronts on social media initially through our Facebook store, and eventually Instagram and TikTok, which we anticipate will help grow our brand awareness. With future plans of using influencer marketing, and partnerships within the gaming community.

(*Screenshot of GameVault Facebook store here*)

We also anticipate additional sales from our exisiting customer base through the use of promotions and invitations to exclusive events offered exclusively via our newsletter.


## Features

- A navbar that provides direction to customers to all the pages across the site. Home, All Products and individual product pages, 
   Shopping Basket, Register, Log In and Log Out.
- A searchbar for shoppers to refine their search for a product.



## Database Design

The database hosted by ElephantSQL, was designed to capture the essential information given by a user for the site with this particular business to consumer business model. These categories included: Console, Genre, Price. 

The plan for the data within the database was to have two seperate views, one for the logged in user so they can view and manage their own booking/s, and also one for the business owner to view all collective bookings from within that database.

## Technologies

- HTML5, CSS3, JavaScript
- Python
- Django
- Bootstrap 5.0
- Postgre ElephantSQL to handle the inventory database
- Allauth for new user account registration
- Balsamiq wireframes
- [Json Formatter](https://jsonformatter.org/)
- Jquery 3.7.1
- django-crispy-forms==1.14.0
- Stripe
- django countries 7.2.1
- Mailchimp



## Testing

- Bugs


## Deployment

- Local Deployment

    * Clone the repository from GitHub by clicking the "Code" button and copying the URL.
    * Open your preferred IDE and open a terminal session in the directory you want to clone the repository to.
    * Type git clone followed by the URL you copied in step 1 and press enter.
    * Install the required dependencies by typing pip install -r requirements.txt in the terminal.
    * Note: The project is setup to use environment variables. You will need to set these up in your local environment. See Environment Variables for 
        more information.
    * Connect your database of choice and run the migrations by typing python manage.py migrate in the terminal.
    * Create a superuser by typing python manage.py createsuperuser in the terminal and following the prompts.
    * Optional: Fixtures for Product-related models are included in the project in the core/fixtures directory. To add pre-populated data to the 
        database, run python manage.py loaddata core/fixtures/[fixture_name].json.
    * Run the app by typing python manage.py runserver in the terminal and opening the URL in your browser.

- Heroku Deployment

    * Login to the Heroku dashboard and create a new app.
    * Connect your GitHub repository to your Heroku app.
    * In the Settings tab, ensure that the Python Buildpack is added.
    * Set environment variables in the Config Vars section of the Settings tab.
    * In the Deploy tab, enable automatic deploys from your GitHub repository.
    * Click the "Deploy Branch" button to deploy the app.
    * Once the app has been deployed, click the "Open App" button to view the app.
    * If using S3, you will need to set up an S3 bucket and add the environment variables to your Heroku app.

- Environment Variables

    * For local deployment, you will need to create a .env file in the root directory of the project and set the environment variables in this file.
    * For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.
    * You need to define the following variables:
         If using a Postgres database:
            DATABASE_URL - the URL for your Postgres database.
            NAME - the name of your database.
            USER - the username for your database.
            PASSWORD - the password for your database.
            HOST - the host for your database.
            PORT - the port for your database.
        Django settings:
            SECRET_KEY - the secret key for your Django project.
            DEBUG - set to True for development, False for production.
        If using S3:
            USE_S3 - set to True to use S3, False to use local storage.
            AWS_ACCESS_KEY_ID - your AWS access key ID.
            AWS_SECRET_ACCESS_KEY - your AWS secret access key.
            AWS_STORAGE_BUCKET_NAME - the name of your AWS S3 bucket.
        If using Mailchimp (Newsletter form):
            MAILCHIMP_API_KEY - your Mailchimp API key.
            MAILCHIMP_DATA_CENTER - your Mailchimp-assigned data center
            MAILCHIMP_LIST_ID - The ID of your mail-list.
        For Stripe checkout:
            STRIPE_PRIVATE_KEY - your private API key.

- Additional Stripe Configuration

    Additional to adding your own STRIPE_PRIVATE_KEY, you must also set the return_url and public key in checkout.js

## Credit

- Product images used in this project have been collected from [Amazon.co.uk](www.amazon.co.uk).
- Product prices and ratings have been collected from [Amazon](www.amazon.co.uk) and [Nintendo](www.store.nintendo.co.uk).
- Product descriptions used have been collected from [Amazon](www.amazon.co.uk) and [Smyths Toys](https://www.smythstoys.com/uk/en-gb). 

- The product images, pricing, ratings and descriptions used from 3rd party sites have been used for educational purposes only.

- Tutor Assistance, 




