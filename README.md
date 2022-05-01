# Kafka/Python test inside Vagrant box


### Prerequisites for Vagrant/Libvirt
1. ```vagrant plugin install vagrant-libvirt```
2. ```vagrant plugin install vagrant-mutate```
3. ```vagrant plugin install vagrant-rsync-back```


### Spin up environment
```
vagrant up
vagrant rsync-auto

vagrant ssh
cd /vagrant_data
pip3 install -r requirements.txt

vagrant rsync-back
```

### Run tests
1. ```python3 consumer.py```
2. ```python3 producer.py```

### Example docs
* https://github.com/staeff/kafka-python-example
* https://www.tutorialsbuddy.com/kafka-python-producer-example
