import React, { useContext } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

import { Context } from "../store/appContext";

import { AiFillHeart } from 'react-icons/ai';

export const Vehicles = (props) => {
  const { actions } = useContext(Context);

  return (
    <div className="col">
      <div className="card shadow my-3">
        <img
          src="https://i.ytimg.com/vi/I6AZLlA2j18/maxresdefault.jpg"
          className="card-img-top"
          alt="..."
        />
        <div className="body text-dark">
          <h4 className="card-title text-center p-3">{props.name}</h4>
          <ul className="list-group list-group-flush">
            <li className="list-group-item">
              Model: <span className="text-capitalize">{props.model}</span>
            </li>
            <li className="list-group-item">
              Manufacturer:{" "}
              <span className="text-capitalize">{props.manufacturer}</span>
            </li>
            <li className="list-group-item">
              Cost: <span className="text-capitalize">{props.cost_in_credits}</span>
            </li>
          </ul>
          <div className="d-flex justify-content-between p-3">
            <div className="">
              <Link to={`/vehicles/${props.id}`}>
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
Vehicles.propTypes = {
  name: PropTypes.string,
  model: PropTypes.string,
  manufacturer: PropTypes.string,
  cost_in_credits: PropTypes.string,
  id: PropTypes.number,
  url: PropTypes.string,
};