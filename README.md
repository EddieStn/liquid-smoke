## Epics Breakdown
### EPIC 1 Product Catalog and Search

As a customer, I want to be able to easily find the candles and essential oils that I'm interested in, so that I can quickly make a purchase without any issues.

To achieve this goal, I expect the following functionality:

* The ability to browse through different categories of candles and essential oils, and view a clear and organized display of the products within each category.
* The ability to filter my search results by different factors, such as scent, price, and product type, and see accurate and relevant results.
* The ability to search for products by keywords or phrases, and see relevant results that match my search terms.
* The ability to view product details and images, and have a clear and accurate understanding of what I'm purchasing.
A smooth and seamless user experience throughout the entire browsing and purchasing process, without encountering any errors, glitches, or technical issues.

As a user, I expect the product catalog and search functionality to meet all of these requirements, and to provide me with a positive and hassle-free shopping experience. During testing, I will be looking for any issues or errors that may prevent me from achieving these goals


### EPIC 2 Shopping Cart and Checkout

As a customer, I want to be able to easily add products to my shopping cart, check out, and complete my purchase, without encountering any issues or errors.

To achieve this goal, I expect the following functionality:

* The ability to add products to my shopping cart, view the contents of my cart, and update the quantities of products as needed.
* The ability to easily navigate to the checkout page, and to enter my shipping and billing information, as well as select from a variety of payment options.
* The ability to securely process my payment and complete my purchase, without encountering any issues or errors.
* The ability to receive email notifications regarding my order status, including order confirmation, shipping notifications, and delivery confirmations.
* A smooth and seamless user experience throughout the entire checkout process, without encountering any errors, glitches, or technical issues.

As a user, I expect the shopping cart and checkout functionality to meet all of these requirements, and to provide me with a positive and hassle-free shopping experience. During testing, I will be looking for any issues or errors that may prevent me from achieving these goals

### EPIC 3 Order Management and Shipping

As a customer, I want to be able to place an order, receive email notifications regarding my order status, and track my shipment, so that I can easily and efficiently receive the products I have purchased.

To achieve this goal, I expect the following functionality:

* The ability to easily place an order and receive a confirmation email indicating that my order has been received.
* The ability to receive email notifications throughout the order processing and shipping process, indicating when my order has been processed and when it has been shipped.
* The ability to track my shipment and receive delivery notifications, allowing me to know when to expect my order and ensuring that it is delivered to the correct address.
* Accurate and up-to-date inventory levels, ensuring that the products I order are in stock and available for purchase.
* Efficient and accurate order processing and shipping, ensuring that my order is shipped quickly and accurately.
* A smooth and seamless user experience throughout the entire order management and shipping process, without encountering any errors, glitches, or technical issues.

As a user, I expect the order management and shipping functionality to meet all of these requirements, and to provide me with a positive and hassle-free shopping experience. During testing, I will be looking for any issues or errors that may prevent me from achieving these goals

### EPIC 4 Customer Accounts and Personalization

As a customer, I want to be able to create an account, save my shipping and payment information, view my order history, and receive personalized product recommendations, so that I can easily manage my purchases and discover new products that I might like.

To achieve this goal, I expect the following functionality:

* A smooth and easy account registration process, allowing me to easily create an account and save my shipping and payment information for future purchases.
* A secure user authentication and authorization system, ensuring that my account information is protected and only accessible by authorized users.
* A clear and easy-to-use interface for viewing my order history, allowing me to easily track my past purchases and spending.
* Accurate and relevant personalized product recommendations, based on my past purchases and browsing history, that help me discover new products that I might like.
* A smooth and seamless user experience throughout the entire account management and personalization process, without encountering any errors, glitches, or technical issues.

As a user, I expect the account management and personalization functionality to meet all of these requirements, and to provide me with a positive and hassle-free shopping experience. During testing, I will be looking for any issues or errors that may prevent me from achieving these goals


### EPIC 5 Customer Support and Feedback

As a customer, I want to be able to contact customer support through various channels, leave reviews and ratings for products, and receive promotional offers and discounts, so that I can feel confident and supported during my shopping experience. During testing, I want to ensure that each of these features is easy to use and works as expected. Specifically, I want to be able to:

* Easily find and access customer support options, such as email, phone, and chat, and receive prompt and helpful responses to my inquiries or issues.
* Leave reviews and ratings for products I've purchased, with the ability to provide detailed feedback and indicate whether or not I would recommend the product to others.
* Receive promotional offers and discounts through email and other channels, with personalized recommendations based on my past purchases and interests.
* Manage my communication preferences and opt-out of certain channels if desired, to ensure that I only receive relevant and useful information.
* Overall, have a positive and streamlined shopping experience that makes it easy to find and purchase products, get help if needed, and receive personalized recommendations and offers.

### EPIC 6 Website Administration and Maintenance

As a website administrator, I want to ensure that the website is always functioning properly, so that customers have a seamless shopping experience. I want to be able to regularly test the website's features and functionalities, and quickly identify and resolve any issues that are found. This will ensure that customers can browse, search, and purchase products without any disruptions, and that the website remains a reliable and trusted source for candles and essential oils.

* Navbar changes
    * I was having responsiveness issues with my original navigation design so I took inspiration from Boutique Ado 

# Testing

- To create automated tests, I had to comment out the postgres DATABASE_URL as I don't have permissions to create TDD, so used the django default database, sqlite3, for testing

# Bugs

### Checkout
* Hitting the back button from the order_detail page leads to an error in the browser
```
InvalidRequestError at /checkout/
stripe.error.InvalidRequestError: Request req_upHWpena88utjx: This value must be greater than or equal to 1.
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


* Submitting a review form will trigger error from the basket form (quantity field required)
    * Fixed by wrapping both form handlers in an if statement `if request.method == 'POST':`
    * Added a hidden input field to both forms `if 'review_form' in request.POST:` & `if 'basket_form' in request.POST:`
    * Added to each form button tag the name attribute to check for hidden input `<button type="submit" name="review_form ( / basket_form)">Submit</button>`
* Clicking an <a> tag (eg. "All products") wouldn`t open the link, but right click > "open in a new tab" works
    * Fixed by removing `data-toggle="dropdown"` that was needed for the account dropdown menu
* The header is covering the body of the website
    * having `html {height: 100%}` and `body {height: calc(100vh - any size)}` doesn't fix it.
    * Fixed by addig `padding-top: 145px;` to the body element


## Django notes

* When changing a model and applying migrations you get an error message to provide a default value or set null=True
    * If you have data stored in your database
        * If you don't want to have those values in your fields, add a default="" to your field, makemigrations>migrate, then remake your model as needed and makemigrations>migrate again
    * If you don't have any data stored
        * Simply comment out your models or delete your migrations files (except __init__.py) and migrate again
        * rm db.sqlite3 > python manage.py makemigrations > python manage.py migrate
