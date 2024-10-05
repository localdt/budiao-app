import React, { useState, useCallback } from 'react';
import axios from 'axios';
import { toast } from "react-toastify";

export default function Upload(props) {
  const [files, setFiles] = useState([])
  const position = [51.505, -0.09]
  const [uploadForm, setUploadForm] = useState({
    latitude: "",
    longitude: "",
  });

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    files.forEach(file => {
      formData.append('file_uploads', file);
    })
    formData.append("latitude", uploadForm.latitude)
    formData.append("longitude", uploadForm.longitude)

    await axios
      .post("http://localhost:8000/sightings/upload", formData)
      .then((response) => {
        console.log(response);
        toast.success(response.data.detail);
      })
      .catch((error) => {
        console.log(error);
        toast.error(error.response.data.detail);
      });

  }

  const handleFileInputChange = (event) => {
    setFiles(Array.from(event.target.files))
  }

  const onChangeForm = (label, event) => {
    switch (label) {
      case "latitude":
        setUploadForm({ ...uploadForm, latitude: event.target.value });
        break;
      case "longitude":
        setUploadForm({ ...uploadForm, longitude: event.target.value });
        break;
    }
  }

  return (
    <React.Fragment>
      <div className="min-h-screen bg-blue-400 flex justify-center items-center">
        <div className="container mx-auto max-w-screen-lg h-full py-12 px-12 bg-white rounded-2xl shadow-xl z-20">
          <div>
            <h1 className="text-3xl font-bold text-center mb-4 cursor-pointer">
              Upload
            </h1>
            <p className="w-100 text-center text-sm mb-8 font-semibold text-gray-700 tracking-wide cursor-pointer mx-auto">
              Informe a localização e selecione o(s) arquivo(s) que deseja enviar:
            </p>
          </div>
          <form onSubmit={handleSubmit}>
            <div className="space-y-4">
             
              <input placeholder="Latitude" className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-blue-400" type="text" onChange={(event) => { onChangeForm("latitude", event); }} />
              <input placeholder="Longitude" className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-blue-400" type="text" onChange={(event) => { onChangeForm("longitude", event); }} />

              <input className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-blue-400" type="file" onChange={handleFileInputChange} multiple />
            </div>
            <div className="text-center mt-6">
              <button type="submit" className="py-3 w-64 text-xl text-white bg-blue-400 rounded-2xl hover:bg-blue-300 active:bg-blue-500 outline-none">Enviar</button>
            </div>
          </form>
        </div>
      </div>
    </React.Fragment>
  );
}