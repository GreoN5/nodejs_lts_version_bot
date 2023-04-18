import requests

from bs4 import BeautifulSoup
from helpers import *


url = 'https://nodejs.org//en'
content = requests.get(url).text

soup = BeautifulSoup(content, 'html.parser')
btn = soup.find('a', class_='home-downloadbutton')

btn_version = btn.get('data-version')
btn_download_href = btn.get('href')
current_version = get_current_node_version()

parsed_btn_version = node_version_parser(btn_version)
parsed_current_version = node_version_parser(current_version)

if parsed_btn_version > parsed_current_version:
    if (check_nvm_usage()):
        run_node_installer(btn_version, btn_download_href)
        print('Installing node.js lts version using node.js installer...')
    else:
        run_shell_output(['nvm', 'install', 'lts'])
        print('Installing node.js lts version using nvm...')

        # apply the lts version
        run_shell_output(['nvm', 'use', 'lts'])
        print('Node.js latest lts version is now used.')
else:
    print('No new lts version available.')
