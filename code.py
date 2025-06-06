import os
import urllib.parse
from bs4 import BeautifulSoup
from collections import defaultdict


"""
EDIT THESE THREE LINES BELOW.
INSTRUCTIONS:
1. in telegram, you can right-click a messsage to copy it's link - use the *base* url of that link (without "19472" for example)
2. export the chat to using the built in telegram export feature, and copy the folder path
3. decide how many 'top reacted' messages you want to print eventually.
"""

url = "https://t.me/ENTER_THE_GROUP_NAME_HERE/"
folder_path = r"C:\Users\YOUR_USERNAME\Downloads\Telegram Desktop\ChatExport_2025-06-06 (1)"
HowManyPrints = 20


def extract_messages_from_html(html_content, source_filename, full_path, telegram_base_url=None):
    soup = BeautifulSoup(html_content, 'html.parser')
    messages = soup.find_all("div", class_="message")
    extracted = []

    for message in messages:
        msg_id = message.get("id", "")
        if not msg_id.startswith("message"):
            continue
        msg_num = msg_id.replace("message", "")
        time_tag = message.find("div", class_="pull_right date details")
        text_tag = message.find("div", class_="text")
        reactions_div = message.find("span", class_="reactions")

        if not reactions_div:
            continue

        reactions = defaultdict(int)
        total_count = 0

        for reaction_span in reactions_div.find_all("span", class_="reaction"):
            emoji_span = reaction_span.find("span", class_="emoji")
            emoji = emoji_span.text.strip() if emoji_span else ''

            count_span = reaction_span.find("span", class_="count")
            if count_span:
                count = int(count_span.text.strip())
            else:
                userpics = reaction_span.find("span", class_="userpics")
                count = len(userpics.find_all("div", class_="userpic")) if userpics else 1

            reactions[emoji] += count
            total_count += count

        file_url = f"file:///{urllib.parse.quote(full_path.replace(os.sep, '/'))}#go_to_message{msg_num}"
        telegram_url = f"{telegram_base_url.rstrip('/')}/{msg_num}" if telegram_base_url else None

        extracted.append({
            'total_reactions': total_count,
            'time': time_tag['title'] if time_tag else 'N/A',
            'text': text_tag.get_text(strip=True) if text_tag else '',
            'reactions': dict(reactions),
            'filename': source_filename,
            'message_id': msg_id,
            'url': file_url,
            'telegram_url': telegram_url
        })

    return extracted


def get_top_reacted_messages_from_folder(folder_path, n=5, telegram_base_url=None):
    all_messages = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".html"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                html = f.read()
                all_messages.extend(
                    extract_messages_from_html(html, filename, file_path, telegram_base_url)
                )

    # Sort by total reaction count
    top_messages = sorted(all_messages, key=lambda x: x['total_reactions'], reverse=True)[:n]

    # Print the results
    for i, msg in enumerate(top_messages, 1):
        print(f"\n--- Top {i} ---")
        #print(f"File: {msg['filename']}")
        #print(f"Message ID: {msg['message_id']}")
        
        if msg['telegram_url']:
            print(f"Telegram Link: {msg['telegram_url']}")
        else:
            print(f"Local Link: {msg['url']}")
        #print(f"Time: {msg['time']}")
        print(f"Text: {msg['text']}")
        #print("Reactions Breakdown:")
        for emoji, count in msg['reactions'].items():
            print(f" {emoji}: {count} " , end='')
        print(f"Total Reactions: {msg['total_reactions']}")

    print()
    return top_messages

get_top_reacted_messages_from_folder(folder_path, n=HowManyPrints, telegram_base_url=url)
