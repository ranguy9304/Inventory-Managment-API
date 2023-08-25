import {
  BrowserRouter as Router,
  Route, 
  Routes
}from "react-router-dom";
import './App.css';
import Header from './components/Header';
import ProductListPage from './pages/ProductListPage';
import SingleProduct from './pages/SingleProduct';
function App() {
  return (
    <Router>
      <div className="container">
      <div className="app">
        <Header />
        <Routes>
          <Route path="/" exact element={<ProductListPage/>} />
          <Route path="/product/:id" element={<SingleProduct/>} />
        </Routes>
      </div>
      </div>
    </Router>
  );
}


export default App;
