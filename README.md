# repository_list_automation
FE Automated Test Suite for Repo Search Portal


Pre-requisites:
- Install python3
- Install pip3
- Install chrome driver
- Install allure (if allure reporting required)

## **To run Automated test suite**

- Run the repo-search web app at your local: follow readme of https://github.com/ajay-grover/repository_list_automation



### **Setup automated test suite at local:**

- Clone the repo https://github.com/ajay-grover/repository_list_automation
- Go to repository_list_automation directory and run `pip3 install -r requirements.txt`
- Export chrome driver path as `SELENIUM_URL` 
    e.g. run cmnd `export SELENIUM_URL=/opt/homebrew/bin/chromedriver`
- Run automated test suite using pytest 
    `pytest test_repository_list/`

- Generate allure report with the test run using below cmnd:
    `pytest test_repository_list/ --alluredir=./artifacts`
    
- Load generated allure report 
    `allure serve path_to_artifacts_folder`