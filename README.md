# Happy Shopping - E-commerce Website 

## Table of contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Django installation](#django-installation)
- [Creating a Django project](#creating-a-django-project)
- [Running the Development server](#running-the-development-server)

## Introduction
Welcome to the Happy Shopping🤍!! This project is designed to provide a seamless and user-friendly platform for users to browse, search, and purchase a wide variety of products from the comfort of their homes.

## Features
- **User Authentication:** Secure registration and login functionalities to ensure user privacy and data protection.
- **Search and Filter:** Advanced search and filtering options to help users find products quickly and easily.
- **Payment Gateway Integration:** Secure and convenient payment options to facilitate smooth transactions.
- **Admin Dashboard:** A powerful admin dashboard to manage products, orders, users, and other aspects of the app.
- **Secure Fund Transfers:** Enhanced security measures for safe and secure fund transfers.

## Technologies used
- **Backend**: Django 4.x, Python 3.x
- **Frontend**: HTML, CSS, JavaScript, Bootstrap, Tailwind CSS
- **Database**: SQLite3
- **Template Engine**: Django Template Language (DTL)

## Django installation
1. **Install virtualenv:**
If you don't have virtualenv installed, you can install it using pip:
    ```
    pip install virtualenv
    ```
2. **Create a virtual environment:**
Navigate to your project directory and create a virtual environment:
    ```
    virtualenv venv
    ```
3. **Activate the virtual environment:**

    On Windows:
    ```
    venv\Scripts\activate
    ``` 
4. **Install Django:**
Once the virtual environment is activated, install Django using pip:
    ```
    pip install django
    ```
## Creating a Django project

To create a new Django project, use the following command:

```
django-admin startproject projectname
```   

## Running the Development Server
Navigate into your project directory and run the development server:
```
python manage.py runserver
```
## Migrations
Django migrations are used to manage changes to your database schema over time. Here are the basic commands and syntax for working with migrations in Django:
- ### Creating Migrations

    To create new migrations based on the changes you have made to your models, use:
    ```
    python manage.py makemigrations
    ```

- ### Applying Migrations
    To apply the migrations to your database (i.e., to synchronize the database schema with the current state of your models), use:

    ```
    python manage.py migrate
    ```

## Stripe 

Stripe is a popular payment processing platform that provides APIs and tools to accept payments online.The Stripe API allows developers to integrate various payment capabilities directly into their websites or applications. Here’s an overview of using Stripe's API in your Django-based online shopping app:

### Using Stripe API with Django

Stripe offers a robust API that allows developers to integrate payment functionality into web applications. Here’s how you can integrate Stripe with your Django project:

1. **Sign up for Stripe:** Create an account on Stripe if you haven't already. Obtain your API keys from the dashboard.

2. **Install Stripe Python library:** Use the `stripe-python` library to interact with Stripe API. Install it using pip:
    ```
    pip install stripe
    ```
3. **Configure Stripe API keys:** 
Add your Stripe API keys to your Django project's settings file (settings.py):
    ```
    STRIPE_PUBLIC_KEY = 'your_stripe_public_key'
    STRIPE_SECRET_KEY = 'your_stripe_secret_key'
    ```
    It's recommended to store sensitive keys securely, such as using environment variables.

4. **Integrate Stripe in views:** 
    
    Implement views to handle payments using Stripe API.

5. **Secure Transactions:**
    
    Ensure secure handling of sensitive information such as API keys and user payment details.

## Images Attachment

### Home page

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/0332e39d-cb02-4491-b834-cdc6da9078c4)

### Login page

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/45d3eef3-f70b-4345-b1f8-4039694d80b8)


### Register page

![rimage](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/95e18643-ae09-45f1-9cbb-cb86f4db0f85)

### Products page

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/ccd7e48e-b8e7-4867-bae4-dfe1f157bce3)

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/5ef4c4b9-5fff-4979-8456-314528d1590d)


![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/489fa6c8-a6d0-4f50-bc66-1e53c254fe68)

### User Profile page
![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/ca148592-72bb-417b-a784-af3380f8d3c6)

### Add product page

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/baf7c50d-4536-4dc1-bcef-dec8bd4546bf)

### Product listing page of a user

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/cf6bf381-347f-4b67-b55b-7d9b5e32d03a)

### Update product page

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/fce07fc7-56b4-4de6-86a3-3d53916dc0fb)

### Delete product page

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/acfb7de6-7f2a-41ce-8894-a674c75334e8)

### Checkout product

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/0a9d2bc0-8b01-44c0-9575-2876a3cf3937)

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/609d151f-e943-425f-8fd5-822b6be7f0e4)

### Payment successful

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/8081114b-2be2-4343-8988-2a3a25ba7674)

### Payment failure

![image](https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/e6d53522-5cd6-4a64-b48d-cf103fecf5e7)

## Video Attachment


https://github.com/Laksanna/django-buy-sell-website-certification/assets/134076446/371f102e-55fb-4af6-ba54-679d09e71aff




## Conclusion

I have designed this project with a focus on providing a secure, user-friendly, and feature-rich platform for online shopping. From robust user authentication to seamless payment processing and personalized shopping experiences, we've integrated the latest technologies and best practices to ensure a smooth journey for our users.


