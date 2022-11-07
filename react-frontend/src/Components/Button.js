import React from 'react'

const Button = ({onClick, id, children}) => {
    return (
        <button id={id} className='mainbuttons' type="button" onClick={onClick}>
            {children}
        </button>
    )
}

export default Button