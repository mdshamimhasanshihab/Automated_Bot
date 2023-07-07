email=input("Enter your Email: ")
password=input("Enter your Password: ")
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.options import Options
#driver = webdriver.Chrome(executable_path='/Users/User/Upwork Project/PlanetX/chromedriver')
# driver.maximize_window()
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36')
# options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("lang=en-GB")
chrome_options.add_argument('--ignore-certificate-errors')
# self.options.add_argument('--lang=en')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
# self.options.add_argument("--log-level=OFF")
chrome_options.add_argument("--log-level=3")
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()
apiToken = '6034662055:AAEFrcg5j5eMKyx6GcOVIgMtPT_LurCXENs'
chatID = '1670178408'
apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

driver.get("https://www.freelancer.com/login")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#emailOrUsernameInput").send_keys(email)
driver.find_element(By.CSS_SELECTOR,"#passwordInput").send_keys(password)
driver.find_element(By.CSS_SELECTOR,"body > app-root > app-logged-out-shell > app-login-page > fl-container > fl-bit > app-login > app-credentials-form > form > app-login-signup-button > fl-button > button").click()
time.sleep(5)
driver.get("https://www.freelancer.com/search/projects?projectSkills=148,1384&projectLanguages=en")
pre_project=""
while True:
    try:
        driver.get("https://www.freelancer.com/search/projects?projectSkills=148,1384&projectLanguages=en")
        time.sleep(15)
        project=driver.find_element(By.CSS_SELECTOR,"body > app-root > app-logged-in-shell > div > fl-container > div > div > app-search > app-search-projects > fl-bit > fl-container > fl-bit > fl-bit.ResultsContainer > app-search-results > fl-card > fl-bit > fl-bit.CardBody > app-search-results-projects > fl-bit > fl-list > fl-list-item:nth-child(1) > fl-bit > fl-bit > fl-bit.BitsListItemHeader.HasHoverState.OuterPadding.First > fl-bit.BitsListItemContent.ng-star-inserted > fl-link > a > fl-project-contest-card > fl-bit.Container > fl-bit.Header > fl-bit.Title > fl-heading > h2").text
        if project!=pre_project:
            des=driver.find_element(By.CSS_SELECTOR,"body > app-root > app-logged-in-shell > div > fl-container > div > div > app-search > app-search-projects > fl-bit > fl-container > fl-bit > fl-bit.ResultsContainer > app-search-results > fl-card > fl-bit > fl-bit.CardBody > app-search-results-projects > fl-bit > fl-list > fl-list-item:nth-child(1) > fl-bit > fl-bit > fl-bit.BitsListItemHeader.HasHoverState.OuterPadding.First > fl-bit.BitsListItemContent.ng-star-inserted > fl-link > a > fl-project-contest-card > fl-text > div").text
            p_url=driver.find_element(By.CSS_SELECTOR,"body > app-root > app-logged-in-shell > div > fl-container > div > div > app-search > app-search-projects > fl-bit > fl-container > fl-bit > fl-bit.ResultsContainer > app-search-results > fl-card > fl-bit > fl-bit.CardBody > app-search-results-projects > fl-bit > fl-list > fl-list-item:nth-child(1) > fl-bit > fl-bit > fl-bit.BitsListItemHeader.HasHoverState.OuterPadding.First > fl-bit.BitsListItemContent.ng-star-inserted > fl-link > a").get_attribute("href")
            budget=driver.find_element(By.CSS_SELECTOR,"body > app-root > app-logged-in-shell > div > fl-container > div > div > app-search > app-search-projects > fl-bit > fl-container > fl-bit > fl-bit.ResultsContainer > app-search-results > fl-card > fl-bit > fl-bit.CardBody > app-search-results-projects > fl-bit > fl-list > fl-list-item:nth-child(1) > fl-bit > fl-bit > fl-bit.BitsListItemHeader.HasHoverState.OuterPadding.First > fl-bit.BitsListItemContent.ng-star-inserted > fl-link > a > fl-project-contest-card > fl-bit.Container > fl-bit.Header > fl-bit.BudgetUpgradeWrapper > fl-bit.BudgetUpgradeWrapper-budget.ng-star-inserted > fl-text > div").text
    #         skill=driver.find_element(By.CSS_SELECTOR,"body > app-root > app-logged-in-shell > div > fl-container > div > div > app-search > app-search-projects > fl-bit > fl-container > fl-bit > fl-bit.ResultsContainer > app-search-results > fl-card > fl-bit > fl-bit.CardBody > app-search-results-projects > fl-bit > fl-list > fl-list-item:nth-child(1) > fl-bit > fl-bit > fl-bit.BitsListItemHeader.HasHoverState.OuterPadding.First > fl-bit.BitsListItemContent.ng-star-inserted > fl-link > a > fl-project-contest-card > fl-bit:nth-child(3)").text
    #         skills=[]
    #         skill=skill.split("\n")
    #         for a in skill:
    #             skills.append(a)
            message = f"New project posted:\n{project}\n\n{budget}\n\nDescription: {des[0:200]}\n\nProject URL:\n{p_url}"
            response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
            pre_project=project
        time.sleep(5)
    except:
        continue