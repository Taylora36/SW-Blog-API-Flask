import React, { useContext } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

import { Context } from "../store/appContext";

import { AiFillHeart } from 'react-icons/ai';

export const Planets = (props) => {
  const { actions } = useContext(Context);

  return (
    <div className="col">
      <div className="card shadow my-3">
        <img
          src="https://www.slashfilm.com/img/gallery/how-star-wars-coruscant-became-the-planet-wide-city-of-your-nightmares/l-intro-1678905687.jpg"
          className="card-img-top"
          alt="..."
        />
        <div className="body text-dark">
          <h4 className="card-title text-center p-3">{props.name}</h4>
          <ul className="list-group list-group-flush">
            <li className="list-group-item">
              Climate: <span className="text-capitalize">{props.climate}</span>
            </li>
            <li className="list-group-item">
              Terrain: <span className="text-capitalize">{props.terrain}</span>
            </li>
            <li className="list-group-item">
              Population:{" "}
              <span className="text-capitalize">{props.population}</span>
            </li>
          </ul>
          <div className="d-flex justify-content-between p-3">
            <div className="">
              <Link to={`/planets/${props.id}`}>
                <div className="btn btn-outline-warning">Details</div>
              </Link>
            </div>
            <div className="">
              <button
                className="btn btn-outline-warning"
                onClick={() => actions.addToFavorites(props.name)}
              >
                <AiFillHeart />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

Planets.propTypes = {
  name: PropTypes.string,
  climate: PropTypes.string,
  terrain: PropTypes.string,
  population: PropTypes.string,
  id: PropTypes.number,
  url: PropTypes.string,
};
