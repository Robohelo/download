# PEC-Downloads
Download reposotory for PEC.

##Install instruction
First download
```bash
# Download repositories into home
$ cd ~
$ wget https://github.com/Robohelo/PEC-Downloads.git
$ unzip 
$ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

$ sudo apt-get update && sudo apt-get install -y nvidia-docker2
$ sudo systemctl restart docker
```
