import React,{useState,useEffect} from 'react'
import ListItem from '../components/ListItem'
import AddButton from '../components/AddButtion'

const ProductListPage = () => {
    let [Products,setProducts] = useState([])
    useEffect(()=>{
        getProducts()

    },[])

    let getProducts =  async () => {
        let response = await fetch('/api/products/')
        let data = await response.json()
        // console.log(data)
        setProducts(data)
    }
    return (
    <div className='notes'>
      
      <div className='note-header'>
        <h2 className='note-title'>&#9782; NOTES</h2>
        <p className='notes-count'>{Products.length}</p>
        </div>
      <div className='notes-list'>

        {Products.map((product,index) =>(
            <ListItem key={index} product={product} />

        ))}
        <AddButton/>
      </div>
    </div>
  )
}

export default ProductListPage
