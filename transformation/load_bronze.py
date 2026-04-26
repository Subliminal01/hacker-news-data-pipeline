import duckdb
import os

# 1. Define our file paths
db_path = os.path.join("data", "warehouse.duckdb")
json_path = os.path.join("data", "hn_raw_data.json")

def load_data():
    print("Spinning up DuckDB Warehouse...")
    
    # 2. Connect to the database (This creates the file if it doesn't exist yet)
    conn = duckdb.connect(db_path)
    
    print("Loading JSON data into the Bronze table...")
    
    # 3. Create a table directly from the JSON file
    conn.execute(f"""
        CREATE OR REPLACE TABLE bronze_hackernews AS 
        SELECT * FROM read_json_auto('{json_path}')
    """)
    
    # 4. Verify it worked by running a SQL query!
    print("\n✅ Success! Here are the top 5 stories currently in your database:\n")
    
    # Fetch the results as a clean Pandas DataFrame so it prints nicely in the terminal
    query_result = conn.execute('SELECT title, score, "by" as author FROM bronze_hackernews LIMIT 5').fetchdf()
    print(query_result)
    
    # 5. Close the connection
    conn.close()

if __name__ == "__main__":
    load_data()