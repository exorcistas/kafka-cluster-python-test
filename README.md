# py-kafka-cluster-test

Kafka/Python test on Docker


### Prerequisites for Vagrant/Libvirt
1. ```vagrant plugin install vagrant-libvirt```
2. ```vagrant plugin install vagrant-mutate```


### Spin up environment
```
vagrant up
vagrant rsync-auto
vagrant rsync-back
vagrant ssh
cd /vagrant_data
```

### Example docs
* https://github.com/staeff/kafka-python-example