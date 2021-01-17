import telegram
import os

uptime = os.popen('uptime').readline()
telegram.SendMessage("Still running PiServer.")
telegram.SendMessage(uptime)
