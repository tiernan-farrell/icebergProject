import React from 'react';
import { Label , Tooltip, Legend, LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';


const Graph = (({data, title}) => {

    return (
        <div id='charts'>
            <h4>{title.name}</h4>
            <LineChart
            width={500}
            height={400}
            data={data}
            margin={{
                top: 0,
                right: 30,
                left: 20,
                bottom: 50,
            }}
            >
                <Label value="100 tuples" offset={0} position="top" />
                <CartesianGrid strokeDasharray="3 3" stroke="#5A5A5A"/>
                <XAxis dataKey="name" stroke='black'>
                <Label value="Minsup" offset={20} position="bottom" />
                </XAxis>

                <YAxis stroke='black'>
                    <Label value={title.label} position="insidebottomleft" angle={-90} offset={20} />
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