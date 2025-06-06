# Telegram - Sort By Reactions

A simple script to sort exported Telegram chat messages by total number of reactions.

## ⚙️ Setup

Edit the following 3 variables in code.py:

    url = "https://t.me/ENTER_THE_GROUP_NAME_HERE/"
    folder_path = r"C:\Users\YOUR_USERNAME\Downloads\Telegram Desktop\ChatExport_2025-06-06 (1)"
    HowManyPrints = 20

## 📥 Instructions

1. **Find the Base URL**  
   In Telegram, right-click any message and choose “Copy Link”.  
   Use only the *base* part of that link.

   Example:  
   If the message link is:  
   https://t.me/YOUR_CHANNEL_OR_GROUP/10648  
   Then the base URL is:  
   https://t.me/YOUR_CHANNEL_OR_GROUP/

2. **Export the Chat**  
   Use Telegram’s built-in export feature and provide the exported folder path as shown above.

3. **Choose How Many Messages to Show**  
   Set HowManyPrints to control how many top-reacted messages will be printed.

## 🧾 Output Example

--- Top 1 ---
Telegram Link: https://t.me/YOUR_CHANNEL_OR_GROUP/6019  
Text: Is this an alien or an old photo of Joe Biden?  
🔥: 35  ❤: 7  🥰: 7  👍: 2  😍: 2  🤮: 1  Total Reactions: 54

--- Top 2 ---
Telegram Link: https://t.me/YOUR_CHANNEL_OR_GROUP/9535  
Text: BREAKING NEWS: Bibi is no longer a prime minister  
🔥: 26  ❤: 3  👍: 3  🥰: 2  👋: 2  👎: 1  Total Reactions: 37

--- Top 3 ---
Telegram Link: https://t.me/YOUR_CHANNEL_OR_GROUP/9055  
Text: watch this AMAZING video by Josef  
👍: 21  🤣: 13  ❤: 1  😁: 1  Total Reactions: 36
