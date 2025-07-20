
import pandas as pd
from app.validator import run_sql_on_data, run_python_on_data, compare_outputs

def test_sql_python_equivalence():
    sql = """
    SELECT region, AVG(sales) as avg_sales
    FROM input_table
    WHERE product_type = 'Electronics'
    GROUP BY region;
    """

    python_code = """
import pandas as pd
df = pd.read_csv('data/sample_data.csv')
df = df[df['product_type'] == 'Electronics']
result = df.groupby('region')['sales'].mean().reset_index()
result = result.rename(columns={'sales': 'avg_sales'})
    """

    csv_path = 'data/sample_data.csv'

    sql_result = run_sql_on_data(sql, csv_path)
    py_result = run_python_on_data(python_code, csv_path)

    assert sql_result is not None, "SQL result is None"
    assert py_result is not None, "Python result is None"
    assert compare_outputs(sql_result, py_result), "SQL and Python outputs do not match"
