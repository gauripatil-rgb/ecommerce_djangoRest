import React from 'react'
import { FaUser } from "react-icons/fa";
import { FaCartArrowDown } from "react-icons/fa";

const Navbar = () => {
  return (
    <div className='bg-amber-400'>
        <div className='flex justify-between h-10 w-100% m-auto'>
            {/* left side  */}
        <div className='font-bold '>
            <h1>JASSA</h1> 
        </div>
             {/* right side  */}
             <div className='flex '>
                <input type="text" placeholder='search'/>
                <FaUser />
                <FaCartArrowDown />
             </div>
        </div>         
    </div>
  )
}

export default Navbar