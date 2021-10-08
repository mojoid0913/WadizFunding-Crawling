from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

url = "https://www.wadiz.kr/web/wreward/category?keyword=&endYn=ALL&order=recommend"

driver = webdriver.Chrome(executable_path='/Users/chanjo/Downloads/chromedriver')
driver.set_window_position(0,0)
driver.set_window_size(550,1000)
driver.get(url)

elem_category = driver.find_element_by_css_selector(".RewardCategoryTabList_category__32e1B")
dir_category = elem_category.find_elements_by_css_selector("li [href]")
links = [category.get_attribute('href') for category in dir_category]

for i in links:
    driver.get(i)

    SCROLL_PAUSE_SEC = 2

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollBy(0, -500);")
        time.sleep(SCROLL_PAUSE_SEC)
        
        try:
            driver.find_element_by_class_name("ProjectListMoreButton_button__27eTb").click()
        except NoSuchElementException:  #spelling error making this code not work as expected
            break

    elem_contents = driver.find_elements_by_class_name("ProjectCardList_item__1owJa")
    print(len(elem_contents))


driver.close()



