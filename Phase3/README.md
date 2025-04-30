### **1. Analyze Original SSH Vulnerability**  

![](./7.png)

**Commands Executed**:  
```bash
systemctl status ssh             # Verify SSH is running  
ssh -V                           # Check vulnerable version  
sudo cat /etc/ssh/sshd_config    # Review weak settings
```


### **2. Implement SSH Hardening**

![](./1.png)
![](./2.png)
![](./3.png)
![](./4.png)
![](./8.png)

Changes Made:

- Port	22 to 2222 : Avoid automated scans. 

- PermitRootLogin	yes	to no : Disable root access. 

- PasswordAuthentication	yes	to no :Force key-based auth. 

- MaxAuthTries:	(unset)	3	Limit brute-force attempts. 

- AllowUsers:	(unset)	msfadmin	Restrict valid users.

**Commands Executed**: 

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak  
sudo nano /etc/ssh/sshd_config  # Apply changes  
sudo service ssh restart
```
