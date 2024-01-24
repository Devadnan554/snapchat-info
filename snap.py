import requests
from bs4 import BeautifulSoup
import json
import sys , os 
import argparse
from colorama import Fore, Back, Style
linux = 'clear'
windows = 'cls'
os.system([linux, windows][os.name == 'nt'])
def parse_args():
    parser = argparse.ArgumentParser(description="Snapchat tool")
    parser.add_argument("-u", help="username", required=True, nargs=1)
    return parser.parse_args()
class SnapInfo:
    def __init__(self):
        self.session = requests.Session()
    def get_info():
        args = parse_args()
        user = args.u
        os.system([linux, windows][os.name == 'nt'])
        print(Fore.BLUE+Style.DIM+ '''
 _______                         ______         __                               
|       \                       /      \       |  \                              
| $$$$$$$\  ______   __     __ |  $$$$$$\  ____| $$ _______    ______   _______  
| $$  | $$ /      \ |  \   /  \| $$__| $$ /      $$|       \  |      \ |       \ 
| $$  | $$|  $$$$$$\ \$$\ /  $$| $$    $$|  $$$$$$$| $$$$$$$\  \$$$$$$\| $$$$$$$
| $$  | $$| $$    $$  \$$\  $$ | $$$$$$$$| $$  | $$| $$  | $$ /      $$| $$  | $$
| $$__/ $$| $$$$$$$$   \$$ $$  | $$  | $$| $$__| $$| $$  | $$|  $$$$$$$| $$  | $$
| $$    $$ \$$     \    \$$$   | $$  | $$ \$$    $$| $$  | $$ \$$    $$| $$  | $$
 \$$$$$$$   \$$$$$$$     \$     \$$   \$$  \$$$$$$$ \$$   \$$  \$$$$$$$ \$$   \$$
                                                                                 

        ''')
        print ('''
'''+Fore.BLUE+Style.DIM+'''[ + ]'''+Fore.WHITE+''' SnapChat : Devadnan'''+Fore.BLUE+'''  [ + ]'''+Fore.WHITE+''' Insta : Dev.adnan  '''+Fore.BLUE+'''[ + ]'''+Fore.WHITE+''' Tiktok : aama5544 '''+Style.RESET_ALL)
        url = f'https://www.snapchat.com/add/{user[0]}'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            script_tag = soup.find('script', {'type': 'application/json'})
            if script_tag:
                data = json.loads(script_tag.string)
                username = data.get('props', {}).get('pageProps', {}).get('userProfile', {}).get('userInfo', {}).get('username')
                display_name = data.get('props', {}).get('pageProps', {}).get('userProfile', {}).get('userInfo', {}).get('displayName')
                bitmoji_url = data.get('props', {}).get('pageProps', {}).get('userProfile', {}).get('userInfo', {}).get('bitmoji3d', {}).get('avatarImage', {}).get('url')
                snapcode = data.get('props', {}).get('pageProps', {}).get('userProfile', {}).get('userInfo', {}).get('snapcodeImageUrl', {})
                info_dict = {
                    'username': username,
                    'display_name': display_name,
                    'bitmoji_url': bitmoji_url,
                    'qr' : snapcode
                } 
                return info_dict
            else:
                raise ValueError('No JSON data found.')
        else:
            if (response.status_code == 404):
                print("User Not Found !!")        
    user = get_info()
    if (user != None):
        print("\n")
        print(Fore.BLUE+"Username : "+Fore.WHITE+user["username"]+"\n"+Fore.BLUE+"Display Name : "+Fore.WHITE+user["display_name"]+"\n"+Fore.BLUE+"Qr : "+Fore.WHITE+user["qr"])
