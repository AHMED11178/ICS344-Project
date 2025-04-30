### **1. Analyze Original SSH Vulnerability**  
**Commands Executed**:  
```bash
systemctl status ssh          # Verify SSH is running  
ssh -V                       # Check vulnerable version  
sudo cat /etc/ssh/sshd_config # Review weak settings
![image](https://github.com/user-attachments/assets/151c61dc-2d62-442b-9b1f-88c5082e9f64)
