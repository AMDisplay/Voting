# Voting

## Install local project

### Download repositories

git clone git@github.com:AMDisplay/Voting.git

### Create virtual env

python -m vev venv

### Run virtual env

source venv/Scripts/activate

### install reuirements

pip install -r requirements.txt

### run project

python manage.py runserver

## instal on servece

### upgrade system

sudo apt update -y

### install gunicorn

pip install gunicorn

sudo systemctl enable gunicorn

### install docker compose

curl -SL https://github.com/docker/compose/releases/download/v2.14.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose

### install docker

sudo apt install docker.io

### install NGINX

sudo apt install nginx -y

### allowed HTTP, HTTPS and SSH

sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH

### run firewall

sudo ufw enable

### run NGINX

sudo systemctl start nginx

### reload all system

sudo systemctl daemon-reload

## Settings in NGINX

### Create dir NGINX and create in create default.conf

mkdir nginx

cd nginx

touch default.conf

### Open default.conf and add your ip adress

nano default.conf

Take settings in repositories and changes ip adress

### Create docker-compose file in home/<user> dir

### Take settings in repositories

### Run docker-compose

sudo docker compose run