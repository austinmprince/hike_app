import React, { useEffect, useState } from "react";
import Grid from "@mui/material/Grid"
import HikeCard from "../components/HikeCard";

const HikeDisplay = (props) => {
  console.log(localStorage.getItem("username"));
  const [hikes, setHikes] = useState([]);

  useEffect(() => {
    async function getHikes() {
      let username = localStorage.getItem("username");
      const response = await fetch(`http://localhost:8000/hikes/${username}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    });
    console.log(response);
    const hikes = await response.json();
    setHikes(hikes);
    }
    getHikes();
  })

  function hikeList() {
    return hikes.map((hike) => {
      return <Grid key={hike.id} item sx={{m:2}} xs={4}><HikeCard/></Grid>
    })
  }
  return (
    <Grid container alignItems="center" justifyContent="center" spacing={2} direction="row">  
        {hikeList()}
    </Grid>
  )
};

export default HikeDisplay;