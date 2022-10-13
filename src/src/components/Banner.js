import logo from '../assets/logo.webp'
import '../styles/Banner.css'

function Banner() {
    const title = 'crvo'
    const altLogo = 'crvo'
    return (
    <div className='main-title'>
        <img src={logo} alt={altLogo} className='logo' />
        <h1>{title}</h1>
    </div>)
}

export default Banner