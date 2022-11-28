import React from 'react';

import Navbar from './Components/Navbar';
import Algorithms from './Pages/Algorithms';
import About from "./Pages/About";
import Results from "./Pages/Results";
import HundredTuples from './Pages/HundredTuples';
import FiveHundredTuples from './Pages/FiveHundredTuples';
import ThousandTuples from './Pages/ThousandTuples';
import TenThousandTuples from './Pages/TenThousandTuples';

function App() {
  let Component 
  switch (window.location.pathname) {
    case "/about":
      Component = About
      break
      case "/results":
        Component = Results
        break
      case "/hundred":
          Component = HundredTuples
          break
      case "/fivehundred":
          Component = FiveHundredTuples
          break
      case "/thousand":
          Component = ThousandTuples
          break
      case "/tenthousand":
          Component = TenThousandTuples
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
