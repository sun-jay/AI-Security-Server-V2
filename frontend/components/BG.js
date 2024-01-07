import React from 'react'

const BG = () => {
    return (
        <div className=" changebg fixed w-screen h-screen top-0 left-0 z-[-2]">
            {/* make z index negative 1 */}
          <div className='blob-c flex justify-center items-center fixed w-screen h-screen top-0 left-0'>
            <div class="shape-blob"></div>
            <div class="shape-blob one"></div>
            <div class="shape-blob two"></div>
            <div class="shape-blob three"></div>
            <div class="shape-blob four"></div>
            <div class="shape-blob five"></div>
            <div class="shape-blob six"></div>
          </div>
        </div>
      )}


export default BG