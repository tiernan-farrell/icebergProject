import React from 'react'
import Graph from '../Components/Graph'
import ResultsNav from '../Components/ResultsNav'
import { testEightMemoryData, testEightTimeData, testNineMemoryData, testNineTimeData, testTenMemoryData, testTenTimeData, testEightMemory, testEightTime, testNineMemory, testNineTime, testTenMemory, testTenTime } from '../graphData'



const TenThousandTuples = (() => {
    return (
        <>
        <ResultsNav />
        <Graph data={testEightTimeData} title={testEightTime}/>
        <Graph data={testEightMemoryData} title={testEightMemory}/>


        <Graph data={testNineTimeData} title={testNineTime}/>
        <Graph data={testNineMemoryData} title={testNineMemory}/> 

        <Graph data={testTenTimeData} title={testTenTime}/>
        <Graph data={testTenMemoryData} title={testTenMemory}/>

        </>
    )
}
)
export default TenThousandTuples