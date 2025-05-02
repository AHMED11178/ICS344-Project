# Splunk Setup Summary: Kali Linux + Metasploitable3 Attack Lab (Windows Host)

This document summarizes the completed setup of Splunk for capturing and analyzing attack logs between:
- **Kali Linux (Attacker VM)**
- **Metasploitable3 (Victim VM)**

Splunk is installed and running on the **Windows host machine**.

---

## ✅ Setup Overview

- **Host OS**: Windows 10
- **Virtualization**: VirtualBox
- **Virtual Machines**:
  - Kali Linux (attacker)
  - Metasploitable3 (victim)
- **Splunk**: Installed on Windows host, accessed via `http://localhost:8000`

---

## 🔧 Configuration Details

### 1️⃣ Splunk Installation (Completed)

- Downloaded Splunk Enterprise Free from:  
  https://www.splunk.com/en_us/download.html

- Installed on Windows host.

- Started Splunk service and accessed the web interface at:  
  `http://localhost:8000`

- Created admin account and set up initial configurations.

---

### 2️⃣ Networking Configuration

- Configured **Host-Only Adapter** (or Bridged Network) for both Kali and Metasploitable3.

- Verified network connectivity:
  - Kali can ping host (`ping <host_ip>`)
  - Metasploitable3 can ping host

---

# Splunk Universal Forwarder Setup (Completed)

This document summarizes the steps I completed to install and configure the Splunk Universal Forwarder on both the Kali Linux and **Metasploitable3** virtual machines, connecting them successfully to my Splunk Enterprise instance running on the host machine.

---

## What Was Done

### ✅ Environment Preparation

* Splunk Enterprise was already installed and running on the host machine, listening on port **9997**.
* Both the Kali Linux and Metasploitable3 VMs were set up in VirtualBox and configured to be on the same Host-Only or Bridged network to ensure they could communicate with the host.

### ✅ Downloaded and Installed Splunk Universal Forwarder

* Downloaded the appropriate Splunk Universal Forwarder Debian package (`.deb`) for both VMs.
* Installed on **both Kali and Metasploitable3** using:

  ```bash
  sudo dpkg -i splunkforwarder-<version>-linux-2.6-amd64.deb
  ```

### ✅ Accepted License and Enabled Boot Start

On both VMs, ran:

```bash
sudo /opt/splunkforwarder/bin/splunk start --accept-license
sudo /opt/splunkforwarder/bin/splunk enable boot-start
```

### ✅ Configured Forwarder Connections

On both Kali and Metasploitable3, pointed the forwarder to the Splunk Enterprise host:

```bash
sudo /opt/splunkforwarder/bin/splunk add forward-server <splunk-host-ip>:9997
```

Verified the connection:

```bash
sudo /opt/splunkforwarder/bin/splunk list forward-server
```

### ✅ Defined Data Inputs

Set up monitoring for key log files on both VMs:

```bash
sudo /opt/splunkforwarder/bin/splunk add monitor /var/log
```

Or more specifically:

```bash
sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/syslog
sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/auth.log
```

### ✅ Restarted Forwarder Services

Restarted the Splunk Universal Forwarder on both VMs to apply changes:

```bash
sudo /opt/splunkforwarder/bin/splunk restart
```

### ✅ Verified Data in Splunk Enterprise

* Checked in Splunk Enterprise under **Settings > Forwarding and Receiving > Configure Receiving** to ensure port **9997** was open.
* Used **Search & Reporting** in Splunk to confirm logs were arriving:

  ```spl
  index=* host=<kali-ip>
  index=* host=<metasploitable3-ip>
  ```
* Confirmed that logs from both VMs were visible and searchable.

### ✅ Addressed Issues

* Resolved network adapter and VirtualBox network configuration issues.
* Ensured no firewall or port-blocking issues between the VMs and the host.
* Focused only on the Splunk Universal Forwarder (avoiding `rsyslog`) to prevent binary data issues.

---

## Summary

I have successfully:

* Installed the Splunk Universal Forwarder using `dpkg` on both Kali and Metasploitable3
* Configured them to forward log data to Splunk Enterprise on the host
* Verified that incoming log data appears correctly in the Splunk web interface

If needed, I can also document the troubleshooting steps or provide a network diagram of the setup.
