import React from "react";
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Avatar  from '@mui/material/Avatar';
import Button from "@mui/material/Button";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid"
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Container } from "@mui/system";
import { CssBaseline, TextField, Typography } from "@mui/material";

async function loginUser(email, password){
  console.log(email, password);
  const response = await fetch("http://localhost:8000/login", {
    method: "POST",
    headers: {
      "ContentType": "application/json"
    },
    body: JSON.stringify({email, password})
  });
}
const theme = createTheme();
const Login = () => {
  console.log("signup page loading");

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('loggin in user user');
    const data = new FormData(event.currentTarget);
    loginUser(data.get('email'), data.get('password'), 'testname').then((response) =>
    {
      console.log(response);
    });
  }
  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline/>
    <Box
    sx={{
      marginTop: 8,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    }}
  >
    <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
      <LockOutlinedIcon/>
    </Avatar>
    <Typography component="h1" variant="h5">
      Login
    </Typography>
    <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
      <TextField
        required
        fullWidth
        id="email"
        label="Email Address"
        name="email"
        autoComplete="email"
        autoFocus
      />
      <TextField sx={{mt:1 }}required fullWidth id="password" label="Password"
      name="password" type="password" autoComplete="password" autoFocus/>
      </Box>
    <Button type="submit" variant="contained" sx={{ mt: 3, mb: 2 }} fullWidth>
      Login
    </Button>
    
 
<Box display="flex" justifyContent="center" whiteSpace="nowrap">
            <Typography fontSize={12} alignItems="center"> 
            <Grid container>
              
              <Grid item xs sx={{mr: 2}}>
                Forgot your password
              </Grid>
              <Grid item xs>
                <Link href="/signup">
                {"Don't have an account click to signup"}
                </Link>
              </Grid>
              
            </Grid>
            </Typography>
            </Box>

    
    </Box>
    </Container>
  );
};
export default Login;