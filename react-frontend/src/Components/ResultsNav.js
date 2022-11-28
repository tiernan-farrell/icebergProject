import { CustomLink } from "./Navbar"

export default function ResultsNav(){
    return (
        <nav className="nav">
            <ul>
                <CustomLink href="/hundred">100 Tuples</CustomLink>
                <CustomLink href="/fivehundred">500 Tuples</CustomLink>
                <CustomLink href="/thousand">1000 Tuples</CustomLink>
                <CustomLink href="/tenthousand">10000 Tuples</CustomLink>
            </ul>
        </nav>
    )
}

