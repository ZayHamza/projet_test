from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chemin vers le ChromeDriver
driver_path = r"C:\chromedriver-win32\chrome-win32\chromedriver.exe"

# Dossier des screenshots
screenshot_folder = r"c:\Users\zayxh\OneDrive\Bureau\fonctionnalite3\\"

# Initialiser Selenium
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://practicetestautomation.com/practice-test-table/')
time.sleep(3)

# --------------------------- Fonction Screenshot -----------------------------
def take_screenshot(name):
    driver.save_screenshot(screenshot_folder + name + ".png")
    print(f"   → Screenshot enregistré : {name}.png")

# --------------------------- TC-01 ------------------------------------------
def test_language_filter():
    try:
        print("TC-01 : Test Language Filter")
        language_checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[1]/label[2]/input'))
        )
        language_checkbox.click()
        time.sleep(1)

        courses = driver.find_elements(By.CLASS_NAME, 'course')
        assert all('Java' in course.text for course in courses)

        print("TC-01 : Pass")
        take_screenshot("TC01_pass")

    except Exception as e:
        print(f"TC-01 : Fail - {e}")

# --------------------------- TC-02 ------------------------------------------
def test_level_filter():
    try:
        print("TC-02 : Test Level Filter")
        beginner = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[2]/label[1]'))
        )
        intermediate = driver.find_element(By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[2]/label[2]')
        advanced = driver.find_element(By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[2]/label[3]')

        intermediate.click()
        advanced.click()
        time.sleep(1)
        beginner.click()
        time.sleep(1)

        courses = driver.find_elements(By.CLASS_NAME, 'course')
        assert all('Beginner' in course.text for course in courses)

        print("TC-02 : Pass")
        take_screenshot("TC02_pass")

    except Exception as e:
        print(f"TC-02 : Fail - {e}")

# --------------------------- TC-03 ------------------------------------------
def test_min_enrollments():
    try:
        print("TC-03 : Test Min Enrollments")
        min_enroll = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[3]'))
        )
        min_enroll.click()
        time.sleep(1)

        courses = driver.find_elements(By.CLASS_NAME, 'course')
        assert all(int(c.get_attribute('data-enrollments')) >= 10000 for c in courses)

        print("TC-03 : Pass")
        take_screenshot("TC03_pass")

    except Exception as e:
        print(f"TC-03 : Fail - {e}")

# --------------------------- TC-04 ------------------------------------------
def test_combined_filters():
    try:
        print("TC-04 : Test Combined Filters")

        python = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[1]/label[3]'))
        )
        intermediate = driver.find_element(By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[2]/label[2]')
        advanced = driver.find_element(By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[2]/label[3]')
        min_enroll = driver.find_element(By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[3]')

        python.click()
        intermediate.click()
        advanced.click()
        time.sleep(1)
        min_enroll.click()
        time.sleep(1)

        courses = driver.find_elements(By.CLASS_NAME, 'course')
        assert len(courses) == 0

        print("TC-04 : Pass")
        take_screenshot("TC04_pass")

    except Exception as e:
        print(f"TC-04 : Fail - {e}")

# --------------------------- TC-05 ------------------------------------------
def test_no_results_state():
    try:
        print("TC-05 : Test No Results State")

        python = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[1]/label[3]'))
        )
        intermediate = driver.find_element(By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[2]/label[2]')
        advanced = driver.find_element(By.XPATH, '//*[@id="xpath-table"]/div[2]/fieldset[2]/label[3]')

        python.click()
        intermediate.click()
        advanced.click()
        time.sleep(1)

        courses = driver.find_elements(By.CLASS_NAME, 'course')
        assert len(courses) == 0

        print("TC-05 : Pass")
        take_screenshot("TC05_pass")

    except Exception as e:
        print(f"TC-05 : Fail - {e}")

# --------------------------- EXECUTION --------------------------
test_language_filter()
test_level_filter()
test_min_enrollments()
test_combined_filters()
test_no_results_state()

driver.quit()
