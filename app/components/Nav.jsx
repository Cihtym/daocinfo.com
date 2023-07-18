"use client";

import Link from "next/link";
import Image from "next/image";

const Nav = ({ textcolor, logocolor }) => {
  return (
    <nav className="flex justify-between items-center w-full mb-2 gap-2 z-50">
      <Link href='/'>
        <Image 
          // src='/images/navbar-logo.png'
          src={`/images/daocinfo-logo-${logocolor}.svg`}
          alt='logo'
          width={115}
          height={115}
          className='object-contain'
        />
        {/* <p className='max-sm:hidden font-satoshi font-semibold text-2xl text-black tracking-wide'>DAoC Info</p> */}
      </Link>
      <div className={`justify-end text-${textcolor} font-semibold text-lg`}>
        {/* <Link href='/Chimp' className="px-3">
          Chimp
        </Link> */}
        <Link href='/search_items' className="px-3">
          Search Items
        </Link>
        <Link href='/browse_templates' className="px-3">
          Browse Templates
        </Link>
        <Link href='/templater' className="px-3">
          Build a Template
        </Link>
      </div>
    </nav>
  )
}

export default Nav
