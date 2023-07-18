import '/styles/globals.css'
// import { Inter } from 'next/font/google'

import Provider from './components/Provider';

export const metadata = {
  title: 'DAoC Info',
  description: 'Companion App for Dark Age of Camelot',
}

const RootLayout = ({ children }) => {
  return (
    <html lang="en">
        <body>
            <Provider>
                <main className="relative z-10 flex justify-center items-center flex-col max-w-7xl mx-auto sm:px-16">
                    {children}
                </main>
            </Provider>
        </body>
    </html>
  )
}

export default RootLayout