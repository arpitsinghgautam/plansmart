from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

def ScrapComment(url):
    option = Options()
    option.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    driver.get(url)
    time.sleep(5)  # Wait for the page to load (adjust as needed)

    # Find the button using its HTML code.
    buttons = driver.find_elements(By.CSS_SELECTOR, "button[data-purpose='show-reviews-modal-trigger-button']")
    # Iterate through the list of buttons and find the one that you want.
    for button in buttons:
        if button.text == "Show all reviews":
            button.click()
            break
    
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup)
    driver.quit()

    course_title = soup.select_one('.clp-lead__title')
    title = course_title and course_title.text.strip()

    review_comments = soup.select('.ud-component--clp--reviews')
    comment_list = [comment.text.strip() for comment in review_comments]

    print(title, comment_list)


if __name__ == "__main__":
    url = "https://www.udemy.com/course/fundamentals-of-math/"  # Replace with the Udemy course URL
    ScrapComment(url)

