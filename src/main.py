import telegram
import steam

import requests
import datetime

target_price = 0.70
current_price = steam.GetLowestPrice("Operation Broken Fang Case")

if current_price <= target_price:
	telegram.SendMessage(f"Market price has dropped to {current_price}!")

#telegram.SendMessage(f"{datetime.datetime.now()}")
