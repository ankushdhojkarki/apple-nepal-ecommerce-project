# 🍏 Apple Nepal E-commerce Project

A clean, modern e-commerce front-end and a hands-on **learning project for Django development**.

This project is currently being developed to master core concepts of the Django framework, including templating, routing, context handling, static file management, and user authentication.

## ✨ Project Highlights (Current State)

This project features a complete, responsive front-end built with Bootstrap, utilizing a custom "Olive Vibe" color palette for a unique aesthetic.

### Key Pages Developed:
* **Home Page (`index.html`):** Features a Bootstrap Carousel and a section for featured products.
* **Products List (`products.html`):** Displays a grid layout of all available items.
* **Product Details (`product-details.html`):** A dedicated page to showcase an individual product, including its price and an "Add to Cart" button.
* **Categories (`categories.html`):** A layout for browsing products by category.
* **User Authentication:**
    * **Sign In (`login.html`):** A simple form for user login.
    * **Sign Up (`signup.html`):** A form for new user registration.

## 💻 Technology Stack

* **Backend Framework:** **Django** (Python)
* **Frontend UI:** **Bootstrap 5.3.2**
* **Styling:** Custom CSS (`styles.css`) featuring a unique **Dark Olive Green** theme for accents.
* **Templating:** Jinja-style Django templates (utilizing tags like `{% load static %}` and `{% url '...' %}`).
* **Formatting:** `django.contrib.humanize` for number formatting (e.g., `|intcomma`).

## 🛠️ Django Learning Goals

The following concepts are being focused on and implemented in this project:
1.  **URL Routing and Views:** Mapping template files to specific URLs.
2.  **Context and Data Display:** Passing product and category data from Python views to the templates (e.g., `{% for product in featured_products %}`).
3.  **Static Files Management:** Correctly loading CSS and images (`{% static 'styles.css' %}`).
4.  **Form Handling:** Implementing the user authentication forms (`login.html`, `signup.html`) and using the `{% csrf_token %}` security tag.

## 🚀 Future Roadmap

* Implement the full **Django backend** (models, database setup).
* Integrate full **User Authentication** and form validation.
* Add a **Shopping Cart** and **Checkout** system.

---
