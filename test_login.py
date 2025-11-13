from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

URL = "https://practicetestautomation.com/practice-test-login/"

def test_login_correcto(driver):
    driver.get(URL)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "username")))

    # Escribir credenciales
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")

    # 📸 Captura justo después de escribir usuario y contraseña
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    driver.save_screenshot(os.path.join(screenshots_dir, "antes_de_hacer_login.png"))

    # Click en Login
    driver.find_element(By.ID, "submit").click()

    # Validar login correcto
    wait.until(EC.url_contains("logged-in-successfully"))
    assert "Logged In Successfully" in driver.page_source

    # 📸 Captura de éxito
    driver.save_screenshot(os.path.join(screenshots_dir, "login_exitoso.png"))
