import requests
import json
import os
from datetime import datetime

# Define where we want to save our raw data
DATA_FOLDER = "data"
OUTPUT_FILE = os.path.join(DATA_FOLDER, "hn_raw_data.json")

def fetch_hacker_news():
    print("Fetching Top Stories IDs from Hacker News...")
    
    # 1. Get the IDs of the current top articles
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(top_stories_url)
    
    # We will just grab the top 50 so our script runs fast
    story_ids = response.json()[:50] 
    
    stories = []
    print(f"Fetching details for the top {len(story_ids)} stories...")
    
    # 2. Loop through each ID and fetch the actual story details
    for i, story_id in enumerate(story_ids):
        item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        item_res = requests.get(item_url)
        item_data = item_res.json()
        
        if item_data:
            item_data['extracted_at'] = datetime.now().isoformat()
            stories.append(item_data)
        
        # Print a progress update every 10 items
        if (i + 1) % 10 == 0:
            print(f"Processed {i + 1}/{len(story_ids)} stories...")

    # 3. Save the list of stories into our local Data Lake (the data folder)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(stories, f, indent=4)
    
    print(f"Success! Saved {len(stories)} stories to {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_hacker_news()