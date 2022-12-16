import React from "react"
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import { AppBar, IconButton, Link, Toolbar, Typography } from '@mui/material';
import Container from '@mui/material/Container';
import { useLocation } from 'react-router-dom';

var x =  {
  user: String,
  isShowing: Boolean,
}

// const location = useLocation();
// const shouldShowLogin;
const Navigation = (props) => {
  console.log(props.props.isShowing);
// export default function Navigation() {
  return(
    <AppBar position="static" >
      <Container maxWidth="xl">
      <Toolbar>
        <IconButton>  
        </IconButton>
        <Typography variant="h6" component="div" sx={{flexGrow: 1}}>
          HikeApp
        </Typography>
        <Box sx={{ marginLeft: "auto", display: "flex", alignItems: "center"}}> 
          { props.props.isShowing ? 
          <Link to="/login" style={{ textDecoration: "none"}}>
          <Button variant="contained" color="primary">
          Login
        </Button>
          </Link> 
          : 
          <Link to="/logout" style={{ textDecoration: "none"}}>
          <Button variant="contained" color="primary">
          Logout
        </Button>
          </Link>  
        }
        </Box>
               
      </Toolbar>
      </Container>
    </AppBar>
  );
};
export default Navigation;
// const NavBar = () => {
//   return (
 
//     // <AppBar position="static" style={{ background: '#2E3B55' }}>
//     //   <Container maxWidth="xl">
//     //   <Toolbar>
//     //     <IconButton>  
//     //     </IconButton>
//     //     <Typography variant="h6" component="div" sx={{flexGrow: 1}}>
//     //       HikeApp
//     //     </Typography>
//     //     <Button sx={{bgColor:'background.paper'}}>
//     //       Login
//     //     </Button>
//     //   </Toolbar>
//     //   </Container>
//     // </AppBar>
// );


