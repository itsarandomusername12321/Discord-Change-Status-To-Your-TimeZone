import sys, os, time, requests, random
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import datetime

time_check_before_run = datetime.datetime.now()
check_second = time_check_before_run.second
    
while check_second != 0:
    time_check_before_run = datetime.datetime.now()
    check_second = time_check_before_run.second
    time.sleep(0.1)

class Discord:
    
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": "YOUR_TOKEN", # make sure to check under too
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "*/*"
        }

    def ChangeStatus(self, status, message):
        jsonData = {
            "status": status,
            "custom_status": {
                "text": message,
        }}
        r = requests.patch("https://discord.com/api/v8/users/@me/settings", headers=self.headers, json=jsonData)
        return r.status_code

def Run(discord, status,):
    discord = discord
    unix_time = int(time.time())
    time_0 = datetime.datetime.utcfromtimestamp(unix_time)
    real_time = time_0 + datetime.timedelta(hours=7) # Your Time Zone here
    hour = real_time.hour
    minute = real_time.minute
    second = real_time.second
    print(real_time)
    message = "{:02d}:{:02d} (24 hour)".format(hour,minute)
    status_code = discord.ChangeStatus(status, message)
    if status_code == 200:
        print("|———————————————————————————————————|")
        print("  Changed your status! ")
        print(f"  Status: {message}")
        print("|———————————————————————————————————|]")
    else:
        print("An error occured. Try again?")

def Main():
    TOKEN = os.environ.get("YOUR_TOKEN") # here!!
    discord = Discord(TOKEN)
    while True:
        time_check_before_run = datetime.datetime.now()
        check_second = time_check_before_run.second
        while check_second != 0:
            time_check_before_run = datetime.datetime.now()
            check_second = time_check_before_run.second
            time.sleep(0.1)
        os.system('cls')
        Run(discord, "idle") # Change circle status | dnd, idle, online


if __name__ == "__main__":
    Main()

