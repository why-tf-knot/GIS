# European Space Agencies GIS Map Layer

This repository contains GIS data and tools for mapping European Space Agency locations including ESA, CNES, and DLR facilities.

## 📍 Locations

The following locations are included in the map layer:

1. **ESA Headquarters** - 8-10 rue Mario Nikis, 75015 Paris, France
2. **ESA ESTEC (Tech Centre)** - Keplerlaan 1, 2201 AZ Noordwijk, Netherlands
3. **ESA ESOC (Operations)** - Robert-Bosch-Strasse 5, 64293 Darmstadt, Germany
4. **CNES Headquarters** - 2 Place Maurice Quentin, 75001 Paris, France
5. **DLR Headquarters** - Linder Höhe, 51147 Köln, Germany

## 📁 Files

- **locations.csv** - Raw location data in CSV format
- **space_agencies.geojson** - GeoJSON format (standard for GIS applications)
- **space_agencies_feature_collection.json** - ArcGIS Feature Collection format
- **map.html** - Interactive web map using ArcGIS JavaScript API
- **generate_geojson.py** - Script to generate GeoJSON from CSV
- **create_arcgis_layer.py** - Script to create ArcGIS-compatible files

## 🗺️ Using the Map Layer

### Option 1: View Interactive Web Map

Simply open `map.html` in a web browser to view an interactive map with all locations marked. The map includes:
- Color-coded markers for each organization (ESA, CNES, DLR)
- Interactive popups with location details
- Legend showing all organizations
- Zoom and pan controls

### Option 2: Import to ArcGIS Online

1. Go to [ArcGIS Online](https://www.arcgis.com)
2. Sign in to your account
3. Click **Content** > **Add Item** > **From your computer**
4. Upload `space_agencies.geojson` or `space_agencies_feature_collection.json`
5. The layer will be added to your content and can be used in web maps

### Option 3: Use with ArcGIS Pro

1. Open ArcGIS Pro
2. Add data to your map
3. Choose **Data** > **Add Data** > **Add Data from Path**
4. Browse to `space_agencies.geojson`
5. The layer will be added to your map

### Option 4: Use with QGIS

1. Open QGIS
2. Layer > Add Layer > Add Vector Layer
3. Browse to `space_agencies.geojson`
4. The layer will be added to your project

## 🔧 Scripts

### Generate GeoJSON from CSV

```bash
python3 generate_geojson.py
```

This script reads `locations.csv` and creates `space_agencies.geojson`.

### Create ArcGIS Feature Collection

```bash
python3 create_arcgis_layer.py
```

This script generates an ArcGIS-compatible Feature Collection JSON file that can be imported directly into ArcGIS Online.

## 📊 Data Format

The GeoJSON file follows the standard GeoJSON specification with Point geometries and includes these properties:
- organization
- location
- address
- postal_code
- city
- country
- name (formatted as "Organization - Location")

All coordinates are in WGS84 (EPSG:4326) format.

## 🚀 Requirements

- **For viewing the web map**: Modern web browser (Chrome, Firefox, Safari, Edge)
- **For Python scripts**: Python 3.6+
- **For ArcGIS API** (optional): `pip install arcgis`

## 📝 License

Public domain data for educational and mapping purposes.