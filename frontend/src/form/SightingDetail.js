import React, { useState, useEffect } from "react";
import "react-datepicker/dist/react-datepicker.css";
import { useParams } from 'react-router-dom';
import axios from "axios";
import { toast } from "react-toastify";

export default function SightingDetail(props) {
    const { id } = useParams();
    console.log(id)
    return (
        <React.Fragment>
            <div className="min-h-screen bg-blue-400 flex justify-center items-center">
                <div className="py-12 px-12 min-w-fit bg-white rounded-2xl shadow-xl z-20">
                    <div>
                        <h1 className="text-3xl font-bold text-center mb-4">
                            Detalhes do Avistamento
                        </h1>
                       
                    </div>
                   
                </div>
            </div>
        </React.Fragment>
    );
}
