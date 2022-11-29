import React from 'react';

import { useEffect } from 'react';
import { useState } from 'react';

import Button from '../Components/Button';
import Header from '../Components/Header';
import Options from '../Components/Options';
import Form from '../Components/Form';
import Table from '../Components/Table';


function Algorithms() {
  const [algoResults, setAlgoResults] = useState("")
  const [metaResults, setMetaResults] = useState("")
  const [minsup, setMinsup] = useState(1)
  const [card, setCard] = useState(7)
  const [numDims, setNumDims] = useState(5)
  const [numTuples, setNumTuples] = useState(1000)

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
  function dataCallback(num=0) {
      // Check response is ready or not
      if (xhr.readyState === 4 && xhr.status === 200) {
          console.log("User data received!");
          const now2 = new Date()
          const end = now2.getTime()
          // eslint-disable-next-line no-undef

          let secs = Math.abs(end-start)/1000
          console.log(typeof(xhr.responseText))
          console.log(xhr.responseText.split('],'))
          setMetaResults("Size: " + xhr.responseText.replace('[[', '').replace(']]', '').replaceAll('],[', '!').split('!').length + "\n | Time: " + secs.toString()+ " seconds")
          setAlgoResults(xhr.responseText)
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

  async function generateData() { 
    console.log("Generating data");
    // eslint-disable-next-line no-undef
    xhr = getXmlHttpRequestObject(); 
    setAlgoResults("Loading")
    xhr.onreadystatechange = dataCallback; 
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
    console.log(numDims)
  }


  return (
    <>
    <Header /> 
    <div className="Algorithms">
      <Options />
      <Button onClick={getDataSet}>Data</Button>
      <Button onClick={getBucResults}>BUC</Button>
      <Button onClick={getTDCResults}>TDC</Button>
      <Button onClick={getAprioriResults}>Apriori</Button>
      <Form onSubmit={chanegeStates} />    
      <Button onClick={generateData} id='genData'>Generate Data</Button>
      <div id='meta-results'>{metaResults}</div>
      <div id='result-container'>
        <Table data= {algoResults.replace('[[', '').replace(']]', '').replaceAll('],[', '!').split('!').map((e) => e.replaceAll('"*"', '*').split(','))} numDims={numDims}/>
      </div>
    </div>
    </>
  );
}

export default Algorithms;