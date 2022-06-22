#!/bin/bash
cd
#echo "Введите путь до папок с файлами: "
#read FILE


if [[ ! -d "/etc/apache2" ]]; then
	echo "Скачиваю пакет Apache"
	sudo apt-get install apache2
#	git init
#	git add *
#	git commit -m "Бэш работает"
#	git remote add origin http://10.20.13.4:3000/Ha11owJack2.0/reposit.git
#	git push -u origin master
else
    echo "Пакет Apache Установелен"
fi


if [[ ! -d "srv/repo/file" ]]; then
	echo "Создаем папку репозитория"
	sudo mkdir -p /srv/repo/file
else
    echo "Папка уже существует"
fi

sudo ln -s /srv/repo /var/www/html/
sudo sed -i "s/#ApacheMod on/AstraMod off/g" /etc/apache2/apache2.conf
# echo "deb http://IP/repo name main contrib non-free" >> /etc/apt/sources.list

echo "Перезагрузка сервера"
sudo systemctl restart apache2
echo "Сервер перезагрузился"
sudo apt-get install
