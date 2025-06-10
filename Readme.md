# 🔍 Technology Detection CLI Tool (Python)

A simple Python-based CLI tool that performs **active reconnaissance** by detecting web technologies (e.g., WordPress, Nginx, PHP) used on a target website. This tool uses the [`python-Wappalyzer`](https://pypi.org/project/python-Wappalyzer/) library for accurate and fast fingerprinting.


## 📁 Module Structure

├── tech_detect.py # Main Python script to run the recon
├── requirements.txt # Dependencies for the tool
└── README.md # Project documentation



## ✨ Features

- Detects frontend and backend technologies of websites
- CLI-based, lightweight and easy to run
- Uses `python-Wappalyzer` with no API key required
- Fast and portable


## 📦 Requirements

Ensure Python 3.7+ is installed.

Python packages:
- `python-Wappalyzer`
- `requests`
- `beautifulsoup4`
- `lxml`
- `tldextract`


## ⚙️ Installation

### 1. Clone or download this repo

```bash
git clone https://github.com/yourusername/tech-detect-tool.git
cd Tech_detect

2. Install dependencies
pip install -r Requirement.txt

🚀 How to Use
Basic usage from the terminal:
python tech_detect.py <target_url>

Example:
python tech_detect.py https://wordpress.com

Sample Output:
[*] Scanning: https://wordpress.com

--- Detected Technologies ---
WordPress, PHP, Nginx, MySQL


