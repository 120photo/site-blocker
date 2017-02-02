import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["nytimes.com", "latimes.com", "facebook.com", "www.facebook.com", "news.ycombinator.com", "reddit.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8, 30) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Working Time...')
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            # print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("{} {}\n".format(redirect, website))
    else:
        print("Off Hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(3)
