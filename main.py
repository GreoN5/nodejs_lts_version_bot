import os
import requests
import urllib.request

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
    current_path = get_current_path()
    file_extension = '.msi'
    file_appendix = 'node'
    file_windows_version = 'x64'

    filename = f'{file_appendix}-{btn_version}-{file_windows_version}{file_extension}'
    url = f'{btn_download_href}{filename}'

    urllib.request.urlretrieve(url, filename)
    node_exe_path = f'{current_path}\{filename}'

    # run the node installer
    os.system(node_exe_path)
