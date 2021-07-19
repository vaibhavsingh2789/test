import paramiko


def connect(host, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    return ssh


def connect_sftp(ssh_con):
    return ssh_con.open_sftp()


def push_file(sftp_con, src, dest):
    return sftp_con.put(src, dest)
    

def execute(ssh_con, command):
    chan = ssh_con.get_transport().open_session()
    chan.exec_command(command)
    exit = chan.recv_exit_status()
    if exit != 0:
        print(chan.recv_stderr(1024))
        return False
    return True


def get_connection_list(host_dict):
    host_cons = []
    for host in host_dict:
        host_cons.append(connect(host, 22, host_dict[host]['username'], host_dict[host]['password']))
    return host_cons
