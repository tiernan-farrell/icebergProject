import React from 'react';
import { useEffect } from 'react';
import { useState } from 'react';

import './App.css';
import Button from './Components/Button';
import Header from './Components/Header';
import Options from './Components/Options';



function App() {
  const [algoResults, setAlgoResults] = useState([])
  const [metaResults, setMetaResults] = useState([])

  var xhr = null;

  const getXmlHttpRequestObject = function () {
    if (!xhr) {
        // Create a new XMLHttpRequest object 
        xhr = new XMLHttpRequest();
    }
    return xhr;
  };
  function dataCallback() {
      // Check response is ready or not
      if (xhr.readyState == 4 && xhr.status == 200) {
          console.log("User data received!");
          // eslint-disable-next-line no-undef
          setMetaResults("Total cube Size: " + xhr.responseText.length + "\n")
          setAlgoResults(xhr.responseText)
          console.log(xhr.responseText)
      }
  }

  async function getBucResults() { 
    console.log("Get Buc...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/buc", true)
    xhr.send(null)
  }
  async function getTDCResults() { 
    console.log("Get TDC...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/tdc", true)
    xhr.send(null)
  }

  async function getAprioriResults() { 
    console.log("Get Apriori...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/apriori", true)
    xhr.send(null)
  }

  async function getStarCubeResults() { 
    console.log("Get Buc...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/buc", true)
    xhr.send(null)
  }


  async function getRunTimes() { 
    console.log("Get Run Times");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/getComputationTimes", true)
    xhr.send(null)
    setMetaResults("")
  }



  async function getDataSet() { 
    console.log("Get Data...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/data", true)
    xhr.send(null)
    setMetaResults("")
  }



  return (
    <>
    <Header /> 
    <div className="App">
      <Options />
      <Button onClick={getDataSet}>Data</Button>
      <Button onClick={getBucResults}>BUC</Button>
      <Button onClick={getTDCResults}>TDC</Button>
      <Button onClick={getAprioriResults}>Apriori</Button>
      <Button onClick={getStarCubeResults}>StarCube</Button>
      <Button onClick={getRunTimes}>RunTimes</Button>
      <div id='meta-results'>{metaResults}</div>
      <div id='result-container'>{algoResults}</div>
    </div>
    </>
  );
}

export default App;
