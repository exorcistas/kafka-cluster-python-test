#!/bin/sh

# update and install main components
sudo apt update -y
sudo apt install -y software-properties-common
sudo apt upgrade -y
sudo apt-get install -y python3 python3-dev python3-pip python3-venv docker docker-compose
python3 -m pip install --upgrade pip
python3 --version

# prepare docker environment
sudo systemctl enable docker
sudo groupadd docker
sudo usermod -aG docker vagrant
sudo chown vagrant /var/run/docker.sock
sudo systemctl start docker
docker --version

# start docker app stack environment
sudo chown vagrant /vagrant_data
su vagrant
cd /vagrant_data
pip3 install -r requirements.txt
docker-compose up -d