
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def filter_bmp(text):
    """Remove characters not in the Basic Multilingual Plane."""
    return ''.join(c for c in text if ord(c) <= 0xFFFF)

# Credentials and details
USERNAME = "chaarigaru"
PASSWORD = "chaarigaru143"
MESSAGE = "Hello, this is an automated message! sent by Venkata Kalyan."
RECIPIENT = "Venkata Kalyan"

# Filter strings to remove non-BMP characters

RECIPIENT = filter_bmp(RECIPIENT)
MESSAGE = filter_bmp(MESSAGE)

# Set up ChromeDriver
chrome_driver_path = "/usr/local/bin/chromedriver"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

# 1. Log in to Instagram
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)  # Allow page to load

username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)
time.sleep(5)

# 2. Dismiss any "Not Now" pop-ups
try:
    not_now_buttons = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//button[contains(text(), 'Not Now')]")
    ))
    for btn in not_now_buttons:
        btn.click()
        time.sleep(2)
except Exception:
    print("No 'Not Now' button found. Continuing...")

# 3. Navigate to Direct Messages
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(5)

# 4. Open the new message composer using alternative locators
new_message_xpaths = [
    "//div[contains(text(), 'Send message')]",
    "//div[@aria-label='New Message']",
    "//*[name()='svg' and @aria-label='New Message']",
    "//div[text()='New Message']"
]

new_message_clicked = False
for xpath in new_message_xpaths:
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        new_message_clicked = True
        time.sleep(3)
        print(f"Clicked new message icon using: {xpath}")
        break
    except Exception as e:
        print(f"Could not click new message icon with xpath {xpath}: {e}")

if not new_message_clicked:
    print("No new message icon found. Exiting...")
    driver.quit()
    exit()

# 5. Locate the search box in the new message dialog (try several options)
search_box = None
search_box_xpaths = [
    "//input[@aria-label='Search input']",
    "//input[@aria-label='Search']",
    "//input[@placeholder='Search...']"
]
for xpath in search_box_xpaths:
    try:
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        if search_box:
            print(f"Found search box using: {xpath}")
            break
    except Exception as e:
        print(f"Search box not found with xpath {xpath}: {e}")

if not search_box:
    print("Search box not found! Exiting...")
    driver.quit()
    exit()

# 6. Enter the recipient's username
search_box.send_keys(RECIPIENT)
time.sleep(3)  # Wait for search results to load

# 7. Select the account from search results by matching the text
try:
    # This XPath looks for an element within the dialog that contains the target username.
    user_result_xpath = f"//div[@role='dialog']//*[contains(text(), '{RECIPIENT}')]"
    user_element = wait.until(EC.element_to_be_clickable((By.XPATH, user_result_xpath)))
    user_element.click()
    time.sleep(2)
    print("Selected the user from search results.")
except Exception as e:
    print("Could not locate the account in search results:", e)
    driver.quit()
    exit()

# 8. Click the Chat button to open the conversation.
# Try several locators for a visible Chat/Next element.
chat_button_xpaths = [
    "//button[contains(text(), 'Next')]",
    "//button[contains(text(), 'Chat')]",
    "//div[contains(text(), 'Chat')]"
]
chat_clicked = False
for xpath in chat_button_xpaths:
    try:
        chat_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        chat_button.click()
        chat_clicked = True
        time.sleep(3)
        print(f"Clicked Chat button using: {xpath}")
        break
    except Exception as e:
        print(f"Chat button not found with xpath {xpath}: {e}")

if not chat_clicked:
    print("Could not find Chat button. It might be auto-opened. Continuing...")

# 9. Locate the message input field.
# Instagram often uses a contenteditable div for message input.
message_box = None
message_box_xpaths = [
    "//div[@contenteditable='true' and @role='textbox']",
    "//div[@contenteditable='true' and contains(@class, 'notranslate')]",
    "//textarea[contains(@placeholder, 'Message')]"
]
for xpath in message_box_xpaths:
    try:
        message_box = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        if message_box:
            print(f"Found message input using: {xpath}")
            break
    except Exception as e:
        print(f"Message box not found with xpath {xpath}: {e}")

if not message_box:
    print("Message input box not found! Exiting...")
    driver.quit()
    exit()

# 10. Send the message
try:
    message_box.send_keys(MESSAGE)
    message_box.send_keys(Keys.RETURN)
    print("✅ Message sent successfully!")
except Exception as e:
    print("Failed to send the message! Error:", e)

time.sleep(5)
driver.quit()
