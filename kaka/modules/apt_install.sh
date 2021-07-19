#! /bin/bash

function usage()
{
        echo "Intall remove deb packages using apt"
        echo "Usage: $0 <package_name> <action>"
	exit 1
}

if [ "$#" -ne 2 ]
then
  usage
fi

PACKAGE=$1
ACTION=$2

if [ "$ACTION" = "install" ]
then
  dpkg -s "$PACKAGE" || apt-get install "$PACKAGE" -y
fi 

if [ "$ACTION" = "remove" ]
then
  apt-get remove "$PACKAGE" --purge -y
fi 
