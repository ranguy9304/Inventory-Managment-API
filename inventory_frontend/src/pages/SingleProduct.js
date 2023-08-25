import React ,{useState,useEffect} from 'react'
import { Link, useParams,useNavigate } from 'react-router-dom'



const SingleProduct = ({} ) => {

    const {id} =useParams()
    const navigate = useNavigate()
    let product_id =id
    // console.log(id+ "dsfsdf")
    let [product , setProduct]= useState(null)

    useEffect(()=>{
      getProduct()

    },[product_id])
    let getProduct = async ()=>{
      let response =await fetch(`/api/product/${product_id}/`)
      let data =await response.json()
      setProduct(data)
    }
    let updateProduct = async ()=>{
      
      // let response =await fetch(`/api/product/${product_id}/`)
      // let data =await response.json()
      // console.log("simething "+data)
      // console.log(data)
      fetch(`http://127.0.0.1:8000/api/product/${product_id}/update/`,{
        method: "PUT",
        headers:{
          'Content-Type':'application/json'
        },
        body:JSON.stringify(product)
      })

    }
    let deleteProduct = async ()=> {
      fetch(`http://127.0.0.1:8000/api/product/${product_id}/delete/`,{
        method: "DELETE",
        headers:{
          'Content-Type':'application/json'
        },
        
      })
      navigate('/')
    }

    let handleSubmit = () =>{
      
      updateProduct()
      navigate('/')
    }
    let saveProduct = async () =>{
      fetch(`http://127.0.0.1:8000/api/product/new/`,{
        method: "POST",
        headers:{
          'Content-Type':'application/json'
        },
        body:JSON.stringify(product)})
        console.log("in save")
      
      navigate('/')}

  return (
    <div className='note'>
      <div className='note-header'>
       
        <h3 onClick={handleSubmit}>Back</h3>
        {product_id !== 'new' ?        <button onClick={deleteProduct}>DELETE</button>
        :  <button onClick={saveProduct}>SAVE</button>}

      
      </div>
      <textarea onChange={(e)=> {setProduct({...product,'product_name':e.target.value})}} value={product?.product_name}></textarea>
    </div>
  )
}

export default SingleProduct
