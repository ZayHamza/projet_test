from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialiser le driver
driver = webdriver.Chrome()

# Créer un dossier pour les captures d'écran si il n'existe pas
if not os.path.exists("captures"):
    os.makedirs("captures")

# ---------------------------------------------------------
# TC-01 : NoSuchElementException
# ---------------------------------------------------------
driver.get("https://practicetestautomation.com/practice-test-login/")
try:
    driver.find_element(By.ID, "elementXYZ")  # Élément inexistant
except NoSuchElementException:
    print("Élément non trouvé")
driver.save_screenshot("captures/Exception_NoSuchElement.png")

# ---------------------------------------------------------
# TC-02 : ElementNotInteractableException
# ---------------------------------------------------------
driver.get("https://practicetestautomation.com/practice-test-login/")
try:
    element = driver.find_element(By.TAG_NAME, "html")
    element.send_keys(Keys.ENTER)  # Action sur un élément non interactif
except ElementNotInteractableException:
    print("Élément non interactif")
driver.save_screenshot("captures/Exception_ElementNotInteractable.png")

# ---------------------------------------------------------
# TC-03 : InvalidElementStateException
# ---------------------------------------------------------
driver.get("https://practicetestautomation.com/practice-test-login/")
try:
    # Utilisation de WebDriverWait avec un délai plus court (5 secondes)
    input_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))  # Utilisation du XPath ici
    )
    input_field.clear()  # État invalide
except InvalidElementStateException:
    print("État de l'élément invalide")
driver.save_screenshot("captures/Exception_InvalidElementState.png")

# ---------------------------------------------------------
# Test du footer - Vérification de l'année
# ---------------------------------------------------------
try:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    # Attente explicite de l'élément footer avec un délai plus court (5 secondes)
    footer_text = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "site-footer"))
    ).text  # Utilisation du bon ID du footer

    # Vérification que l'année est correcte
    if "2025" in footer_text or "2024" in footer_text:
        print("L'année du footer est correcte")
        driver.save_screenshot("captures/Footer_year_correct.png")
    else:
        print("L'année dans le footer est incorrecte - FAIL")
        driver.save_screenshot("captures/Footer_year_incorrect.png")

except TimeoutException:
    print("Le footer n'a pas pu être chargé dans le délai imparti.")
    driver.save_screenshot("captures/Footer_year_not_found.png")

# Fermer le navigateur
driver.quit()
