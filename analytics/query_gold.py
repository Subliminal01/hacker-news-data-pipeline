import duckdb
import os

# Point to our existing Data Warehouse
db_path = os.path.join("data", "warehouse.duckdb")

def analyze_data():
    print("Connecting to the Data Warehouse...\n")
    conn = duckdb.connect(db_path)
    
    # Query our new Gold layer
    query = """
        SELECT author, total_stories, total_score 
        FROM gold_top_authors 
        ORDER BY total_score DESC 
        LIMIT 5
    """
    
    # Fetch the results as a Pandas DataFrame for clean printing
    results = conn.execute(query).fetchdf()
    
    print("🏆 TOP HACKER NEWS AUTHORS 🏆")
    print("-" * 35)
    print(results)
    print("-" * 35)
    
    conn.close()

if __name__ == "__main__":
    analyze_data()