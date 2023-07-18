"use client";

import { Limelight } from "next/font/google";
import React from 'react';
import { Image } from "@nextui-org/react";
import Nav from "./Nav";

const limelight = Limelight({ subsets: ['latin'], weight: '400' })

const Hero = () => {
  return (
    <div className="fixed w-screen h-5/6 top-0 bg-gradient-to-tr from-stone-200 to-black flex flex-col p-8">
        <Nav textcolor="white" logocolor="white" />

        <div className="relative w-full max-w-5xl h-full mb-20 grid place-content-center"> {/* container */}

            <div className="absolute bottom-0 right-0 z-5 grayscale-[100%] opacity-50"> {/* image */}
                <Image
                    src="/images/dragon-doorknocker.svg"
                    width={600}
                    height={600}
                />
            </div>

            <div className={`${limelight.className} absolute bottom-0 w-full leading-snug text-[80px] text-white z-10`}> {/* text */}
                <h1>Discover magical items for the ultimate quest.</h1>
            </div>

        </div>
    </div>
  )
}

export default Hero