import pyautogui,time, random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Function to log in to Discord
def login_discord(email, password):
    driver.get("https://discord.com/login?redirect_to=%2Fchannels%2Fxxxxxxxxxxx%2Fxxxxxxxxxxx")  # Set the chat channel link
    time.sleep(2)

    email_field = driver.find_element("name", "email")
    email_field.send_keys(email)

    password_field = driver.find_element("name", "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    time.sleep(2)

# Function to send a message in a specific channel
def send_channel_message(messages):
    while True:
        i = random.randint(1, 7)
        time.sleep(XX)  # Set the Discord server cooldown

        pyautogui.keyDown('alt')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.keyUp('alt')
        
        message_field = driver.switch_to.active_element
        message_field.send_keys(messages[i])
        time.sleep(0.2)
        message_field.send_keys(Keys.RETURN)
        
        pyautogui.keyDown('alt')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.keyUp('alt')

# Settings
email = "xxxxxxxxxxx" # Set your Discord Email
password = "xxxxxxxxxxx" # Set your Discord Password

# Driver settings
driver = webdriver.Chrome()
driver.maximize_window()

# Login to Discord
login_discord(email, password)
time.sleep(2)

# Send message
messages = ["TEXT1", "TEXT2", "TEXT3", "TEXT4", "TEXT5", "TEXT6", "TEXT7"]
send_channel_message(messages)

# Close the browser
driver.quit()