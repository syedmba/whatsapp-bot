# WhatsApp Messaging Bot

### This bot is designed for you to be able to send your holiday well-wishes to all your friends and family without having to embarrassingly show that you used broadcast lists

#### The bot uses an exported contact list in csv format with contact names and numbers listed.

#### The bot supports uploading one image before all the messages or with the first message. The filepath is input by the user.


#### For simple messages, use the built-in input function.
#### For customized messages that mention your contacts by name, hardcode the message in bot.py as seen in the example:

```
for num, name in numbers_list:
    driver.get(f"https://web.whatsapp.com/send?phone={num}")
    sleep(7)

    messages = ["Good morning {name}!", "Wishing you and your family a very happy and enjoyable Eid!"]
```


 
