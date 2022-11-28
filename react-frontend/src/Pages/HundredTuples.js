import React from 'react'
import Graph from '../Components/Graph'
import ResultsNav from '../Components/ResultsNav'
import { testOneTimeData, testOneMemoryData, testTwoMemoryData, testTwoTimeData, testOneTime, testOneMemory, testTwoTime, testTwoMemory } from '../graphData'


const HundredTuples = () => {
    return (
        <>
        <ResultsNav />
        <Graph data={testOneTimeData} title={testOneTime}/>
        <Graph data={testOneMemoryData} title={testOneMemory}/>
        <Graph data={testTwoTimeData} title={testTwoTime}/>
        <Graph data={testTwoMemoryData} title={testTwoMemory}/>  
        </>    
    )
}

export default HundredTuples