import logo from './logo.svg';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import { AppBar, CssBaseline, IconButton, Toolbar, Typography } from '@mui/material';
import Container from '@mui/material/Container';
import Navigation from './components/Navigation'
import { BrowserRouter } from "react-router-dom";
import { Route, Routes } from "react-router";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Signup from './pages/Signup';
import Login from './pages/Login'
import HikeDisplay from './pages/HikeDisplay';


var testProps = { user: 'userName', isShowing: false };

const theme = createTheme({
  palette: {
    mode: "light",
  },
});

function App() {
  //console.log(testProps.user);
  return (
  
    <ThemeProvider theme={theme}>
      <CssBaseline/>
      <BrowserRouter>
    <Navigation props={testProps}/>
    <div>
      <Routes>
        <Route path="/hikedisplay" element={<HikeDisplay/>}/>
        <Route path="/signup" element={<Signup/>} />
        <Route path="/login" element={<Login/>} />
      </Routes>
    </div>
    </BrowserRouter>
    </ThemeProvider>
  );
}




export default App;
