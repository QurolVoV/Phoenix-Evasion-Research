#!/usr/bin/env python3
"""
Setup configuration for Phoenix-Evasion-Research Framework

Installation:
    pip install -e .  (for development)
    pip install .     (for production)
"""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_file(filename):
    """Read file contents"""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# Read requirements
def read_requirements():
    """Read requirements from requirements.txt"""
    filepath = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="phoenix-evasion-research",
    version="1.0.0",
    author="Woodlabs Security Research",
    author_email="security@woodlabs-research.com",
    description="Educational Windows Evasion Research Framework",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/QurolVoV/phoenix-evasion-research",
    project_urls={
        "Bug Reports": "https://github.com/QurolVoV/phoenix-evasion-research/issues",
        "Documentation": "https://github.com/QurolVoV/phoenix-evasion-research/blob/main/README.md",
        "Source Code": "https://github.com/QurolVoV/phoenix-evasion-research",
        "Security": "https://github.com/QurolVoV/phoenix-evasion-research/blob/main/SECURITY.md",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Education",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "phoenix-research=src.phoenix_evasion_research:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "security",
        "research",
        "evasion",
        "education",
        "cybersecurity",
        "anti-analysis",
        "sandbox-detection",
        "syscall",
    ],
)
