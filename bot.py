from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com/")

input("Enter anything after scanning the QR Code")

# df = pd.read_csv("phonebook.csv")
# phone_list = list(df["Phone"])

################## phone number technique ##################

all_numbers = []
# for number in phone_list:
#     all_numbers.append(number)

numbers_list = ["+923218401700", "+923032596033", "+923008383072"]

################## phone number technique ##################


messages = []
message = input("Enter all messages one by one, enter \"-1\" to delete previous message and \"0\" to terminate message input and finalize choices: ")
while message != "0":
    if message == "-1":
        try:
            messages = messages[:-1]
        except:
            print("message list is empty!")
    else:
        messages.append(message)
    message = input("Enter next message: ")
        
    
filepath = input("Enter full filepath: ")
# filepath = "/Users/syedmuhammadbinasif/Desktop/tree.png/"
# filepath = "/Users/syedmuhammadbinasif/Desktop/swaggy.jpg"


if filepath != "":
    first_msg_attached_flag = True
    first_msg_attached = input("Do you want the first message to be sent as the caption of the file? (Y/N): ")
    if first_msg_attached == "N":
        first_msg_attached_flag = False

for num in numbers_list:
    driver.get(f"https://web.whatsapp.com/send?phone={num}")
    sleep(7)

    if filepath != "":
        # attachment_box = driver.find_element(By.XPATH, '//div[@title = "Attach"]')
        # attachment_box.click()
        driver.find_element(By.CSS_SELECTOR, "span[data-icon='attach-menu-plus']").click()

        sleep(2)

        try:

            driver.find_element(By.CSS_SELECTOR, "input[accept='image/*']").send_keys(filepath)
            sleep(2)

            if first_msg_attached_flag:
                msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
                msg_box.send_keys(messages[0])
                msg_box.send_keys(Keys.ENTER)
            
            send_button = driver.find_element(By.CSS_SELECTOR, "span[data-icon='send']")
            send_button.click()

        except:
            print("filepath does not exist!")

        sleep(4)

    # find the message box
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')

    

    # send each message and ENTER
    if first_msg_attached_flag:
        try:
            messages = messages[1:]
        except:
            messages = []

    for msg in messages:
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)

    sleep(12)


