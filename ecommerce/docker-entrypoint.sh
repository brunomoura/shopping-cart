#!/bin/bash
/usr/sbin/sshd -D &! 

rm /etc/localtime
ln -s /usr/share/zoneinfo/America/Recife /etc/localtime

cd /var/www/

pip3 install --upgrade pip
pip3 install --upgrade wheel
pip3 install -r requirements.txt
python3 manage.py migrate 
python3 manage.py runserver 0.0.0.0:$port