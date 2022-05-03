# Kafka/Python test inside Vagrant box


### Prerequisites for Vagrant/Libvirt
1. ```vagrant plugin install vagrant-libvirt```
2. ```vagrant plugin install vagrant-mutate```
3. ```vagrant plugin install vagrant-rsync-back```


### Spin up environment
1. Start up Vagrant box:
    ```
    vagrant up
    vagrant ssh
    ```
2. Install python requirements:
    ```
    cd /vagrant_data
    pip3 install -r requirements.txt
    ```
3. In separate terminal start auto-sync: ```vagrant rsync-auto```
* Use ```vagrant rsync-back``` if changes should be synced from Vagrant box back to host

### Run test
1. Run consumer on terminal 1: ```python3 consumer.py```
2. Run producer on terminal 2: ```python3 producer.py```

### TBD
* Dockerize ```producer.py```
* Update Vagrant box to cd into working dir on ssh

### Example docs
* https://github.com/staeff/kafka-python-example
* https://www.tutorialsbuddy.com/kafka-python-producer-example
* https://www.youtube.com/watch?v=LHNtL4zDBuk