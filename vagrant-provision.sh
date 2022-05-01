#!/bin/sh

# update and install base components
sudo apt update -y
sudo apt install -y software-properties-common
sudo apt-get install -y python3 python3-dev python3-pip python3-venv
python3 -m pip install --upgrade pip
python3 --version

# install and setup docker
sudo apt install docker docker-compose -y
sudo systemctl enable docker
sudo groupadd docker
sudo usermod -aG docker vagrant
sudo chown vagrant /var/run/docker.sock
sudo systemctl start docker
docker --version

# prepare environment
su vagrant
chown vagrant /vagrant_data
cd /vagrant_data
docker-compose up -d
rm -rf venv
#python3 -m venv venv
#source venv/bin/activate
#pip3 install -r requirements.txt