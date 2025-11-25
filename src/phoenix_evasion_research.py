#!/usr/bin/env python3
"""
Phoenix-Evasion-Research Framework 2025 - Educational Version
For research and defensive security purposes only. Do not use for malicious activities.
This version removes all offensive components (e.g., injection, bypass, persistence) to focus on evasion techniques for educational use.
Copyright (c) 2025 - Woodlabs Security Research
"""

__version__ = "1.0.0"
__author__ = "QurolVoV - Woodlabs Security Research"

import platform
import sys
import os
import re
import argparse
import concurrent.futures
import random
import time
import socket
import subprocess
import threading
import base64
import json
import sqlite3
import xml.etree.ElementTree as ET
import hashlib
import hmac
import zipfile
import io
import struct
import urllib3
import ssl
import traceback
import secrets
import tempfile
import asyncio
import psutil
import getpass
import math
import datetime
import glob
import shutil
import logging
from collections import Counter, deque
from urllib.parse import urljoin, urlparse, quote, unquote
from datetime import datetime, timedelta

# =============================================================================
# LOGGING SETUP
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# =============================================================================
# CROSS-PLATFORM COMPATIBILITY HANDLING
# =============================================================================

IS_WINDOWS = platform.system().lower() == 'windows'
IS_LINUX = platform.system().lower() == 'linux'
IS_MACOS = platform.system().lower() == 'darwin'

# Platform-specific imports dengan error handling
if IS_WINDOWS:
    try:
        import winreg
        import ctypes
    except ImportError as e:
        logger.warning(f"Windows modules import failed: {e}")
        winreg = None
        ctypes = None
else:
    winreg = None
    ctypes = None
    logger.info("Windows-specific modules not available on this platform")

# Cross-platform imports with error handling
try:
    import requests
except ImportError:
    logger.error("requests library not installed. Install with: pip install requests")
    sys.exit(1)

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.primitives.asymmetric import x25519
    from cryptography.hazmat.primitives.kdf.hkdf import HKDF
    from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM
    from cryptography.hazmat.primitives import serialization
except ImportError:
    logger.error("cryptography library not installed. Install with: pip install cryptography")
    sys.exit(1)

from concurrent import futures
import zlib

# Optional imports dengan error handling
try:
    import dns.resolver
    import dns.message
    import dns.query
    HAS_DNS = True
except ImportError:
    logger.warning("dnspython not installed, DNS features disabled. Install with: pip install dnspython")
    HAS_DNS = False
    dns = None

try:
    import grpc
    HAS_GRPC = True
except ImportError:
    logger.warning("grpcio not installed, gRPC features disabled. Install with: pip install grpcio")
    HAS_GRPC = False
    grpc = None

try:
    import zstandard as zstd
    HAS_ZSTD = True
except ImportError:
    logger.warning("zstandard not installed, compression features limited. Install with: pip install zstandard")
    HAS_ZSTD = False
    zstd = None

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =============================================================================
# DISCLAIMER: EDUCATIONAL USE ONLY
# =============================================================================

DISCLAIMER = """
╔════════════════════════════════════════════════════════════════════════════╗
║                        EDUCATIONAL USE ONLY                                ║
║                                                                            ║
║  Phoenix-Evasion-Research Framework is for authorized security research   ║
║  and educational purposes only. Unauthorized access to computer systems   ║
║  is illegal. Users are responsible for complying with all applicable laws.║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def validate_target_url(target: str) -> bool:
    """Validate target URL format"""
    try:
        result = urlparse(target)
        return all([result.scheme in ['http', 'https'], result.netloc])
    except:
        return False

def get_system_info() -> dict:
    """Get current system information"""
    return {
        'os': platform.system(),
        'release': platform.release(),
        'python_version': platform.python_version(),
        'architecture': platform.architecture()[0],
        'processor': platform.processor(),
    }

# =============================================================================
# LAZY LOADING IMPORTS (Kept for efficiency demonstration)
# =============================================================================

class LazyImporter:
    """Lazy loading utility for modules"""
    def __init__(self):
        self._loaded_modules = {}
        self._import_map = {
            'ct': 'ctypes', 'ps': 'psutil', 'gp': 'getpass', 'wr': 'winreg',
            'zs': 'zstandard', 'dn': 'dns', 'pl': 'platform', 'so': 'socket',
            'sr': 'subprocess', 'cr': 'cryptography', 'gr': 'grpc', 'zc': 'zlib',
            'zp': 'zipfile', 'xm': 'xml.etree.ElementTree', 'sq': 'sqlite3',
            'ur': 'urllib3', 'ss': 'ssl', 'as': 'asyncio', 'th': 'threading',
            'co': 'concurrent.futures', 'ha': 'hashlib', 'hm': 'hmac',
            'ba': 'base64', 'js': 'json', 're': 're', 'ar': 'argparse',
            'ti': 'time', 'ra': 'random', 'os': 'os', 'sy': 'sys'
        }
    
    def __getattr__(self, name):
        if name in self._import_map:
            if name not in self._loaded_modules:
                module_name = self._import_map[name]
                self._loaded_modules[name] = __import__(module_name)
            return self._loaded_modules[name]
        raise AttributeError(f"Module {name} not found")

# =============================================================================
# ADVANCED OBFUSCATION SYSTEM
# =============================================================================

class PhoenixObfuscator:
    """Enhanced obfuscation with ChaCha20-Poly1305 for string protection demo.
    
    Note: This is for EDUCATIONAL purposes only. Master key is regenerated
    on each instance and not persistent. Do NOT use in production.
    """
    
    def __init__(self):
        self.master_key = secrets.token_bytes(64)
        self.nonce_tracker = {}
        self.cache_lock = threading.Lock()
        self.nonce_ttl = 3600
        self.max_nonces = 100000
        threading.Thread(target=self._cleanup_nonces, daemon=True).start()
        logger.info("PhoenixObfuscator initialized")
    
    def _cleanup_nonces(self):
        """Cleanup expired nonces periodically"""
        while True:
            time.sleep(300)
            current_time = time.time()
            with self.cache_lock:
                expired = [nonce for nonce, ts in self.nonce_tracker.items() 
                          if current_time - ts > self.nonce_ttl]
                for nonce in expired:
                    del self.nonce_tracker[nonce]
                if len(self.nonce_tracker) > self.max_nonces:
                    sorted_nonces = sorted(self.nonce_tracker.items(), 
                                         key=lambda x: x[1])
                    for nonce, _ in sorted_nonces[:int(self.max_nonces * 0.2)]:
                        del self.nonce_tracker[nonce]
    
    def obfuscate_string(self, plaintext: str) -> bytes:
        """Obfuscate a string using ChaCha20-Poly1305"""
        data = plaintext.encode('utf-8')
        nonce = secrets.token_bytes(8)
        with self.cache_lock:
            self.nonce_tracker[nonce] = time.time()
        salt = secrets.token_bytes(16)
        key = hashlib.pbkdf2_hmac('sha512', self.master_key + nonce, 
                                 salt, 500000, dklen=32)
        chacha = ChaCha20Poly1305(key)
        inner_nonce = secrets.token_bytes(12)
        ciphertext = chacha.encrypt(inner_nonce, data, None)
        return nonce + salt + inner_nonce + ciphertext
    
    def deobfuscate_string(self, blob: bytes) -> str:
        """Deobfuscate an obfuscated string"""
        try:
            nonce, salt, inner_nonce, ciphertext = (blob[:8], blob[8:24], 
                                                    blob[24:36], blob[36:])
            key = hashlib.pbkdf2_hmac('sha512', self.master_key + nonce, 
                                     salt, 500000, dklen=32)
            chacha = ChaCha20Poly1305(key)
            plaintext = chacha.decrypt(inner_nonce, ciphertext, None)
            return plaintext.decode('utf-8')
        except Exception as e:
            logger.error(f"Deobfuscation error: {str(e)[:50]}")
            return f"[DECRYPT ERROR: {str(e)[:30]}]"

# =============================================================================
# ADVANCED SYSCALL ENGINE
# =============================================================================

class HadesSyscallEngine:
    """Polymorphic direct syscall engine demo for EDR evasion research.
    
    Windows-specific functionality. On non-Windows platforms, returns
    graceful defaults.
    """
    
    def __init__(self):
        self.os_version = self._detect_os_version()
        self.ssn_cache = {}
        self.ntdll_handle = None
        
        if IS_WINDOWS and ctypes:
            try:
                self.kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
                self.ntdll = ctypes.WinDLL('ntdll', use_last_error=True)
                self._load_ntdll_from_disk()
                logger.info(f"HadesSyscallEngine initialized for {self.os_version}")
            except Exception as e:
                logger.warning(f"Failed to initialize HadesSyscallEngine: {e}")
                self.kernel32 = None
                self.ntdll = None
        else:
            self.kernel32 = None
            self.ntdll = None
    
    def _detect_os_version(self) -> str:
        """Detect Windows OS version or return system info"""
        try:
            if not IS_WINDOWS:
                return f'{platform.system()}_{platform.release()}'
            
            if winreg:
                reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
                key = winreg.OpenKey(reg, 
                    r'SOFTWARE\Microsoft\Windows NT\CurrentVersion')
                build = winreg.QueryValueEx(key, 'CurrentBuild')[0]
                build_int = int(build)
                
                if build_int >= 22000:
                    return 'Windows11'
                elif build_int >= 19041:
                    return 'Windows10_21H2'
                else:
                    return 'WindowsOther'
            else:
                return 'Windows_Unknown'
        except Exception as e:
            logger.warning(f"OS detection failed: {e}")
            return f'{platform.system()}_Unknown'
    
    def _load_ntdll_from_disk(self):
        """Load ntdll.dll from disk (Windows only)"""
        if not IS_WINDOWS or not self.kernel32:
            self.ntdll_handle = None
            return
            
        try:
            system32 = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 
                                   'System32')
            ntdll_path = os.path.join(system32, 'ntdll.dll')
            
            if not os.path.exists(ntdll_path):
                logger.warning(f"ntdll.dll not found at {ntdll_path}")
                self.ntdll_handle = None
                return
            
            file_hash = hashlib.sha256()
            with open(ntdll_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    file_hash.update(chunk)
            self.ntdll_hash = file_hash.hexdigest()
            self.ntdll_handle = self.kernel32.LoadLibraryExW(
                ntdll_path.encode('utf-16-le'), None, 0x00000001)
            logger.info(f"ntdll.dll loaded: {self.ntdll_hash[:16]}...")
        except Exception as e:
            logger.warning(f"Failed to load ntdll: {e}")
            self.ntdll_handle = None
    
    def get_syscall_number(self, func_name: str) -> int:
        """Get syscall number for a given function (Windows only)"""
        if not IS_WINDOWS or not self.ntdll_handle:
            logger.debug(f"Syscall extraction not available on {platform.system()}")
            return 0
            
        if func_name in self.ssn_cache:
            return self.ssn_cache[func_name]
        
        if not self.ntdll_handle or not self.kernel32:
            return 0
        
        try:
            addr = self.kernel32.GetProcAddress(self.ntdll_handle, 
                                               func_name.encode())
            code = ctypes.string_at(addr, 64)
            patterns = {'Windows11': [(b"\x4C\x8B\xD1\xB8", 4)]}
            pattern_list = patterns.get(self.os_version, [])
            
            for prologue, offset in pattern_list:
                if code.startswith(prologue):
                    ssn = struct.unpack('<I', code[offset:offset+4])[0]
                    self.ssn_cache[func_name] = ssn
                    return ssn
            return 0
        except Exception as e:
            logger.debug(f"Syscall extraction failed for {func_name}: {e}")
            return 0

# =============================================================================
# SECURITY & EVASION
# =============================================================================

class SecurityEvasion:
    """Demonstration of evasion techniques for educational purposes."""
    
    def __init__(self):
        self.anti_debug = AntiDebug()
        self.sandbox_detector = SandboxDetector()
    
    def execute_evasion(self):
        """Execute evasion demonstrations"""
        logger.info("Demonstrating evasion techniques for research...")
        if self.anti_debug.is_debugged():
            logger.warning("Debugger detected - exiting")
            sys.exit(1)
        if self.sandbox_detector.detect_sandbox():
            logger.warning("Sandbox detected - exiting")
            sys.exit(1)
        logger.info("Evasion demo completed")

class AntiDebug:
    """Anti-debugging demonstration (Windows-specific)."""
    
    def __init__(self):
        self.kernel32 = None
        if IS_WINDOWS and ctypes:
            try:
                self.kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
            except Exception as e:
                logger.debug(f"Failed to load kernel32: {e}")
    
    def is_debugged(self) -> bool:
        """Check if process is being debugged"""
        if not IS_WINDOWS or not self.kernel32:
            logger.debug("Anti-debug checks limited on non-Windows platforms")
            return False
        
        try:
            return bool(self.kernel32.IsDebuggerPresent())
        except Exception as e:
            logger.debug(f"Debugger check failed: {e}")
            return False

class SandboxDetector:
    """Sandbox detection demo (cross-platform)."""
    
    def detect_sandbox(self) -> bool:
        """Detect if running in sandbox environment"""
        checks = [
            self._check_cpu_cores, 
            self._check_ram_size, 
            self._check_runtime
        ]
        failed_checks = sum(1 for check in checks if not check())
        logger.info(f"Sandbox detection: {failed_checks}/{len(checks)} checks failed")
        return failed_checks >= 2
    
    def _check_cpu_cores(self) -> bool:
        """Check CPU cores"""
        try:
            cores = psutil.cpu_count()
            result = cores >= 2 if cores else False
            logger.info(f"CPU cores check: {cores} cores - {'PASS' if result else 'FAIL'}")
            return result
        except Exception as e:
            logger.warning(f"CPU check error: {e}")
            return True
    
    def _check_ram_size(self) -> bool:
        """Check available RAM"""
        try:
            ram_gb = psutil.virtual_memory().total / (1024 ** 3)
            result = ram_gb >= 2.0
            logger.info(f"RAM size check: {ram_gb:.1f} GB - {'PASS' if result else 'FAIL'}")
            return result
        except Exception as e:
            logger.warning(f"RAM check error: {e}")
            return True
    
    def _check_runtime(self) -> bool:
        """Check system runtime/uptime"""
        try:
            if IS_WINDOWS:
                boot_time = psutil.boot_time()
                uptime = time.time() - boot_time
                result = uptime > 300  # 5 minutes
                logger.info(f"Runtime check: {uptime:.0f}s - {'PASS' if result else 'FAIL'}")
            elif IS_LINUX:
                try:
                    with open('/proc/uptime', 'r') as f:
                        uptime_seconds = float(f.readline().split()[0])
                    result = uptime_seconds > 300
                    logger.info(f"Runtime check: {uptime_seconds:.0f}s - {'PASS' if result else 'FAIL'}")
                except IOError:
                    logger.warning("Could not read /proc/uptime")
                    return True
            else:
                logger.info("Runtime check: Not implemented for this platform")
                return True
            
            return result
        except Exception as e:
            logger.warning(f"Runtime check error: {e}")
            return True

# =============================================================================
# MAIN FRAMEWORK
# =============================================================================

class PhoenixFramework:
    """Phoenix-Evasion-Research Framework for educational use."""
    
    def __init__(self):
        logger.info(f"Initializing Phoenix Framework on {platform.system()}")
        self.syscall_engine = HadesSyscallEngine()
        self.security = SecurityEvasion()
        self.obfuscator = PhoenixObfuscator()
        self.system_info = get_system_info()
    
    def execute_evasion(self):
        """Execute evasion demonstrations"""
        self.security.execute_evasion()
    
    def demonstrate_obfuscation(self):
        """Demonstrate string obfuscation capabilities"""
        logger.info("Demonstrating advanced obfuscation...")
        test_strings = [
            "Hello Phoenix Framework",
            "Sensitive Research Data",
            "Evasion Technique Demo"
        ]
        
        for test_str in test_strings:
            try:
                encrypted = self.obfuscator.obfuscate_string(test_str)
                decrypted = self.obfuscator.deobfuscate_string(encrypted)
                logger.info(f"Obfuscation test: {test_str[:30]}... "
                           f"({len(encrypted)} bytes) - "
                           f"{'OK' if test_str == decrypted else 'MISMATCH'}")
            except Exception as e:
                logger.error(f"Obfuscation test failed: {e}")
    
    def demonstrate_syscall_research(self):
        """Demonstrate syscall research capabilities"""
        logger.info("Demonstrating syscall research...")
        if IS_WINDOWS:
            syscalls = ["NtCreateFile", "NtOpenProcess", "NtAllocateVirtualMemory"]
            for syscall in syscalls:
                try:
                    ssn = self.syscall_engine.get_syscall_number(syscall)
                    if ssn > 0:
                        logger.info(f"{syscall}: SSN = 0x{ssn:X}")
                    else:
                        logger.info(f"{syscall}: Not found or not available")
                except Exception as e:
                    logger.error(f"Syscall research failed for {syscall}: {e}")
        else:
            logger.info(f"Syscall research is Windows-specific, current platform: {platform.system()}")
    
    def run_research_assessment(self, target_url: str):
        """Run complete research assessment"""
        logger.info("="*60)
        logger.info("PHOENIX-EVASION-RESEARCH 2025 - DEMO")
        logger.info(f"Platform: {self.system_info['os']} {self.system_info['release']}")
        logger.info(f"Python: {self.system_info['python_version']}")
        logger.info("="*60)
        
        try:
            self.execute_evasion()
            self.demonstrate_obfuscation()
            self.demonstrate_syscall_research()
            self._generate_research_report(target_url)
            logger.info("ASSESSMENT DEMO COMPLETED")
        except KeyboardInterrupt:
            logger.info("Assessment interrupted by user")
            raise
        except Exception as e:
            logger.error(f"Assessment failed: {e}", exc_info=True)
            raise
    
    def _generate_research_report(self, target_url: str):
        """Generate research report in markdown"""
        report = f"""# PHOENIX-EVASION-RESEARCH REPORT
Generated: {datetime.now().isoformat()}
Framework Version: {__version__}

## Assessment Summary
- Target: {target_url}
- Platform: {self.system_info['os']} {self.system_info['release']}
- Python Version: {self.system_info['python_version']}
- Architecture: {self.system_info['architecture']}

## Techniques Demonstrated
- Platform Analysis: {self.system_info['os']}
- Anti-Debug Checks: {'Available (Windows)' if IS_WINDOWS else 'Basic (Non-Windows)'}
- Sandbox Detection: Available (Multi-platform)
- Syscall Extraction: {'Available (Windows)' if IS_WINDOWS else 'Limited (Non-Windows)'}
- Advanced Obfuscation: Available (Cross-platform)

## Research Findings
This educational demonstration shows how modern evasion techniques can be studied
for defensive security purposes. The framework successfully demonstrates:

1. Cryptographic string obfuscation using ChaCha20-Poly1305
2. Cross-platform sandbox detection heuristics
3. Windows-specific syscall research capabilities
4. Anti-analysis techniques for research purposes

## Defensive Recommendations
- Monitor for unusual cryptographic operations
- Implement behavioral analysis for sandbox detection bypass
- Study syscall patterns for EDR evasion detection
- Enhance debugger detection capabilities

## System Information
- CPU Cores: {psutil.cpu_count()}
- RAM: {psutil.virtual_memory().total / (1024**3):.1f} GB
- Architecture: {self.system_info['architecture']}

## Disclaimer
This report is generated for EDUCATIONAL AND RESEARCH PURPOSES ONLY.
All techniques demonstrated are for defensive security improvement.
Unauthorized access to computer systems is illegal.
"""
        
        try:
            report_path = 'phoenix_research_report.md'
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            logger.info(f"Research report generated: {report_path}")
        except IOError as e:
            logger.error(f"Failed to write report: {e}")

# =============================================================================
# COMMAND LINE INTERFACE
# =============================================================================

def main():
    """Main entry point"""
    print(DISCLAIMER)
    
    parser = argparse.ArgumentParser(
        description='Phoenix-Evasion-Research Framework - Educational Version',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python phoenix_evasion_research.py --target https://example.com
  python phoenix_evasion_research.py --target https://test.org --quick
        
Disclaimer: For educational and research purposes only.
        """
    )
    parser.add_argument('--target', required=True, 
                       help='Target URL for research assessment')
    parser.add_argument('--quick', action='store_true', 
                       help='Run quick assessment only')
    parser.add_argument('--output', help='Custom output file for research report')
    
    args = parser.parse_args()
    
    # Validate target URL
    if not validate_target_url(args.target):
        logger.error(f"Invalid target URL: {args.target}")
        logger.error("Please provide a valid HTTP/HTTPS URL (e.g., https://example.com)")
        sys.exit(1)
    
    try:
        framework = PhoenixFramework()
        
        if args.quick:
            logger.info("Running quick assessment...")
            framework.execute_evasion()
            framework.demonstrate_obfuscation()
        else:
            framework.run_research_assessment(args.target)
            
        if args.output:
            try:
                shutil.copy('phoenix_research_report.md', args.output)
                logger.info(f"Report saved to: {args.output}")
            except (IOError, shutil.Error) as e:
                logger.error(f"Failed to copy report: {e}")
                sys.exit(1)
            
    except KeyboardInterrupt:
        logger.info("Assessment interrupted by user")
        sys.exit(0)
    except SystemExit:
        raise
    except Exception as e:
        logger.error(f"Assessment failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
