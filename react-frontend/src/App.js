import React from 'react';

import { useEffect } from 'react';
import { useState } from 'react';

import './App.css';
import Button from './Components/Button';
import Header from './Components/Header';
import Options from './Components/Options';
import Results from './Components/Results';
import Form from './Components/Form';



function App() {
  const [algoResults, setAlgoResults] = useState("")
  const [metaResults, setMetaResults] = useState("")
  const [minsup, setMinsup] = useState(1)
  const [card, setCard] = useState(7)
  const [numDims, setNumDims] = useState(5)
  const [numTuples, setNumTuples] = useState(1000)
  const [urlParams, setUrlParams] = useState("")
  // useEffect(() => {
  //   const rdiv = document.getElementById('result-container')
  //   rdiv.innerHTML = "HEllo"
  // }, [algoResults])

  useEffect(() => { 
    console.log(minsup)
  },[minsup])

  var xhr = null;
  var start = 0

  const getXmlHttpRequestObject = function () {
    if (!xhr) {
        // Create a new XMLHttpRequest object 
        xhr = new XMLHttpRequest();
    }
    return xhr;
  };
  function dataCallback() {
      // Check response is ready or not
      if (xhr.readyState === 4 && xhr.status === 200) {
          console.log("User data received!");
          const now2 = new Date()
          const end = now2.getMilliseconds()
          // eslint-disable-next-line no-undef
          console.log(start)
          console.log(end)
          console.log(-start)
          const t = end-start
          // setMetaResults("Size: " + xhr.responseText.split("\",\"").length + "\n | Time: " + t.toString()+ "seconds")
          setAlgoResults(xhr.responseText)
          console.log(typeof xhr.responseText)
      }
  }

  async function getBucResults() { 
    console.log("Get Buc...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    setAlgoResults("Loading")
    const nowsBuc = new Date()
    start = nowsBuc.getMilliseconds()
    const url = "http://localhost:6969/buc?minsup=" + minsup + "&numDims=" + numDims + "&card=" + card
    await xhr.open("GET", url, true)
    xhr.send(null)
  }
  async function getTDCResults() { 
    console.log("Get TDC...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    setAlgoResults("Loading")
    const nowstdc = new Date()
    start = nowstdc.getMilliseconds()
    await xhr.open("GET", "http://localhost:6969/tdc", true)
    xhr.send(null)

  }

  async function getAprioriResults() { 
    console.log("Get Apriori...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    setAlgoResults("Loading")
    const nowApriori = new Date()
    start = nowApriori.getMilliseconds()
    await xhr.open("GET", "http://localhost:6969/apriori", true)
    xhr.send(null)
  }

  async function getStarCubeResults() { 
    console.log("Get Buc...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    setAlgoResults("Loading")
    const nowsstarCube = new Date()
    start = nowsstarCube.getMilliseconds()
    await xhr.open("GET", "http://localhost:6969/starCube", true)
    xhr.send(null)
  }


  async function getRunTimes() { 
    console.log("Get Run Times");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    setAlgoResults("Loading")
    const nowsgetComputationTimes = new Date()
    start = nowsgetComputationTimes.getMilliseconds()
    await xhr.open("GET", "http://localhost:6969/getComputationTimes", true)
    xhr.send(null)
  }



  async function generateData() { 
    console.log("Generating data");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    setAlgoResults("Loading")
    const nowGenerateData = new Date()
    start = nowGenerateData.getMilliseconds()
    const s = "?numTuples=" + numTuples + "&numDims=" + numDims + "&card=" + card
    const url = "http://localhost:6969/generateData" + s
    await xhr.open("GET", url, true)
    xhr.send(null)
  }

  async function getDataSet() { 
    console.log("Get Data...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    setAlgoResults("Loading")
    const now = new Date()
    start = now.getMilliseconds()
    await xhr.open("GET", "http://localhost:6969/data", true)

    // setMetaResults(metaResults + " | Time: " + edata-sdata)
    xhr.send(null)
  }

  function chanegeStates(newNumTuples, newNumDims, newCard) {
    setNumTuples(newNumTuples)
    setNumDims(newNumDims)
    setCard(newCard)
    console.log(numTuples)
    console.log(numDims)
    console.log(card)
    
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
      <Button onClick={generateData}>genData</Button>
      <Form onSubmit={chanegeStates} />    
      <div id='meta-results'>{metaResults}</div>
      <div id='result-container'>
        <Results results={algoResults}/>  
      </div>
    </div>
    </>
  );
}

export default App;
