

#importing the paramiko
import paramiko

#creating an object called ssh
ssh = paramiko.SSHClient()

#print(ssh)
#connecting to a cisco device
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.122.3',port=22,username='R1',password='cisco')
stdin,stdout,stderr = ssh.exec_command('show ip interface brief')
output=stdout.readlines()
print('\n'.join(output))
