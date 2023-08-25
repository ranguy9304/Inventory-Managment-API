import React from 'react'
import { Link} from 'react-router-dom'
const AddButtion = () => {
  return (
    <Link to="/product/new" className='floating-button'>
        <h3>ADD</h3>
    </Link>
  )
}

export default AddButtion
