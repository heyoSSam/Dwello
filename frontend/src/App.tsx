import Footer from "./components/Footer/Footer"
import Navbar from "./components/Navbar/Navbar"

function App() {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar/>
      <div className='flex-grow text-center'>
        
      </div>

      <footer>
        <Footer/>
      </footer>
    </div>
  )
}

export default App
