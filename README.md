# ICS344 Course Project

## 📌 Group Members
| Name            | ID        
|-----------------|-------
| AHMED RADWAN       | 202045860
| ABDULLA ALAHMDI    | 202157210
| HAIDAR ABUGURAIN   | 202064700

---

## 🎯 Project Overview
This project demonstrates the **attack and defense** of the **SMB service** on a Metasploitable3 VM.  
**Key phases:**  
1. **Phase 1:** Compromise SMB using Metasploit and a custom Python script.  
2. **Phase 2:** Analyze attacks using Splunk (SIEM).  
3. **Phase 3:** Implement defenses (patching, hardening) and validate effectiveness.  

---

## 📂 Repository Structure
- /Phase1 - Attack screenshots and scripts
- /Phase2 - Splunk dashboards
- /Phase3 - Defense steps and test results
  
---

## ⚙️ Setup Instructions
### Prerequisites
- **Victim Machine:** [Metasploitable3](https://github.com/rapid7/metasploitable3)
- **Attacker Machine:** Kali Linux (Metasploit, Python 3.10+)
- **SIEM:** Splunk Enterprise (Free license)
  
---

## 🚀 Key Results
- Successfully exploited SMB using EternalBlue  
- Created attack visualizations in Splunk  
- Fixed vulnerabilities by:  
  - Patching MS17-010  
  - Disabling SMBv1  
  - Adding firewall rules
