import React from "react";
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Avatar  from '@mui/material/Avatar';
import Button from "@mui/material/Button";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Container } from "@mui/system";
import { CssBaseline, TextField, Typography } from "@mui/material";

async function signupUser(email, password){
  console.log(email, password);
  const response = await fetch("http://localhost:8000/signup", {
    method: "POST",
    headers: {
      "ContentType": "application/json"
    },
    body: JSON.stringify({email, password})
  });
}
const theme = createTheme();
const Signup = () => {
  console.log("signup page loading");

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('adding user');
    const data = new FormData(event.currentTarget);
    signupUser(data.get('email'), data.get('password'), 'testname').then((response) =>
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
      Sign up
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
      <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign In
            </Button>
    </Box>
    </Box>
    </Container>
  );
};
export default Signup;