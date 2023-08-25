import React from 'react'
import { Link} from 'react-router-dom'
const ListItem = ({product }) => {
  return (
    <div>
        <Link to={`/product/${product.id}`}>
          <div className='notes-list-item'>
        <h3 >{product.product_name}</h3>
        </div>
        </Link>
      
    </div>
  )
}

export default ListItem
