from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Portfolio:
    home = "//span[text()='Home']"
    aboutme = "//span[text()='About Me']"
    skills = "//span[text()='Skills']"
    skills_items = [
        "//button[text()='Programming']",
        "//button[text()='Frontend']",
        "//button[text()='Others']"
    ]
    projects = "//span[text()='Projects']"
    projects_items = [
        "//button[text()='Static']",
        "//button[text()='Responsive']",
        "//button[text()='Dynamic']"
    ]
    contact = "//span[text()='Contact Me']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_home(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.home))).click()

    def click_aboutme(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.aboutme))).click()

    def click_skills(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.skills))).click()

    def click_skills_items(self):
        for item_xpath in self.skills_items:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath))).click()

    def click_projects(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.projects))).click()

    def click_projects_items(self):
        for item_xpath in self.projects_items:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath))).click()

    def click_contact(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.contact))).click()
