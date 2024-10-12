import NavbarRegion from "./NavbarRegion"
import Years from "./NavbarYears"

export default function Navbar(){
    return(
        <div className="flex justify-around my-3">
            <h1 className="text-3xl font-bold">Dwello</h1>
            <NavbarRegion/>
            <Years/>
        </div>
    )
}