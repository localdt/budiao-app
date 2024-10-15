import React, { useState, useEffect } from "react";
import "react-datepicker/dist/react-datepicker.css";
import axios from "axios";
import { toast } from "react-toastify";
import { useNavigate  } from 'react-router-dom'
import Moment from 'moment';

export default function Sighting(props) {
    const moment = require('moment-timezone');
    const [rows, setRows] = useState([]);
    const navigate = useNavigate();
    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const response = await axios
                .get(`http://localhost:8000/sightings/sightings?skip=0&limit=100`)
                .then((response) => {
                    console.log(response.data.length);
                    console.log(response.data);
                    console.log(response.data);
                    setRows(response.data);
                })
                .catch((error) => {
                    console.log(error);
                    toast.error(error.response.data.detail || "Error fetching data");
                });
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };

    const handleEditRow = (id) => {
        navigate(`/sighting-detail/${id}`);
    };

    return (
        <React.Fragment>
            <div className="min-h-screen bg-blue-400 flex justify-center items-center">
                <div className="py-12 px-12 min-w-fit bg-white rounded-2xl shadow-xl z-20">
                    <div>
                        <h1 className="text-3xl font-bold text-center mb-4">
                            Meus Avistamentos
                        </h1>
                       
                    </div>
                    <table className="min-w-full table-auto bg-white border-collapse border border-gray-200">
                        <thead>
                            <tr className="bg-gray-100">
                                <th className="border p-2">ID</th>
                                <th className="border p-2">Longitude</th>
                                <th className="border p-2">Latitude</th>
                                <th className="border p-2">Data/Hora</th>
                             
                                <th className="border p-2">Imagens</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rows.length > 0 ? (
                                rows.map((row) => (
                                    <tr key={row.id} className="text-center">
                                        <td className="border p-2">{row.id}</td>
                                        <td className="border p-2">{row.longitude}</td>
                                        <td className="border p-2">{row.latitude}</td>
                                       
                                        <td className="border p-2">{moment(row.created).tz('America/Sao_Paulo').format('DD/MM/YYYY HH:mm:ss')}</td>
                                      
                                        <td className="border p-2">
                                            <button id="imagens"
                                                className="bg-yellow-500 text-white p-1 rounded mr-2"
                                                onClick={() => handleEditRow(row.id)}
                                            >
                                                Imagens
                                            </button>
                                        </td>
                                    </tr>
                                ))
                            ) : (
                                <tr>
                                    <td colSpan="3" className="border p-2 text-center">
                                        No data available
                                    </td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
            </div>
        </React.Fragment>
    );
}
