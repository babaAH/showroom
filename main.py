import datetime
import time

import requests
from datetime import date, time


"""
отправляем GET запрос на страницу шоурума
если в ответе не содержится строка о том, что все авто распроданы
то надо будет создавать новых файл с содержимым ответа от сервера
"""
def main():
    while True:
        time.sleep(2)
        r = requests.get("https://showroom.hyundai.ru/")
        if "На данный момент все автомобили распроданы. Ожидайте поступления новых автомобилей в ближайшее время." \
                not in r.text:
            file_name = datetime.datetime.now()
            with open("responses/" + file_name, "w") as f:
                    f.write(r.text)

if __name__ == '__main__':
    print(datetime.datetime.now())
    # main()