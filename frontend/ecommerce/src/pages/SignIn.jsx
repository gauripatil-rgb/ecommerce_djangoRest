import React from 'react'

const SignIn = () => {
  return (
    <>
      <div>
        <h1>Login</h1>
        <form action="">
          
          <label htmlFor="">Username</label>
          <input className='border-2' type='text' placeholder='enter username'/>
          <br />
          <label htmlFor="">Password</label>
          <input className='border-2' type="password" placeholder='enter password'/>
          <br/>
          <button>Login</button>
        </form>
      </div>
    </>
  )
}

export default SignIn