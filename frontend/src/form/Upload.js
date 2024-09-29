import React, { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
import { toast } from "react-toastify";

export default function Upload(props) {
  const [files, setFiles] = useState([]);
  const [uploadProgress, setUploadProgress] = useState({}); // To track the progress
  const [previews, setPreviews] = useState([]); // Store image previews
  const [messages, setMessages] = useState({}); // Store upload messages

  // Handle file drop
  const onDrop = useCallback((acceptedFiles) => {
    const filteredFiles = acceptedFiles.filter(file => file.name.split('.').pop().toLowerCase() === 'png');

    if (filteredFiles.length !== acceptedFiles.length) {
      toast.warn(`Somente imagens com extensão .png serão aceitas.`);
    }

    setFiles((prevFiles) => [...prevFiles, ...filteredFiles]);

    // Generate previews for PNG files only
    const previewUrls = filteredFiles.map((file) =>
      Object.assign(file, {
        preview: URL.createObjectURL(file), // Create a preview URL
      })
    );
    setPreviews((prevPreviews) => [...prevPreviews, ...previewUrls]);
  }, []);

  // Remove an individual file from the preview and files list
  const removeFile = (indexToRemove) => {
    setFiles((prevFiles) => prevFiles.filter((_, index) => index !== indexToRemove));
    setPreviews((prevPreviews) => prevPreviews.filter((_, index) => index !== indexToRemove));
  };

  // File upload handler with progress tracking and file type check
  const handleUpload = () => {
  
    const uploadPromises = files.map((file, index) => {
      const fileExtension = file.name.split('.').pop().toLowerCase();
  
      if (fileExtension === 'png') {
        const formData = new FormData();
        formData.append('file', file);
  
        // Return the axios request as a promise
        return axios.post('http://localhost:8000/sightings/upload', formData, {
          onUploadProgress: (progressEvent) => {
            const progress = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            setUploadProgress((prevProgress) => ({
              ...prevProgress,
              [index]: progress, // Update the progress of each file
            }));
          },
        })
        .then((response) => {
          // Track successful upload
          setMessages((prevMessages) => ({
            ...prevMessages,
            [index]: 'Enviado com sucesso',
          }));
        })
        .catch((error) => {
          // Track failed upload
          setMessages((prevMessages) => ({
            ...prevMessages,
            [index]: 'Falha ao enviar',
          }));
        });
      } else {
        return Promise.resolve(); // Skip non-png files
      }
    });
  
    // Wait for all uploads to complete
    Promise.all(uploadPromises).then(() => {
      const failedUploads = files.filter((_, index) => messages[index] === 'Falha ao enviar');
      const successfulUploads = files.filter((_, index) => messages[index] === 'Enviado com sucesso');
  
      // Show a single toast after all uploads are done
      if (failedUploads.length === 0) {
        toast.success(`Arquivo(s) enviado(s) com sucesso!`);
      } else if (successfulUploads.length > 0) {
        toast.warn(`Imagens parcialmente enviadas. Sucesso: ${successfulUploads.length} arquivo(s). Falha: ${failedUploads.length}  arquivo(s).`);
      } else {
        toast.error('Falhar ao enviar o(s) arquivo(s).');
      }
    });
  };
  
  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    multiple: true, // Enable multiple uploads
    accept: 'image/*', // Accept only image files
  });

  return (
    <React.Fragment>
      <div className="min-h-screen bg-blue-400 flex justify-center items-center">
      <div className="container mx-auto max-w-screen-lg h-full py-12 px-12 bg-white rounded-2xl shadow-xl z-20">
          <div className="upload-page">
            <div {...getRootProps()} style={{ border: '2px dashed #ccc', padding: '20px' }}>
              <input {...getInputProps()} />
              <p>Arraste as imagens aqui ou clique para selecioná-las</p>
            </div>
            {files.map((file, index) => {
              const progressBarColor = 'blue'; // Always blue for .png files

              return (
                <div key={index} style={{ marginTop: '20px' }}>
                  <p>{file.name}</p>
                  <progress
                    value={uploadProgress[index] || 0}
                    max="100"
                    style={{
                      width: '100%',
                      color: progressBarColor,
                      backgroundColor: progressBarColor,
                    }}
                  />
                  <div style={{ marginTop: '10px', display: 'flex', alignItems: 'center' }}>
                    {previews[index] && (
                      <>
                        <img
                          src={previews[index].preview}
                          alt={`preview ${index}`}
                          style={{ width: '100px', height: '100px', objectFit: 'cover' }}
                        />
                        <button
                          onClick={() => removeFile(index)}
                          style={{ marginLeft: '10px', color: 'red' }}
                        >
                          Remover
                        </button>
                      </>
                    )}
                  </div>
                  <div style={{ marginTop: '10px', color: 'green' }}>
                    {messages[index] && <p>{messages[index]}</p>}
                  </div>
                </div>
              );
            })}
            <button onClick={handleUpload} class="block mt-4 lg:inline-block text-sm px-4 py-2 leading-none border rounded text-blue-500 border-blue-500 hover:text-blue-500 hover:bg-white">
              Enviar
            </button>
            
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}