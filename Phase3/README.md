### **1. Analyze Original SSH Vulnerability**  

![](./7.png)

**Commands Executed**:  
```bash
systemctl status ssh             # Verify SSH is running  
ssh -V                           # Check vulnerable version  
sudo cat /etc/ssh/sshd_config    # Review weak settings
```


### **2. Implement SSH Hardening**

Changes Made:

Port	22 to 2222 : Avoid automated scans
PermitRootLogin	yes	to no : Disable root access
PasswordAuthentication	yes	to no :Force key-based auth
MaxAuthTries:	(unset)	3	Limit brute-force attempts
AllowUsers:	(unset)	msfadmin	Restrict valid users
