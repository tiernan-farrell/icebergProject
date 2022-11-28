import React from 'react'
import Graph from '../Components/Graph'
import ResultsNav from '../Components/ResultsNav'
import { testThreeTimeData, testThreeMemoryData, testFourTimeData, testFourMemoryData, testThreeTime, testThreeMemory,  testFourMemory, testFourTime } from '../graphData'

const FiveHundredTuples = (() => {
    return (
        <>
        <ResultsNav />
        <Graph data={testThreeTimeData} title={testThreeTime}/>
        <Graph data={testThreeMemoryData} title={testThreeMemory}/>


        <Graph data={testFourTimeData} title={testFourTime}/>
        <Graph data={testFourMemoryData} title={testFourMemory}/>
        </>
    )
})

export default FiveHundredTuples