import '/styles/globals.css'
import { Inter } from 'next/font/google'

import Nav from './components/Nav';
import Provider from './components/Provider';
import Equipment from "./components/EquipmentCard";

export const metadata = {
  title: 'DAoC Info',
  description: 'Companion App for Dark Age of Camelot',
}


const RootLayout = ({ children }) => {
  return (
    <html lang="en">
        <body>
            <Provider>
                <div className="main">
                    <div className="gradient" />
                </div>

                <main className="app">
                    <Nav />
                    {children}
                </main>
            </Provider>
        </body>
    </html>
  )
}

export default RootLayout