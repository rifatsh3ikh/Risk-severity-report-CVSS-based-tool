# Risk Severity Report (CVSS-Based) Tool

A CVSS (Common Vulnerability Scoring System)-based risk severity reporting tool that analyzes vulnerabilities and generates detailed severity reports. This tool helps in assessing the risk level of vulnerabilities using CVSS metrics and produces structured output for easy review and prioritization.

## ⚠️ Legal Disclaimer

This tool is intended for **educational, authorized security testing, and internal vulnerability risk assessment only**.  
**Do NOT** use it to scan or assess systems without **explicit permission**. The author is not responsible for misuse or damage caused by improper actions.

## 📌 Features

- **CVSS Score Calculation**: Computes CVSS scores based on supplied vulnerability vectors or data inputs.
- **Risk Severity Classification**: Categorizes vulnerability risk levels (e.g., Low, Medium, High, Critical) based on CVSS metrics.
- **Report Generation**: Produces comprehensive **HTML and/or CSV reports** including CVSS scores, severity, and risk details.
- **Batch Processing**: Accepts multiple vulnerabilities at once for group reporting.
- **Static File Support**: Integrates with uploaded scan reports or vulnerability lists.
- **Web & CLI Interfaces** *(update as applicable)*.

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rifatsh3ikh/Risk-severity-report-CVSS-based-tool.git
   cd Risk-severity-report-CVSS-based-tool
   ```
   
## Create a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
Install Python dependencies:

pip install -r requirements.txt
🚀 Usage
📌 Replace example commands with your actual CLI or script names.

Run analysis for a single vulnerability
python analyze.py --cvss "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
Process a list of CVEs
python batch_report.py --input vulnerabilities.csv --output report.html
Generate a comprehensive HTML report
python generate_report.py --data cvss_results.json --format html
Example Output
After analysis, you’ll find:

A generated report.html in the reports/ directory

A summary table of CVSS scores & risk levels

Charts or graphs (if supported)

## 📋 Input Formats
Format	Description
CSV	List of CVE IDs and/or CVSS vectors
JSON	Structured CVSS data with metadata
API	Input from external CVE/feeds (optional)
(Adjust based on actual supported formats.)

## 📊 Severity Levels (CVSS)
Critical: 9.0–10.0

High: 7.0–8.9

Medium: 4.0–6.9

Low: 0.1–3.9

None: 0.0

(Based on standard CVSS scoring guidelines.) 

## 🤝 Contributing

Contributions are welcome!
To contribute:

Fork the project

Create a feature branch (git checkout -b feature/your‑idea)

Commit your changes (git commit -m "Add feature")

Push to your branch (git push)

Open a Pull Request

## 📬 Contact

Maintained by rifatsh3ikh

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
