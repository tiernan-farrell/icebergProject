import React from 'react';
import { Label , Tooltip, Legend, LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';


const Graph = (({data, title}) => {

    return (
        <div id='charts'>
            <h4>{title.name}</h4>
            <LineChart
            width={600}
            height={500}
            data={data}
            margin={{
                top: 0,
                right: 10,
                left: 30,
                bottom: 25,
            }}
            >
                <CartesianGrid strokeDasharray="3 3" stroke="#5A5A5A"/>
                <XAxis dataKey="name" stroke='black'>
                    <Label value="Minsup" offset={19} position="bottom" style={{textAnchor: 'middle', fontSize: "150%"}}/>
                </XAxis>

                <YAxis stroke='black' angle={-45}>
                    
                    <Label angle={-90} value={title.label} position="left"  style={{textAnchor: 'middle', fontSize: "150%"}}/>
                </YAxis>
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="tdc" stroke="black"  />
                <Line type="monotone" dataKey="buc" stroke="green" />
                <Line type="monotone" dataKey="apriori" stroke="purple" />
            </LineChart>
        </div>
        )
}
)

export default Graph