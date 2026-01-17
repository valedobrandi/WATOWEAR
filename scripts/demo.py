import requests
import json
import sys

def run_demo():
    print("--- Attempting to connect to WATOWEAR API ---")
    url = "http://localhost:8000/generate-outfit"

    wardrobe = [
        "Black Blazer", "White Dress Shirt", "Navy Chinos", "Leather Loafers",  # Formal
        "Oversized Graphic Hoodie", "Baggy Cargo Pants", "Jordan 1 Sneakers",   # Street
        "Compression Gym Tee", "Running Shorts", "Nike Pegasus Shoes",          # Sport
        "Floral Swim Trunks", "Linen Beach Shirt", "Rubber Flip-flops",         # Beach
        "Beige Trench Coat", "Sunglasses"                                       # Accessories
    ]
    
    dinner_payload = {
        "clothes": wardrobe,
        "occasion": "A trendy dinner at a high-end restaurant",
        "weather": "Chilly evening, 10°C",
        "style": "Sophisticated but Modern",
        "temperature": 0.5  # Lower temperature for a consistent, professional look
    }

    payload_gym = {
        "clothes": wardrobe,
        "occasion": "High-intensity interval training session",
        "weather": "Indoor gym, 20°C",
        "style": "Functional Athletic",
        "temperature": 0.3
    }

    payload_beach = {
        "clothes": wardrobe,
        "occasion": "Sunset drinks at a Mediterranean beach club",
        "weather": "Hot and sunny, 30°C",
        "style": "Summer Chic",
        "temperature": 0.7
    }

    for payload in [dinner_payload, payload_gym, payload_beach]:
        try:
            response = requests.post(url, json=payload, timeout=10)
            # This will show us the raw status if it's not 200
            print(f"Status Code: {response.status_code}")
        
            if response.status_code == 200:
                data = response.json()
                print("\n✨ OUTFIT GENERATED:")
                print(json.dumps(data, indent=2))
            else:
                print(f"❌ Server returned an error: {response.text}")
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection Failed: {e}")

if __name__ == "__main__":
    run_demo()
else:
    # This helps debug if the script is being imported instead of run
    print("Script was imported, not run directly.")