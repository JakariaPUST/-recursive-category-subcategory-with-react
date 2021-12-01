import { Container } from 'react-bootstrap'
import { BrowserRouter as Router, Route } from 'react-router-dom'

import Footer from './components/Footer'
import Header from './components/Header'

import HomeScreens from './sreens/HomeScreens'
import ProductScreen from './sreens/ProductScreen'
import CartScreen from './sreens/CartScreen'
import LoginScreen from './sreens/LoginScreen'
import RegisterScreen from './sreens/RegisterScreen'



function App() {
  return (
    <Router>
      
      <Header></Header>
      <main className="py-3">
        <Container>
        <Route path='/' component={HomeScreens} exact/>
        <Route path='/login' component={LoginScreen} />
        <Route path='/register' component={RegisterScreen} />
        
        <Route path='/product/:id' component={ProductScreen} />
        <Route path='/cart/:id?' component={CartScreen} />
        </Container>
      </main>
      <Footer></Footer>
      
    </Router>
  );
}

export default App;
