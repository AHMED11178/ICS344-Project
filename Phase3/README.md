### **1. Analyze Original SSH Vulnerability**  
**Commands Executed**:  
```bash
systemctl status ssh          # Verify SSH is running  
ssh -V                       # Check vulnerable version  
sudo cat /etc/ssh/sshd_config # Review weak settings
![7](https://github.com/user-attachments/assets/b0dd1779-7437-4409-bf1c-f745ddb12ac8)
