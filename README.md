# QA Automation Starter  
This repository provides a starter kit for QA automation using Python, pytest, and httpx. It includes a sample API test against jsonplaceholder.typicode.com and a GitHub Actions workflow to run tests on push.  

## Prerequisites  
- Python 3.8+  
- pip  

## Setup  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/ihabnk91/qa-automation-starter.git  
   cd qa-automation-starter  
   ```  
2. Create a virtual environment (optional but recommended) and activate it.  
3. Install dependencies:  
   ```bash  
   pip install pytest httpx  
   ```  

## Running Tests  
To run the test suite locally:  
```bash  
pytest  
```  

## GitHub Actions CI  
A GitHub Actions workflow (`python-tests.yml`) is configured to automatically run the tests on each push to the repository. This ensures that your API tests run continuously.  

## Sample Test  
The sample test located in `tests/test_sample.py` sends a GET request to jsonplaceholder.typicode.com and asserts the response.
