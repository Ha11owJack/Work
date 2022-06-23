#!/bin/bash
cd
echo "Введите название файла: "
#read FILE
#read Path
read Name

if [[ ! -d "/etc/apache2" ]]; then
	echo "Скачиваю пакет Apache"
	sudo apt install apache2
else
    echo "Пакет Apache Установелен"
fi
#if [[ ! -d "srv/$Name/file" ]]; then
#	echo "Создаем папку репозитория"
#	sudo mkdir -p /srv/$Name/file
#else
#    echo "Папка уже существует"
#fi

#sudo chmod -R 755 /var/www/$Name
#sudo sed -i "s/# AstraMode on/AstraMode off/g" /etc/apache2/apache2.conf
#sudo sed -i '$Name' /etc/apache2/sites-enabled/000-default.conf
sudo sed -i '2i<Directory /var/www/WORD_TO_REPLACE> \n\tOptions Indexes MultiViews FollowSymLinks \n\tAllowOverride None \n\tOrder Deny,Allow \n\tRequire all granted \n</Directory>' /etc/apache2/sites-enabled/000-default.conf
sudo sed -i 's/WORD_TO_REPLACE/($Name;n_)/g' /etc/apache2/sites-enabled/000-default.conf
sudo sed -i 's|DocumentRoot /var/www/html|DocumentRoot /var/www/{$Name}|g' /etc/apache2/sites-enabled/000-default.conf
#echo "Перезагрузка сервера"
#sudo systemctl restart apache2
#echo "Сервер перезагрузился"
