import React, { useState, useEffect, useContext } from "react";
import PropTypes from "prop-types";
import { Context } from "../store/appContext";
import { Link, useParams } from "react-router-dom";

export const Single = (props) => {
const { store, actions } = useContext(Context);
const params = useParams();
{store.people.map((elem, idx) => {
return (
    <div className="container">
    <div class="card mb-3" style="max-width: 540px;">
    <div class="row g-0">
      <div class="col-md-4">
        <img src="..." class="img-fluid rounded-start" alt="..."/>
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <h5 class="card-title">{props.title ? props.title : "Title"}</h5>
          <p class="card-text">{props.children}</p>
          <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
        </div>
      </div>
    </div>
  </div>
  <br />
  <div className="row">
    <div className="col">
        <h5>Name</h5>
        <p>{elem.name}</p>
    </div>
  </div>
  </div>			
 	);
 }
)
}
};

Single.propTypes = {
    title: PropTypes.string,
    imageURL: PropTypes.string,
    text: PropTypes.string,
match: PropTypes.object
};
