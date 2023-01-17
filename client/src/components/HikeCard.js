import React from "react";
import {Card, CardContent, Typography, CardActions, Button } from "@mui/material";
import { format } from 'date-fns'


const HikeCard = (hike) => {
  console.log();
  var date = new Date(hike.date).toDateString();
  
  
  return (
    <Card sx={{ minWidth: 275 }}>
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
         {date}
        </Typography>
        <Typography variant="h5" component="div">
          {hike.hike_name}
        </Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
          {hike.region}
        </Typography>
        <Typography variant="body2">
          well meaning and kindly.
          <br />
          {'"a benevolent smile"'}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Learn More</Button>
      </CardActions>
    </Card>
  );
}
export default HikeCard