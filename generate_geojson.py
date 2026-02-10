#!/usr/bin/env python3
"""
Generate GeoJSON file from location data for ArcGIS mapping.
"""

import json
import csv


def generate_geojson():
    """
    Read locations from CSV and generate GeoJSON format suitable for ArcGIS.
    """
    features = []
    
    with open('locations.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        float(row['Longitude']),
                        float(row['Latitude'])
                    ]
                },
                "properties": {
                    "organization": row['Organization'],
                    "location": row['Location'],
                    "address": row['Address'],
                    "postal_code": row['Postal Code'],
                    "city": row['City'],
                    "country": row['Country'],
                    "name": f"{row['Organization']} - {row['Location']}"
                }
            }
            features.append(feature)
    
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    
    with open('space_agencies.geojson', 'w', encoding='utf-8') as f:
        json.dump(geojson, f, indent=2)
    
    print(f"Generated GeoJSON with {len(features)} locations")
    print("Output file: space_agencies.geojson")


if __name__ == '__main__':
    generate_geojson()
