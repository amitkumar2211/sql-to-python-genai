
# SQL to Python Converter using Google Gemini

This project helps you automatically convert legacy SQL scripts into clean, modular Python code using Google Gemini's public API (`google-generativeai` SDK). It is designed to speed up SQL migration efforts, help data teams modernize pipelines, and validate conversions using real data.

---

## 🚀 What This Tool Does

- Accepts SQL input from a `.sql` file or paste box
- Converts SQL into equivalent Python using Pandas or PySpark
- Uses Google Gemini to generate high-quality, readable Python code
- Validates the SQL and Python outputs on test data (via SQLite and Pandas)
- Provides a friendly Streamlit interface for non-technical users

---

## 🧠 Why It Matters

If you're modernizing legacy data platforms, you're probably drowning in old SQL scripts. Manually rewriting them into Python for Spark, Pandas, or dbt can take weeks.

This tool leverages generative AI to automate the boring parts, freeing engineers to focus on validation, optimization, and integration.

---

## ✨ Features

- ✅ Gemini API integration using `google-generativeai`
- ✅ Supports Pandas and PySpark as Python output
- ✅ Modular prompt-driven architecture
- ✅ Streamlit web UI
- ✅ SQL and Python output validator using SQLite + Pandas
- ✅ Downloadable Python code output
- ✅ Local `.env` configuration for API key security

---

## 🧪 How It Works

1. **Upload or paste SQL**
2. **Select output framework** (Pandas or PySpark)
3. **Click "Convert"** — Gemini handles the code generation
4. **Review and download** Python output
5. **(Optional) Validate** output against sample data to confirm logic accuracy

---

## 📁 Project Structure

```
sql-to-python-genai/
├── app/
│   ├── ui.py                  # Streamlit UI
│   ├── converter.py           # Gemini API interaction
│   ├── validator.py           # SQL vs Python output validator
│   └── config.py              # API key and settings
├── data/
│   └── sample_data.csv        # Sample data to validate transformations
├── tests/
│   └── test_cases.py          # Optional unit tests
├── prompts/
│   └── convert_sql_to_python.prompt  # Prompt template (optional)
├── .env.example               # Example .env file
├── requirements.txt           # Dependencies
└── README.md
```

---

## 🧰 Requirements

- Python 3.8+
- Google Gemini API key from [makersuite.google.com](https://makersuite.google.com/app/apikey)

---

## 🔧 Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/sql-to-python-genai.git
cd sql-to-python-genai
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Create `.env`**
```bash
cp .env.example .env
# Add your Gemini API key to .env
```

4. **Run the Streamlit app**
```bash
streamlit run app/ui.py
```

---

## 🔐 .env Example

```
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-1.5-pro
```

---

## ✅ Sample Validation Data

To use the validation feature, make sure your test CSV is saved as:

```
data/sample_data.csv
```

Ensure your SQL is written assuming the table name is `input_table`.

---

## 🧠 Prompt Engineering

The core logic uses carefully crafted prompts like:

> "You are a senior data engineer. Convert the following SQL into Python using the Pandas library. Preserve joins, filters, window functions, and output only valid Python code."

---

## 📌 Limitations

- Gemini outputs must define or return a DataFrame (preferably in `result`)
- Validation only supports flat queries for now (no procedural SQL)
- For production workloads, always manually review and test before deployment

---

## 📄 License

MIT

---

## 👋 Contributing

Feel free to fork, extend, or open issues. PRs welcome!

---

## 🔗 Author

Built by [Your Name]  
Inspired by real-world enterprise data migration needs.
