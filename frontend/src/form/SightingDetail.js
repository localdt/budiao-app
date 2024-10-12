import React, { useState, useEffect } from "react";
import "react-datepicker/dist/react-datepicker.css";
import { useParams } from 'react-router-dom';
import axios from "axios";
import { toast } from "react-toastify";

export default function SightingDetail(props) {
    const baseURL = "http://localhost:8000/sightings/sightings/images/";
    const { id } = useParams();
    const [rows, setRows] = useState([]);
    console.log(id)
    useEffect(() => {
        fetchData();
    }, [id]);

    const fetchData = async () => {
        try {
            const response = await axios
                .get(`http://localhost:8000/sightings/files/${id}`)
                .then((response) => {
                    console.log("Pós resposta do endpoint:")
                    console.log(response.data.length);
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
                                <th className="border p-2">Imagem</th>
                                <th className="border p-2">Caminho da Imagem</th>
                                <th className="border p-2">Status</th>
                                <th className="border p-2">Resultado</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rows.length > 0 ? (
                                rows.map((row) => (
                                    <tr key={row.id} className="text-center">
                                        <td className="border p-2">{row.id}</td>
                                        <td className="border p-2">{row.path} </td>
                                        <td className="border p-2"><img 
                                                src={`${baseURL}${row.id}`} 
                                                alt="Imagem" 
                                                style={{ width: "100px", height: "100px", objectFit: "cover" }} 
                                            /></td>
                                        <td className="border p-2">Processando</td>
                                        <td className="border p-2">
                                           
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
