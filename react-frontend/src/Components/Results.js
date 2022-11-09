import React from 'react'

const Results = ({results}) => {
    const s = results.split("\",\"")[0].replaceAll('[', '').replaceAll(']', '')
    var dim = 0
    var res = []
    var temp = []
    for(var i =0; i<s.length; i++) { 
        if(s[i] === ',') { 
            dim = 0
            res.push(temp)
            temp = []
        }
        else  {
            temp.push(s[i])
        }

        dim += 1

    }
    console.log(typeof res)
    const dims =2
    return (
        <>
                <p>{results}
                {/* {s} 
                {res.map((e, i) => i%dims===0 ? ' ': e)} */}
                </p>    
        </>
    )
}   

export default Results