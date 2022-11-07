import React, {useState} from 'react'

const Form = ({onSubmit}) => {  

    const [minsup, setMinsup] = useState(1)
    const [card, setCard] = useState(7)
    const [numDims, setNumDims] = useState(5)
    const [numTuples, setNumTuples] = useState(1000)

  
  
    return (
        <>
        <div id="form-wrapper">
            <form>
                <label for="tuples">Enter # of Tuples</label>
                <input type="text" id="tuples" placeholder='Enter Number of Tuples' onChange={(e) => setNumTuples(e.target.value)}></input>
                <label for="tuples">Enter # of Dimensions</label>
                <input type="text" id="dims" placeholder='Enter Number of Dimensions' onChange={(e) => setNumDims(e.target.value)}></input>
                <label for="tuples">Enter Cardinality</label>
                <input type="text" id="card" placeholder='Enter Cardinality' onChange={(e) => setCard(e.target.value)}></input>
                <label for="minsup">Enter Minsup</label>
                <input type="text" id="minsup" placeholder='Enter Minsup' onChange={(e) => setMinsup(e.target.value)}></input>
                <input type="submit" id="submit-button" onClick={onSubmit(numTuples, numDims, card, minsup)}></input>
    
            </form>
        </div>
        </>
    )
}

export default Form