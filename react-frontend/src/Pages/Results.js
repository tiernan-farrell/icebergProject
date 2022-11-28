import React from "react";
import Graph from "../Components/Graph";
import { testOneTimeData, testOneMemoryData, testTwoTimeData, testTwoMemoryData, testThreeTimeData, testThreeMemoryData, testFourTimeData, testFourMemoryData, testFiveTimeData, testSixMemoryData, testSevenTimeData, testSevenMemoryData, testEightTimeData, testEightMemoryData, testNineTimeData, testNineMemoryData, testTenTimeData, testTenMemoryData } from "../graphData";


const testOneTime = {name: '100 Tuples, 5 Dimensions, 2 Cardinality', 
                label: 'Runtime (seconds)'}
const testOneMemory = {name: '100 Tuples, 5 Dimensions, 2 Cardinality', 
                label: 'Memory (bytes)'}

const testTwoTime = {name: '100 Tuples, 5 Dimensions, 5 Cardinality',
                label: 'Runtime (seconds)'}
const testTwoMemory = {name: '100 Tuples, 5 Dimensions, 5 Cardinality', 
label: 'Memory (bytes)'}

const testThreeTime = {name: '500 Tuples, 3 Dimensions, 5 Cardinality',
                label: 'Runtime (seconds)'}
const testThreeMemory = {name: '500 Tuples, 3 Dimensions, 5 Cardinality',
label: 'Memory (bytes)'}

const testFourTime = {name: '500 Tuples, 6 Dimensions, 8 Cardinality',
                label: 'Runtime (seconds)'}
const testFourMemory = {name: '500 Tuples, 6 Dimensions, 8 Cardinality',
label: 'Memory (bytes)'}

const testFiveTime = {name: '1000 Tuples, 3 Dimensions, 6 Cardinality',
                label: 'Runtime (seconds)'}
const testFiveMemory = {name: '1000 Tuples, 3 Dimensions, 6 Cardinality',
label: 'Memory (bytes)'}

const testSixTime = {name: '1000 Tuples, 5 Dimensions, 4 Cardinality',
                label: 'Runtime (seconds)'}
const testSixMemory = {name: '1000 Tuples, 5 Dimensions, 4 Cardinality',
label: 'Memory (bytes)'}

const testSevenTime = {name: '1000 Tuples, 7 Dimensions, 9 Cardinality',
                label: 'Runtime (seconds)'}
const testSevenMemory = {name: '1000 Tuples, 7 Dimensions, 9 Cardinality',
label: 'Memory (bytes)'}

const testEightTime = {name: '10000 Tuples, 6 Dimensions, 6 Cardinality',
                label: 'Runtime (seconds)'}
const testEightMemory = {name: '10000 Tuples, 6 Dimensions, 6 Cardinality',
label: 'Memory (bytes)'}

const testNineTime = {name: '10000 Tuples, 8 Dimensions, 2 Cardinality',
                label: 'Runtime (seconds)'}
const testNineMemory = {name: '10000 Tuples, 8 Dimensions, 2 Cardinality',
label: 'Memory (bytes)'}

const testTenTime = {name: '10000 Tuples, 10 Dimensions, 5 Cardinality',
                label: 'Runtime (seconds)'}
const testTenMemory = {name: '10000 Tuples, 10 Dimensions, 5 Cardinality',
label: 'Memory (bytes)'}


const Results = (() => {
    return (
        <div id='charts-box'>
            <Graph data={testOneTimeData} title={testOneTime}/>
            {/* <Graph data={testOneMemoryData} title={testOneMemory}/>


            <Graph data={testTwoTimeData} title={testTwoTime}/>
            <Graph data={testTwoMemoryData} title={testTwoMemory}/>


            <Graph data={testThreeTimeData} title={testThreeTime}/>
            <Graph data={testThreeMemoryData} title={testThreeMemory}/>


            <Graph data={testFourTimeData} title={testFourTime}/>
            <Graph data={testFourMemoryData} title={testFourMemory}/>


            <Graph data={testFiveTimeData} title={testFiveTime}/>
            <Graph data={testFiveMemoryData} title={testFiveMemory}/>


            <Graph data={testSixTimeData} title={testSixTime}/>
            <Graph data={testSixMemoryData} title={testSixMemory}/>


            <Graph data={testSevenTimeData} title={testSevenTime}/>
            <Graph data={testSevenMemoryData} title={testSevenMemory}/>


            <Graph data={testEightTimeData} title={testEightTime}/>
            <Graph data={testEightMemoryData} title={testEightMemory}/>


            <Graph data={testNineTimeData} title={testNineTime}/>
            <Graph data={testNineMemoryData} title={testNineMemory}/> 
            
            <Graph data={testTenTimeData} title={testTenTime}/>
            <Graph data={testTenMemoryData} title={testTenMemory}/> */}
        </div>
    )
})

export default Results