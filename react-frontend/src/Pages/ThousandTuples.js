import React from 'react'
import Graph from '../Components/Graph'
import ResultsNav from '../Components/ResultsNav'

import { testFiveMemoryData, testFiveTimeData, testSixTimeData, testSixMemoryData, testSevenTimeData, testSevenMemoryData,testFiveTime, testFiveMemory, testSixTime, testSixMemory, testSevenTime, testSevenMemory } from '../graphData'


const ThousandTuples = (() => {
    return (
        <>
            <ResultsNav />
            <Graph data={testFiveTimeData} title={testFiveTime}/>
            <Graph data={testFiveMemoryData} title={testFiveMemory}/>


            <Graph data={testSixTimeData} title={testSixTime}/>
            <Graph data={testSixMemoryData} title={testSixMemory}/>


            <Graph data={testSevenTimeData} title={testSevenTime}/>
            <Graph data={testSevenMemoryData} title={testSevenMemory}/>

        </>)
})

export default ThousandTuples