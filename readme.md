# AURA – Premium Jewelry Store

AURA is a modern and elegant online jewelry store designed to provide customers with a premium and luxurious shopping experience. The system allows users to explore different jewelry collections, view product details, add products to their shopping bag, and place orders through Cash on Delivery.

## Features

### Customer Features

- Browse premium jewelry products
- Explore different jewelry collections
- View product images
- View product names and prices
- View product descriptions
- Browse Pendants
- Browse Rings
- Browse Bracelets
- Browse Earrings
- Add products to shopping bag
- View shopping bag
- Remove products from shopping bag
- Automatically calculate total price
- Checkout system
- Enter customer information
- Cash on Delivery option
- About Us section
- Contact Us section

## Jewelry Collections

### Pendants
Elegant and stylish pendant designs for different occasions.

### Rings
Beautiful rings with modern and classic designs.

### Bracelets
Premium bracelets and bangles designed for an elegant look.

### Earrings
Stylish earrings suitable for everyday wear and special occasions.

## Shopping Bag

The shopping bag allows customers to manage their selected jewelry products.

Customers can:

- Add products to the bag
- View selected products
- View product prices
- Remove products
- Check the total amount
- Proceed to checkout

## Checkout

The checkout system collects customer information required for order placement.

### Customer Information

- Full Name
- Phone Number
- Shipping Address

### Payment Method

- Cash on Delivery (COD)

## Database

AURA uses **MongoDB** to store and manage jewelry product information.

### Database

`aura_jewelry_db`

### Collection

`products`

The product database contains information such as:

- Product name
- Category
- Price
- Image
- Description

## API

The Flask backend provides an API for retrieving products according to their category.

### Product API

`GET /api/products/<category>`

Supported categories include:

- Rings
- Pendants
- Bracelets
- Earrings

The API retrieves the required products from the MongoDB database and sends them to the frontend.

## Technologies Used

- Python
- Flask
- MongoDB
- PyMongo
- HTML
- CSS
- JavaScript

## Project Structure

```text
AURA-Jewelry/
│
├── app.py
├── db.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
└── readme.md
User Experience

The website provides a smooth and modern shopping experience through:

Luxury-themed interface
Product category navigation
Interactive product cards
Shopping bag drawer
Dynamic product loading
Responsive design
Smooth animations
Modern typography
Design

AURA follows a premium jewelry-inspired design using:

Soft pink shades
Rose-gold accents
Gold highlights
Clean white backgrounds
Elegant typography
Modern layouts
Responsive product sections
Future Improvements
User registration and login
Online payment integration
Order history
Admin dashboard
Product management
Product search and filtering
Wishlist
Product reviews and ratings
Order tracking
Inventory management
Email order confirmation
Author

Maria Saleem

Project Name

AURA – Premium Jewelry Store