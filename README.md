# SLEN Utils
A bundle of utilities to manage SLEN resources.


## System Requirements
#### Ubuntu/Debain
    $ sudo apt-get update

    $ sudo apt-get install -y python-dev python-setuptools python-pip git gcc

#### CentOS/RHEL/Fedora
    $ sudo yum update

    $ sudo yum install -y python-devel python-setuptools git gcc

    $ sudo easy_install pip

## Installation
    $ sudo pip install slen-utils --no-binary slen-utils


## Configuration
    $ sudo slen-config


## Usage
#### Sync Identity on Server
    $ sudo slen-cli --resource identity --action sync --params '{"stack_id":231,"identity_id":1892}'

#### Delete Identity
    $ sudo slen-cli --resource identity --action delete --params '{"stack_id":231,"identity_id":1892}'
  

## Support
> SLEN DevOps <devops@sloopengine.io>