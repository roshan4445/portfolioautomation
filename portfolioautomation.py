import pytest
from selenium import webdriver
from Portfolio import Portfolio
import time

class TestPortfolio:
    @pytest.fixture
    def setup_requirements(self):
        driver = webdriver.Chrome()
        driver.get("https://portfoliorz-li82.vercel.app/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        obj = Portfolio(driver)
        yield driver, obj
        time.sleep(3)  # Optional: Keep browser open briefly to view result
        driver.quit()

    def test_home(self, setup_requirements):
        driver, obj = setup_requirements
        obj.click_home()
        time.sleep(2)
        assert driver.current_url == "https://portfoliorz-li82.vercel.app/#Home"

    def test_aboutme(self, setup_requirements):
        driver, obj = setup_requirements
        obj.click_aboutme()
        time.sleep(2)
        assert driver.current_url == "https://portfoliorz-li82.vercel.app/#Aboutme"

    def test_skills(self, setup_requirements):
        driver, obj = setup_requirements
        obj.click_skills()
        obj.click_skills_items()
        assert driver.current_url == "https://portfoliorz-li82.vercel.app/#Skills"

    def test_projects(self, setup_requirements):
        driver, obj = setup_requirements
        obj.click_projects()
        time.sleep(2)
        obj.click_projects_items()

        assert driver.current_url == "https://portfoliorz-li82.vercel.app/#Project"

    def test_contact(self, setup_requirements):
        driver, obj = setup_requirements
        obj.click_contact()
        assert driver.current_url == "https://portfoliorz-li82.vercel.app/#Contact"
