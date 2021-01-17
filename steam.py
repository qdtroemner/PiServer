import requests
import re

BASE_URL = 'https://steamcommunity.com/market/'

def GetLowestPrice(item_hash, app_id=730):
	if not item_hash:
		return
	
	url = f'{BASE_URL}priceoverview'
	params = {
		'appid': app_id,
		'market_hash_name': item_hash
	}
	formatted_price = requests.get(url, params=params).json()["lowest_price"]
	str_price = re.compile(r'\d+(?:\.\d+)?').findall(formatted_price)[0]
	return float(str_price)
