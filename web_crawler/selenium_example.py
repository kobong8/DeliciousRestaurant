from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

if __name__ == "__main__":
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.get("https://map.kakao.com/")

    search_input = driver.find_element(By.ID, "search.keyword.query")
    search_input.send_keys("강남구 카페")
    search_input.send_keys(Keys.ENTER)

    # show_more_btn의 역할 여기 위치하는게 맞는지?
    show_more_btn = driver.find_element(By.ID, "info.search.place.more")
    show_more_btn.click()

    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.ID, "info.search.place.list")))

    place_list = driver.find_element(By.ID, "info.search.place.list")
    shop_list = place_list.get_attribute("innerHTML")

    print(place_list)
    print(shop_list)

    driver.quit()
