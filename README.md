# [Liquid Smoke](https://liquid-smoke.herokuapp.com/)
## Shop for high-quality candles and essential oils at our online store. We offer a wide selection of scents to suit any taste.

<img src="static/images/multy-device.png"> 

# Table of contents
* [Design and Build](#design-and-build)
    * [Planning](#the-planning-for-this-project-was-based-on-this-idea)
    * [Model diagrams](#model-diagrams)
    * [Marketing](#marketing-has-been-made-by-a-facebook-page)
    * [Agile](#agile)
* [Features](#features-ux-design)
    * [Navbar](#navbar)
    * [Footer](#footer)
    * [Products](#products)
    * [Candles](#candles)
    * [Essential oils](#essential-oils)
    * [Specials](#specials)
    * [Basket](#basket)
    * [Checkout](#checkout)
    * [Order detail](#order-detail)
    * [Profile](#profile)
    * [Sign in/ Register](#sign-inregister)
    * [Product management](#product-management)
    * [FAQ](#faq)
    * [404](#404-page)
* [Future Features](#features-to-be-implemented)
* [Technology used](#technology-used)
* [Framerowks and libraries](#frameworks-and-libraries-used)
* [Agile methodoloy](#agile-methodology)
    * [User stories](#agile-user-stories)
    * [Tasks](#agile-tasks)
* [Testing](#testing)
    * [Lighthouse](#lighthouse)
    * [Validation](#validation)
    * [Unit testing](#automated-testing-tdd)
    * [Manual testing](#manual-testing)
    * [Responsive](#responsive)
* [Bugs](#bugs)
    * [Django notes](#django-notes)
* [Development and deployment](#development-and-deployment)
    * [Local development](#local-development)
    * [Heroku deployment](#heroku-deployment)
    * [Deployment checklist](#deployment-checklist)
    * [Forking and cloning](#forking-a-repository)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)
* [Other sources](#other-sources)


# Design and build
### This is a Business to Customer( B2C ) focused application. The intent of this website is to sell candles and essential oils to customers for a single payment at checkout.

## The planning for this project was based on this idea: 

* As a customer: 
    * Open the app to see the products,
    * Add items to the basket,
    * Checkout,
    * Pay and provide delivery details,
    * Get a confirmation email with my order.
    * See past orders
    * Repeat

## Wireframes

<img src="static/images/wireframe.png"> 

<img src="static/images/wireframe-products.png"> 


## Model diagrams
### Graphviz diagram
<img src="static/images/models.png"> 

[Graphviz SVG file](https://github.com/EddieStn/liquid-smoke/tree/main/static/images/models.svg)

To generate the diagram follow the next steps:
* pip install django_extensions
* sudo apt-get install graphviz 
* pip install graphviz
* add django_extensions to installed apps in settings.py
* generate a dot file with all your models `python3 manage.py graph_models -a > models.dot`
* convert it into a png `dot -Tpng models.dot -o models.png`

NOTE* Gitpod doesn't run on your machine, it runs on a Linux virtual server, so you can use the Linux commands in the gitpod console.

## Marketing has been made via a [Facebook page](https://www.facebook.com/profile.php?id=100092371081770)

<img src="static/images/fb-page.png"> 

## Agile
### This Project was built following agile methodology and practices
[User stories](#agile-user-stories) further down.

# Features UX design

## Landing page

<img src="static/images/landing-page.png">

<img src="static/images/landing-page-2.png">

### When a user first enters the website this is what they see, the landing page containing the navigation panel, footer and a hero image with links to the offers page that is just long enough so users can see there's further content down the page, the collections and the footer

## Navbar
<img src="static/images/desktop-nav.png">

### Navbar on desktop has all the links to other pages on display. The Logo is also a link to the landing page. "My account" is a dropdown menu with links to "My profile/Sign in/Register". The Bag icon is a link to the basket.

<img src="static/images/mobile-nav.png">

<img src="static/images/dropdown-nav.png">

### On smaller devices, the products links are turned into a dropdown(hamburger) menu.

## Footer

<img src="static/images/footer.png">

### In the footer we have the newsletter subscription form, Contact Us address, links to social media, including our facebook page, and FAQ page.

## Products

<img src="static/images/products-page.png">

### On all products page we see candles and oils combined, we can sort by name/price/rating and filter to see only candles/oils

<img src="static/images/product-detail.png">

### In the product detail page, we can add to basket (up to 10 products), submit a review and edit/delete a product(Admin only).

<img src="static/images/product-edit.png">

<img src="static/images/product-management.png">

### The admin has to option to enter the product management form the account dropdown where they can add more products to the store.

## Candles

<img src="static/images/candles-page.png">

### The candles page is only for products in the Candles category, we can see each candle with it's scent, burn time and rating(if any) and can perform sorting.

## Essential Oils

<img src="static/images/oils-page.png">

### The Oils page is only for products in the Oils category, we can see each oil with it's scent, volume and rating(if any) and can perform sorting.

## Specials

<img src="static/images/specials-page.png">

### In the specials page we have the products on sale ( with discounted price ).

## Basket

<img src="static/images/basket-empty.png">

### On an empty basket, we cannot see the Secure checkout button.

<img src="static/images/basket.png">

### The products added to the basket are laid out as a table. The quantity is updated instant on any whole number (up to 10)

<img src="static/images/remove-from-basket.png">

### Removing an item from the basket triggers a modal for confirmation

## Checkout

<img src="static/images/checkout-page.png">

### Once you have items in your basket you can then go to the checkout page, where you add your delivery details, apply coupon if any, and pay.

## Orders

<img src="static/images/order.png">

### The order success confirmation is triggered after a successful order has been placed, and a very similar email will be sent to your inbox.

<img src="static/images/order-history.png">

### In the order history page, all orders are laid out as a list displaying the order numbare and the date it's been made. Each link will bring up the order success page for that order

## Profile

<img src="static/images/profile-page.png">

### The fields in the profile page are in sync with the checkout page, once you put an order in, meaning that they update every time they a new input is provided. You can also set a new password if you wish so.

## Sign in/Register

<img src="static/images/sign-in.png">

<img src="static/images/sign-up.png">

<img src="static/images/log-out.png">

### Account creation is provided by django allauth, meaning everything from registering to loggin' out to resetting password.

## FAQ

<img src="static/images/faq-page.png">

## 404 Page

<img src="static/images/404.png">

### The 404 page is triggered when a user tries to enter a link that's not connected with this website.

## Messages / Toasts

<img src="static/images/message-1.png">
<img src="static/images/message-2.png">
<img src="static/images/message-3.png">
<img src="static/images/message-4.png">
<img src="static/images/message-5.png">

### Messages are triggered as website feedback for users performing actions such as adding to basket/ successful order/ submitting forms...

## Features to be implemented
* If the logged in user is the admin/staff, review and approve reviews from the front-end.
* Provide recommendations to users based on their search/order history.
* Update product management to see how many products are in stock; get notified if a stock is running low.
* As the products list grows larger, pagination will be needed

# Technology used
* HTML5
* CSS3
* Javascript
* Python

# Frameworks and libraries used
* Django
* Jquery
* Bootstrap 4
* ElephantSQL - PostgreSQL was used as database for this project
* Stripe for payments
* AWS S3 bucket sstorage for storing static files and media files

# Agile methodology
### Link to the project board [Liquid Smoke board](https://github.com/users/EddieStn/projects/3)

## Epics Breakdown
### [#1 EPIC 1 Product Catalog and Search](https://github.com/EddieStn/liquid-smoke/issues/1)

As a customer, I want to be able to easily find the candles and essential oils that I'm interested in, so that I can quickly make a purchase without any issues.

To achieve this goal, I expect the following functionality:

* The ability to browse through different categories of candles and essential oils, and view a clear and organized display of the products within each category.
* The ability to filter my search results by different factors, such as scent, price, and product type, and see accurate and relevant results.
* The ability to search for products by keywords or phrases, and see relevant results that match my search terms.
* The ability to view product details and images, and have a clear and accurate understanding of what I'm purchasing.
A smooth and seamless user experience throughout the entire browsing and purchasing process, without encountering any errors, glitches, or technical issues.

As a user, I expect the product catalog and search functionality to meet all of these requirements, and to provide me with a positive and hassle-free shopping experience. During testing, I will be looking for any issues or errors that may prevent me from achieving these goals


### [#2 EPIC 2 Shopping Cart and Checkout](https://github.com/EddieStn/liquid-smoke/issues/2) 

As a customer, I want to be able to easily add products to my shopping cart, check out, and complete my purchase, without encountering any issues or errors.

To achieve this goal, I expect the following functionality:

* The ability to add products to my shopping cart, view the contents of my cart, and update the quantities of products as needed.
* The ability to easily navigate to the checkout page, and to enter my shipping and billing information, as well as select from a variety of payment options.
* The ability to securely process my payment and complete my purchase, without encountering any issues or errors.
* The ability to receive email notifications regarding my order status, including order confirmation, shipping notifications, and delivery confirmations.
* A smooth and seamless user experience throughout the entire checkout process, without encountering any errors, glitches, or technical issues.

As a user, I expect the shopping cart and checkout functionality to meet all of these requirements, and to provide me with a positive and hassle-free shopping experience. During testing, I will be looking for any issues or errors that may prevent me from achieving these goals

### [#3 EPIC 3 Order Management and Shipping](https://github.com/EddieStn/liquid-smoke/issues/3)

As a customer, I want to be able to place an order, receive email notifications regarding my order status, and track my shipment, so that I can easily and efficiently receive the products I have purchased.

To achieve this goal, I expect the following functionality:

* The ability to easily place an order and receive a confirmation email indicating that my order has been received.
* The ability to receive email notifications throughout the order processing and shipping process, indicating when my order has been processed and when it has been shipped.
* The ability to track my shipment and receive delivery notifications, allowing me to know when to expect my order and ensuring that it is delivered to the correct address.
* Accurate and up-to-date inventory levels, ensuring that the products I order are in stock and available for purchase.
* Efficient and accurate order processing and shipping, ensuring that my order is shipped quickly and accurately.
* A smooth and seamless user experience throughout the entire order management and shipping process, without encountering any errors, glitches, or technical issues.

As a user, I expect the order management and shipping functionality to meet all of these requirements, and to provide me with a positive and hassle-free shopping experience. During testing, I will be looking for any issues or errors that may prevent me from achieving these goals

### [#4 EPIC 4 Customer Accounts and Personalization](https://github.com/EddieStn/liquid-smoke/issues/4)

As a customer, I want to be able to create an account, save my shipping and payment information, view my order history, and receive personalized product recommendations, so that I can easily manage my purchases and discover new products that I might like.

To achieve this goal, I expect the following functionality:

* A smooth and easy account registration process, allowing me to easily create an account and save my shipping and payment information for future purchases.
* A secure user authentication and authorization system, ensuring that my account information is protected and only accessible by authorized users.
* A clear and easy-to-use interface for viewing my order history, allowing me to easily track my past purchases and spending.
* Accurate and relevant personalized product recommendations, based on my past purchases and browsing history, that help me discover new products that I might like.
* A smooth and seamless user experience throughout the entire account management and personalization process, without encountering any errors, glitches, or technical issues.

As a user, I expect the account management and personalization functionality to meet all of these requirements, and to provide me with a positive and hassle-free shopping experience. During testing, I will be looking for any issues or errors that may prevent me from achieving these goals


### [#5 EPIC 5 Customer Support and Feedback](https://github.com/EddieStn/liquid-smoke/issues/5)

As a customer, I want to be able to contact customer support through various channels, leave reviews and ratings for products, and receive promotional offers and discounts, so that I can feel confident and supported during my shopping experience. During testing, I want to ensure that each of these features is easy to use and works as expected. Specifically, I want to be able to:

* Easily find and access customer support options, such as email, phone, and chat, and receive prompt and helpful responses to my inquiries or issues.
* Leave reviews and ratings for products I've purchased, with the ability to provide detailed feedback and indicate whether or not I would recommend the product to others.
* Receive promotional offers and discounts through email and other channels, with personalized recommendations based on my past purchases and interests.
* Manage my communication preferences and opt-out of certain channels if desired, to ensure that I only receive relevant and useful information.
* Overall, have a positive and streamlined shopping experience that makes it easy to find and purchase products, get help if needed, and receive personalized recommendations and offers.

###  [#23 EPIC 6 Website Administration and Maintenance](https://github.com/EddieStn/liquid-smoke/issues/23)

As a website administrator, I want to ensure that the website is always functioning properly, so that customers have a seamless shopping experience. I want to be able to regularly test the website's features and functionalities, and quickly identify and resolve any issues that are found. This will ensure that customers can browse, search, and purchase products without any disruptions, and that the website remains a reliable and trusted source for candles and essential oils.


## Agile User Stories

## For [#1 Epic 1: Product Catalog and Search](https://github.com/EddieStn/liquid-smoke/issues/1)
Epic for the user stories related to products management, browsing, filtering, and searching

### [#39 USER STORY: Homepage structure](https://github.com/EddieStn/liquid-smoke/issues/39)
As a customer, I want to be able to see a clear, concise, and user-friendly menu structure, so that I can navigate easily through different sections of the website.


### [#6 USER STORY: Browsing](https://github.com/EddieStn/liquid-smoke/issues/6)
As a customer, I want to be able to browse through different categories of candles and essential oils, so that I can easily find products that meet my needs.

### [#7 USER STORY: Filtering by category](https://github.com/EddieStn/liquid-smoke/issues/7)
As a customer, I want to be able to filter my search results by factors such as scent, price, and product type, so that I can quickly find the products that meet my specific preferences.

### [#8 USER STORY: View Product Details](https://github.com/EddieStn/liquid-smoke/issues/8)
As a customer, I want to be able to view product details and images, so that I can make informed purchasing decisions.

### [#9 USER STORY: Manage Products](https://github.com/EddieStn/liquid-smoke/issues/9)
As a website administrator, I want to be able to manage product descriptions and images, so that I can ensure that product information is accurate and appealing to customers.

### [#37 USER STORY: Website feedback](https://github.com/EddieStn/liquid-smoke/issues/37)
As a customer, I want to be able to receive automated feedback as I use the website, so that I won't worry if my actions have not been processed.

## For [#2 Epic 2: Shopping Cart and Checkout](https://github.com/EddieStn/liquid-smoke/issues/2)
This epic includes all the features related to the shopping cart and checkout process, such as allowing users to add items to their cart, adjust quantities, and remove items; displaying a summary of the cart with the total price and any applicable discounts or taxes; providing a form for users to enter their shipping and billing information; and processing payment securely.

### [#10 USER STORY: Add products to cart](https://github.com/EddieStn/liquid-smoke/issues/10)
As a customer, I want to be able to add products to my shopping cart, so that I can easily purchase multiple items at once.

### [#11 USER STORY: Checkout and Payment](https://github.com/EddieStn/liquid-smoke/issues/11)
As a customer, I want to be able to easily check out and pay for my purchases, using a variety of payment options.

### [#12 USER STORY: Shipping and fees](https://github.com/EddieStn/liquid-smoke/issues/12)
As a website administrator, I want to be able to manage shipping and handling fees, so that I can ensure that these costs are accurate and fair for customers.

## For [#3 Epic 3: Order Management and Shipping](https://github.com/EddieStn/liquid-smoke/issues/3)
This epic includes all the features related to order management, such as allowing admins to view and manage orders placed by customers; providing an interface for admins to change the order status (such as "processing," "shipped," or "delivered"); and sending email notifications to customers when their order status changes.

### [#13 USER STORY: Order notifications](https://github.com/EddieStn/liquid-smoke/issues/13)
As a customer, I want to receive email notifications when my order is processed and shipped, so that I can track my shipment and know when to expect it.

### [#14 USER STORY: Manage inventory](https://github.com/EddieStn/liquid-smoke/issues/14)
As a website administrator, I want to be able to manage inventory levels, so that I can ensure that products are available for customers to purchase.

### [#15 USER STORY: Manage orders](https://github.com/EddieStn/liquid-smoke/issues/15)
As a website administrator, I want to be able to manage customer orders and shipping information, so that I can ensure that orders are processed and shipped accurately and efficiently.

## For [#4 Epic 4: User Accounts and Authentication](https://github.com/EddieStn/liquid-smoke/issues/4)
This epic includes all the features related to user accounts and authentication, such as allowing users to register for an account with their email address and password, or sign in with an existing account; allowing users to view their order history and saved addresses; and providing options for users to reset their password or log out.

### [#16 USER STORY: Create account](https://github.com/EddieStn/liquid-smoke/issues/16)
As a customer, I want to be able to create an account and save my shipping and payment information, so that I can easily make future purchases without having to re-enter my information every time.

### [#17 USER STORY: Order history](https://github.com/EddieStn/liquid-smoke/issues/17)
As a customer, I want to be able to view my order history and track my past purchases, so that I can keep track of my spending and remember what products I've tried in the past.

## For [#5 Epic 5: Customer Support, Subscription and Feedback](https://github.com/EddieStn/liquid-smoke/issues/5)
This epic includes all the features related to customer support; subscriptions, such as allowing users to sign up for the newsletter to receive promotional offers; and customer reviews and feedback, such as allowing users to leave reviews and ratings for products they have purchased; displaying reviews on the product page; and allowing admins to moderate reviews (such as by approving or rejecting them, or flagging them for spam).

### [#19 USER STORY: Customer support](https://github.com/EddieStn/liquid-smoke/issues/19)
As a customer, I want to be able to contact customer support through various channels (such as email, phone, or chat), so that I can get help with any issues or questions that arise during my shopping experience.

### [#20 USER STORY: Customer reviews](https://github.com/EddieStn/liquid-smoke/issues/20)
As a customer, I want to be able to leave reviews and ratings for products I've purchased, so that I can share my feedback with other customers and help them make informed purchasing decisions.

### [#22 USER STORY: Moderate reviews](https://github.com/EddieStn/liquid-smoke/issues/22)
As a website administrator, I want to be able to approve or reject customer reviews, so that I can make sure every review is appropriate and not spam.

## For [#23 Epic 6: Website Administration and Maintenance](https://github.com/EddieStn/liquid-smoke/issues/23)
This epic focuses on the ongoing maintenance and upkeep of the website to ensure that it continues to function properly and remain relevant to customers. This includes tasks related to testing website functionality and performance, updating and maintaining website content, and managing customer data in compliance with data privacy regulations.

Regular testing of the website's features and functionalities is necessary to identify and address any issues that may arise, such as broken links, slow loading times, or errors in the shopping cart and checkout process. Updating and maintaining website content is also important to keep the website engaging and informative for customers, and to ensure that product information and pricing is accurate and up-to-date.

### [#24 USER STORY: Website testing](https://github.com/EddieStn/liquid-smoke/issues/24)
As a website administrator, I want to be able to test website functionality and performance regularly, so that I can identify and address any issues that may arise.

### [#25 USER STORY: Website and content update](https://github.com/EddieStn/liquid-smoke/issues/25)
As a website administrator, I want to be able to regularly update and maintain website content, so that the website remains engaging and relevant to customers.

### [#26 USER STORY: Customer privacy](https://github.com/EddieStn/liquid-smoke/issues/26)
As a website administrator, I want to be able to manage customer data in compliance with data privacy regulations, so that I can protect customer privacy and avoid legal issues.

* We don't use customer's data for anything else other than sending orders and email confirmations

## Could have User Stories

### [#18 USER STORY: Personalised reccomendations](https://github.com/EddieStn/liquid-smoke/issues/18)
As a customer, I want to be able to receive personalized recommendations for products based on my past purchases and browsing history, so that I can discover new products that I might like.

### [#21 USER STORY: Promotional offers](https://github.com/EddieStn/liquid-smoke/issues/21)
As a customer, I want to be able to receive promotional offers and discounts through email and other channels, so that I can save money on products that I want to buy

### [#40 USER STORY: Navigation path](https://github.com/EddieStn/liquid-smoke/issues/40)
As a customer, I want to be able to see the path I have taken from the home page to the current page I am on, so that I can navigate back to previous pages or sections of the website easily.

## Agile Tasks
### I've set tasks for each user story, in a separate project [Tasks board](https://github.com/users/EddieStn/projects/4)

# Testing

## Lighthouse

| App name  |  file name | result |
| ------ | ------ |------ |
| Home - Desktop| index.html | [no errors](static/images/lighthouse/home-desktop.png)
| Home - Mobile | products.html | [no errors](static/images/lighthouse/home-mobile.png)
| Products - Desktop | index.html | [no errors](static/images/lighthouse/products-desktop.png)
| Products - Mobile | products.html | [no errors](static/images/lighthouse/products-mobile.png)

Low performance score and high loading time mostly because of the large size images, I did not have time to adjust all the products

## Validation

* HTML

| App name  |  file name | result |
| ------ | ------ |------ |
| homepage | index.html | [no errors](static/images/html/html-home.png)
| products | products.html | [no errors](static/images/html/html-products.png)
| candles | candles.html | [no errors](static/images/html/html-candles.png)
| essential_oils | essential_oils.html | [no errors](static/images/html/html-oils.png)
| product_detail | product_detail.html | [no errors](static/images/html/html-product-detail.png)
| basket | basket.html | [no errors](static/images/html/basket.png)
| profile | profile.html | [no errors](static/images/html/profile.png)

* CSS

| App name  |  file name | result |
| ------ | ------ |------ |
| css | base.css | [no errors](static/images/html/css-validator.png)

* JShint

| App name  |  file name | result |
| ------ | ------ |------ |
| Javascipt | propducts.html | [no errors](static/images/jshint/jshint-products.png)
| Javascipt | basket.html | [no errors](static/images/jshint/jshint-basket.png)
| Javascipt | stripe_elements.js | [no errors](static/images/jshint/jshint-stripe.png)

* pep8online

| App name  |  file name | result |
| ------ | ------ |------ |
|liquid-smoke | urls.py | [no errors](static/images/pep8/app-urls.png)
|basket | forms.py | [no errors](static/images/pep8/basket-forms.png)
|basket | models.py | [no errors](static/images/pep8/basket-models.png)
|basket | urls.py | [no errors](static/images/pep8/basket-urls.png)
|basket | views.py | [no errors](static/images/pep8/basket-views.png)
|catalog | admin.py | [no errors](static/images/pep8/catalog-admin.png)
|catalog | forms.py | [no errors](static/images/pep8/catalog-forms.png)
|catalog | models.py | [no errors](static/images/pep8/catalog-models.png)
|catalog | urls.py | [no errors](static/images/pep8/catalog-urls.png)
|catalog | views.py | [no errors](static/images/pep8/catalog-views.png)
|checkout | admin.py | [no errors](static/images/pep8/checkout-admin.png)
|checkout | forms.py | [no errors](static/images/pep8/checkout-forms.png)
|checkout | models.py | [no errors](static/images/pep8/checkout-models.png)
|checkout | signals.py | [no errors](static/images/pep8/checkout-signals.png)
|checkout | tests.py | [no errors](static/images/pep8/checkout-tests.png)
|checkout | views.py | [no errors](static/images/pep8/checkout-views.png)
|checkout | urls.py | [no errors](static/images/pep8/checkout-urls.png)
|checkout | context_proccessors.py | [no errors](static/images/pep8/checkout-context_procesors.png)
|profile | forms.py | [no errors](static/images/pep8/profile-forms.png)
|profile | models.py | [no errors](static/images/pep8/profile-models.png)
|profile | urls.py | [no errors](static/images/pep8/profile-urls.png)
|profile | views.py | [no errors](static/images/pep8/profile-views.png)


## Automated testing TDD
* To create automated tests, I had to comment out the postgres DATABASE_URL as I don't have permissions to create TDD, so used the django default database, sqlite3, while testing

### Created unit tests for the Order form 
* All tests passed
### Created unit tests for the ChackoutView 
* It did not pass all the tests. As the view being fairly complicated it would've taken me more time to create it all using TDD

## Manual testing

### Manual testing performed based on the order of the flow (following the user's journey)

### Landing page

* As a first time user, I see the landing page with a background image and nothing looks out of place ( both desktop and mobile )
* followed by the collections section with a small description of the store's products, Candles and Essential oils
* followed by the "About us" and footer with the newsletter form and, contact info and links to social media/ faq
    * The navigation/collection/faq links all perform the actions that their designed to do, internal links that all lead to their expected destination with no errors
    * social links open in a new page to the expected destination
    * The newsletter form:
        * If submitted without input triggers a "field required" alert
        * The correct input triggers "Thank you for subscribing!" alert
        * Invalid input triggers "Please enter a valid email address." alert
        * Invalid email triggers "ddaw@test.com is an invalid email address and cannot be imported." alert
    * The search bar works the same on all pages of the website and it always redirects to "products" page
        * Searching with no input brings up all the products
        * Searching with input that cannot be found in the products triggers warning alert "No results found for 'input'." and displays the products page with No products
        * Searching with input that can be found in the products triggers success alert "Products found for 'input'." and displays the products page with all the products found
        * Searching by category brings up products in that category, eg. "candles" displays all the candles found
    * "My account" dropdown displays:
        * If not logged in: "Login" & "Register" links
        * if logged in: "My profile" & "Logout" & "Product Management"(admin only)
    * Basket (bag icon) redirects a user not logged in to the "Sign In" page

### Register / Login / Logout

* To perform any basket/checkout actions a user needs to be logged in
* Registering is only possible with a valid email as email confirmation is required 
    * The form will not submit if any inputs are incorrect, an email/username is already taken or the password is too common

    <img src="static/images/register-form.png" width="400" height="500">

    * The corect form will send a confirmation email
    * In the email there's a link to confirm the email and redirect back to shop
* Signing in either by email or username and password
    * Wrong inputs triller alerts to notify the user
    * Successful login returns back to homepage and triggers alert Success! "Successfully signed in as 'username'!"
* Sign out redirects to the logout page where asked for confirmation. You can either Sign out or cancel and both redirects to homepage


### Candles / Essential oils pages / Specials / All products

* At the top of the page there is the link to all products, the product count on that page and the sorting/filtering
    * Filtering is only available in the products page
    * No errors or bugs:
        * when clicking the products link 
        * when sorting by any option (price/name/rating)
        * when filtering by any category (candle/essential oil)
* Candles page will display only products in the Candle category
* Essential oils page will only display products in the Essential Oil category
* Specials page will only display products with a discounted price
* Clicking on the image/name of any products in any of the pages will redirect the user to that product's detail page

### Product detail page

* On top of the details we see in the card of the product as displayed in the products page, here we also have:
    * The product`s description 
    * The add to basket form with quantity and "Add to basket" input
    * Edit/Delete product buttons if logged in as admin
        * Edit button will open the edit product page where we can edit all the fields
            * Can only edit with the fields not blank,
            * Price less than 6 digits, max 4 before the decimal point, max 2 decimals
            
            <img src="static/images/edit-price.png">

            <img src="static/images/edit-price-2.png">

            * Successful updating will redirect to the product's category page

        * Deleting the product will trigger a modal to ask for confirmation
            * The cancel button closes the modal
            * The delete button deletes the product

        <img src="static/images/delete-modal.png" widht="300" height="400">
        
    * Review form with Title/Body/Rating(1-5)
        * Submitting a review with any blank fields will not submit the form and point the user to the input at fault
        * Submitting a review will trigger Success! alert

        <img src="static/images/success-review.png">

        * Only admins will be able to see reviews that have been submitted but not approved

        <img src="static/images/review.png">

        * Once a review has been approved, other users will be able to see it, and the rating will start counting towards the average rating of the product
        * If a user tries to submit a review again, the Error! alert is triggered

        <img src="static/images/review-error.png">

### Product management 

* I know that having 2 forms is very redundant, but because I started with 2 separate models for candle and oils, I found it quite difficult to merge the 2 forms into 1 and only display one form on the page and I didn't have the time to complete it(could not pass the scent/volume/burn_time field to the product form). Made a note of all my attempts in merge_forms_attemts.txt
* No form will submit with invalid inputs such as a blank input for required fields, wrong image format or price not in the correct parameters
* Category field is not required by design, but choosing each one or both will pass the category(ies) to the product

### Basket

* On an empty basket we see the message "Your basket is empty" and the button "Continue Shopping"
    * clicking the button redirects to products page
* Adding an item to the basket triggers Success! alert
* Updating the quantity triggers alert Success! on any action
    * Typing another number or clicking the buttons - / + updates the quantity and triggers alert Success!
    * Typing a number above and below 10 resets the quantity to 1
    * Cannot reduce the quantity below 1 / Cannot increase above 10
    * letters are not being read by the form
    * typing a float number triggers form validation
* Removing an item from the basket triggers confirmation modal
    * Clicking Cancel closes modal 
    * Clicking Remove removes the item completely from the basket
* If a product has discounted price it is correctly calculated to display the total price
    * Any quantity updates correctly the total
* Now that we have items in our basket, we see the "Secure Checkout" button
    * Clicking it redirects to checkout page
* Deleting an item after it's been added to the basket removes it from the basket too, without affecting the other items in the basket


### Checkout

* Here we see the products we're about to purchase, a coupon field and the delivery details and payment forms
    * Ordering for the first time will have the fields empty, but a having "Save info" checkbox ticket will save our delivery address to our profile
    * All fields are required expect for address line 2
        * A form will not submit if there are any invalid inputs
        * If the fields in "My profile" are filled, we will see our checkout fields prefilled next time we checkout
    * Payment form is handled by stripe 
        * The basket total is also displayed and updated correctly below the form
        
        <img src="static/images/payment-form.png">

        * Tested using the card details provided by stripe

        <img src="static/images/card-details.png">

        * An invalid card will not submit the form


        <img src="static/images/card-invalid.png">
    
    * Tested checkout functionality with coupons expired/invalid/active to be rendered in the order_details view
        * Check with coupon "123123"
        * Applying an invalid coupon triggers alert Error!
        * Applying an active coupon triggers alert Success!
        * Applying an invalid coupon AFTER a valid coupon does not remove the active from the session
        * Making a coupon inactive while I have it applied in my checkout, It redirects to 404.html after refreshing/completing the order or accessing the checkout again
            * A coupon is only removed form the session after a successful order or after logging out
            * So after a coupon becomes inactive, logging out and back in removes the coupon from your order
        * The total basket price is correctly updated after taking into account the coupon and displays the amount saved and the coupon

        <img src="static/images/coupon-empty.png">

        <img src="static/images/coupon.png">
    
    * Clicking Adjust basket redirects to basket 
    * Clicking Complete Order redirects to order detail page, triggers alert Success! 

### Order success

* Now that we have a successful order we get to the order detal page
* We get the order number for that order, 
* All the order details are correct
* Clicking "Go to profile" redirects to "My profile"
* Clicking "Order history" redirects to "Order history"
    * Here we have laid out all past orders in form of a table 
    * Clicking any order brings up the past order detail of that order 
* Clicking the back button on the browser redirects to the products page and triggers alert "Your basket is empty"
* When an order has been placed, we get a confirmation email

<img src="static/images/order-success.png">

<img src="static/images/email-order.png">

### My Profile

* A basic page, where we can easily reset the password and see/update our delivery information
    * Updating info triggers Success! alert and updates the form with no errors
    * Clicking the reset password link redirects to reset password page
    * Clicking Order history redirects to order history and triggers Info alert
        * Clicking each order brings up the order confirmation page
* The delivery fields are in sync with the checkout page, if the profile is updated, next time you checkout you will be the new details prefilled


## Responsive

### No problems were found when building the app and manually checking for responsiveness with chrome dev tools

To generate a multi device mockup I used [Techsini](https://techsini.com/multi-mockup/index.php)
To ensure my website is fully responsive I used [responsivedesignchecker](https://responsivedesignchecker.com/)

* Mobile 
    * Iphone 5

    <img src="static/images/iphone-5.png">

    <img src="static/images/iphone-5s.png">

    * iphone 6

    <img src="static/images/iphone-5.png">

    * Google pixel

    <img src="static/images/google-pixel.png">

    * Nexus 5

    <img src="static/images/nexus-5.png">
    
* Tablet
    * fire-hd
    
    <img src="static/images/fire-hd.png">

    * nexus

    <img src="static/images/nexus.png">

    * ipad

    <img src="static/images/ipad.png">

* Laptop
    * notebook-10"
    
    <img src="static/images/notebook-10in.png">

    * notebook 15"

    <img src="static/images/notebook-15in.png">

* Desktop
    * Desktop 20"

    <img src="static/images/desktop-20in.png">

    * Desktop 24"

    <img src="static/images/desktop-24in.png">

# Bugs

### CSS
* The header is covering the body of the website
    * having `html {height: 100%}` and `body {height: calc(100vh - any size)}` doesn't fix it.
    * Fixed by addig `padding-top: 145px;` to the body element
* Clicking an `<a>` tag (eg. "All products") wouldn`t open the link, but right click > "open in a new tab" works
    * Fixed by removing `data-toggle="dropdown"` that was needed for the account dropdown menu

### Products
* During final testing, I noticed that editing a product's category doesn't update it in the individual template. Looking back now I realize I shouldn't have created separate views for candles and oils, but instead make better use of filtering and provide my pages this way. However, being short of time I updated the current views.
    * Fixed by rebuilding my views to get the filtered products instead of candles/oils from Candle/EssentialOil models
    ```
    Before: candles = Candle.objects.all()
    After: products = Product.objects.filter(categories__name='Candles')
    // same for oils
    ```
### Product detail page
* A user resubmitting the review form a second time will throw a Server error(500)
    * To prevent this, I added a check in the view, this also allows users that are not logged in to view the reviews
    ```
    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(
            product=product, user=request.user).first()  // to prevent asking for "Confirm form submission" when reloading the page
    form = ReviewForm()

    if request.method == 'POST':
        if 'review_form' in request.POST:
            if user_review:
                messages.error(
                    request, "You have already submitted \
                    a review for this product.")
                return redirect('product_details', product_id=product_id)  // to prevent asking for "Confirm form submission" when reloading the page
    ```
* Submitting a review form will trigger error from the basket form (quantity field required)
    * Fixed by wrapping both form handlers in an if statement `if request.method == 'POST':`
    * Added a hidden input field to both forms `if 'review_form' in request.POST:` & `if 'basket_form' in request.POST:`
    * Added to each form button tag the name attribute to check for hidden input `<button type="submit" name="review_form ( / basket_form)">Submit</button>`

### Checkout
* After a successful order, hitting the back button from the order_detail page leads to an error in the browser
    * Fixed by adding an exception to the stripe intent
    ```
    InvalidRequestError at /checkout/
    stripe.error.InvalidRequestError: Request req_upHWpena88utjx: This value must be greater than or equal to 1.


    try:
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe's API
        return redirect(reverse('home'))
    ```
* If I make a coupon inactive while I have it applied in my checkout, It redirects me to 404.html
    * Tried and failed 
    * If I make a coupon inactive from the admin panel, triggers InactiveCoupon, so I deleted that
    * Looking back now I see that I could've handle the coupon functionality better and maybe use is_valid better
    * So this bug is left unfixed due to lack of time
    ``` 
    Coupon(models.Model)
    ---
    class InactiveCoupon(Exception):
        pass

    def clean(self):
        if not self.active:
            raise Coupon.InactiveCoupon('This coupon is inactive.')
    ---

    apply_coupon view
    ---
    coupon_id = request.session.get('coupon_id')
    if coupon_id:
        try:
            coupon = Coupon.objects.get(id=coupon_id,
                                        active=True,
                                        valid_from__lte=now,
                                        valid_to__gte=now)
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            messages.error(request, 'The coupon used in checkout has become inactive')
        except Coupon.InactiveCoupon:
            request.session['coupon_id'] = None
            messages.error(request, 'Coupon is not active')
    ---

    checkout view
    ---
    coupon_id = request.session.get('coupon_id')
    coupon = None
    if coupon_id:
        coupon = get_object_or_404(Coupon, id=coupon_id, active=True,
                                   valid_from__lte=timezone.now(),
                                   valid_to__gte=timezone.now())
        if not coupon:
            del request.session['coupon_id']
            coupon_id = None
            messages.warning(request, "The coupon you applied is no longer \
                valid. Try logging out and back in")
            return redirect('basket')
    ---
    ```

### Basket 
* Adding an offer item will not add it with the discounted price
    * Fixed by changing the model to include a discounted_price field and the view_basket to check for the discounted_price
* Hitting enter on the quantity field in the basket & clicking Remove will reduce the quantity by 1
    * Fixed the remove button by updating the view to only delete the item
    * Fixed the quantity issues with javascript event listeners in view_basket.html
* The basket will always have one empty product displayed
    * Fixed by adding a check to make sure `product_id is not None` before creating the BasketItem object.
* First added item to the basket will always be 1 regardless of set quantity
    * Fixed by modifying the add_to_basket to check if the BasketItem object already exists, and update its quantity accordingly.



## Django notes

* When changing a model and applying migrations you get an error message to provide a default value or set null=True
    * If you have data stored in your database
        * If you don't want to have those values in your fields, add a default="" to your field, makemigrations>migrate, then remake your model as needed and makemigrations>migrate again
    * If you don't have any data stored
        * Simply comment out your models or delete your migrations files (except __init__.py) and migrate again
        * rm db.sqlite3 > python manage.py makemigrations > python manage.py migrate

# Development and Deployment
## Local development
* Create your Django app. In the terminal write the following in order:
    1. Install Django and gunicorn: `pip3 install django gunicorn`
    2. Install database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url psycopg2`
    4. Create file for requirements file: `pip freeze --local > requirements.txt`
    5. Create your project: `django-admin startproject your_project_name .` ( remember the . at the end)
    6. Create your app: `django-admin startapp your_app_name`
    7. Migrate: `python3 manage.py makemigrations` and `python3 manage.py migrate`
    8. Run the server to test if the app is installed: `python3 manage.py runserver`

### Setting AWS bucket

1. Go to [Amzon Web Services](https://aws.amazon.com/) page and login or register

2. You should be redirected to AWS Managment Console, if not click onto AWS logo in top left corner or click Services icon and choose Console Home

3. Below the header AWS Services click into All Services and find **S3** under Storage

4. Create New Bucket using **Create Bucket** button in top right hand corner

- **Configuration:** type in your chosen name for the bucket (preferably matching your heroku app name) and AWS Region closest to you


- **Object ownership:** ACLs enabled, Bucket owner preffered

- **Block Public Access settings:** Uncheck to allow public access, Acknowledge that the current settings will result that the objects within the bucket will become public

- Click **Create Bucket**

5. You are redirected to Amazon S3 with list of your buckets. Click into the name of the bucket you just created

6. Find the tab **Properties** on the top of the page:
**Static website hosting** at the bottom of the properties page: clik to edit, click enable, fill in index document: index.html and error.html for error

7. On the **Permissions** tab:
- Cross-origin resource sharing (**CORS**) Paste in the below code as configuration and save

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- **Bucket Policy** within permissions tab: Edit bucket policy
Click AWS Policy Generator (top right conrner)

Select type of policy: S3 Bucket policy
Principal: * (allows all)
Actions: Get object
Amazon Resource Name (ARN): paste from the Edit bucket policy page in permissions
Click Add statement Than Click Generate Policy and Copy the policy into bucket policy editor. 
In the policy code find "Resource" key and add "/*" after the name of the bucket to enable all
Save changes

- **Access control list (ACL)** within permissions tab: click Edit

find Everyone (public access) and check List box and save

8. Identity and Access Management (IAM)
Go back to the AWS Management Console and find IAM in AWS Services

- side menu - User Groups and click **Create Group**
name group "manage-your-app-name" and click Create group

- side menu - Policies and click **Create Policy**
Click import managed policy - find AmazonS3FullAccess
Copy ARN again and paste into "Resource" add list containint two elements "[ "arn::..", ""arn::../*]" First element is for bucket itself, second element is for all files and foldrs in the bucket

Click bottom right Add Tags, than Click bottom right Next: Review
Add name of the policy and description

Click bottom right Create policy

9. Attach policy to the group we created:
- go to User Groups on side menu
- select your group from the list
- go to permissions tab and add permissions drop down and choose **Attach policies**
- find the policy created above and click button in bottom right Add permissions

10. Create User to go in the group
- **Users** in the side menu and click add users

User name: your-app-staticfiles-user
Check option: Access key - Programmatic access
Click button at the bottom right for Next
- Add user group and add user to the group you created earlier
Click Next Tags and Next: review and Create user
- Download .csv file


11. Connect django to AWS S3 bucket
- install boto3
- install django-storages
- freeze to requirements.txt
- add storages to installed apps in settings.py

```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

12. Go to heroku to set up enviromental variables

open CSV file downloaded earlier and copy each variable into heroku Settings

AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID from csv
AWS_SECRET_ACCESS_KEY from csv
USE_AWS = True
remove DISABLE_COLLECTSTATIC variable from heroku

13. Create file in root directory custom_storages.py

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

14. Go to settings.py, add the AWS settings

```
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

15. To load the media files to S3 bucket

- Go to your S3 bucket page on AWS. Create new folder "media"
- go to the media folder and click Upload


## Heroku deployment
### The site was deployed via Heroku. The live link can be found here - [Liquid Smoke](https://liquid-smoke.herokuapp.com/)
* To deploy the project through Heroku I followed these steps:

    * Sign up / Log in to Heroku
    * From the main Heroku Dashboard page select `New` and then `Create New App`
    * Give the project a name - in my case liquid-smoke and select a `region`, then select `create app`.
    * This will create the app within Heroku.
    * For the database, I used ElephantSQL
        * Navigate to ElephantSQL.com and log-in/sign-up.
        * Create new instance
        * Choose a name and the free plan, tags can be left blank
        * Select a region and click Review and then Create
        * From the dashboard, select the created instance and copy the URL to the clipboard
    * In Heroku navigate to the setting tab and scroll utill you find `Reveal config vars`.
    * Add to the config vars DATABASE_URL as the KEY and paste the URL from your ElephantSQL as the VALUE
    * Add to the config vars AWS_SECRET_KEY as the KEY and paste the URL as the VALUE
    * Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
        * This key value pair must be removed prior to final deployment
    * In the root directory of your repository in github create a new file called `env.py` and write the following code:
        ```
        import os

        os.environ["DATABASE_URL"]="postgres://url"
        os.environ["SECRET_KEY"]="your secret key"
        os.environ["AWS_SECRET_KEY"]="cloudinary://url"
        ```
    * Add the secret key just created to the Heroku Config Vars. SECRET_KEY as the KEY and the secret key value you created as the VALUE
    * In settings.py write the following code:
        ```
        from pathlib import Path
        import os
        import dj_database_url
        if os.path.isfile('env.py'):
            import env
        ```
    * Replace the secret key that django has in the settings.py with `SECRET_KEY = os.environ.get('SECRET_KEY')`
    * Comment out the default database and replace it with:
        ```
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
        ```
    * Make migrations:
        * python3 manage.py makemigrations
        * python3 manage.py migrate
    * In the following order, add the Cloudinary libraries to the Django settings.py section for installed apps:
        ```
        'cloudinary_storage'
        'django.contrib.staticfiles',
        'cloudinary',
        ```
    * Add the following in settings.py to connect Cloudinary to Django:
        ```
        STATIC_URL = '/static/'
        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        MEDIA_URL = '/media/'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        ```
    * Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    * Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
    * For the `ALLOWED_HOSTS` add your heroku url and your localhost:
        ```
        ALLOWED_HOSTS = ['liquid-smoke.herokuapp.com', 'localhost']
        ```
    * In your root directory, create three new top folders: media, static and templates
    * Create a `Procfile` file in the root directory
    * Within the Procfile add the code - `web: guincorn PROJECT_NAME.wsgi`
    * In the terminal, add the changed files, commit and push to GitHub
    * In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
    * Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

## Deployment checklist
* Upon completion of development, change in settings.py DEBUG = True to DEBUG = False
* In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0
* 'Choose a branch to deploy' should be 'main' and search for your repository
* To manually deploy click the button 'Deploy Branch'
* Your app was successfully deployed will be displayed when the app is deployed.
* The deployed app will appear in the browser after you click "view."

## Forking a repository
### A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.
1. On GitHub.com, navigate to https://github.com/EddieStn/liquid-smoke.
2. In the top-right corner of the page, click Fork.

## Cloning your forked repository
### Right now, you have a fork of the liquid-smoke repository, but you do not have the files in that repository locally on your computer.
1. On GitHub.com, navigate to your fork of the liquid-smoke repository.
2. Above the list of files, click Code.
3. Copy the URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub username instead of YOUR-USERNAME:
   - git clone https://github.com/YOUR-USERNAME/liquid-smoke
7. Press Enter. Your local clone will be created.

# Credits 

* Copied Readme aws section from [JoGorska](https://github.com/JoGorska/bonsai-shop) README.md
* Search form/checkout design is inspired from Boutique-Ado ( Code institute walkthrough project )
* Navbar changes
    * I was having responsiveness issues with my original navigation design so I took inspiration from Boutique Ado, as it fit the purpose.

# Acknowledgements

* Thanks to my mentor Chris Quinn for guidance and for providing me with the resources needed to expand my Django knowledge
* Thanks to Code Institute tutors Jason and Sarah for helping me with bug fixes

## Other sources

* [Code with mosh - full Python and Django courses](https://codewithmosh.com/courses)
* [Code institute](https://learn.codeinstitute.net/)