
# GameVault

Welcome to The Pizza Project. Our aim is to provide the local and surrounding communities of Bristol with the freshest and highest quality pizza imaginable, outside of Italy or the pizza hotspots of the USA. We craft out pizza sauce and dough every morning, then load up our mobile pizza truck and head out on the open road where we top and cook our pizzas to order on site. Wether that is at your front door, wedding venue, high street or charity event. If we can drive there, we can cook there. Our pizzas are cooked in a wood fired pizza oven in the back of our pizza truck to ensure that authentic pizza experience.
 
The live link to The Pizza Project website can be found here: *website link here*

- *Home page screen shot here*

This project, based on a fictitous mobile pizza restaurant of my own deisgn but inspired by a company with a similar business model from the local area of my home town in Bristol. Is designed to allow customers to create and log into an account, and to book The Pizza Project mobile truck on a selected date, and have the option to leave a comment on their booking. As well as for the business owner to log into the website as the super user, to manage their bookings and menu.

## Contents

The Contents of this site include,

- A base html template, that handles the navbar and footer across all pages. Allowing for the ability to write once and reuse across the site by using block tags.

- The Home page, featuring our masthead image and brand name, with a short introduction to The Pizza Project. It was originally intended to host the booking form also, but this was eventually moved to the profiles page.

- The Menu page features a custom WePik image used for the menu itself. Designed to be straight to the point, but with scope to possibly improve upon this page in a future release by adding menu items, prices and nutritional information into a database and then displayed to allow for better customisation by the site owner.

- Enquiries is a basic page found on most sites with similar buisness models. Featuring some images and brief snippets of text expanding some of what The Pizza Project can offer their customers, not mentioned in the Home page.

- Profile page, is intended for the Business Owner to view the collective of all the bookings made.

- User Bookings was intended to allow logged in users to make a booking, show those booking/s and also edit and delete them if required.

- Reigster, a page that allows users to register an account for The Pizza Project.

- Log In, a page that sits along side Register in the navbar that allows users to log in.

- Log Out, This page allows users to log out. It is hidden on the navbar to those that have yet to register/log in to The Pizza Project Website, then once signed in replaces the Register and Log In spots within the navbar.


## User Experience

### Strategy Plane

The primary site goal of GameVault, is to serve as a business to consumer website for a video game retailer. GameVault offers its customers a selection of video games and gaming accessories across all modern gaming consoles. Product inventory is categorised by console, and customers can filter products further by price and rating. Products images are displayed to show customers  of similar mobile pizza , a menu and a booking form that could be submitted by users following registering/logging into the website, where they could also edit and delete their booking providing the were still logged in.

### Scope Plane

 Agile Planning

 - A Kanban board was created to help breakdown individual Epics and User Stories tasks

 *Kanban board screen shot*
*EPICS*
*User Stories*

## Skeleton Plane

## Surface Plane

Making use of Bootstrap 5.0, I chose to use the Grayscale bootstrap theme from StartBootstrap.com. This decision was made to help reduce the required amount of custom css and javascript that would normally be required.


## Features

- A navbar that provided direction to all the pages across the site. Home, Menu, Enquiries, Profile, My Booking, Register, Log In and Log Out.

- A planned booking form to capture user information for bookings, with CRUD functionality.

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



## Testing

- Bugs


## Deployment

Site deployment was carried out via Heroku.

## Credit

- Proudct images have been taken from Amazon.co.uk, the images used are for educational purposes only.

- Tutor Assistance, 




