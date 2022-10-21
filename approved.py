from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC



def main():
    options = Options()
    options.add_argument = ("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("http://192.168.1.235")

    try:
        authorization(driver, )
        #button(driver, )


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def authorization(driver, path_login, path_password, path_enter, login, password):
    driver.find_element(By.XPATH, path_login).send_keys(login)
    driver.find_element(By.XPATH, path_password).send_keys(password)
    driver.find_element(By.XPATH, path_enter).click()


def button(driver, path):
    WebDriverWait(driver, 5, 3).until(
        EC.visibility_of_element_located((By.XPATH, path)))

    driver.find_element(By.XPATH, path).click()


if __name__ == "__main__":
    main()



