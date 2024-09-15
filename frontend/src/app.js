import "./App.css";
import React, { useState, useEffect } from "react";
import Forgot from "./form/Forgot";
import Login from "./form/Login";
import Register from "./form/Register";
import Home from "./Home";
import Map from "./form/Map";

function App() {
  const [page, setPage] = useState("login");
  const [token, setToken] = useState();

  useEffect(() => {
    const auth = localStorage.getItem("auth_token");
    setToken(auth);
  }, [token]);

  const chosePage = () => {
    if (page === "login") {
      return <Login setPage={setPage} />;
    }
    if (page === "forgot") {
      return <Forgot setPage={setPage} />;
    }
    if (page === "register") {
      return <Register setPage={setPage} />;
    }
    if (page === "map") {
      return <Map setPage={setPage} />;
    }
  };

  const pages = () => {
    
    if (token == null) {
      return (        
        <div>
            {chosePage()}
        </div>
      );
    } else {
      return <Home />;
    }
    
  };

  return <React.Fragment>{pages()}</React.Fragment>;
}

export default App;