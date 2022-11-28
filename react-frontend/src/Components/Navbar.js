export default function Navbar(){
    return (
        <nav className="nav">
            <a href="/" className="site-title">Home</a>
            <ul>
                <CustomLink href="/about">About</CustomLink>
                <CustomLink href="/results">Test Results</CustomLink>

            </ul>
        </nav>
    )
}


export function CustomLink({ href, children, ...props}){
    const path = window.location.pathname
    console.log(path)
    return (
        <li>
            <a href = {href} {...props}>
                {children}
            </a>
        </li>

    )
}