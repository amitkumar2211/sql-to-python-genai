# app/validator.py

import sqlite3
import pandas as pd
import tempfile
import traceback

def run_sql_on_data(sql_code: str, csv_path: str) -> pd.DataFrame:
    """
    Run the original SQL on a sample dataset using SQLite.
    """
    try:
        df = pd.read_csv(csv_path)
        with tempfile.NamedTemporaryFile(suffix=".db") as tmp:
            conn = sqlite3.connect(tmp.name)
            df.to_sql("input_table", conn, index=False, if_exists="replace")
            result = pd.read_sql_query(sql_code, conn)
            conn.close()
        return result
    except Exception as e:
        print("SQL execution failed:", e)
        traceback.print_exc()
        return None

def run_python_on_data(python_code: str, csv_path: str) -> pd.DataFrame:
    """
    Execute AI-generated Python code and return output dataframe.
    """
    try:
        local_vars = {"pd": pd}
        exec(python_code, {}, local_vars)
        # Expect result in a variable named 'result' or return last dataframe
        result = local_vars.get("result")
        if result is None:
            # Try to find the last DataFrame assigned
            for var in reversed(local_vars.values()):
                if isinstance(var, pd.DataFrame):
                    return var
        return result
    except Exception as e:
        print("Python code execution failed:", e)
        traceback.print_exc()
        return None

def compare_outputs(sql_df: pd.DataFrame, py_df: pd.DataFrame) -> bool:
    """
    Compare two dataframes for equality (ignoring row order).
    """
    try:
        sql_sorted = sql_df.sort_index(axis=1).reset_index(drop=True)
        py_sorted = py_df.sort_index(axis=1).reset_index(drop=True)
        return sql_sorted.equals(py_sorted)
    except Exception as e:
        print("Comparison failed:", e)
        return False