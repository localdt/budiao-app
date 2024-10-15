import React from "react";
import { Link } from "react-router-dom";
export default function Menu(props) {
    return (
        <React.Fragment>
            <div>
                <nav class="flex items-center justify-between flex-wrap bg-blue-400 p-6">
                    <div class="flex items-center flex-shrink-0 text-white mr-6">

                        <span class="font-semibold text-xl tracking-tight">Budião App</span>
                    </div>
                    <div class="block lg:hidden">
                        <button class="flex items-center px-3 py-2 border rounded text-blue-200 border-blue-400 hover:text-white hover:border-white">
                            <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" /></svg>
                        </button>
                    </div>
                    <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
                        <div class="text-sm lg:flex-grow">
                            
                            <Link
                                to="/upload"
                                onClick={() => {
                                    props.setPage("upload");
                                }}
                            >
                                <span className="block mt-4 lg:inline-block lg:mt-0 text-blue-200 hover:text-white cursor-pointer mr-4">Cadastrar Avistamento</span>
                            </Link>
                            <Link
                                to="/sighting"
                                onClick={() => {
                                    props.setPage("sighting");
                                }}
                            >
                                <span className="block mt-4 lg:inline-block lg:mt-0 text-blue-200 hover:text-white cursor-pointer mr-4">Meus Avistamentos</span>
                            </Link>
                        </div>
                        <div>
                            <a href="/login" class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-blue-500 hover:bg-white mt-4 lg:mt-0">Logout</a>
                        </div>
                    </div>
                </nav>
            </div>
        </React.Fragment>
    )
}
