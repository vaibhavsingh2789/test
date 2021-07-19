#! /usr/bin/python3

import connection
import os

def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Module {func.__name__} has failed with error {e}")
            return False
    return inner_function

def copy_file_to_remote(ssh_con, src, dest):
    sftp = connection.connect_sftp(ssh_con)
    connection.push_file(sftp, src, dest)
    success = connection.execute(ssh_con, 'chmod +x {script}'.format(script=dest))
    if not success:
       raise Exception('Failed to copy module file to remote server') 


def apt(ssh_con, module_conf, module_path):
    package_name = module_conf['name']
    action = module_conf['action']
    copy_file_to_remote(ssh_con, "{module_path}/apt_install.sh".format(module_path=module_path), '/tmp/apt.sh')
    return connection.execute(ssh_con, "/tmp/apt.sh {package} {action}".format(package=package_name, action=action))
 

def copy_file(ssh_con, module_conf, module_path):
    src = module_conf['src'] 
    remote_src = '/tmp/{filename}'.format(filename=os.path.basename(src))
    dest = module_conf['dest']
    mode = module_conf['mode']
    copy_file_to_remote(ssh_con, "{module_path}/file.sh".format(module_path=module_path), '/tmp/file.sh')
    copy_file_to_remote(ssh_con, src, remote_src) 
    return connection.execute(ssh_con, "/tmp/file.sh {remote_src} {dest} {mode}".format(remote_src=remote_src, dest=dest, mode=mode))


def systemd(ssh_con, module_conf, module_path):
    service = module_conf['service']
    action = module_conf['action']
    copy_file_to_remote(ssh_con, "{module_path}/systemd.sh".format(module_path=module_path), '/tmp/systemd.sh')
    return connection.execute(ssh_con, "/tmp/systemd.sh {service} {action}".format(service=service, action=action))

module_func = {
                'apt': apt,
                'file': copy_file,
                'systemd': systemd
              }

def call_module(module, con, module_conf, modules_path):
    return module_func[module](con, module_conf, modules_path)
