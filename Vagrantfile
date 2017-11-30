# Defines our Vagrant environment
#
# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$setupScript = <<SCRIPT
echo provisioning ansible and docker...

apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
apt-get -y -o Dpkg::Options::="--force-confold" install ansible
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common bash-completion

sudo mkdir -p /tmp/tests-workspace
sudo cp -R /vagrant/* /tmp/tests-workspace/
sudo mkdir -p /tmp/tests-workspace/tests/roles
sudo ln -sf /tmp/tests-workspace/ /tmp/tests-workspace/tests/roles/role_under_test
if [ -f "/tmp/tests-workspace/tests/requirements.yml" ]; then 
  sudo ansible-galaxy install --roles-path "/tmp/tests-workspace/tests/roles/" -r "/tmp/tests-workspace/tests/requirements.yml"
fi
sudo env ANSIBLE_FORCE_COLOR=1 ansible-playbook -i "/tmp/tests-workspace/tests/inventory" -c local -v "/tmp/tests-workspace/tests/tests.yml"

sudo usermod -a -G docker vagrant

docker version

docker-compose version
echo "###########################################"
echo "#                IP ADDRESS               #"
echo "#                                         #"
ip a | grep brd | egrep "[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\/[[:digit:]]{1,2}" | awk '{print "               ",$2}'
echo "###########################################"
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.synced_folder ".", "/vagrant",
    owner: "vagrant", group: "vagrant",
    mount_options: ["dmode=777,fmode=777"]
  config.vm.define "server" do |host|
    host.vm.hostname = "server"
    config.vm.network "private_network", type: "dhcp"
    host.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = "1"
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
      vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
    end
    host.vm.provision :shell, :inline => $setupScript
  end
end
