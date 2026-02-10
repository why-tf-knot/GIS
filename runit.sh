#!/bin/bash
# Run all GIS data generation scripts
#
# This script executes the data generation pipeline:
# 1. Generate GeoJSON from CSV
# 2. Create ArcGIS Feature Collection

set -e  # Exit on error

echo "======================================"
echo "   GIS Data Generation Pipeline"
echo "======================================"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed or not in PATH"
    exit 1
fi

# Check if required files exist
if [ ! -f "locations.csv" ]; then
    echo "Error: locations.csv not found"
    exit 1
fi

echo "Step 1: Generating GeoJSON from CSV..."
echo "--------------------------------------"
python3 generate_geojson.py
echo ""

echo "Step 2: Creating ArcGIS Feature Collection..."
echo "--------------------------------------"
python3 create_arcgis_layer.py
echo ""

echo "======================================"
echo "   Pipeline Complete!"
echo "======================================"
echo ""
echo "Generated files:"
echo "  - space_agencies.geojson"
echo "  - space_agencies_feature_collection.json"
echo ""
echo "To view the interactive map, open map.html in a web browser"
