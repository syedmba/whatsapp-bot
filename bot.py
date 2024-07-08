from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com/")

input("Enter anything after scanning the QR Code")

df = pd.read_csv("phonebook.csv")
phone_list = list(df["Phone"])

################## phone number technique ##################

all_numbers = []
for number in phone_list:
    # number = "852" + str(number)
    all_numbers.append(number)

numbers_list = ["85298392039", "85298685934", "85256244077"]

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


for num in numbers_list:
    driver.get(f"https://web.whatsapp.com/send?phone={num}")
    sleep(12)

    attachment_box = driver.find_element(By.XPATH, '//div[@title = "Attach"]')
    attachment_box.click()

    sleep(1)

    image_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span')
    image_box.click()
    sleep(10)
    image_box.send_keys(filepath)

    sleep(4)

    # find the message box
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')

    # send each message and ENTER
    for msg in messages:
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)

    sleep(12)


