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
  
**Zero Trust Workflow**  
[Authenticate] → [Authorize] → [Encrypt/Protect] → [Audit]  
  
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
  
zero-trust-fs/  
├── orchestrator/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# request validation pipeline  
│&nbsp;&nbsp;&nbsp;&nbsp;├── main.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# orchestrator main script  
│&nbsp;&nbsp;&nbsp;&nbsp;├── pipeline.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# orchestrator flow control  
│&nbsp;&nbsp;&nbsp;&nbsp;└── scheduler.py&nbsp;&nbsp;&nbsp;&nbsp;# scheduled execution manager  
├── identity/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# authentication + identity validation  
│&nbsp;&nbsp;&nbsp;&nbsp;├── auth_service.py&nbsp;&nbsp;&nbsp;&nbsp;# handles login requests  
│&nbsp;&nbsp;&nbsp;&nbsp;├── session_validator.py&nbsp;&nbsp;&nbsp;# session verification  
│&nbsp;&nbsp;&nbsp;&nbsp;└── identity_store.py&nbsp;&nbsp;&nbsp;&nbsp;# stores user credentials  
├── device_trust/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# device + context verification  
│&nbsp;&nbsp;&nbsp;&nbsp;├── device_validator.py&nbsp;&nbsp;&nbsp;# checks device trust level  
│&nbsp;&nbsp;&nbsp;&nbsp;├── risk_engine.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# calculates risk score  
│&nbsp;&nbsp;&nbsp;&nbsp;└── context_analyzer.py&nbsp;&nbsp;&nbsp;# evaluates device context  
├── policy_engine/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# authorization (RBAC / rules)  
│&nbsp;&nbsp;&nbsp;&nbsp;├── policy_evaluator.py&nbsp;&nbsp;# applies policies  
│&nbsp;&nbsp;&nbsp;&nbsp;├── rbac.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# role-based access control  
│&nbsp;&nbsp;&nbsp;&nbsp;└── rules.yaml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# policy definitions  
├── crypto/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# encryption + key management  
│&nbsp;&nbsp;&nbsp;&nbsp;├── aes_engine.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# AES encryption module  
│&nbsp;&nbsp;&nbsp;&nbsp;├── rsa_engine.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# RSA encryption module  
│&nbsp;&nbsp;&nbsp;&nbsp;├── key_manager.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# key lifecycle management  
│&nbsp;&nbsp;&nbsp;&nbsp;└── vault_simulator.py&nbsp;&nbsp;&nbsp;&nbsp;# simulates secure storage  
├── access_gateway/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# secure file operations  
│&nbsp;&nbsp;&nbsp;&nbsp;├── file_handler.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# handles file requests  
│&nbsp;&nbsp;&nbsp;&nbsp;├── secure_transfer.py&nbsp;&nbsp;&nbsp;&nbsp;# manages encrypted transfers  
│&nbsp;&nbsp;&nbsp;&nbsp;└── validator.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# validates access  
├── audit/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# logging + compliance tracking  
│&nbsp;&nbsp;&nbsp;&nbsp;├── logger.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# event logger  
│&nbsp;&nbsp;&nbsp;&nbsp;├── audit_log.json&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# raw audit logs  
│&nbsp;&nbsp;&nbsp;&nbsp;└── integrity_checker.py&nbsp;&nbsp;&nbsp;# verifies log integrity  
└── config/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# policies + system settings  
&nbsp;&nbsp;&nbsp;&nbsp;├── settings.yaml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# main configuration  
&nbsp;&nbsp;&nbsp;&nbsp;├── policies.yaml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# policy definitions  
&nbsp;&nbsp;&nbsp;&nbsp;└── trust_rules.yaml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# device/user trust rules  
  
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
  
**Proves or shows the following:**  
Understanding of secure system design and zero trust principles  
Practical implementation of encryption, authentication, and access control  
Ability to produce auditable and compliant security outputs (very federal-friendly)  
  
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
