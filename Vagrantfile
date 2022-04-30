# -*- mode: ruby -*-
# vi: set ft=ruby :

ENV['VAGRANT_DEFAULT_PROVIDER'] = 'libvirt'
Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu1804"
  config.vm.box_check_update = true
  config.vm.hostname = "kafka-dev"

  config.vm.network "forwarded_port", guest: 80, host: 7001, host_ip: "127.0.0.1"
  #config.vm.network :private_network, ip: "192.168.33.33"
  config.vm.synced_folder ".", "/vagrant_data"

  config.vm.provider :libvirt do |v|
   v.memory = "512"
   v.cpus = "1"
   v.default_prefix="kafka_dev_"
  end

  config.vm.provision "shell" do |s|
    s.path = "./vagrant-provision.sh"
  end
end
