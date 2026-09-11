# Persistent Personal Expense Tracker

A modular, console-based financial ledger built with Python to track daily transactions, categorize expenditures, and generate dynamic analytical summaries.

---

## 🏗️ Core Application Architecture

This system demonstrates structured procedural backend programming split into isolated modular components:

* **Persistent Data Storage:** Automatic reading and appending to a local `expenses.csv` layer to ensure zero data loss across active script restarts.
* **Input Standardization:** Real-time data scrubbing that automatically infers timestamps for current actions or formats manual entries cleanly.
* **Aggregated Metrics Engine:** Dynamic mathematical calculations parsing data matrices on demand to present a detailed percentage-based financial overview.

---

## ⚙️ Implemented System Modules

* **Data Entry Hub:** Collects and standardizes numeric values alongside custom metadata categorization labels.
* **Fault-Tolerant Input Validation:** Wraps runtime user inputs inside error-proofing boundaries (`try-except`) to handle incorrect parameters without app crash events.
* **Analytical Matrix Summary:** Loops through structural flat records to isolate totals by specific accounts and present budget ratios.

---

## 🚀 Execution Visuals

### Main Navigation Menu
```text
==============================
💸 PERSONAL EXPENSE TRACKER
==============================
1. ➕ Add Expense
2. 📋 View Expenses
3. 📊 View Summary
4. ❌ Exit
```

### Generated Analytical Report
```text
--- 📊 Spending Summary ---
💰 Grand Total Spent: \$170.00

Breakdown by Category:
 🔹 Food: \$100.00 (58.8%)
 🔹 Shopping: \$50.00 (29.4%)
 🔹 Entertainment: \$20.00 (11.8%)
```

---

## 🛠️ Infrastructure Requirements
* Python 3.x+
* Core Standard Modules (`csv`, `os`, `datetime`)
