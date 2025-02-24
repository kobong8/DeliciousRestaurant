from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

if __name__ == "__main__":
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.get("https://map.kakao.com/")
    wait = WebDriverWait(driver, 10)
