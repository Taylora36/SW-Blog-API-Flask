import React, { useContext } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

import { Context } from "../store/appContext";

import { AiFillHeart } from 'react-icons/ai';

export const Characters = (props) =>{
  const { actions } = useContext(Context);
  return (
    <div className="col">
      <div className="card shadow my-3">
        <img
          src="https://cdn.vox-cdn.com/thumbor/_3sxdcRY2QVXlvtFzm9QbU8XTDA=/0x0:2770x1166/1200x800/filters:focal(1668x327:2110x769)/cdn.vox-cdn.com/uploads/chorus_image/image/66532457/Screen_Shot_2020_01_22_at_9.38.17_AM.0.png"
          className="card-img-top"
          alt="..."
        />
        <div className="body text-dark">
          <h4 className="card-title text-center p-3">{props.name}</h4>
          <ul className="list-group list-group-flush">
            <li className="list-group-item">
              Gender: <span className="text-capitalize">{props.gender}</span>
            </li>
            <li className="list-group-item">
              Birth Year:{" "}
              <span className="text-capitalize">{props.birth_year}</span>
            </li>
            <li className="list-group-item">
              Height: <span className="text-capitalize">{props.height}</span>
            </li>
          </ul>
          <div className="d-flex justify-content-between p-3">
            <div className="">
              <Link to={`/people/${props.id}`}>
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
    )
}

Characters.propTypes = {
    name: PropTypes.string,
    gender: PropTypes.string,
    height: PropTypes.string,
    birth_year: PropTypes.string,
    id: PropTypes.number,
    url: PropTypes.string,
  };