#! /bin/bash

function usage()
{
        echo "Start, Stop, Restart or reload a systemd service"
        echo "Usage: $0 <service> <action>"
	exit 1
}

if [ "$#" -ne 2 ]
then
  usage
fi

SERVICE="$1"
ACTION="$2"

if [ "$ACTION" = "reload" ]
then
  systemctl reload "$SERVICE"
  echo "reloaded the $SERVICE service"
fi 

if [ "$ACTION" = "restart" ]
then
  systemctl restart "$SERVICE"
  echo "restarted the $SERVICE service"
fi 

if [ "$ACTION" = "start" ]
then
  systemctl is-active "$SERVICE" || systemctl start "$SERVICE"
  echo "started the $SERVICE service"
fi 

if [ "$ACTION" = "stop" ]
then
  systemctl is-active "$SERVICE" && systemctl stop "$SERVICE"
  echo "stopped the $SERVICE service"
fi 
