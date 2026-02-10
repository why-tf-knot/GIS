#!/usr/bin/env python3
"""
Create ArcGIS Feature Layer from GeoJSON data.

This script demonstrates how to publish the space agencies data 
as an ArcGIS Feature Layer using the ArcGIS API for Python.

Requirements:
    pip install arcgis

Note: Requires ArcGIS Online or ArcGIS Enterprise credentials.
"""

import json
from typing import Dict, List


def load_geojson(filepath: str = 'space_agencies.geojson') -> Dict:
    """Load GeoJSON data from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def create_feature_layer_with_arcgis_api():
    """
    Create an ArcGIS Feature Layer using ArcGIS API for Python.
    
    This function demonstrates the workflow for publishing data to ArcGIS Online.
    Uncomment and run if you have arcgis package installed and valid credentials.
    """
    try:
        from arcgis.gis import GIS
        from arcgis.features import FeatureLayerCollection
        
        # Load GeoJSON data
        geojson_data = load_geojson()
        
        # Connect to ArcGIS Online (or your portal)
        # Replace with your credentials or use 'home' for default profile
        # gis = GIS("https://www.arcgis.com", "username", "password")
        # Or use: gis = GIS("home")  # if you have a profile configured
        
        print("To publish to ArcGIS Online:")
        print("1. Uncomment the GIS connection line above")
        print("2. Add your ArcGIS Online credentials")
        print("3. Run this script")
        print("\nAlternatively:")
        print("- Upload space_agencies.geojson to ArcGIS Online manually")
        print("- Or use map.html for a standalone web map")
        
    except ImportError:
        print("ArcGIS API for Python not installed.")
        print("Install with: pip install arcgis")
        print("\nAlternative options:")
        print("1. Use the generated GeoJSON file (space_agencies.geojson)")
        print("2. Upload to ArcGIS Online via web interface")
        print("3. Open map.html in a web browser for interactive map")


def create_feature_collection() -> Dict:
    """
    Create an ArcGIS Feature Collection JSON structure.
    
    This format can be used directly with ArcGIS Online's Add Data functionality.
    """
    geojson_data = load_geojson()
    
    feature_collection = {
        "layers": [
            {
                "layerDefinition": {
                    "name": "Space Agency Locations",
                    "geometryType": "esriGeometryPoint",
                    "objectIdField": "OBJECTID",
                    "fields": [
                        {
                            "name": "OBJECTID",
                            "type": "esriFieldTypeOID",
                            "alias": "OBJECTID"
                        },
                        {
                            "name": "organization",
                            "type": "esriFieldTypeString",
                            "alias": "Organization",
                            "length": 50
                        },
                        {
                            "name": "location",
                            "type": "esriFieldTypeString",
                            "alias": "Location",
                            "length": 100
                        },
                        {
                            "name": "address",
                            "type": "esriFieldTypeString",
                            "alias": "Address",
                            "length": 200
                        },
                        {
                            "name": "city",
                            "type": "esriFieldTypeString",
                            "alias": "City",
                            "length": 100
                        },
                        {
                            "name": "country",
                            "type": "esriFieldTypeString",
                            "alias": "Country",
                            "length": 100
                        }
                    ],
                    "spatialReference": {
                        "wkid": 4326
                    }
                },
                "featureSet": {
                    "geometryType": "esriGeometryPoint",
                    "spatialReference": {
                        "wkid": 4326
                    },
                    "features": []
                }
            }
        ]
    }
    
    # Convert GeoJSON features to ArcGIS features
    for idx, feature in enumerate(geojson_data['features']):
        coords = feature['geometry']['coordinates']
        props = feature['properties']
        
        arcgis_feature = {
            "attributes": {
                "OBJECTID": idx + 1,
                "organization": props.get("organization", ""),
                "location": props.get("location", ""),
                "address": props.get("address", ""),
                "city": props.get("city", ""),
                "country": props.get("country", "")
            },
            "geometry": {
                "x": coords[0],
                "y": coords[1]
            }
        }
        
        feature_collection["layers"][0]["featureSet"]["features"].append(arcgis_feature)
    
    return feature_collection


def save_feature_collection(filepath: str = 'space_agencies_feature_collection.json'):
    """Save ArcGIS Feature Collection to file."""
    feature_collection = create_feature_collection()
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(feature_collection, f, indent=2)
    
    print(f"Created ArcGIS Feature Collection: {filepath}")
    print(f"Features: {len(feature_collection['layers'][0]['featureSet']['features'])}")
    print("\nYou can import this file to ArcGIS Online:")
    print("1. Go to ArcGIS Online")
    print("2. Click 'Add' -> 'Add Layer from File'")
    print("3. Upload this JSON file")


def print_summary():
    """Print summary of available data files."""
    geojson_data = load_geojson()
    
    print("\n=== Space Agencies Data Summary ===")
    print(f"Total locations: {len(geojson_data['features'])}")
    print("\nLocations:")
    
    for feature in geojson_data['features']:
        props = feature['properties']
        coords = feature['geometry']['coordinates']
        print(f"\n- {props['name']}")
        print(f"  Address: {props['address']}, {props['city']}, {props['country']}")
        print(f"  Coordinates: {coords[1]:.6f}, {coords[0]:.6f}")


if __name__ == '__main__':
    print("=== ArcGIS Feature Layer Generator ===\n")
    
    # Create Feature Collection JSON
    save_feature_collection()
    
    # Print summary
    print_summary()
    
    # Show API usage info
    print("\n=== Publishing to ArcGIS ===")
    create_feature_layer_with_arcgis_api()
