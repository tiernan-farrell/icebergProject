import React from 'react'

const Button = ({onClick, children}) => {
    return (
        <button type="button" onClick={onClick}>
            {children}
        </button>
    )
}

export default Button