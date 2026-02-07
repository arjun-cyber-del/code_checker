PYTHON CODE CHECKER (WEB VERSION)
================================

This project is a simple Flask-based web application that checks Python code
for syntax errors and highlights exactly where the error occurs using an arrow (^).

The goal of this project is to demonstrate basic static code analysis concepts
related to cybersecurity and secure coding practices.

--------------------------------------------------
FEATURES
--------------------------------------------------
- Paste Python code into a web interface
- Detects syntax errors before execution
- Displays:
  - Error message
  - Line number
  - Exact position of the error with an arrow (^)
- Helps developers identify issues early and avoid unsafe code execution

--------------------------------------------------
TECH STACK
--------------------------------------------------
- Python
- Flask
- HTML (Jinja2 templates)

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------
code-checker-web/
|
|-- app.py
|-- requirements.txt
|
|-- templates/
|   |-- index.html
|
|-- static/
    |-- (optional CSS files)

--------------------------------------------------
HOW TO RUN LOCALLY
--------------------------------------------------
1. Install Python (3.x)

2. In
