import requests

target_url = input('[+] Enter Page URL: ')
file_name = input('[+] Enter Password File to Use: ')

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

file = open(file_name, 'r')
for line in file:
    directory = line.strip()
    full_url = target_url + '/' + directory
    response = request(full_url)
    if response is not None and response.status_code == 200:
        print('[*] Discovered directory at this path: ' + full_url)
