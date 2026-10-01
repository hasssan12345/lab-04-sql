import logging
import os

import mysql.connector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _connect():
    """Open a MySQL connection using env vars."""
    return mysql.connector.connect(
        host=os.environ["DBHOST"],
        user=os.environ["DBUSER"],
        password=os.environ["DBPASS"],
        database=os.environ["DBNAME"],
    )


def get_data_by_group(value):
    """Return rows from mock where the group column equals value."""
    logger.info("Querying group = %s", value)
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, `group`, last_name, email, gender, ip_address "
        "FROM mock WHERE `group` = %s",
        (value,),
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def plot_counts(groupby):
    """Count rows per distinct value of a column."""
    logger.info("Counting by %s", groupby)
    allowed = {"id", "group", "last_name", "email", "gender", "ip_address"}
    if groupby not in allowed:
        raise ValueError(f"Invalid column: {groupby}")
    conn = _connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT `{groupby}`, COUNT(*) FROM mock GROUP BY `{groupby}`")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def main():
    """Run the query demos."""
    print("Rows in group B:")
    for row in get_data_by_group("B"):
        print(row)
    print()
    print("Counts by gender:")
    for value, count in plot_counts("gender"):
        print(f"  {value}: {count}")


if __name__ == "__main__":
    main()
