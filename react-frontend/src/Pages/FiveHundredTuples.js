import React from 'react'
import Graph from '../Components/Graph'
import ResultsNav from '../Components/ResultsNav'
import { 
    testFiveMemory, testFiveMemoryData, testFiveTime, testFiveTimeData,
    testSixMemory, testSixMemoryData, testSixTime, testSixTimeData,
    testSevenMemory, testSevenMemoryData, testSevenTime, testSevenTimeData,
    testEightMemory, testEightMemoryData, testEightTime, testEightTimeData,    
 } from '../graphData'

const FiveHundredTuples = (() => {
    return (
        <>
        <ResultsNav />
        <Graph data={testFiveTimeData} title={testFiveTime}/>
        <Graph data={testFiveMemoryData} title={testFiveMemory}/>
        <Graph data={testSixTimeData} title={testSixTime}/>
        <Graph data={testSixMemoryData} title={testSixMemory}/>  
        <Graph data={testSevenTimeData} title={testSevenTime}/>
        <Graph data={testSevenMemoryData} title={testSevenMemory}/>
        <Graph data={testEightTimeData} title={testEightTime}/>
        <Graph data={testEightMemoryData} title={testEightMemory}/>
        </>
    )
})

export default FiveHundredTuples