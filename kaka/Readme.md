# Kakaw
Kaka is a config management tool for managing the server configs

## Architecture
Kaka is a push based config management tool. It connects to the servers using ssh connection
and no agent needs to be installed on the servers being managed. It copies the module script/program to the servers
and run them to perform the actions defined in config. Components of the kaka are discussed in detail as follows.

### Inventory
Inventory is a yaml file which contains the servers ip/dns and credentials. Inventory has a concept of host
group which is used to club the set of server in same group based on similar characterstics.
Lets say for example all the backend servers go into the group called backend_servers.

Sample inventory file

inventory.yml
```
nginx_servers:
  nginx01.foo.com:
    username: root
    password: xyzpass
  nginx02.foo.com:
    username: root
    password: somepass
  192.168.0.33:
    username: root
    password: foopass

java_apps:
  b1.foo.com:
    username: root
    password: xyzpass
 
```

In above snippet `nginx_servers` and `java_apps` is host group. Using the host groups deployment can be targeted on the perticular group of servers.

### Play  
Play is a yaml file which consist of tasks and host groups to run those tasks on. This file simply defines
where to run what. Play file contains list of tasks and each task uses a module to define the action of task.

Sample play for installing `apache2` on `lamp` host group

sample_play.yml
```
hosts: lamp
tasks:
  - name: Install the apache2 package
    apt:
      name: apache2
      action: install
```

### Module
Module are standalone scripts/programs which runs on the server to perform the desired actions defined in play.
In above sample play we have used a moudule called `apt` which takes the arguments `name` and `action`.
Behind the scene the apt module scripts gets copied to the server over ssftp and then we pass the given arguments to the script to perform the action.

## Installing and using
Kaka can be install by running `./install.sh` script present in the root of the project.

Once installed you can run the sample plays given as the example in this documents as follows
`play.py --play slacktest.yml --inventory ../kaka/inventory.yml`
