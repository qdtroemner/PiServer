import requests

TOKEN = "1221070278:AAH6ObFCU0Tq0ebjfgzcdHcqEYES6yC6i1Y"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"
CHANNEL_ID = "1216993479"

def SendMessage(content, user=CHANNEL_ID):
	if not content:
		return;
	
	url = f"{BASE_URL}sendMessage"
	payload = {
		"chat_id": user,
		"text": content
	}
	requests.post(url, data=payload)
