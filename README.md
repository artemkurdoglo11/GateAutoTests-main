# LiveCoding

pip install -r requirements.txt

pytest --alluredir=allure-results

npm install -g npm@11.4.0

npm install -g allure-commandline
npm config get prefix

allure generate --clean -o allure-report allure-results

allure serve allure-results
