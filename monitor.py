import steam
import datetime
from time import sleep

while True:
	price = steam.GetLowestPrice("Operation Broken Fang Case")
	print(datetime.datetime.now())
	print(f'The current Operation Broken Fang Case price is ${price}.')
	sleep(60 * 10)
