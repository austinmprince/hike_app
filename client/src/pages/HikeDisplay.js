import React, { useEffect, useState } from "react";
import Grid from "@mui/material/Grid"
import HikeCard from "../components/HikeCard";

const HikeDisplay = ({user}) => {
  const [hikes, setHikes] = useState([]);
  console.log(user);
  useEffect(() => {
    async function getHikes() {
      console.log('calling get hikes');
      console.log(`${document.cookie}`)
      let username = localStorage.getItem("username");
      const response = await fetch(`http://localhost:8000/hikes/${username}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: 'include'
    });
    const hikes = await response.json();
    setHikes(hikes);
    }
    getHikes();
    return;
  }, [hikes.length]);

  function hikeList() {
    console.log(hikes);
    return hikes.map((hike) => {
      return <Grid item sx={{m:2}} xs={4}><HikeCard key={hike.hike_name} {...hike}/></Grid>
    })
  }
  return (
    <Grid container alignItems="center" justifyContent="center" spacing={2} direction="row">  
        {hikeList()}
    </Grid>
  )
};

export default HikeDisplay;