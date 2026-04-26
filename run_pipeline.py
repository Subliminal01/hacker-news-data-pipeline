import subprocess
import sys

def run_step(step_name, command, cwd=None):
    print(f"\n{'='*50}")
    print(f"🚀 STARTING: {step_name}")
    print(f"{'='*50}")
    
    # Run the command and wait for it to finish
    result = subprocess.run(command, shell=True, cwd=cwd)
    
    # If a step fails, stop the entire pipeline!
    if result.returncode != 0:
        print(f"\n❌ PIPELINE FAILED AT STEP: {step_name}")
        sys.exit(1)
        
    print(f"✅ SUCCESS: {step_name}\n")

def orchestrate():
    print("🤖 STARTING MASTER ELT PIPELINE...\n")
    
    # STEP 1: Extract (API to JSON)
    run_step(
        "Day 2: Extraction", 
        "python extraction/extract_hn.py"
    )
    
    # STEP 2: Load (JSON to Bronze DuckDB)
    run_step(
        "Day 3: Load Bronze", 
        "python transformation/load_bronze.py"
    )
    
    # STEP 3: Transform (dbt Silver & Gold)
    run_step(
        "Day 4: dbt Transformations", 
        "python ../run_dbt.py run",
        cwd="transformation/hn_models"
    )
    
    # STEP 4: Test (dbt Data Quality)
    run_step(
        "Day 5: dbt Testing", 
        "python ../run_dbt.py test",
        cwd="transformation/hn_models"
    )

    print("🎉 PIPELINE COMPLETED SUCCESSFULLY! YOUR WAREHOUSE IS UP TO DATE. 🎉")

if __name__ == "__main__":
    orchestrate()