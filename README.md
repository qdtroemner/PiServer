# PiServer
This is my custom server for my Raspberry Pi.

### About
Currently, all it does is track Steam market prices for a specific item, and when the price gets low enough, it sends a message via Telegram.

### Usage
If you would like to use this code on your Raspberry Pi server (or any other computer), the only thing that must be added is a file named `secrets.py` in the `src/` folder. Once you have done this, include a variable named `TELEGRAM` which has a value of your bot's Telegram token.
