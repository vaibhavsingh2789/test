import sys
import pxssh
import getpass
import thread

ServerDic={}

def Connect(hostname):
  '''ASk's credentials for each server and returns pxssh object on successful connection.'''
  try:
    print "enter cridentials for server:"+hostname
    username = raw_input('username: ')
    password = getpass.getpass('password: ')
    s = pxssh.pxssh()
    s.login (hostname, username, password)
    return s
  except:
    print ("error while connecting to server:"+hostname)

def SendCommand(con,ServerName,cmd):
    '''Send command to sever. '''
    if con != None:
       con.sendline (cmd)
       con.prompt()
       print ServerName+"$"+con.before

if len(sys.argv)==1:
     print("usage:\n multissh server1 server2 .... servern")
if len(sys.argv)>1:
     for l in range(1,len(sys.argv)):
         ServerDic[sys.argv[l]]=Connect(sys.argv[l])
     print(ServerDic.keys())
     print("Type 'exit' to close program or type command you want to execute on servers")
     while (1):
       command = raw_input("$")
       if command == 'exit':
          for l in range(1,len(sys.argv)):
            ServerDic[sys.argv[l]].logout()
          break
       else:
          for l in range(1,len(sys.argv)):
            thread.start_new_thread( SendCommand,(ServerDic[sys.argv[l]],sys.argv[l],command))
