import React from 'react';

import Navbar from './Components/Navbar';
import Algorithms from './Pages/Algorithms';
import About from "./Pages/About";


function App() {
  let Component 
  switch (window.location.pathname) {
    case "/about":
      Component = About
      break
    default:
      Component = Algorithms
      break
  }
  return (
    <div className='app'>
      <Navbar />
      <div className="container">
        <Component />
      </div>
    </ div> 
  );
}

export default App;
