import pandas as pd

def get_top_students(conn):
    query = """
    SELECT name, Average
    FROM Students
    ORDER BY Average DESC
    LIMIT 3
    """
    return pd.read_sql(query, conn)

def Class_average(conn):
    query = """
    SELECT class,
           AVG(Average) AS total_avg
    FROM Students
    GROUP BY class
    """
    return pd.read_sql(query, conn)
