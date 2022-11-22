import React from 'react';

import Navbar from './Components/Navbar';
import Algorithms from './Pages/Algorithms';
import Home from "./Pages/Home";
import About from "./Pages/About";


function App() {
  let Component 
  switch (window.location.pathname) {
    case "/":
      Component = Home
      break
    case "/algorithms":
      Component = Algorithms
      break
    case "/about":
      Component = About
      break
  }
  return (
    <>
      <Navbar />
      <div className="container">
        <Component />
      </div>
    </> 
  );
}

export default App;
