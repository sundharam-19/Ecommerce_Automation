E-Commerce Web Application Automation Testing

Project Title

Automated Testing of E-Commerce Web Application using Python Selenium

---

Project Objective

The objective of this project is to automate the testing of the e-commerce web application:

https://www.saucedemo.com

The automation framework validates core functionalities of the application by simulating real-time user actions using Selenium WebDriver and Python.

The project ensures the stability, reliability, and functionality of major application workflows such as login, product selection, cart management, checkout process, sorting functionality, and application reset state.

---

Technologies Used

- Python 3.11
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Allure Reports
- ChromeDriver
- PyCharm / VS Code

---

Project Structure

Ecommerce/
│
├── cart_page.py
├── checkout_page.py
├── login_page.py
├── products_page.py
├── conftest.py
├── requirements.txt
│
├── test_login.py
├── test_logout.py
├── test_cart.py
├── test_checkout.py
├── test_sorting.py
├── test_resetapp.py
│
├── reports/
├── allure-report/
└── README.md

---

Features Automated

1. Login Functionality

- Valid login verification
- Username and password handling
- Login button validation

2. Logout Functionality

- Open side menu
- Logout verification

3. Product Selection

- Add products to cart
- Random product selection

4. Cart Validation

- Verify products added to cart
- Cart item visibility validation

5. Checkout Process

- Checkout button validation
- User information form handling
- Order completion validation

6. Product Sorting

- Sort products by price
- Sort validation

7. Reset App State

- Reset application data
- Cart reset validation

---

Framework Design

The project follows the Page Object Model (POM) design pattern.

Advantages of POM

- Reusable code
- Better maintenance
- Improved readability
- Scalable automation framework

---

Installation

Clone the Repository

git clone <repository-url>

Navigate to Project Directory

cd Ecommerce

Create Virtual Environment

python -m venv venv

Activate Virtual Environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

---

Running Test Cases

Run All Tests

pytest -v

Run Specific Test File

pytest test_login.py -v

---

Allure Reporting

Generate Allure Results

pytest --alluredir=reports

Serve Allure Report

allure serve reports

Generate Static Allure Report

allure generate reports -o allure-report --clean

Open Allure Report

allure open allure-report

---

Challenges Faced

- Chrome password manager popup interruption
- Selenium element synchronization issues
- Dynamic element handling
- Timeout exceptions
- Element click interception

---

Solutions Implemented

- Explicit waits using WebDriverWait
- Chrome popup disabling through ChromeOptions
- JavaScript click execution
- Improved element synchronization
- Robust locator strategies

---

Test Execution Summary

Test Case| Status
Login Test| Passed
Logout Test| Passed
Cart Test| Passed
Checkout Test| Passed
Sorting Test| Passed
Reset App State Test| Passed

---

Future Enhancements

- Cross-browser testing
- Parallel execution
- Jenkins CI/CD integration
- Screenshot capture on failure
- Data-driven testing
- Docker integration
- Headless execution

---

Author

S Sundharam

GitHub: https://github.com/sundharam-19

---

Conclusion

This project successfully automates the major functionalities of the SauceDemo e-commerce application using Selenium with Python. The framework is scalable, maintainable, and follows industry-standard automation practices using Pytest and Page Object Model architecture.
