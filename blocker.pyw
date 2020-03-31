import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list = ["www.theuselessweb.com", "theuselessweb.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(hosts_temp, 'r+') as file:
            #this way variable content is a list of strings from each line of hosts file
            content = file.readlines()
            #stavi na početak
            file.seek(0)
            for line in content:
                #provjerava je li ono što je u website_list slučaju u contentu koji je kopija filea
                #ako nije, onda upisuje u file jer je ideja obrisati blokirane stranice
                #kada su fun hoursi
                if not any(website in line for website in website_list):
                    file.write(line)
                #briše sve iza točke cursora
                file.truncate()

        print("Fun hours...")
    time.sleep(5)