# Website Connectivity Checker Using Threads

import requests
import threading

def check_website_availability(url, websites):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f'{url} is available')
        else:
            print(f'{url} is not available')

    except requests.ConnectionError:
        print(f"Connection Error Occur in this url {url}")

    except requests.Timeout:
        print(f'Request Timeout For this url {url} Connectivity')


websites = ["https://www.google.com/", "https://www.facebook.com/", "https://www.instagram.com/", "https://www.youtube.com/", "https://www.worldbabanews.com/"]



for i in range(len(websites)):
    thread = threading.Thread(target=check_website_availability, args=(websites[i], websites))
    thread.start()
    thread.join()


print("Website Connectivity Finished...")
