import React, { useState, useEffect, useContext } from "react";

import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";

export const CharacterDetails = () => {
  const { id } = useParams();
  const { store, actions } = useContext(Context);
  const name = store.singleCharacter?.name;
  const gender = store.singleCharacter?.gender;
  const hairColor = store.singleCharacter?.hair_color;
  const height = store.singleCharacter?.height;
  const skinColor = store.singleCharacter?.skin_color;
  const eyeColor = store.singleCharacter?.eye_color;
  const birthYear = store.singleCharacter?.birth_year;

  useEffect(() => {
    actions.getSingleCharacter(id);
    console.log(store.singleCharacter);
  }, [id]);
  console.log(store.singleCharacter);
  return (
    <>
      <h1 id="heading1" className="title text-center">
        {name}
      </h1>
      <div className="container">
        <div className="card mb-3">
          <div className="row g-0">
            <div className="col-md-4">
              <img
                src="https://static1.moviewebimages.com/wordpress/wp-content/uploads/2022/03/grogu-star-wars.jpeg"
                id="grogu"
                class="img-fluid rounded-start"
                alt="..."
              />
            </div>
            <div className="col-md-8">
              <div className="card-body">
                <h3 className="card-title">About This Character</h3>
                <p className="card-text">
                  Below is a list of further information about this Star Wars
                  character.
                </p>
                <h5>{name}</h5>
                <ul>
                  <li>
                    <strong>Gender:</strong> {gender}
                  </li>
                  <li>
                    <strong>Hair Color:</strong> {hairColor}
                  </li>
                  <li>
                    <strong>Height:</strong> {height}
                  </li>
                  <li>
                    <strong>Skin Color:</strong> {skinColor}
                  </li>
                  <li>
                    <strong>Eye Color:</strong> {eyeColor}
                  </li>
                  <li>
                    <strong>Birthyear:</strong> {birthYear}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};