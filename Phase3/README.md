### **1. Analyze Original SSH Vulnerability**  

![](./7.png)

**Commands Executed**:  
```bash
systemctl status ssh             # Verify SSH is running  
ssh -V                           # Check vulnerable version  
sudo cat /etc/ssh/sshd_config    # Review weak settings


