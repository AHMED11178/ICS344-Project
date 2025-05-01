# Splunk Setup for Kali + Metasploitable3 Attack Lab

This guide explains how we sat up Splunk on our **host machine** to collect and analyze logs from:
- **Kali Linux (Attacker)**
- **Metasploitable3 (Victim)**

## 🛠 Requirements
- Host machine with Windows/macOS/Linux (8GB+ RAM recommended)
- VirtualBox or VMware with:
  - Kali Linux VM
  - Metasploitable3 VM

## ⚙️ Steps

---

### 1️⃣ Install Splunk on Host

1. Download Splunk Enterprise Free:  
   https://www.splunk.com/en_us/download.html

2. Choose the version for your host OS (Windows/macOS/Linux).

3. Install Splunk following the installer instructions.

4. Start Splunk and access it in your browser:  
   `http://localhost:8000`

5. Create an admin username and password when prompted.

---

### 2️⃣ Set Up Networking Between Host + VMs

- In VirtualBox/VMware, configure **Host-Only Adapter** or **Bridged Network** for both Kali and Metasploitable3.
- From Kali, verify connection to host:
  ```bash
  ping <host_machine_ip>
