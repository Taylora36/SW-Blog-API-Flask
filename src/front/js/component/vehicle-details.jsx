import React, { useEffect, useContext } from "react";
import { useParams } from "react-router-dom";
import { Context } from "../store/appContext";

export const VehicleDetails = () => {
  const { id } = useParams();
  const { store, actions } = useContext(Context);

  useEffect(() => {
    actions.getSingleVehicle(id);
  }, []);

  return (
    <>
      <h1 id="heading1" className="title text-center">
        {store.singleVehicle.name}
      </h1>
      <div className="container">
        <div className="card mb-3">
          <div className="row g-0">
            <div className="col-md-4">
              <img
                src="https://www.cnet.com/a/img/resize/8364177c9fdeddb3a35b8434a164b6f29619bd93/hub/2015/02/05/11b50968-7eef-47da-a344-33ebe0d18be0/star-wars-vehicles-at-at.jpg?auto=webp&width=1200"
                id="vehicle"
                className="img-fluid rounded-start"
                alt="..."
              />
            </div>
            <div className="col-md-8">
              <div className="card-body">
                <h3 className="card-title">About This Vehicle</h3>
                <p className="card-text">
                  {store.singleVehicle.name} is a vehicle with a model of {store.singleVehicle.model} and manufactured
                  at {store.singleVehicle.manufacturer}.
                  <br />
                  <br />
                  <strong>Cost in Credits: </strong>{store.singleVehicle.cost_in_credits}
                  <br />
                  <strong>Length: </strong>{store.singleVehicle.length}
                  <br />
                  <strong>Crew: </strong>{store.singleVehicle.crew}
                  <br />
                  <strong>Passengers: </strong>{store.singleVehicle.passengers}
                  <br />
                  <strong>Cargo Capacity: </strong>{store.singleVehicle.cargo_capacity}
                  <br />
                  <strong>Vehicle Class: </strong>{store.singleVehicle.vehicle_class}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};