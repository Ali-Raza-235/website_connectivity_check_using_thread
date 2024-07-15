import requests
import asyncio

async def check_website_availability(url):
    try:
        response = await asyncio.to_thread(requests.get, url, timeout=5)
        if response.status_code == 200:
            print(f'{url} is available')
        else:
            print(f'{url} is not available')
    except requests.ConnectionError:
        print(f"Connection Error Occur in this url {url}")
    except requests.Timeout:
        print(f'Request Timeout For this url {url} Connectivity')

async def main(websites):
    tasks = [check_website_availability(url) for url in websites]
    await asyncio.gather(*tasks)

websites = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://www.youtube.com/",
    "https://www.worldbabanews.com/"
]


asyncio.run(main(websites))

print("Website Connectivity Finished...")
