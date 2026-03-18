# 🚀 Antigravity User Comparison Tool

A powerful **Streamlit-based web application** to compare **All User Details** with **Running Users**, identify mismatches, and generate a complete comparison report.

---

## 📌 Overview

This tool helps operations and monitoring teams quickly:

* Compare user data across two files
* Identify missing or extra users
* Detect mismatches in **Allocation** and **Max Loss**
* Apply important data filters automatically

---

## ✨ Key Features

✅ Remove **Dealer Accounts (DLR ACC)**
✅ Exclude users where **algo = 0**
✅ Ignore **non-running servers**
✅ Identify:

* Users missing in Running File
* Users missing in Master File
* Allocation mismatches
* Max Loss mismatches

✅ Download full comparison report (CSV)

---

## 📂 Input Files

You need to upload **two files**:

### 1. All User Details File

* Format: `.xlsx` or `.csv`

### 2. Running Users File

* Format: `.xlsx` or `.csv`

---

## 📊 Required Columns

Both files should contain the following columns:

* `userId`
* `server`
* `algo`
* `allocation`
* `max_loss`

> ⚠️ Column names must match exactly (case-sensitive recommended).

---

## ⚙️ How It Works

1. Upload both files
2. Click **Start Comparison**
3. Tool automatically:

   * Cleans data using filters
   * Compares user lists
   * Matches values across files
4. Displays:

   * Unmatched users
   * Value mismatches
   * Summary metrics
5. Download final report

---

## 📈 Output Sections

* **Users in All Users File but NOT Running**
* **Users Running but NOT in Master File**
* **Allocation / Max Loss Mismatch**
* **Summary Metrics Dashboard**

---

## 💾 Export

Download full report using:

👉 **Download Full Comparison Report**

Includes:

* Missing users
* Extra users
* Value mismatches
* Status column for clarity

---

## 🖥️ Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/user-comparison-tool.git
cd user-comparison-tool
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run App

```bash
streamlit run app.py
```

---

## 🌐 Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Click **New App**
4. Select:

   * Repo: `user-comparison-tool`
   * Branch: `main`
   * File: `app.py`
5. Click **Deploy**

---

## 🧰 Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **OpenPyXL**

---

## 📌 Use Cases

* Trading operations monitoring
* User account validation
* Data reconciliation
* Risk management checks

---

## ⚠️ Notes

* Ensure clean data before upload
* Large files may take a few seconds to process
* Missing columns may cause errors

---

## 👨‍💻 Author

**Antigravity Monitoring Utility**

---

## 📜 License

This project is for internal and operational use.

---

## ⭐ Support

If you find this tool useful, consider giving it a ⭐ on GitHub!
