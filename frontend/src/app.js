import "./App.css";
import React, { useState, useEffect } from "react";
import { Route, Routes } from 'react-router-dom'
import Forgot from "./form/Forgot";
import Login from "./form/Login";
import Register from "./form/Register";
import Map from "./form/Map";
import Upload from "./form/Upload";

function App() {
  return (
    <div>
      <Routes>
        <Route path='/' element={<Login/>} />
        <Route path='/login' element={<Login/>} />
        <Route path='/register' element={<Register/>}/>
        <Route path='/map' element={<Map/>}/>
        <Route path='/upload' element={<Upload/>}/>
        <Route/>
      </Routes>
    </div>
  )
}

export default App;