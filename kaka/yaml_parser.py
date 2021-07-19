import yaml


def read_yaml(yaml_file):
    with open(yaml_file) as f:
        return yaml.load(f, Loader=yaml.FullLoader)

#
#def get_hosts(yaml_file, host_pattern):
#    return read_yaml(yaml_file)[host_pattern]
#
#def get_tasks_from_play(yaml_file):
#    return read_yaml(yaml_file)['tasks']
#
#def get_host_pattern_from_play():
