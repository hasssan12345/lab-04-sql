import logging
import os

import mysql.connector
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TYPE_MAPPING = {
    "int64": "BIGINT",
    "int32": "INT",
    "float64": "DOUBLE",
    "bool": "TINYINT(1)",
    "datetime64[ns]": "DATETIME",
    "object": "VARCHAR(255)",
    "string": "VARCHAR(255)",
}


def read_data(filename):
    """Load the CSV into a DataFrame."""
    df = pd.read_csv(filename)
    logger.info("Read %d rows", len(df))
    return df


def clean_data(data):
    """Remove rows with missing values."""
    before = len(data)
    data = data.dropna().reset_index(drop=True)
    logger.info("Cleaned %d -> %d", before, len(data))
    return data


def _mysql_type_for(dtype):
    """Map pandas dtype to a MySQL type."""
    return TYPE_MAPPING.get(str(dtype), "VARCHAR(255)")


def load_data(data, table):
    """Create the table and insert every row."""
    host = os.environ["DBHOST"]
    user = os.environ["DBUSER"]
    password = os.environ["DBPASS"]
    database = os.environ["DBNAME"]
    try:
        conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        cursor = conn.cursor()
        columns_sql = []
        for col, dtype in data.dtypes.items():
            columns_sql.append(f"`{col}` {_mysql_type_for(dtype)}")
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS `{table}` ({', '.join(columns_sql)})"
        )
        cols = list(data.columns)
        placeholders = ", ".join(["%s"] * len(cols))
        col_names = ", ".join(f"`{c}`" for c in cols)
        insert_stmt = f"INSERT INTO `{table}` ({col_names}) VALUES ({placeholders})"
        rows = [tuple(row) for row in data.itertuples(index=False, name=None)]
        cursor.executemany(insert_stmt, rows)
        conn.commit()
        logger.info("Inserted %d rows", cursor.rowcount)
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        logger.error("MySQL error: %s", err)
        raise


def main():
    """Read, clean, and load MOCK_DATA.csv into mock."""
    df = read_data("MOCK_DATA.csv")
    df = clean_data(df)
    load_data(df, "mock")


if __name__ == "__main__":
    main()
