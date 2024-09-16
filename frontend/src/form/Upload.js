import React, { useState } from "react";
import { Link } from "react-router-dom";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { toast } from "react-toastify";

export default function Upload(props) {

    return (
        <React.Fragment>
            <div className="min-h-screen bg-blue-400 flex justify-center items-center">
                <div className="py-12 px-12 bg-white rounded-2xl shadow-xl z-20">
                    <p>upload</p>
                </div>
            </div>
        </React.Fragment >
    )
}