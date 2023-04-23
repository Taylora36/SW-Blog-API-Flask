import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

import { useParams } from "react-router-dom";
import { Characters } from "../component/character-card.jsx";
import { Planets } from "../component/planets-card.jsx";
import { Vehicles } from "../component/vehicles-card.jsx";
import "../../styles/home.css";

export const Home = () => {
  const { store, actions } = useContext(Context);
  const { id } = useParams();
  
  useEffect(() => {
    actions.getPeople();
  }, []); 
  
  useEffect(() => {
    actions.getPlanets();
  }, []);

  useEffect(() => {
    actions.getVehicles();
  }, []);

  return(
	<div className="container">
      <div className="container">
        <h1 id="heading">Characters</h1>
      </div>

      <div className="album py-5 d-flex justify-content-center" id="card">
        <div className="container">
          <div className="d-flex justify-content-between row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
            {store.people.map((elem, idx) => {
              return (
                <div key={idx}>
                <Characters
                  key={idx}
                  name={elem.name}
                  gender={elem.gender}
                  birth_year={elem.birth_year}
                  height={elem.height}
                  id={idx + 1}
                />
              </div>
			  );
            })}
          </div>
        </div>
      </div>

      <div className="container">
        <div className="row">
          <h1 id="heading">Planets</h1>
        </div>

        <div className="album py-5 d-flex justify-content-center">
          <div className="container">
            <div className="d-flex justify-content-between row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
              {store.planets.map((elem, idx) => {
                return (
					<div key={idx}>
                <Planets
                  key={idx}
                  name={elem.name}
                  climate={elem.climate}
                  terrain={elem.terrain}
                  population={elem.population}
                  id={idx + 1}
                />
              </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>

      <div className="container">
        <div className="row">
          <h1 id="heading">Vehicles</h1>
        </div>

        <div className="album py-5 d-flex justify-content-center">
          <div className="container">
            <div className="d-flex justify-content-between row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
              {store.vehicles.map((elem, idx) => {
                return (
                  <div key={idx}>
                    <Vehicles
                      key={idx}
                      name={elem.name}
                      model={elem.model}
                      manufacturer={elem.manufacturer}
                      cost_in_credits={elem.cost_in_credits}
                      id={idx + 4}
                    />
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};