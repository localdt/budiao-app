import React, { useEffect, useState } from 'react'
import Menu from "./Menu";
import { Helmet } from "react-helmet";
import { MapContainer, TileLayer, Marker, Popup, Tooltip } from 'react-leaflet'
import 'leaflet/dist/leaflet.css';
import markerIconPng from "leaflet/dist/images/marker-icon.png"
import { Icon } from 'leaflet'
import axios from "axios";
import { toast } from "react-toastify";

export default function Map(props) {
    useEffect(() => {
        fetchData();
    }, []);
    const [pins, setPins] = useState([])
    const fetchData = async () => {
        try {
            const response = await axios
                .get(`http://localhost:8000/sightings/sightings?skip=0&limit=100`)
                .then((response) => {
                    console.log(response.data.length);
                    console.log(response.data);
                    console.log(response.data);
                    setPins(response.data);
                })
                .catch((error) => {
                    console.log(error);
                    toast.error(error.response.data.detail || "Error fetching data");
                });
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };

    const latitude = -18.715765;
    const longitude = -36.496786;

    return (
        <React.Fragment>
            <Menu />
            <Helmet>
                {/* Javascript required - Leafleat */}
                <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
                    integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
                    crossorigin=""></script>
            </Helmet>
            {/* HTML id required - Leafleat */}
            <div id="map">
                <MapContainer center={[latitude, longitude]} zoom={5} style={{ height: "100vh", width: "100vw" }}> {/* if style is not set, Leafleat will not render */}
                    <TileLayer
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                    {pins.length > 0 ? (
                        pins.map((pin) => (
                            <Marker position={[pin.latitude, pin.longitude]} icon={new Icon({ iconUrl: markerIconPng, iconSize: [25, 41], iconAnchor: [12, 41] })}>
                                <Popup>
                                    Avistamento: {pin.id} <br />
                                    Latitude: {pin.latitude} <br />
                                    Longitude: {pin.longitude}
                                </Popup>
                                <Tooltip sticky>
                                    Avistamento: {pin.id} <br />
                                    Latitude: {pin.latitude} <br />
                                    Longitude: {pin.longitude}
                                </Tooltip>
                            </Marker>
                        ))
                    ) : (
                        <Marker position={[latitude, longitude]} icon={new Icon({ iconUrl: markerIconPng, iconSize: [25, 41], iconAnchor: [12, 41] })}>
                            <Popup>
                                Latitude: {latitude} <br />
                                Longitude: {longitude}
                            </Popup>
                            <Tooltip sticky>
                                Latitude: {latitude} <br />
                                Longitude: {longitude}
                            </Tooltip>
                        </Marker>
                    )}
                </MapContainer>
            </div>
        </React.Fragment>
    )
}
