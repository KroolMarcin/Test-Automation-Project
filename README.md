# Project Name: Test Automation Project

## Description
The project involves automated testing for the [HerokuApp](https://the-internet.herokuapp.com) website using various tools and frameworks.

The goal is to compare these tools in terms of performance, ease of use, and support.

## Technologies
- Java
- Python
- TypeScript
- Selenium
- Cypress
- Playwright

## Python with Selenium
### Prerequisites:
- Python 3.x
- Selenium WebDriver
- Allure (for reporting) - Installation instructions can be found at the https://allurereport.org/docs/gettingstarted/installation/

### Setup:
```bash
git clone https://github.com/KroolMarcin/Test-Automation-Project.git
cd Selenium_Python
pip install -r requirements.txt
```
### Running Tests:
Run tests using the following command:
```bash
python -m pytest --alluredir=/allure_results test_herokuapp.py
```
### Reporting with Allure:
Before generating reports with Allure, ensure it's installed and properly configured on your system.
To install Allure, refer to the official Allure documentation.
After running tests, generate Allure reports using:
```bash
allure serve /allure_results
```