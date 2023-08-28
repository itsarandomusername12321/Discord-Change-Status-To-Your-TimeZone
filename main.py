import sys, os, time, requests
import datetime

# CONFIG HERE
TICKET = input("Your token here : ") # your token here
time_son = input("your timezone (example like GMT+7 then 7; or GMT-7 then -7) : ") # just number of your time zone
Discord_status = input("Discord status you want to set to (dnd,idle,online) : ") # Change circle status | dnd, idle, online
# MAIN CODE
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Discord:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization":TICKET,
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
    real_time = time_0 + datetime.timedelta(hours=time_son)
    time12 = real_time.strftime("%I:%M %p")
    print(real_time)
    message = time12
    status_code = discord.ChangeStatus(status, message)
    if status_code == 200:
        print("|———————————————————————————————————|")
        print("  Changed your status! ")
        print(f"  Status: {message}")
        print("   Made by Dummy!!")
        print("|———————————————————————————————————|")
    elif status_code == 429:
        print("____________________________________|")
        print("    uh oh you got ratelimited")
        print("  so you gonna wait in 5 to 6 hours i guess")
        wait(120)
        os.execv(sys.executable, ['python'] + sys.argv)
        
    else:
        print("um another error code, you better go check your discord")
        wait(400)
        os.execv(sys.executable, ['python'] + sys.argv)

def Main():
    discord = Discord(TICKET)
    while True:
        a = datetime.datetime.now()
        check_second = a.second
        while check_second != 0:
            time_check_before_run = datetime.datetime.now()
            check_second = time_check_before_run.second
            time.sleep(0.1)
        cls()
        Run(discord, Discord_status) 
if __name__ == "__main__":
    Main()
