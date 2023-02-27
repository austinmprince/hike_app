import React from "react";
import {
  Box,
  Avatar,
  Button,
  Link,
  Grid,
  CssBaseline,
  TextField,
  Typography,
  appBarClasses,
} from "@mui/material";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { Container } from "@mui/system";
import App from "../App";

async function loginUser(username, password) {
  console.log(username, password);
  const response = await fetch("http://localhost:8000/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `grant_type=password&username=${username}&password=${password}`,
  });
  const data = await response.json();
  document.cookie = `Authorization=${data.access_token}; SameSite=None; Secure`;
}

const theme = createTheme();
const Login = ({setUser}) => {
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const username = data.get("username");
    const password = data.get("password");
    try {
      await loginUser(username, password);
      setUser(username);
      window.location.href = '/hikedisplay'
      
    } catch (error) {
      window.location.href = '/';
      console.log(error);
    }
  };
  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Login
        </Typography>
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
          <TextField
            required
            fullWidth
            id="username"
            label="Username"
            name="username"
            autoComplete="username"
          />
          <TextField
            sx={{ mt: 1 }}
            required
            fullWidth
            id="password"
            label="Password"
            name="password"
            type="password"
            autoComplete="password"
            autoFocus
          />
          <Button
            type="submit"
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            fullWidth
          >
            Login
          </Button>
        </Box>

        <Box display="flex" justifyContent="center" whiteSpace="nowrap">
          <Typography fontSize={12} alignItems="center">
            <Grid container>
              <Grid item xs sx={{ mr: 2 }}>
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
