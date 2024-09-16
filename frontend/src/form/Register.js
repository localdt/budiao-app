import React, { useState } from "react";
import { Link } from "react-router-dom";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { toast } from "react-toastify";

export default function Register(props) {

    const apiUrl = process.env.REACT_APP_API_URL;

    const options = [
        { value: "", label: "Selecione o gênero" },
        { value: "Male", label: "Masculino" },
        { value: "Female", label: "Feminino" },
        { value: "Other", label: "Outro" },
    ];
    // Register Form
    const [formRegister, setFormRegister] = useState({
        name: "",
        username: "",
        email: "",
        phone_number: "",
        password: "",
        birth: "",
        sex: "",
        profile: "",
    });
    //    default value datepicker
    const [birthDate, setBirthDate] = useState(null);

    // convert format date to string
    const formatDate = (date) => {
        let d = new Date(date),
            month = "" + (d.getMonth() + 1),
            day = "" + d.getDate(),
            year = d.getFullYear();

        if (month.length < 2) month = "0" + month;
        if (day.length < 2) day = "0" + day;
        return [day, month, year].join("-");
    };
    const onChangeForm = (label, event) => {
        switch (label) {
            case "name":
                setFormRegister({ ...formRegister, name: event.target.value });
                break;
            case "username":
                setFormRegister({ ...formRegister, username: event.target.value });
                break;
            case "email":
                // email validation
                const email_validation = /\S+@\S+\.\S+/;
                if (email_validation.test(event.target.value)) {
                    setFormRegister({ ...formRegister, email: event.target.value });
                }
                break;
            case "phone_number":
                setFormRegister({ ...formRegister, phone_number: event.target.value });
                break;
            case "password":
                setFormRegister({ ...formRegister, password: event.target.value });
                break;
            case "sex":
                setFormRegister({ ...formRegister, sex: event.target.value });
                break;
            case "birth":
                setBirthDate(event);
                setFormRegister({ ...formRegister, birth: formatDate(event) });
                break;
            default:

        }
    };

    //   Submit handler
    const onSubmitHandler = async (event) => {
        event.preventDefault();
        console.log(formRegister);
        console.log({ apiUrl })
        toast.success("test");
    }


    return (
        <React.Fragment>
            <div className="min-h-screen bg-blue-400 flex justify-center items-center">
                <div className="py-12 px-12 bg-white rounded-2xl shadow-xl z-20">
                    <div>
                        <h1 className="text-3xl font-bold text-center mb-4 cursor-pointer">
                            Criar uma conta
                        </h1>
                        <p className="w-80 text-center text-sm mb-8 font-semibold text-gray-700 tracking-wide cursor-pointer mx-auto">
                            Bem Vindo ao Budiao-App!
                        </p>
                    </div>
                    <form onSubmit={onSubmitHandler}>
                        <div className="space-y-4">
                            <input
                                type="text"
                                placeholder="Nome completo"
                                className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-blue-400"
                                onChange={(event) => {
                                    onChangeForm("name", event);
                                }}
                            />
                            <DatePicker
                                className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-blue-400"
                                wrapperClassName="w-full"
                                dateFormat="dd-MM-yyyy"
                                placeholderText="Data de aniversário"
                                selected={birthDate}
                                onChange={(event) => {
                                    onChangeForm("birth", event);
                                }}
                            />
                            <select
                                value={formRegister.sex}
                                className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                onChange={(event) => {
                                    onChangeForm("sex", event);
                                }}
                            >
                                {options.map((data) => {
                                    if (data.value === "") {
                                        return (
                                            <option key={data.label} value={data.value} disabled>
                                                {data.label}
                                            </option>
                                        );
                                    } else {
                                        return (
                                            <option key={data.label} value={data.value}>
                                                {data.label}
                                            </option>
                                        );
                                    }
                                })}
                            </select>
                            <input
                                type="email"
                                placeholder="Email"
                                className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-blue-400"
                                onChange={(event) => {
                                    onChangeForm("email", event);
                                }}
                            />
                            <input
                                type="password"
                                placeholder="Senha"
                                className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-blue-400"
                            />
                        </div>
                        <div className="text-center mt-6">
                            <button
                                type="submit"
                                className="py-3 w-64 text-xl text-white bg-blue-400 rounded-2xl hover:bg-blue-300 active:bg-blue-500 outline-none"
                            >
                                Criar conta
                            </button>
                            <p className="mt-4 text-sm">
                                Já possui uma conta?{" "}
                                <Link
                                    to="/login"
                                    onClick={() => {
                                        props.setPage("login");
                                    }}
                                >
                                    <span className="underline cursor-pointer">Logar</span>
                                </Link>
                                {" "}
                            </p>
                        </div>
                    </form>
                </div>
            </div>
        </React.Fragment >
    )
}