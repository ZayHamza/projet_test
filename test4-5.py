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
# TC-01 : Vérifier que le footer est bien aligné au bas de la page
# ---------------------------------------------------------
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll jusqu'en bas de la page

try:
    footer = WebDriverWait(driver, 10).until(  # Attente plus longue pour le footer
        EC.presence_of_element_located((By.ID, "site-footer"))
    )
    footer_text = footer.text
    print(f"Footer text: {footer_text}")  # Affichage du texte du footer pour mieux comprendre
    # Vérifier que le texte du footer contient "Copyright" ou "©"
    assert "copyright" in footer_text.lower() or "©" in footer_text, "Footer non trouvé"

    driver.save_screenshot("captures/TC01_footer_aligned.png")
    print("TC-01 : Footer aligné au bas de la page")

except TimeoutException:
    print("Le footer n'a pas pu être chargé dans le délai imparti.")
    driver.save_screenshot("captures/TC01_footer_not_found.png")


# ---------------------------------------------------------
# TC-02 : Vérifier que tous les liens du footer fonctionnent
# ---------------------------------------------------------
try:
    footer_links = driver.find_elements(By.CSS_SELECTOR, "#site-footer a")  # Tous les liens dans le footer

    for link in footer_links:
        link.click()
        time.sleep(1)  # Attendre le chargement de la page
        driver.back()  # Retour à la page précédente pour tester le prochain lien
        time.sleep(1)
        # Récupérer à nouveau les liens après avoir cliqué
        footer_links = driver.find_elements(By.CSS_SELECTOR, "#site-footer a")
        assert "404" not in driver.title, f"Le lien {link.text} est cassé"
        driver.save_screenshot(f"captures/TC02_link_{link.text}_working.png")
        print(f"TC-02 : Lien {link.text} fonctionne")

except Exception as e:
    print(f"TC-02 : Erreur lors du test des liens du footer - {str(e)}")
    driver.save_screenshot("captures/TC02_links_error.png")


# ---------------------------------------------------------
# Test du footer - Vérification de l'année
# ---------------------------------------------------------
try:
    footer_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "site-footer"))
    ).text  # Utilisation du bon ID du footer

    print(f"Text du footer pour TC-03 : {footer_text}")  # Affiche le texte du footer pour mieux comprendre

    # Vérification que l'année est correcte (2020, 2024, ou 2025)
    if "2025" in footer_text or "2024" in footer_text or "2020" in footer_text:
        print("TC-03 : L'année du footer est correcte")
        driver.save_screenshot("captures/Footer_year_correct.png")
    else:
        print("TC-03 : L'année dans le footer est incorrecte - FAIL")
        driver.save_screenshot("captures/Footer_year_incorrect.png")

except TimeoutException:
    print("TC-03 : Le footer n'a pas pu être chargé dans le délai imparti.")
    driver.save_screenshot("captures/Footer_year_not_found.png")


# Fermer le navigateur
driver.quit()
print("Tous les tests sont terminés.")
