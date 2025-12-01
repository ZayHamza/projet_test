from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Initialiser le driver
driver = webdriver.Chrome()

# Créer un dossier pour les captures d'écran si il n'existe pas
if not os.path.exists("captures"):
    os.makedirs("captures")

# ---------------------------------------------------------
# TC-01 : Ouvrir la page Contact
# ---------------------------------------------------------


def test_contact_page():
    driver.get("https://practicetestautomation.com/contact/")
    time.sleep(2)  # Temps d'attente pour charger la page
    driver.save_screenshot("captures/Contact_page_opened.png")
    print("PASS: La page Contact a été ouverte.")

# ---------------------------------------------------------
# TC-02 : Vérifier la visibilité du formulaire de contact
# ---------------------------------------------------------


def test_contact_form_visibility():
    try:
        driver.get("https://practicetestautomation.com/contact/")

        # Utilisation de WebDriverWait pour attendre que le formulaire soit visible
        contact_form = driver.find_element(By.ID, "wpforms-form-161")  # Utilisation de l'ID du formulaire
        assert contact_form.is_displayed()
        print("PASS: Le formulaire de contact est visible.")
        driver.save_screenshot("captures/Contact_form_visible.png")
    except Exception as e:
        print(f"FAIL: Le formulaire de contact n'est pas visible. {e}")
        driver.save_screenshot("captures/Contact_form_fail.png")

# ---------------------------------------------------------
# TC-03 : Vérifier la visibilité des placeholders
# ---------------------------------------------------------


def test_contact_form_placeholders():
    driver.get("https://practicetestautomation.com/contact/")
    try:
        # Utilisation de WebDriverWait pour attendre que les éléments soient visibles
        name_field = driver.find_element(By.ID, "wpforms-161-field_0-container")  # Nom
        email_field = driver.find_element(By.ID, "wpforms-161-field_1-container")  # Email
        message_field = driver.find_element(By.ID, "wpforms-161-field_2-container")  # Message

        # Vérification de la visibilité des placeholders
        assert name_field.is_displayed()
        assert email_field.is_displayed()
        assert message_field.is_displayed()

        print("PASS: Les champs de formulaire sont visibles.")
        driver.save_screenshot("captures/Contact_form_placeholders.png")
    except Exception as e:
        print(f"FAIL: Les champs de formulaire ne sont pas visibles. {e}")
        driver.save_screenshot("captures/Contact_form_placeholders_fail.png")


# Lancer les tests
test_contact_page()
test_contact_form_visibility()
test_contact_form_placeholders()

# Fermer le navigateur
driver.quit()
