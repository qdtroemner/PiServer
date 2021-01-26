# PiServer
This is my custom server for my Raspberry Pi.

## About
Currently, it tracks the Steam market price for a specific item, and when the price gets low enough, it sends a message via Telegram.

## Usage
If you would like to use this code on your computer, the only thing that must be added is a file named `secrets.py` in the `src/` folder. Once you have done this, include a variable named `TELEGRAM` which holds your bot's Telegram token.
#### Configuring a cron-job
In order to run the script(s) in a time-based manner, you can implement a cron job. In order to do this on a Raspberry Pi, you run the command `crontab -e` in the terminal. The file has instructions on how to create cron-job entries. For help with configuring a specific schedule, you can use [Crontab Guru](https://crontab.guru/).
