# 🔥 Phoenix Evasion Research Framework

![Banner](https://github.com/user-attachments/assets/2e786b42-cf54-4787-a40a-444d0c81cdca)

**Educational Windows Evasion Research Framework**  
Riset teknik evasion modern untuk memperkuat pertahanan siber Indonesia.


[![Donasi Saweria](https://img.shields.io/badge/☕_Dukung_WoodLabs-Saweria.co/WoodLabs-ff6b35?style=for-the-badge&logo=coffee&logoColor=white)](https://saweria.co/WoodLabs)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows_%7C_Linux_%7C_macOS-lightgrey.svg)](https://github.com/QurolVoV/phoenix-evasion-research)
[![Stars](https://img.shields.io/github/stars/QurolVoV/phoenix-evasion-research?style=social)](https://github.com/QurolVoV/phoenix-evasion-research/stargazers)
[![CI/CD Pipeline](https://github.com/QurolVoV/Phoenix-Evasion-Research/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/QurolVoV/Phoenix-Evasion-Research/actions/workflows/ci-cd.yml)


[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

> **100% edukasi • 0% offensive • Untuk Blue Team & Researcher Indonesia**

---

## Dukung Riset Kami

Proyek ini 100% gratis dan open-source berkat dukungan kalian semua.  
Setiap donasi membantu kami merilis riset & workshop gratis untuk komunitas Indonesia!

[![Saweria QR](https://saweria.co/qr/3583835?size=200)](https://saweria.co/WoodLabs)  
**https://saweria.co/WoodLabs**

---

---

## 📋 Daftar Isi

- [Tentang Proyek](#tentang-proyek)
- [Fitur Utama](#fitur-utama)
- [Requirements](#requirements)
- [Instalasi](#instalasi)
- [Penggunaan Cepat](#penggunaan-cepat)
- [Struktur Proyek](#struktur-proyek)
- [Core Modules](#core-modules)
- [Kontribusi](#kontribusi)
- [Disclaimer & Legal](#disclaimer--legal)

---

## 🎯 Tentang Proyek

Phoenix Evasion Research adalah **framework open-source gratis** yang dirancang untuk membantu profesional cybersecurity memahami teknik evasion modern yang digunakan oleh malware dan APT tingkat lanjut.

**Fokus:** Defensive Security | Educational Purpose | Zero Offensive Code

### Untuk Siapa?

✅ Blue Team & SOC Analyst  
✅ Peneliti Keamanan Siber  
✅ Mahasiswa & Akademisi  
✅ Red Team (dengan autorisasi)  

### Apa yang TIDAK ada di sini?

❌ Process Injection | ❌ C2 Infrastructure | ❌ AMSI Bypass | ❌ Persistence Mechanism

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| 🔐 **Advanced Encryption** | ChaCha20-Poly1305 + PBKDF2-HMAC-SHA512 (500k iterasi) |
| 🔍 **Syscall Engine** | Ekstraksi SSN langsung dari ntdll.dll (on-disk) |
| 🛡️ **Anti-Analysis** | Deteksi debugger, VM, sandbox (multi-teknik) |
| 🔀 **Polymorphic Code** | Lazy loading + dynamic SSN resolution |
| 📊 **Auto Reporting** | Generate laporan riset dalam Markdown |
| 📦 **100% Open Source** | MIT License - Gratis untuk pendidikan & riset |

---

## 💻 Requirements

### Minimum
- **Python:** 3.8+
- **RAM:** 2GB
- **Storage:** 100MB
- **OS:** Windows 10+ atau Linux

### Recommended
- **Python:** 3.10+
- **RAM:** 8GB+
- **Storage:** 1GB
- **OS:** Windows 11 atau Ubuntu 20+

---

## 📥 Instalasi

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

### 4. Verifikasi Instalasi

```bash
python -c "import sys; sys.path.insert(0, 'src'); from phoenix_evasion_research import *; print('✅ Installation successful!')"
```

---

## 🚀 Penggunaan Cepat

### Menjalankan Framework

```bash
python src/phoenix_evasion_research.py --help
```

### Contoh Penggunaan Dasar

```bash
# Analisis obfuscation
python src/phoenix_evasion_research.py --module obfuscation --target "test_string"

# Analisis syscall
python src/phoenix_evasion_research.py --module syscall

# Deteksi evasion
python src/phoenix_evasion_research.py --module evasion --output report.md

# Jalankan semua module
python src/phoenix_evasion_research.py --module all --output full_report.md
```

### Opsi Command Line

```
--help, -h                      Tampilkan bantuan
--module {all, obfuscation, syscall, evasion}
                                Pilih module untuk dijalankan
--target TARGET                 Target/input untuk analisis
--output OUTPUT                 Output file untuk laporan (default: report.md)
```

---

## 📁 Struktur Proyek

```
Phoenix-Evasion-Research/
├── src/
│   ├── phoenix_evasion_research.py    # Main framework
│   ├── obfuscator.py                  # String obfuscation module
│   ├── syscall_engine.py              # Syscall analysis engine
│   └── evasion_detector.py            # Anti-analysis detection
├── tests/                              # Test suite
│   ├── test_obfuscation.py
│   ├── test_syscall.py
│   └── test_evasion.py
├── requirements.txt                    # Python dependencies
├── .github/workflows/
│   └── ci-cd.yml                      # CI/CD Pipeline
├── README.md                           # Dokumentasi ini
├── LICENSE                             # MIT License
└── CONTRIBUTING.md                     # Guidelines kontribusi
```

---

## 🔧 Core Modules

### PhoenixFramework
Framework utama yang mengorkestra seluruh penelitian evasion. Mengelola workflow, input/output, dan reporting otomatis.

**Usage:**
```python
import sys
sys.path.insert(0, 'src')
from phoenix_evasion_research import PhoenixFramework

framework = PhoenixFramework()
framework.run_assessment(target="example.com", output="report.md")
```

### PhoenixObfuscator
Modul enkripsi string dan data protection menggunakan ChaCha20-Poly1305.

**Fitur:**
- Authenticated encryption dengan PBKDF2
- Nonce management otomatis
- Thread-safe operations
- TTL cleanup

### HadesSyscallEngine
Engine untuk ekstraksi dan analisis system calls dari ntdll.dll.

**Fitur:**
- Direct SSN extraction
- Memory caching
- Windows 10/11 detection
- SSN validation

### SecurityEvasion
Modul anti-analysis dan detection orchestration.

**Fitur:**
- Debugger detection
- VM/Sandbox detection
- Environment validation
- Multi-teknik evasion analysis

---

## 🧪 Testing

### Jalankan Semua Tests

```bash
pytest tests/ -v
```

### Test dengan Coverage Report

```bash
pytest tests/ -v --cov=src/phoenix_evasion_research --cov-report=html
```

### Test Spesifik Module

```bash
# Test obfuscation
pytest tests/test_obfuscation.py -v

# Test syscall
pytest tests/test_syscall.py -v

# Test evasion
pytest tests/test_evasion.py -v
```

---

## 🤝 Kontribusi

Kami sangat menerima kontribusi dari komunitas! 

### Cara Berkontribusi

1. **Fork** repository ini
2. **Buat feature branch**
   ```bash
   git checkout -b feature/nama-fitur
   ```
3. **Commit perubahan Anda**
   ```bash
   git commit -m "Add: deskripsi fitur baru"
   ```
4. **Push ke branch**
   ```bash
   git push origin feature/nama-fitur
   ```
5. **Buat Pull Request** dengan deskripsi detail

### Area yang Dibutuhkan

- Advanced evasion techniques
- Cross-platform support
- Detection heuristics improvement
- Documentation enhancement
- Performance optimization

Lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk guidelines lengkap.

---

## 🐛 Troubleshooting

### Dependency Error
```bash
pip install -r requirements.txt --upgrade
```

### Import Error
```bash
# Pastikan berada di root directory
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
python src/phoenix_evasion_research.py --help
```

### Windows Permission Denied
```cmd
# Jalankan Command Prompt atau PowerShell as Administrator
python src/phoenix_evasion_research.py --help
```

### Virtual Environment Issue
```bash
# Hapus venv lama dan buat ulang
rm -rf venv  # Linux/macOS
rmdir /s venv  # Windows
python -m venv venv
source venv/bin/activate  # atau venv\Scripts\activate
pip install -r requirements.txt
```

---

## ❓ FAQ

**Q: Apakah framework ini aman digunakan?**  
A: Ya, untuk keperluan riset dan edukasi yang sah. Tidak ada kode berbahaya di dalam repository.

**Q: Apakah legal menggunakan framework ini?**  
A: Framework ini adalah educational tool. Gunakan hanya dengan izin yang sesuai dan patuhi hukum lokal.

**Q: Apakah antivirus akan mendeteksi ini?**  
A: Mungkin, karena framework ini mempelajari teknik evasion. Ini normal untuk research tools.

**Q: Bisakah digunakan untuk keperluan komersial?**  
A: Ya, under MIT License dengan catatan compliance terhadap guidelines legal.

---

## 🔒 Disclaimer & Legal

### EDUCATIONAL & RESEARCH USE ONLY

Framework ini dirancang untuk:
- ✅ Riset keamanan yang diotorisasi
- ✅ Pengembangan defensive security
- ✅ Training akademik
- ✅ Meningkatkan threat detection

### PENGGUNAAN YANG DILARANG

- ❌ Malicious/unauthorized access
- ❌ Testing tanpa autorisasi
- ❌ Weaponization & offensive use
- ❌ Melanggar hukum

### Tanggung Jawab Pengguna

1. Dapatkan autorisasi yang diperlukan sebelum penggunaan
2. Patuhi semua hukum dan regulasi lokal
3. Lindungi dan jaga kerahasiaan findings
4. Lakukan responsible disclosure

### No Warranty

Authors dan contributors tidak bertanggung jawab atas:
- Misuse atau abuse framework
- Damage atau loss of data
- Legal consequences dari penggunaan tidak sah
- Segala konsekuensi negatif lainnya

---

## 📞 Support & Contact 🌟 Support the Project

### GitHub
- **Issues:** [GitHub Issues](https://github.com/QurolVoV/Phoenix-Evasion-Research/issues)
- **Discussions:** [GitHub Discussions](https://github.com/QurolVoV/Phoenix-Evasion-Research/discussions)

### Email
📧 **Security-related:** redmoonstonee@gmail.com

If this framework helps your research or educational efforts, please consider supporting our work:  
[![Saweria](https://saweria.co/qr/3583835)](https://saweria.co/WoodLabs)

- Sustained development and updates
- New features
- Community support
- Open research


---

## 📝 Changelog

### Version 1.0 Beta (2025-11-25)
- ✨ Initial release
- 🔐 Advanced obfuscation (ChaCha20-Poly1305)
- 🔍 Syscall engine untuk EDR studies
- 🛡️ Anti-analysis framework
- 📊 Automated research reporting

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

**Thank you for supporting WoodLabs Security Research!**

---

## 🙏 Terima Kasih

Proyek ini 100% gratis. Jika project ini membantu riset atau pembelajaran Anda:

- ⭐ **Star** repository ini
- 🍴 **Fork** dan berkontribusi
- 💬 **Share** feedback dan suggestions
- 📧 **Support** kami untuk continued development

---

**Building Better Defenses Through Understanding Evasion**

<div align="center">
🔥 Phoenix-Evasion-Research Framework
Advanced Security Research for Defensive Excellence
<br>Get Started • Documentation • Examples • Support
<br>
Building better defenses through understanding evasion
<br>
Woodlabs Security Research • 2025
</div>
