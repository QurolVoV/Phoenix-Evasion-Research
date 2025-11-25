"""
Phoenix-Evasion-Research Framework

A comprehensive educational platform for cybersecurity researchers,
red teams, and defensive security professionals.
"""

__version__ = "1.0.0"
__author__ = "QurolVoV - Woodlabs Security Research"
__license__ = "MIT"

from .phoenix_evasion_research import (
    PhoenixFramework,
    PhoenixObfuscator,
    HadesSyscallEngine,
    SecurityEvasion,
    AntiDebug,
    SandboxDetector,
    validate_target_url,
    get_system_info,
    LazyImporter,
)

__all__ = [
    "PhoenixFramework",
    "PhoenixObfuscator",
    "HadesSyscallEngine",
    "SecurityEvasion",
    "AntiDebug",
    "SandboxDetector",
    "validate_target_url",
    "get_system_info",
    "LazyImporter",
]
