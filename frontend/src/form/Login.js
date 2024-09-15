import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";

export default function Login(props) {
    const [loginForm, setLoginform] = useState({
        username: "",
        password: "",
    });
    //const apiUrl = process.env.REACT_APP_API_URL;
    const navigate = useNavigate(); // Create a navigate function
    const onChangeForm = (label, event) => {
        switch (label) {
            case "username":
                setLoginform({ ...loginForm, username: event.target.value });
                break;
            case "password":
                setLoginform({ ...loginForm, password: event.target.value });
                break;
        }
    };
    const onSubmitHandler = async (event) => {
        event.preventDefault();
        console.log(loginForm);
        await axios
            .post("http://localhost:8000/auth/login", loginForm)
            .then((response) => {
                console.log(response);
                // add successfully notif
                toast.success(response.data.detail);
                // reload page after success login
                setTimeout(() => {
                    navigate("/?map")
                    props.setPage("map");
                }, 1000);

            })
            .catch((error) => {
                // add error notif
                console.log(error);
                toast.error(error.response.data.detail);
            });
    }
    return (
        <React.Fragment>
            <div className="min-h-screen bg-blue-400 flex justify-center items-center">
                <div className="py-12 px-12 bg-white rounded-2xl shadow-xl z-20">
                    <div>
                        <h1 className="text-3xl font-bold text-center mb-4 cursor-pointer">
                            Bem-vindo ao Budião App!
                        </h1>
                        <p className="w-80 text-center text-sm mb-8 font-semibold text-gray-700 tracking-wide cursor-pointer mx-auto">
                            Por favor, insira seu login:
                        </p>
                    </div>
                    <form onSubmit={onSubmitHandler}>
                        <div className="space-y-4">
                            <input
                                type="text"
                                placeholder="Usuário"
                                className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-blue-400"
                                onChange={(event) => {
                                    onChangeForm("username", event);
                                }}
                            />
                            <input
                                type="password"
                                placeholder="Senha"
                                className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-blue-400"
                                onChange={(event) => {
                                    onChangeForm("password", event);
                                }}
                            />
                        </div>
                        <div className="text-center mt-6">
                            <button
                                type="submit"
                                className="py-3 w-64 text-xl text-white bg-blue-400 rounded-2xl hover:bg-blue-300 active:bg-blue-500 outline-none"
                            >
                                Login
                            </button>
                            <p className="mt-4 text-sm">
                                Não possui login?{" "}
                                <Link
                                    to="/?register"
                                    onClick={() => {
                                        props.setPage("register");
                                    }}
                                >
                                    <span className="underline cursor-pointer">Registrar</span>
                                </Link>{" "}
                                <span className="underline cursor-pointer">Esqueceu a senha?</span>
                            </p>
                        </div>
                    </form>
                </div>
            </div>

        </React.Fragment >
    )
}