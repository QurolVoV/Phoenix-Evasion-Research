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
