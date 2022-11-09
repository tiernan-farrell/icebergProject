import React from 'react';

import { useEffect } from 'react';
import { useState } from 'react';
import {DataGrid, GridRowsProp, GridColDef } from '@mui/x-data-grid' 
import './App.css';
import Button from './Components/Button';
import Header from './Components/Header';
import Options from './Components/Options';
import Results from './Components/Results';
import Form from './Components/Form';
import ResultColumn from './Components/ResultColumn';
import Table from './Components/Table';




function App() {
  const [algoResults, setAlgoResults] = useState("")
  const [metaResults, setMetaResults] = useState("")
  const [minsup, setMinsup] = useState(1)
  const [card, setCard] = useState(7)
  const [numDims, setNumDims] = useState(5)
  const [numTuples, setNumTuples] = useState(1000)
  const [numDimsArr, setNumDimsArr] = useState([])
  const [displayData, setDisplayData] = useState([
    {
      0: 2,
      1: 1,
      2: 2, 
      3: 3, 
      4: 3,
    },
    {
      0: 2,
      1: 1,
      2: 2, 
      3: 3, 
      4: 3,
    },
    {
      0: 2,
      1: 1,
      2: 2, 
      3: 3, 
      4: 3,
    },
  ])
  // useEffect(() => {
  //   const rdiv = document.getElementById('result-container')
  //   rdiv.innerHTML = "HEllo"
  // }, [algoResults])

  useEffect(() => { 
    console.log(minsup)
  },[minsup])

  useEffect(()=> { 
    setNumDimsArr((numDimsArr) => {
      numDimsArr = []
      for (let i = 0; i < numDims; i++) { 
        numDimsArr.push(i)
      }
      return numDimsArr
    })
  }, [numDims])

  var xhr = null;
  var start = 0

  const getXmlHttpRequestObject = function () {
    if (!xhr) {
        // Create a new XMLHttpRequest object 
        xhr = new XMLHttpRequest();
    }
    return xhr;
  };
  function dataCallback(num=0) {
      // Check response is ready or not
      if (xhr.readyState === 4 && xhr.status === 200) {
          console.log("User data received!");
          const now2 = new Date()
          const end = now2.getTime()
          // eslint-disable-next-line no-undef

          let secs = Math.abs(end-start)/1000
          
          setMetaResults("Size: " + xhr.responseText.split("\",\"").length + "\n | Time: " + secs.toString()+ " seconds")
           setAlgoResults(xhr.responseText)
          console.log(typeof xhr.responseText)
      }
  }
  function dataCallbackGenerateData() {
    // Check response is ready or not
    if (xhr.readyState === 4 && xhr.status === 200) {
        console.log("User data received!");
        const now2 = new Date()
        const end = now2.getTime()
        // eslint-disable-next-line no-undef
        let secs = Math.abs(end-start)/1000
        setMetaResults("Size: " + xhr.responseText.split("\",\"").length + "\n | Time: " + secs.toString()+ " seconds")
        setAlgoResults(xhr.responseText.replaceAll('\\n', ', '))


        const s = xhr.responseText.replaceAll('\\n', ', ').replaceAll('[', '').replaceAll(',', '').replaceAll(']', '')
        let i = 0
        let j = -1
        let a = new Array(new Array(numDims))
        console.log(s.length)
        console.log(s)
        while(i<s.length) { 
            j === numDims ? j = 0 : j +=1
            console.log(i + " " + j)
            console.log(s[i])

            a[j]?.push({dim: s[i]})
            i+=1
        }
        console.log(a)

    }
}

  async function getBucResults() { 
    console.log("Get Buc...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    setAlgoResults("Loading")
    const nowsBuc = new Date()
    start = nowsBuc.getTime()
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
    start = nowstdc.getTime()
    const url = "http://localhost:6969/tdc?minsup=" + minsup + "&numDims=" + numDims + "&card=" + card
    await xhr.open("GET", url, true)
    xhr.send(null)

  }

  async function getAprioriResults() { 
    console.log("Get Apriori...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    setAlgoResults("Loading")
    xhr.onreadystatechange = dataCallback; 
    const nowApriori = new Date()
    start = nowApriori.getTime()
    const url = "http://localhost:6969/apriori?minsup=" + minsup + "&numDims=" + numDims + "&card=" + card
    await xhr.open("GET", url, true)
    xhr.send(null)
  }

  async function getStarCubeResults() { 
    console.log("Get Buc...");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    setAlgoResults("Loading")
    const nowsstarCube = new Date()
    start = nowsstarCube.getTime()
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
    start = nowsgetComputationTimes.getTime()
    await xhr.open("GET", "http://localhost:6969/getComputationTimes", true)
    xhr.send(null)
  }



  async function generateData() { 
    console.log("Generating data");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    setAlgoResults("Loading")
    xhr.onreadystatechange = dataCallbackGenerateData; 
    const nowGenerateData = new Date()
    start = nowGenerateData.getTime()
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
    start = now.getTime()
    await xhr.open("GET", "http://localhost:6969/data", true)

    // setMetaResults(metaResults + " | Time: " + edata-sdata)
    xhr.send(null)
  }

  function chanegeStates(newNumTuples, newNumDims, newCard, newMinsup) {
    setNumTuples(newNumTuples)
    setNumDims(newNumDims)
    setCard(newCard)
    setMinsup(newMinsup)
    setDisplayData()
  }

  const dimsContext = React.useContext(numDims)
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
      <Form onSubmit={chanegeStates} />    
      <Button onClick={generateData} id='genData'>Generate Data</Button>
      <div id='meta-results'>{metaResults}</div>
      <div id='result-container'>
        <Table d={displayData} numDims={dimsContext}/>
      </div>
    </div>
    </>
  );
}

export default App;
