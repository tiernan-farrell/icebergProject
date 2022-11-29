import React from 'react'
import Graph from '../Components/Graph'
import ResultsNav from '../Components/ResultsNav'
import { testOneTimeData, testOneMemoryData, testTwoMemoryData, testTwoTimeData, testOneTime, 
    testOneMemory, testTwoTime, testTwoMemory, testThreeMemory, testThreeMemoryData, testThreeTime, testThreeTimeData,
    testFourMemory, testFourTime, testFourMemoryData, testFourTimeData
} from '../graphData'


const HundredTuples = () => {
    return (
        <>
        <ResultsNav />
        <Graph data={testOneTimeData} title={testOneTime}/>
        <Graph data={testOneMemoryData} title={testOneMemory}/>
        <Graph data={testTwoTimeData} title={testTwoTime}/>
        <Graph data={testTwoMemoryData} title={testTwoMemory}/>  
        <Graph data={testThreeTimeData} title={testThreeTime}/>
        <Graph data={testThreeMemoryData} title={testThreeMemory}/>
        <Graph data={testFourTimeData} title={testFourTime}/>
        <Graph data={testFourMemoryData} title={testFourMemory}/>
        </>    
    )
}

export default HundredTuples