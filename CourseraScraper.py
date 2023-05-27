from CourseraClass import CourseraCourse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def main():
    subjects = ["Data_Science", "Business", "Computer_Science", "Arts_and_Humanities", "Social_Sciences", \
                "Language_Learning", "Health", "Personal_Development", "Physical_Sciences_and_Engineering", \
                "Life_Sciences"]

    url_file = "~/Course_URLS/" + subjects[0] + "_urls.txt"
    with open(url_file, "r") as infile:
        all_urls = infile.readlines()
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
        for course_url in all_urls:
            course = CourseraCourse(course_url, driver)
            course.get_info()
            course.get_reviews()
            # course.print_some_reviews()
            if course.has_reviews():
                course.build_reviews_df()
                course.export_reviews_df(file_path="~/Reviews/" + subjects[0] + "_Reviews/")
                course.build_course_json(file_path="~/JSON_files/" + subjects[0] + "_JSON/")
        driver.quit()
    

    

main()


from selenium import webdriver
import time


driver = webdriver.Chrome("~/chromedriver")

# {Subject name: Url of all courses from that subject}
subject_dict = {"Business": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Business&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true",
                "Computer_Science": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Computer%20Science&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true",
                "Health": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Health&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true",
                "Physical_Science_and_Engineering": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Physical%20Science%20and%20Engineering&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_suggestions%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_suggestions%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_careers%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_degrees_keyword_only%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_products%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bpage%5D=1",
                "Data_Science": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Data%20Science&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true",
                "Social_Sciences": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Social%20Sciences&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_suggestions%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_suggestions%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_careers%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_degrees_keyword_only%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_products%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bpage%5D=1",
                "Arts_and_Humanities": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Arts%20and%20Humanities&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_suggestions%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_suggestions%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_careers%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_degrees_keyword_only%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_products%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bpage%5D=1",
                "Language_Learning": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Language%20Learning&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_suggestions%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_suggestions%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_careers%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_degrees_keyword_only%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_products%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bpage%5D=1",
                "Personal_Development": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Personal%20Development&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_suggestions%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_suggestions%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_careers%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_degrees_keyword_only%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_products%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bpage%5D=1",
                "Information_Technology": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Information%20Technology&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_suggestions%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_suggestions%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_careers%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_degrees_keyword_only%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_products%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bpage%5D=1",
                "Math_and_Logic": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Math%20and%20Logic&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_suggestions%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_suggestions%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_careers%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_degrees_keyword_only%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_products%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bpage%5D=1",
                "Life_Sciences": "https://www.coursera.org/courses?query=&refinementList%5Btopic%5D%5B0%5D=Life%20Sciences&page=1&configure%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_suggestions%5D%5Bconfigure%5D%5BhitsPerPage%5D=7&indices%5Btest_suggestions%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_suggestions%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_careers%5D%5Bconfigure%5D%5BhitsPerPage%5D=1&indices%5Btest_careers%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_careers%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_degrees_keyword_only%5D%5Bconfigure%5D%5BhitsPerPage%5D=4&indices%5Btest_degrees_keyword_only%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_degrees_keyword_only%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Btest_products%5D%5BrefinementList%5D%5Bpage%5D=1&indices%5Btest_products%5D%5Bpage%5D=1"}


def click_show_more(url):

    driver.get(url)
    while True:
        try:
            button = driver.find_element_by_xpath("//button[@class='ais-InfiniteHits-loadMore']")
            button.click()
            time.sleep(2)
        except Exception as e:
            print(e)
            print("Got to the end!")
            break


def get_all_urls():
    results = driver.find_elements_by_xpath("//li[@class='ais-InfiniteHits-item']//a")
    time.sleep(5)
    print(len(results), "total links found!")
    hrefs = [result.get_attribute("href") for result in results if "/learn/" in result.get_attribute("href")]
    print(len(hrefs), "course links found!")
    return hrefs


def extract_all_subjects():
    for name, url in subject_dict.items():
        print(f"Extracting links from {name}...")
        click_show_more(url)
        links = get_all_urls()
        with open(name + "_urls.txt", "w") as file:
            for link in links:
                file.write(link + "\n")


def extract_one_subject(subj_name):
    url = subject_dict[subj_name]
    click_show_more(url)
    links = get_all_urls()

    with open(subj_name + "_urls.txt", "w") as file:
        for link in links:
            file.write(link + "\n")


def main():
    # extract_all_subjects()
    extract_one_subject("Business")


main()