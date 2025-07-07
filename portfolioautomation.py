from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://portfoliorz-li82.vercel.app/")
home=driver.find_element(By.XPATH,"//span[text()='Home']")
home.click()
time.sleep(2)
if driver.current_url=="https://portfoliorz-li82.vercel.app/#Home":
    print("working sucessfully home")
else:
    print("not working as expected")
aboutme=driver.find_element(By.XPATH,"//span[text()='About Me']")
aboutme.click()
time.sleep(2)
if driver.current_url=="https://portfoliorz-li82.vercel.app/#Aboutme":
    print("working sucessfully aboutme")
else:
    print("not working as expected")
skills=driver.find_element(By.XPATH,"//span[text()='Skills']")
skills.click()
time.sleep(2)
if driver.current_url=="https://portfoliorz-li82.vercel.app/#Skills":
    print("working sucessfully skills")
else:
    print("not working as expected")
skills_all=driver.find_element(By.XPATH,"//button[text()='All']")
skills_all.click()
time.sleep(1)
skills_programming=driver.find_element(By.XPATH,"//button[text()='Programming']")
skills_programming.click()
time.sleep(1)
skills_frontend=driver.find_element(By.XPATH,"//button[text()='Frontend']")
skills_frontend.click()
time.sleep(1)
skills_others=driver.find_element(By.XPATH,"//button[text()='Others']")
skills_others.click()
time.sleep(1)
projects=driver.find_element(By.XPATH,"//span[text()='Projects']")
projects.click()
time.sleep(1)
if driver.current_url=="https://portfoliorz-li82.vercel.app/#Projects":
    print("working sucessfully Projects")
else:
    print("not working as expected")
time.sleep(1)
projects_static=driver.find_element(By.XPATH,"//button[text()='Static']")
projects_static.click()
time.sleep(1)
projects_responsive=driver.find_element(By.XPATH,"//button[text()='Responsive']")
projects_responsive.click()
time.sleep(1)
projects_dynamic=driver.find_element(By.XPATH,"//button[text()='Dynamic']")
projects_dynamic.click()
time.sleep(1)
contactme=driver.find_element(By.XPATH,"//span[text()='Contact Me']")
contactme.click()
if driver.current_url=="https://portfoliorz-li82.vercel.app/#Contact":
    print("working sucessfully ContactMe")
else:
    print("not working as expected")
time.sleep(1)


