import requests
import json

urls = {
    "current": "https://mars.nasa.gov/mmgis-maps/MSL/Layers/json/MSL_waypoints_current.json",
    "all_waypoints": "https://mars.nasa.gov/mmgis-maps/MSL/Layers/json/MSL_waypoints.json",
    "traverse": "https://mars.nasa.gov/mmgis-maps/MSL/Layers/json/MSL_traverse.json"
}

for name, url in urls.items():
    try:
        # Fetch raw NASA data
        data = requests.get(url).json()
        
        # CRITICAL FIX: Strip out the custom Mars CRS that breaks ArcGIS Online
        if "crs" in data:
            del data["crs"]
            
        # Save the scrubbed, valid GeoJSON file
        with open(f"{name}.geojson", "w") as f:
            json.dump(data, f, indent=2)
            
        print(f"Successfully scrubbed and saved {name}.geojson")
    except Exception as e:
        print(f"Failed to process {name}: {e}")
