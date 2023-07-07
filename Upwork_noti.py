
eml=input("Enter your email: ")
pas=input("Enter your email password: ")
flag=int(input("Input 1 or 2 according to option:\n1.Metatrader + Pine Script\n2.Only Pine Script"))

import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()

chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=chrome_options)
driver.maximize_window()
# Navigate to Google sign in page
driver.get("https://accounts.google.com/signin")

# Fill in email
email = driver.find_element(By.ID, "identifierId")
email.send_keys(eml)

# Click next
next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button.click()
time.sleep(15)
# Fill in password
password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(pas)

# Click next
next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
next_button.click()

while True:
    try:
        driver.get("https://www.upwork.com/")
        time.sleep(2)
        # Now you should be logged in
        driver.find_element(By.CSS_SELECTOR,"#nav-main > div > a.nav-item.login-link.d-none.d-lg-block.px-20").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#login_google_submit").click()
        time.sleep(2)
        input("Enter anything here:")
        # driver.find_element(By.CSS_SELECTOR,"#next_continue").click()
        # time.sleep(2)
        # otp=input("Enter Your OTP code: ")
        # driver.find_element(By.CSS_SELECTOR,"#deviceAuthOtp_otp").send_keys(otp)
        # driver.find_element(By.CSS_SELECTOR,"#next_continue").click()
        time.sleep(5)
        if flag==1:
            main_url="https://www.upwork.com/nx/jobs/search/?q=%22pine%20script%22%20OR%20%22metatrader%205%22%20OR%20%22pinescript%22&sort=recency"
        else:
            main_url="https://www.upwork.com/nx/jobs/search/?q=%22pine%20script%22%20OR%20%22pinescript%22&sort=recency"
        # main_url="https://www.upwork.com/nx/jobs/search/?q=%22php%22%20OR%20%22Python%22%20OR%20%22Data%20entry%22&sort=recency"
        driver.get(main_url)
        time.sleep(2)
        apiToken = '6034662055:AAEFrcg5j5eMKyx6GcOVIgMtPT_LurCXENs'
        chatID = '1670178408''1670178408'
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

        pre_project=""
        while True:
            try:
                main_div=driver.find_element(By.CSS_SELECTOR,"#main > div.container > div.row.app-frame.is-user > div > div > div.col-9 > div > div.up-card-section.pt-0 > div > div:nth-child(2)")
                job_box=main_div.find_element(By.TAG_NAME,"section")
                p_title=job_box.find_element(By.TAG_NAME,"h3").text
                des=job_box.find_element(By.CLASS_NAME,"mt-10").text[0:200]
                p_url=job_box.find_element(By.TAG_NAME,"a").get_attribute("href")
                budget=job_box.find_elements(By.TAG_NAME,"small")
                budget=budget[1].text.split("-")
                budget.pop()
                budget= '-'.join(budget)
                project=p_title
                if project!=pre_project:
                    message = f"New UpWork project posted:\n{p_title}\n\n{budget}\n\nDescription: {des}\n\nProject URL:\n{p_url}"
                    response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
                    pre_project=p_title        
                time.sleep(2)

                time.sleep(2)
                driver.get(main_url)
                time.sleep(2)


            except:
                continue
    except:
        continue
