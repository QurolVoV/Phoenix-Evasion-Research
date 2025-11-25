# Phoenix-Evasion-Research Framework 2025

![Banner](https://github.com/user-attachments/assets/2e786b42-cf54-4787-a40a-444d0c81cdca)

**Educational Windows Evasion Research Framework**  
Riset teknik evasion modern untuk memperkuat pertahanan siber Indonesia.

[![Donasi Saweria](https://img.shields.io/badge/☕_Dukung_WoodLabs-Saweria.co/WoodLabs-ff6b35?style=for-the-badge&logo=coffee&logoColor=white)](https://saweria.co/WoodLabs)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows_%7C_Linux_%7C_macOS-lightgrey.svg)](https://github.com/QurolVoV/phoenix-evasion-research)
[![Stars](https://img.shields.io/github/stars/QurolVoV/phoenix-evasion-research?style=social)](https://github.com/QurolVoV/phoenix-evasion-research/stargazers)

> **100% edukasi • 0% offensive • Untuk Blue Team & Researcher Indonesia**

---

## Dukung Riset Kami

Proyek ini 100% gratis dan open-source berkat dukungan kalian semua.  
Setiap donasi membantu kami merilis riset & workshop gratis untuk komunitas Indonesia!

[![Saweria QR](https://saweria.co/qr/3583835?size=200)](https://saweria.co/WoodLabs)  
**https://saweria.co/WoodLabs**

---

## Apa itu Phoenix-Evasion-Research?

Framework open-source untuk **mempelajari teknik evasion modern** yang digunakan oleh malware/APT kelas tinggi — **tanpa menyertakan kode berbahaya**.

Dirancang khusus untuk:
- Blue Team & SOC Analyst
- Peneliti Keamanan Siber
- Mahasiswa & Akademisi
- Red Team (authorized only)

**Tidak ada** process injection, C2, AMSI bypass, atau persistence di dalam repo ini.

---

## Fitur Utama

| Fitur                          | Deskripsi                                                                 |
|---------------------------------|---------------------------------------------------------------------------|
| Advanced String Obfuscation     | ChaCha20-Poly1305 + PBKDF2-HMAC-SHA512 (500k iterasi) + nonce management |
| HadesSyscallEngine              | Ekstraksi SSN langsung dari `ntdll.dll` bersih (on-disk)                 |
| Anti-Debug & Sandbox Detection  | Deteksi debugger, VM, dan lingkungan analisis otomatis                   |
| Polymorphic Code Elements       | Lazy loading + dynamic SSN resolution                                     |
| Educational Reporting           | Generate laporan riset otomatis dalam Markdown                            |
| 100% Open Source & Gratis       | MIT License — bebas digunakan untuk pendidikan & riset                    |

---

## Instalasi Cepat

```bash
git clone https://github.com/QurolVoV/phoenix-evasion-research.git
cd phoenix-evasion-research
python -m venv venv
source venv/bin/activate        # Linux/macOS
# .\venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

---

## Support Our Research 💖

If you find this project valuable and want to support our ongoing security research, consider making a donation.  
**Your support helps us maintain and improve this framework for the cybersecurity community.**

[![Donate Saweria](https://img.shields.io/badge/%F0%9F%92%96_Donate-Saweria-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white)](https://saweria.co/WoodLabs)

Your support enables us to:
- Continue open-source security research
- Maintain and update the framework regularly
- Develop new defensive security features
- Support the cybersecurity community with free tools
- Conduct advanced threat intelligence research

---

## Quick Start 🎯

```bash
# Clone the repository
git clone https://github.com/QurolVoV/phoenix-evasion-research.git
cd phoenix-evasion-research

# Install dependencies
pip install -r requirements.txt

# Run your first assessment
python Woodlabs_Phoenix_Framework_beta.py --target https://example.com
```

---

## 📖 Table of Contents

- Overview
- Key Features
- Installation Guide
- Quick Examples
- Architecture
- Core Modules
- Advanced Usage
- API Reference
- CLI Guide
- Testing
- Contributing
- Security
- Troubleshooting
- FAQ
- Changelog
- License
- Disclaimer

---

## 🛡️ Overview

Phoenix-Evasion-Research Framework 2025 adalah platform edukasi mutakhir untuk profesional cybersecurity, peneliti, dan tim security defensif. Framework ini menyediakan lingkungan riset aman untuk memahami teknik evasion tanpa risiko legal atau ethical.

### 🎯 Purpose

- **Educational Research:** Studi teknik evasion di lingkungan terkontrol
- **Defensive Development:** Menyempurnakan deteksi & mekanisme pertahanan
- **Threat Intelligence:** Memahami tradecraft adversary untuk pertahanan yang lebih baik
- **Security Training:** Melatih tim di deteksi ancaman tingkat lanjut

### ⚠️ Critical Notice

**LEGAL & ETHICAL USAGE ONLY:**
- Untuk riset keamanan yang sah
- Tujuan edukasi
- Pengembangan defensive security
- Studi akademik cybersecurity
- Penggunaan tidak sah/dilarang dilarang keras

---

## ✨ Key Features

### 🔒 Advanced Cryptography System
- ChaCha20-Poly1305 authenticated encryption
- PBKDF2-HMAC-SHA512 key derivation (500,000 iterasi)
- Nonce management otomatis + TTL cleanup
- Operasi enkripsi thread-safe

### 🛡️ Anti-Analysis Framework
- Pendeteksian debugger & sandbox (multi-teknik)
- Analisis environment
- Validasi integritas sistem

### ⚡ Syscall Research Engine
- Analisis syscall langsung untuk studi EDR evasion
- Pendeteksian Windows 10/11
- Caching SSN & analisis memori modul

### 🚀 Performance Optimizations
- Lazy loading module
- Memory management + resource cleanup otomatis
- Caching & operasi concurrent

### 📊 Research & Reporting
- Otomasi dokumentasi riset (Markdown)
- Progress monitoring
- Ekspor data riset ke berbagai format

---

## 🚀 Installation Guide

### System Requirements

| Component | Minimum   | Recommended        |
|-----------|-----------|-------------------|
| Python    | 3.8+      | 3.10+             |
| RAM       | 2GB       | 8GB+              |
| Storage   | 100MB     | 1GB               |
| OS        | Win 10+   | Win 11/Ubuntu 20+ |

### Step-by-step

1. Clone repo & buat virtual environment

    ```bash
    git clone https://github.com/QurolVoV/phoenix-evasion-research.git
    cd phoenix-evasion-research
    python -m venv venv
    source venv/bin/activate    # Untuk Linux/macOS
    # .\venv\Scripts\activate   # Untuk Windows
    ```

2. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

3. Verifikasi

    ```bash
    python -c "from Woodlabs_Phoenix_Framework_beta import PhoenixFramework; print('Installation successful!')"
    python Woodlabs_Phoenix_Framework_beta.py --help
    ```

---

## 📚 API Reference

See the code for details on:
- `PhoenixFramework` – research assessment controller
- `PhoenixObfuscator` – string/data protection module
- `HadesSyscallEngine` – system call resolution & research
- `SecurityEvasion` – anti-analysis orchestration

---

## 💻 Command Line Interface

```
usage: Woodlabs_Phoenix_Framework_beta.py [-h] --target TARGET [--output OUTPUT] [--module {all,obfuscation,syscall,evasion}]

Phoenix-Evasion-Research Framework 2025

options:
  -h, --help            show this help message and exit
  --target TARGET       Target URL for research assessment (required)
  --output OUTPUT       Custom output file for research report
  --module {all,obfuscation,syscall,evasion}
                        Specific research module to execute
```

Example:

```bash
python Woodlabs_Phoenix_Framework_beta.py --target https://example.com --output my_report.md
```

---

## 🧪 Testing & Validation

Testing & benchmarks located under `/tests` and `/benchmarks` folder.

```bash
python -m pytest tests/ -v
python -m pytest tests/ --cov=Woodlabs_Phoenix_Framework_beta --cov-report=html
```

---

## 🤝 Contributing

**We welcome contributions!**

How to help:
- Fork repository
- Create feature branch (`git checkout -b feature/cool-feature`)
- Code with type hints & docstrings
- Add tests
- Open a Pull Request

Areas needed: advanced evasion, cross-platform, detection heuristics, documentation, performance.  
See full guidelines in CONTRIBUTING.md.

---

## 🔒 Security Considerations

**Responsible usage only.**  
Approved: academic, defensive, authorized red team.  
Prohibited: malicious use, unauthorized testing, weaponization.

Security features include automatic environment validation.

See LICENSE and Disclaimer below for full legal notice.

---

## 🛠️ Troubleshooting

Common issues:
- Dependency errors: `pip install -r requirements.txt --upgrade`
- Windows: run as Administrator, use proper Python arch
- Performance: tune PBKDF2 iterations for dev
- Sandbox false positives: adjust thresholds in code

Support:  
- GitHub Issues/Discussions  
- Email: redmoonstonee@gmail.com (security-sensitive)

---

## ❓ FAQ

**Q1:** Is it safe to use?  
**A:** Yes, for legitimate research/education. No malicious code.

**Q2:** Legal considerations?  
**A:** Use only with permission. Comply with laws.

**Q3:** Does AV detect the framework?  
**A:** Sometimes; normal for research tools.

**Q4:** Commercial use?  
**A:** Allowed under MIT, comply with legal guidelines.

---

## 📋 Changelog

**Version 1.0 Beta (2025-11-25)**
- Initial release
- Advanced obfuscation (ChaCha20-Poly1305)
- Syscall engine for EDR studies
- Anti-analysis framework
- Research reporting/doc

---

## 📄 License

MIT License

Copyright (c) 2025 Woodlabs Security Research

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.**

---

## ⚠️ Disclaimer

**EDUCATIONAL AND RESEARCH USE ONLY**

This framework is designed for:
- Authorized security research
- Defensive cybersecurity development
- Academic training
- Improving threat detection

**Users are responsible for:**
- Obtaining proper authorization
- Legal and ethical compliance
- Protecting data and findings

**Authors/contributors:**
- Provide no warranty
- Not responsible for misuse/damages
- Support responsible disclosure and open research

**By using this software, you agree to:**
- Use only for legitimate, authorized purposes
- Accept responsibility for all actions
- Respect privacy, data protection

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
