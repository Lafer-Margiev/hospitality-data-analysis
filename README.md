# 📊 Hospitality Labor Analysis Tool
**Strategic Operations | Python Data Processing | WGU Computer Science**

## 🎯 Project Objective
This tool bridges the gap between hospitality management and data science. It automates the analysis of "Prime Cost" by ingesting raw POS sales data and calculating labor efficiency against industry-standard benchmarks.

## 🚀 Business Impact
In high-volume NYC environments (like **The Fulton** or **Morimoto**), labor is the most volatile variable. This script:
* **Identifies Leakage:** Flags shifts exceeding the 18% labor target.
* **Automates Reporting:** Replaces manual spreadsheet calculations with an idempotent Python script.
* **Supports Scalability:** Can be expanded to ingest weekly or monthly enterprise-level datasets.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Core Logic:** Functional programming for status flagging and data parsing.
* **Data Handling:** CSV (Comma Separated Values) for POS export compatibility.

## 📋 Features
- **Dynamic Logic:** Custom `calculate_labor_percentage` function.
- **Conditional Formatting:** Automated terminal output with `✅ OPTIMAL` or `⚠️ HIGH` status indicators.
- **Data Ingestion:** Reads from `mock_sales_data.csv` to simulate a real-world POS data export.

## 💻 Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate to the directory:**
   ```bash
   cd hospitality-data-analysis
   ```
3. **Execute the analysis:**
   ```bash
   python analyze_labor.py
   ```

---
**Author:** Lafer Margiev – CS Student @ WGU | Operations Manager @ Jean-Georges
