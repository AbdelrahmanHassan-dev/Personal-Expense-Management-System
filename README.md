# Personal-Expense-Management-System
Description: Backend-oriented Python application for managing personal expenses with structured data validation, monthly analytics, live RUB→EGP currency conversion via web scraping, and automated PDF report generation. Demonstrates OOP, functional programming, and backend data processing principles.
Project Overview

A backend-oriented personal expense management system developed in Python.
The application allows users to record, validate, analyze, and report daily expenses while integrating real-time currency conversion through external data scraping.

The system focuses on clean business logic, data processing, and automation, demonstrating core backend programming principles such as structured data handling, validation, analytics, and external service integration.

Key Features

Structured expense tracking with category, amount, and date

Robust input validation using Regular Expressions

Monthly expense filtering and statistical analysis

Average daily spending calculation

Detection and filtering of high-expense records

Live currency conversion (RUB → EGP) via web scraping

Automated generation of professional PDF financial reports

Technical Details

Language: Python

Programming Paradigms: Object-Oriented Programming (OOP), Functional Programming

Data Handling: CSV file storage with structured read/write operations

Validation: Regex-based input parsing and error prevention

Data Analysis: map, filter, lambda expressions

External Integration: Web scraping using Requests and BeautifulSoup

Reporting: PDF generation using fpdf2

Architecture Summary

Central control flow managed through a main application loop

Business logic separated into dedicated processing functions

Expense data represented as objects for clarity and scalability

Analytical functions operate on structured datasets rather than raw input

External currency data fetched dynamically at runtime

Demo

YouTube: https://youtu.be/JPDN5npJKwI

Google Drive: https://drive.google.com/file/d/1ondRhL9Pc-8Cx_B61dfCx5zCug2ca6C1/view

Installation & Usage
pip install -r requirements.txt
python project.py


Users interact through a menu-driven interface to record expenses, view statistics, convert currency values, and generate reports.
