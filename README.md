# Kafka/Python test on Docker inside Vagrant box


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

vagrant rsync-back
```

### Example docs
* https://github.com/staeff/kafka-python-example