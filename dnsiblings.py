import requests

headers = {
  'accept': 'application/json',
  'Accept-Ianguage': 'en-US,en;q=0.9,es;q=0.8',
  'content-type': 'application/json',
  'Referer': 'https://www.virustotal.com/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36',
  'x-app-version': 'v1x64x0',
  'X-Tool': 'vt-ui-main',
  'X-VT-Anti-Abuse-Header': 'MTQxMDEzOTY0NDctWkc5dWRDQmlaU0JsZG1scy0xNjQzOTYzNDYzLjczNw=='
}
url = input("[i] Enter the URL:\n[>] ").replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
r = requests.get(f"https://www.virustotal.com/ui/domains/{url}/subdomains?relationships=resolutions", headers=headers)

try:
    for i in r.json()['data']:
        print(f"[+] {i['id']}\t")
        for j in i['relationships']['resolutions']['data']:
            print(f"\t[~] {j['id'].replace(i['id'], '')}")
except KeyError:
    print("[!] No subdomains found or invalid URL")
