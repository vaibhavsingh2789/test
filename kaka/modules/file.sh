#! /bin/bash

function usage()
{
        echo "Copy the file to destination and set the perms"
        echo "Usage: $0 <src> <dest> <perms>"
	exit 1
}

if [ "$#" -ne 3 ]
then
  usage
fi

SRC=$1
DEST=$2
PERMS=$3

diff -s "$1" "$2" || cp "$1" "$2"
stat -c "%a" "$DEST" | grep "$PERMS" || chmod "$PERMS" "$DEST"

