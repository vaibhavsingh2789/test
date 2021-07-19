#! /usr/bin/python3

import connection
import yaml_parser
import module_utils
import parser
import argparse
import sys

def parseargs():
     argparser = argparse.ArgumentParser(description='Install or remove a deb package')
     argparser.add_argument('--play', required=True, help='Specify the path of yaml play file')
     argparser.add_argument('--inventory', required=True, help='specify the path of yaml inventory file')
     argparser.add_argument('--config', help='specify the path of yaml config file', default='/opt/kaka/config.yml')
     return argparser.parse_args()


def main():
    args = parseargs()
    play_file = args.play
    inventory_file = args.inventory
    config_file = args.config
    
    # Load the yaml files 
    play_dict = yaml_parser.read_yaml(play_file)
    inventory_dict = yaml_parser.read_yaml(inventory_file)
    config_dict = yaml_parser.read_yaml(config_file)
    play_tasks = play_dict['tasks']
    module_path = config_dict['module_path']

    # Find and connect to the hosts to run the play on
    run_on_host_group = play_dict['hosts']
    hosts = inventory_dict.get(run_on_host_group)
    if not hosts:
        print('No hosts found')
        sys.exit(1)
    host_cons = connection.get_connection_list(hosts)
    print('Connected to the hosts {host_list}'.format(host_list=list(hosts.keys())))

    # Run the play on hosts
    for con in host_cons:
        for task in play_tasks:
            print('Running: {task}'.format(task=task['name']))
            module = list(task.keys())[1]
            status = module_utils.call_module(module, con, task[module], module_path)
            if status:
                print('Success')
            else:
                print('Failed')


if __name__ == '__main__':
    main()
