import React from 'react'
import Menu from "./Menu";
import { Helmet } from "react-helmet";
import { MapContainer, TileLayer, Marker, Popup, Tooltip } from 'react-leaflet'
import 'leaflet/dist/leaflet.css';
import markerIconPng from "leaflet/dist/images/marker-icon.png"
import { Icon } from 'leaflet'

export default function Map(props) {

    const latitude = -8.08915093091523;
    const longitude = -34.79692857333338;

    return (
        <React.Fragment>
            <Menu />
            <Helmet>
                /* Javascript required - Leafleat */
                <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
                    integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
                    crossorigin=""></script>
            </Helmet>
            /* HTML id required - Leafleat */
            <div id="map">
                <MapContainer center={[latitude, longitude]} zoom={7} style={{ height: "100vh", width: "100vw" }}> /* if style is not set, Leafleat will not render */
                    <TileLayer
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                    <Marker position={[latitude, longitude]} icon={new Icon({ iconUrl: markerIconPng, iconSize: [25, 41], iconAnchor: [12, 41] })}>
                        <Popup>
                            Latitude: {latitude} <br/>
                            Longitude: {longitude}
                        </Popup>
                        <Tooltip sticky>
                            Latitude: {latitude} <br/>
                            Longitude: {longitude}
                        </Tooltip>
                    </Marker>
                </MapContainer>
            </div>
        </React.Fragment>
    )
}
