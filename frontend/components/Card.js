import React from 'react'

const Card = ({ name, desc, grades, school, score }) => {
    return (
        <div className='flex flex-col justify-center items-center'>
            <div className='hidden m-4 md:flex flex-col justify-center items-center bg-opacity-75 bg_white w-8/12  rounded-lg'>
                <div className='relative pt-2  '>
                    Query Match Score:<span className="font-bold"> {score.toFixed(3)}</span>
                </div>
                <div className='m-4 text-2xl'>{name}</div>
                <div className=' mx-10'>
                    {desc}
                </div>
                <div className='m-4 mb-6 w-full flex flex-row items-center justify-evenly text-xl'>
                    <div>Schools: {school}</div>
                    <div>Grades: {grades}</div>
                </div>
            </div>
            <div className='flex m-4 md:hidden flex-col justify-center items-center bg-opacity-75 bg_white w-12/12  rounded-lg'>
                <div className='relative pt-2  '>
                    Query Match Score:<span className="font-bold"> {score.toFixed(3)}</span>
                </div>
                <div className='m-4 text-2xl text-center '>{name}</div>
                <div className=' mx-10'>
                    {desc}
                </div>
                <div className='m-4 mb-6 w-full flex flex-row items-center justify-evenly text-xl'>
                    <div>Schools: {school}</div>
                    <div>Grades: {grades}</div>
                </div>
            </div>
        </div>
    )
}

export default Card