#!/bin/sh

# update and install base components
sudo apt update -y
sudo apt install -y software-properties-common
sudo apt-get install -y python3 python3-dev python3-pip python3-venv libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
python3 -m pip install --upgrade pip

# install and setup docker
sudo apt install docker docker-compose -y
sudo systemctl enable docker
sudo groupadd docker
sudo usermod -aG docker $USER
sudo chown $USER /var/run/docker.sock
sudo systemctl start docker
docker --version
docker-compose up -d

# prepare python environment
cd /vagrant_data
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install --upgrade pip
#sudo pip install -r requirements.txt
