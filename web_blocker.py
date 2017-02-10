import time
from datetime import datetime as dt
from settings import *


if mode == "live":
    host = hosts_live
    interval = 60  # pause while loop 60 seconds when live
else:
    host = hosts_dev
    interval = 3  # pause while loop 3 seconds when in dev

redirect = "127.0.0.1"

website_list = []
with open("block.txt", "r") as file:
    for site in file:
        website_list.append(site.strip("\n"))


while True:
    if start_hours < dt.now() < end_hours:
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
    time.sleep(interval)
