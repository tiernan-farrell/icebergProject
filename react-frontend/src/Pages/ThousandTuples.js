import React from 'react'
import Graph from '../Components/Graph'
import ResultsNav from '../Components/ResultsNav'
import { 
    testNineMemory, testNineMemoryData, testNineTime, testNineTimeData,
    testTenMemory, testTenMemoryData, testTenTime, testTenTimeData,
    testElevenMemory, testElevenMemoryData, testElevenTime, testElevenTimeData,
    testTwelveMemory, testTwelveMemoryData, testTwelveTime, testTwelveTimeData,    
 } from '../graphData'

const ThousandTuples = (() => {
    return (
        <>
            <ResultsNav />
            <Graph data={testNineTimeData} title={testNineTime}/>
            <Graph data={testNineMemoryData} title={testNineMemory}/>
            <Graph data={testTenTimeData} title={testTenTime}/>
            <Graph data={testTenMemoryData} title={testTenMemory}/>  
            <Graph data={testElevenTimeData} title={testElevenTime}/>
            <Graph data={testElevenMemoryData} title={testElevenMemory}/>
            <Graph data={testTwelveTimeData} title={testTwelveTime}/>
            <Graph data={testTwelveMemoryData} title={testTwelveMemory}/>

        </>)
})

export default ThousandTuples