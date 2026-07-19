import os

def cleanup_dynalite_duplicates():
    directory = "/home/ubuntu/Sydney-Automation-Co"
    all_files = os.listdir(directory)
    
    # Identify my new Dynalite pages
    my_pages = [f for f in all_files if f.endswith("-dynalite-repair-sydney.html")]
    
    # Identify other pages (excluding my new ones, index, test, etc.)
    existing_pages = [f for f in all_files if f.endswith(".html") and 
                      not f.endswith("-dynalite-repair-sydney.html") and 
                      f not in ["index.html", "test.html", "google_submission_guide.html"]]
    
    removed_count = 0
    for my_page in my_pages:
        # Extract suburb name from my page: "vaucluse-dynalite-repair-sydney.html" -> "vaucluse"
        suburb = my_page.replace("-dynalite-repair-sydney.html", "")
        
        # Check if any existing page contains this suburb name
        is_duplicate = False
        for existing in existing_pages:
            if suburb in existing.lower():
                is_duplicate = True
                break
        
        if is_duplicate:
            os.remove(os.path.join(directory, my_page))
            print(f"Removed duplicate: {my_page}")
            removed_count += 1
            
    print(f"Total Dynalite duplicates removed: {removed_count}")

if __name__ == "__main__":
    cleanup_dynalite_duplicates()
