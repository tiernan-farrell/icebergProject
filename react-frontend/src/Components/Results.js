import React from 'react'

const Results = ({results}) => {

    return (
        <>
            <div id='results-table'>

                <p>{results.split("\",\"")}
                </p>    

            </div>
        </>
    )
}   

export default Results