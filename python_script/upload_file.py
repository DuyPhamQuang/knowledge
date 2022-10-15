
import os
import paramiko

def get_connect(server, username, password):
    ssh = paramiko.SSHClient() 
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(server, username=username, password=password)
    return ssh
def put_file(ssh, localpath, remotepath):
    sftp = ssh.open_sftp()
    sftp.put(localpath, remotepath)
    sftp.close()
def exec_command(ssh, command):
    stdout = ssh.exec_command(command)[1]
    for line in stdout:
        print(line)
def extract_war_file(warpath):
    if not os.path.exists("tmp/"):
        print("Tao thu muc tmp")
        os.makedirs("tmp")
    
    os.system('cp "'+warpath+'" tmp/')
    os.system('jar -xvf "' + warpath + '"')
    
    # os.system('rm -rf tmp/')
    return 1

server="192.168.56.3"
username="root"
password="123"
localpath="test2.txt"
remotepath="/tmp/test2.txt"
command="ls -lh"

ssh = get_connect(server=server, username=username, password=password)
put_file(ssh=ssh, localpath=localpath, remotepath=remotepath)
exec_command(ssh, command=command)
extract_war_file('mysql-connector-java-8.0.28.jar')

ssh.close()
