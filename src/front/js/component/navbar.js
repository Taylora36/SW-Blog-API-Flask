import React, { useContext } from "react";
import { AiFillHeart } from 'react-icons/ai';
import { BsFillTrash3Fill } from 'react-icons/bs';
import { Context } from "../store/appContext";
import {  Link } from "react-router-dom";

export const Navbar = () => {
	const { store, actions } = useContext(Context);
	return (
		<nav className="navbar">
  			<div className="container">
			  <a href="https://3000-taylora36-starwarsblog-ms8dpddpb4e.ws-us90.gitpod.io/" target="_self" rel="noreferrer" className="navbar-brand col-4 offset-5">
     		 <img src="https://lumiere-a.akamaihd.net/v1/images/sw_logo_stacked_2x-52b4f6d33087_7ef430af.png?region=0,0,586,254" alt="Bootstrap" width="120" height="50"/>
    		</a>
			<div className="dropdown">
          	<button className="btn btn-warning dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            Favorites <AiFillHeart  />
          	</button>
			  
        <ul className="dropdown-menu dropdown-menu-dark dropdown-menu-end">
            {store.favorites.map((item, index) => <li><a className="dropdown-item d-flex justify-content-between align-items-center">{item}<BsFillTrash3Fill style={{cursor:"pointer"}} onClick = {() => actions.removeFromFavorites(index)} /></a></li>)}
          </ul>
		  </div>
  			</div>
		</nav>
	);
};
