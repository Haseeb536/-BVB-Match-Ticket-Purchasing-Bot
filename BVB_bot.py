from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def capture_dom(driver):
    script = """
    var domContent = document.documentElement.outerHTML;
    return domContent;
    """
    return driver.execute_script(script)

def capture_svg(driver):
    script = """
    var svgContent = document.querySelector('svg') ? document.querySelector('svg').outerHTML : '';
    return svgContent;
    """
    return driver.execute_script(script)


driver = Driver(uc=True)

try:
    driver.get("https://www.ticket-onlineshop.com/ols/bvb/de/profis/channel/shop/index/")
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="cookieConsentAgree"]').click()
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="login-link"]/div').click()
    time.sleep(5)

    username_input = driver.find_element(By.XPATH, '//*[@id="text-input-id-0"]')
    username_input.send_keys("bloodeye369@gmail.com")
    password_input = driver.find_element(By.XPATH, '//*[@id="password-input-id-0"]')
    password_input.send_keys("Superman@12345")
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

    driver.find_element(By.XPATH, '//*[@id="menu-item-1543"]').click()
    time.sleep(10)

    driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div[2]/div[2]/a').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="choose-seat-button"]').click()
    time.sleep(10)

    # Capture DOM content
    dom_content = capture_dom(driver)
    print("DOM content captured:")
    print(dom_content)
    
    # Capture SVG content
    svg_content = capture_svg(driver)
    print("\nSVG content captured:")
    print(svg_content)

finally:
    driver.quit()
