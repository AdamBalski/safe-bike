import { ExpoLeaflet, MapMarker, MapShape } from 'expo-leaflet'
import React, { useEffect, useState } from 'react'
import axios from 'axios';
const baseUrl = '10.250.160.126';
const fetchingPort = '8000';
type LatLngLiteral = { lat: number, lng: number }
import {
  ActivityIndicator,
  Alert,
  Button,
  Platform,
  SafeAreaView,
  StyleSheet,
  Text,
  View,
} from 'react-native'
import { MapLayer } from 'expo-leaflet'

const mapLayers: Array<MapLayer> = [
  {
    attribution:
      '&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    baseLayerIsChecked: true,
    baseLayerName: 'OpenStreetMap',
    layerType: 'TileLayer',
    url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  },
  {
    baseLayerIsChecked: true,
    baseLayer: true,
    baseLayerName: 'Mapbox',
    layerType: 'TileLayer',
    url: `https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoid2hlcmVzbXl3YXZlcyIsImEiOiJjanJ6cGZtd24xYmU0M3lxcmVhMDR2dWlqIn0.QQSWbd-riqn1U5ppmyQjRw`,
  },
]

const mapOptions = {
  attributionControl: false,
  zoomControl: Platform.OS === 'web',
}

const initialPosition = {
  lat: 52.2297,
  lng: 21.0117,
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  header: {
    height: 60,
    backgroundColor: 'dodgerblue',
    paddingHorizontal: 10,
    paddingTop: 30,
    width: '100%',
  },
  headerText: {
    color: 'white',
    fontSize: 18,
    fontWeight: '600',
  },
  mapControls: {
    backgroundColor: 'rgba(255,255,255,.5)',
    borderRadius: 5,
    bottom: 25,
    flexDirection: 'row',
    justifyContent: 'space-between',
    left: 0,
    marginHorizontal: 10,
    padding: 7,
    position: 'absolute',
    right: 0,
  },
  mapButton: {
    alignItems: 'center',
    height: 42,
    justifyContent: 'center',
    width: 42,
  },
  mapButtonEmoji: {
    fontSize: 28,
  },
})

export default function App() {
  axios({
    method: 'get',
    url: `${baseUrl}:${fetchingPort}`,
  }).then((response) => {
    console.log(response.data)    ;
  });
  const [zoom, setZoom] = useState(7)
  const [mapCenterPosition, setMapCenterPosition] = useState(initialPosition)
  const points: LatLngLiteral[] = [
    { lat: 52.2297, lng: 21.0117 },
    { lat: 53.2297, lng: 22.0117 },
    { lat: 50.57304, lng: 21.67937 }
  ]

  let mapMarkers: MapMarker[] = []
  let routeLine: MapShape = {
    shapeType: 'polyline',
    color: 'black',
    id: String(0),
    positions: [],
  }

  let start: MapMarker = {
    id: String(0),
    position: points[0],
    icon: '📍',
    size: [32, 32],
  }
  mapMarkers.push(start)
  let end: MapMarker = {
    id: String(1),
    position: points[points.length - 1],
    icon: '📍',
    size: [32, 32],
  }
  mapMarkers.push(end)

  for (let i = 0; i < points.length; i++) {
    routeLine.positions.push(points[i])
  }

  let mapShapes: Array<MapShape> = [
    routeLine,
  ]

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerText}>showing route</Text>
      </View>
      <View style={{ flex: 1, position: 'relative' }}>
        <ExpoLeaflet
          loadingIndicator={() => <ActivityIndicator />}
          mapShapes={mapShapes}
          mapCenterPosition={mapCenterPosition}
          mapLayers={mapLayers}
          mapMarkers={mapMarkers}
          mapOptions={mapOptions}
          maxZoom={20}
          onMessage={(message) => {
            switch (message.tag) {
              case 'onMapMarkerClicked':
                Alert.alert(
                  `Map Marker Touched, ID: ${message.mapMarkerId || 'unknown'}`,
                )
                break
              case 'onMapClicked':
                Alert.alert(
                  `Map Touched at:`,
                  `${message.location.lat}, ${message.location.lng}`,
                )
                break
              case 'onMoveEnd':
                setMapCenterPosition(message.mapCenter)
                break
              case 'onZoomEnd':
                setZoom(message.zoom)
                break
              default:
                if (['onMove'].includes(message.tag)) {
                  return
                }
                console.log(message)
            }
          }}
          zoom={zoom}
        />
      </View>
      <View style={{flexDirection:"row"}}>
      <Button
        onPress={() => {
          setMapCenterPosition(initialPosition)
          setZoom(7)
        }}
        title="Reset Map"
      />
      <Button
        onPress={() => {
          axios.get(`${baseUrl}:${fetchingPort}`).then((response) => {
            console.log(response.data);
          })
        }}
        title="Get Route"
      />
      </View>
    </SafeAreaView>
  )
}
