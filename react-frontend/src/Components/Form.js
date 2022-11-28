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
                <input type="text" id="tuples" placeholder='# tuples' onChange={(e) => setNumTuples(e.target.value)}></input>
                <label for="dims">Enter # of Dimensions</label>
                <select onChange={(e) => setNumDims(e.target.value)}>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <label for="card">Enter Cardinality</label>
                <input type="text" id="card" placeholder='Cardinality' onChange={(e) => setCard(e.target.value)}></input>
                <label for="minsup">Enter Minsup</label>
                <input type="text" id="minsup" placeholder='Minsup' onChange={(e) => setMinsup(e.target.value)}></input>
                <input type="submit" id="submit-button" onClick={onSubmit(numTuples, numDims, card, minsup)}></input>
    
            </form>
        </div>
        </>
    )
}

export default Form