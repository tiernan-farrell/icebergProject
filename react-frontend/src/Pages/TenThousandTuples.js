import React from 'react'
import Graph from '../Components/Graph'
import ResultsNav from '../Components/ResultsNav'
import { 
    testThirteenMemory, testThirteenMemoryData, testThirteenTime, testThirteenTimeData,
    testFourteenMemory, testFourteenMemoryData, testFourteenTime, testFourteenTimeData,
    testFifteenMemory, testFifteenMemoryData, testFifteenTime, testFifteenTimeData,
    testSixteenMemory, testSixteenMemoryData, testSixteenTime, testSixteenTimeData,    
 } from '../graphData'

const TenThousandTuples = (() => {
    return (
        <>
        <ResultsNav />
        <Graph data={testThirteenTimeData} title={testThirteenTime}/>
        <Graph data={testThirteenMemoryData} title={testThirteenMemory}/>
        <Graph data={testFourteenTimeData} title={testFourteenTime}/>
        <Graph data={testFourteenMemoryData} title={testFourteenMemory}/>  
        <Graph data={testFifteenTimeData} title={testFifteenTime}/>
        <Graph data={testFifteenMemoryData} title={testFifteenMemory}/>
        <Graph data={testSixteenTimeData} title={testSixteenTime}/>
        <Graph data={testSixteenMemoryData} title={testSixteenMemory}/>
        </>
    )
}
)
export default TenThousandTuples