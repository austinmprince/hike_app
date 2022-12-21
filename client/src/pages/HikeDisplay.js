import React from "react";
import Grid from "@mui/material/Grid"
import HikeCard from "../components/HikeCard";

var hikes = [{"id": 1, "date": "09-01-1994", "title": "Angle Lake"}, {"id": 1, "date": "09-01-1994", "title": "Angle Lake"}, {"id": 1, "date": "09-01-1994", "title": "Angle Lake"}, {"id": 1, "date": "09-01-1994", "title": "Angle Lake"}];
const HikeDisplay = () => {
  return (
    <Grid container alignItems="center" justifyContent="center" spacing={2} direction="row">  
        {hikes.map((hike) => (
        <Grid key={hike.id} item sx={{m:2}} xs={4}>
          <HikeCard />
        </Grid>
        ))}
    </Grid>
  )
};

export default HikeDisplay;