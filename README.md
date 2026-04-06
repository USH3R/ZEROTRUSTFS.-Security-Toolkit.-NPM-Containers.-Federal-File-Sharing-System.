# **ZERO TRUST. Federal File Sharing System**  
![Role – Builder](https://img.shields.io/badge/Role-Builder-lightgrey?style=for-the-badge&logo=hackthebox&logoColor=white)
![Skill – Secure System Design](https://img.shields.io/badge/Skill-Secure_System_Design-lightgrey?style=for-the-badge&logo=python&logoColor=white)
![Output – Secure File Sharing](https://img.shields.io/badge/Output-Secure_File_Sharing-lightgrey?style=for-the-badge&logo=files&logoColor=white)
![Compliance – NIST_800-53/FISMA](https://img.shields.io/badge/Compliance-NIST_800--53%2FFISMA-lightgrey?style=for-the-badge&logo=government&logoColor=white)
![Simulation – Lab-Ready Security Environment](https://img.shields.io/badge/Simulation-Lab_Ready_Security_Environment-lightgrey?style=for-the-badge&logo=flask&logoColor=white)
![Encryption – AES/RSA + Key Rotation](https://img.shields.io/badge/Encryption-AES%2FRSA_+_Key_Rotation-lightgrey?style=for-the-badge&logo=auth0&logoColor=white)  
A secure file-sharing platform built around zero trust principles, where all access is continuously verified and never implicitly trusted.  
✅ Simulates real-world secure system design  
End-to-end encryption for all files  
Role-based access control (RBAC)  
Audit logging for all actions  
Key rotation and revocation simulation  
✅ Follows secure system workflow  
  
**Chain:**   
File upload/download with encryption  
Access control verification (roles & permissions)  
Audit logging of all events  
Key management & rotation  
Reporting (secure activity summaries)  
  
**Stack:**    
Python / Node.js backend  
AES and RSA encryption for secure data  
OAuth / JWT for authentication and authorization  
Optional frontend interface for file management  
  
**Features:**  
Secure file upload and download  
Continuous access verification based on zero trust principles  
Role-based access (Administrator, Editor, Viewer)  
Audit logs of all file actions  
Key rotation simulation to demonstrate secure operations  
  
**Security modules:**  
End-to-end encryption enforcement  
Access control validation  
Audit and compliance logging  
  
**Reporting engine:**  
Generates PDF or HTML summaries of user activity and access attempts  
Demonstrates system integrity and security posture  
  
# **Zero Trust Architecture**  
**Primary Files / Structure**  
zero_trust_fs/  
├── main.py  
├── auth_service.py  
├── policy_evaluator.py  
├── device_validator.py  
├── file_handler.py  
└── settings.yaml  
  
**Zero Trust Workflow**  
[Authenticate] → [Authorize] → [Encrypt/Protect] → [Audit]  
  
Future Files / Structure:  
zero trust fs/  
├── orchestrator/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# controls request validation flow  
├── identity/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# authentication + identity validation  
├── device_trust/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# device + context verification  
├── policy_engine/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# authorization (RBAC / rules)  
├── crypto/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# encryption + key management  
├── access_gateway/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# secure file operations  
├── audit/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# logging + compliance tracking  
├── reporting/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# security reports  
├── lab_env/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# simulated users/devices  
└── rules_of_engagement/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# safety + compliance  
   
Potential / Future Files / Structure  
zero trust fs/  
│  
├── README.md  
├── LICENSE  
├── requirements.txt  
├── docker-compose.yml  
├── docs/  
│   ├── architecture.md  
│   ├── zero_trust_workflow.md  
│   ├── nist_mapping.md  
│   └── rules_of_engagement.md  
├── config/  
│   ├── settings.yaml  
│   ├── policies.yaml  
│   └── trust_rules.yaml  
├── lab_env/  
│   ├── users/  
│   │   ├── normal_user.py  
│   │   └── malicious_user.py  
│   ├── devices/  
│   │   ├── trusted_device.json  
│   │   └── untrusted_device.json  
│   └── file_server/  
│       ├── Dockerfile  
│       └── sample_files/  
├── orchestrator/  
│   ├── main.py  
│   ├── pipeline.py  
│   └── scheduler.py  
├── identity/  
│   ├── auth_service.py  
│   ├── session_validator.py  
│   └── identity_store.py  
├── device_trust/  
│   ├── device_validator.py  
│   ├── risk_engine.py  
│   └── context_analyzer.py  
├── policy_engine/  
│   ├── policy_evaluator.py  
│   ├── rbac.py  
│   └── rules.yaml  
├── crypto/  
│   ├── aes_engine.py  
│   ├── rsa_engine.py  
│   ├── key_manager.py  
│   └── vault_simulator.py  
├── access_gateway/  
│   ├── file_handler.py  
│   ├── secure_transfer.py  
│   └── validator.py  
├── audit/  
│   ├── logger.py  
│   ├── audit_log.json  
│   └── integrity_checker.py  
├── reporting/  
│   ├── report_generator.py  
│   ├── templates/  
│   │   ├── activity_report.html  
│   │   └── compliance_report.html  
│   └── output/  
│       └── (generated reports)  
├── dashboard/  
│   ├── app.py  
│   └── templates/  
│       └── index.html  
├── logs/  
│   ├── access.log  
│   ├── audit.log  
│   └── security_events.log  
└── tests/  
    ├── test_identity.py  
    ├── test_policy_engine.py  
    ├── test_crypto.py  
    ├── test_pipeline.py  
    └── test_access_flow.py  
  
**Prove or show the following:**  
Understanding of secure system design and zero trust principles  
Practical implementation of encryption, authentication, and access control  
Ability to produce auditable and compliant security outputs  
  
**👉 Bonus:**  
“Rules of engagement” section to show understanding of operational security and secure system limitations  

# **Portfolio Context**    
This project is part of a full-spectrum cybersecurity portfolio that demonstrates end-to-end capability in offensive, defensive, and secure system design workflows:  
**Red Team (OffSec Simulator):** Simulates attacker workflows and penetration testing.  
https://github.com/USH3R/REDTEAM.-Offensive-Security-Simulator  
**Blue Team (SentinelOps):** Detects threats and generates actionable incident reports.  
https://github.com/USH3R/BLUETEAM.-SentinelOps.-Defense-Detection-System-Dashboard  
**Zero Trust (Federal File Sharing System):** Builds secure, auditable, zero trust-compliant systems.  
Together, these projects showcase full-spectrum cybersecurity capability, illustrating that the author can attack, defend, and build secure systems across the complete security lifecycle.  
  
# **Zero Trust FS Security Toolkit - Instructions and Interaction**  
To access, run, and interact with the **Zero Trust FS Security Toolkit**:  
1. Open a **Codespace terminal** in your repository on GitHub.com.  
2. In the terminal, type the following command to start the application:  
    bash run.sh
3. Terminal Prompts. The Zero Trust FS Security Toolkit will start and sequentially prompt you for input. Follow the prompts carefully:
- When the terminal displays 'Enter username:', type the Username listed in the table below.
- When the terminal displays 'Enter password:', type the Password corresponding to that Username listed in the table below.
- When the terminal displays 'Enter device ID:', type the Device ID associated with that Username listed in the table below.
- When the terminal displays Enter file to access:', type the file that Username: is allowed to access, listed in the table below.
<table>
  <thead>
    <tr>
      <th>Username</th>
      <th>Password</th>
      <th>Device ID</th>
      <th>Accessible File</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice</td>
      <td>alicepass</td>
      <td>device123</td>
      <td>secret_report.txt</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>bobpass</td>
      <td>device456</td>
      <td>edit_document.txt</td>
    </tr>
    <tr>
      <td>Eve</td>
      <td>evepass</td>
      <td>device789</td>
      <td>public_note.txt</td>
    </tr>
  </tbody>
</table>
⚠️ Important: Usernames, passwords, devices, and accessible files are not interchangeable. Do not mix them when using the Security Toolkit app.  
