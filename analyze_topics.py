import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.abspath(__file__))
TECH_LIB = os.path.join(ROOT, 'tech-library')

def analyze_tech_library():
    brands = []
    faults = []
    
    files = [f for f in os.listdir(TECH_LIB) if f.endswith('.html')]
    
    for f in files:
        # Extract brand/model from filename
        # Example: clipsal-c-bus-5000ct-stuck-on-channels-eastern-suburbs.html
        # Example: dynalite-ddbc1200-blinking-or-flashing-led-codes-eastern-suburbs.html
        
        parts = f.replace('.html', '').split('-')
        
        # Basic heuristic: first two parts are usually brand/model
        brand_part = []
        if 'clipsal' in parts:
            brand_part.append('Clipsal C-Bus')
        elif 'dynalite' in parts:
            brand_part.append('Dynalite')
        elif 'rapix' in parts:
            brand_part.append('RAPIX')
        elif 'dali' in parts:
            brand_part.append('DALI')
        
        if brand_part:
            brands.append(brand_part[0])
            
        # Extract fault/symptom
        # Heuristic: the parts after model but before suburb
        # e.g. stuck-on-channels, blinking-led-codes, etc.
        # This is tricky without a strict naming convention. 
        # Let's just look at common keywords.
        
    brand_counts = Counter(brands)
    
    print("=== Brand/Topic Distribution ===")
    for brand, count in brand_counts.items():
        print(f"{brand}: {count}")

    print("\n=== Missing High-Value Topics (Suggestions) ===")
    print("- Dynalite: expand beyond basic fault codes to 'Integration & Programming'")
    print("- RAPIX: expand to 'Emergency Lighting Fault Finding'")
    print("- DALI: expand to 'DALI Address Management & Control'")
    print("- C-Bus: expand to 'Advanced Troubleshooting & Logic'")

if __name__ == "__main__":
    analyze_tech_library()
