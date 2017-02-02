import time
from datetime import datetime as dt

hosts_dev = "hosts"
hosts_live = "/etc/hosts" #path for macOS and linux, change for windows.
mode = "dev" # change to read "live" when you want to go live.
if mode == "live":
    host = hosts_live
else:
    host = hosts_dev

redirect = "127.0.0.1"

website_list = []
with open("block.txt", "r") as file:
    for site in file:
        website_list.append(site.strip("\n"))

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 13, 30) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Working Time...')
        with open(host, 'r+') as file:
            content = file.read()
            # print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("{} {}\n".format(redirect, website))
    else:
        print("Off Hours...")
        with open(host, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(3)
