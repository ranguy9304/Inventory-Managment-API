
# Stockpile: Inventory Management System with Django

## Introduction:

Stockpile is a database management system tailored to offer an all-in-one solution for efficient inventory management. Built using Django and PostgreSQL, Stockpile enables businesses to seamlessly manage inventory items, suppliers, customers, orders, and sales.

## Table of Contents:

  -  Features
  -  Installation and Setup
  - Database Models and Relationships
  - API Endpoints
  - Assumptions
  - Contributing

## Features <a name="features"></a>

  Inventory Tracking: Log and manage every inventory item, monitor stock levels, and maintain item locations.
  Automated Inventory Management: Set up purchase orders, update stock levels, and automate inventory tasks.
  Reports & Analytics: Extract comprehensive reports on inventory metrics, sales, and more.
  Customer Data Management: Record and manage customer purchase history and contact details.

## Installation and Setup <a name="installation"></a>

  Clone the repository:

```

git clone https://github.com/yourusername/stockpile.git

```
Move to the directory:

```bash

cd stockpile
```
Set up a virtual environment:

```bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Install dependencies:

```bash

pip install -r requirements.txt
```
Setup database:

```bash

python manage.py migrate
```
Run the server:

```bash

    python manage.py runserver
```
## Database Models and Relationships <a name="db-models"></a>

  Customer: Stores customer data including contact details and purchase history.
  Orders: Contains details about individual orders and associated products.
  Employee: Holds details about the employee including job status.
  Shop: Information about individual shops.
  StorageUnit: Details about each storage unit, its capacity and associated products.
  Product: Contains details about the individual products, their category, and supplier.

###  FOR MORE DETAILED MODEL DESCRIPTION AND OTHER DETAILES PLEASE REFER TO REPORT DOCUMENT UPLOADED WITH CODE


