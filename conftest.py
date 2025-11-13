import os
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # Descomenta si quieres que NO se abra la ventana del navegador:
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest que se ejecuta después de cada test.
    Si el test falla y hay un fixture 'driver', hace una captura.
    """
    outcome = yield
    report = outcome.get_result()

    # Solo nos interesa la fase "call" (cuando se ejecuta el test, no el setup/teardown)
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            # Carpeta donde se guardan las capturas de fallo
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            print(f"\n➡️ Captura de fallo guardada en: {file_path}")
