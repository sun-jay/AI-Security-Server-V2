import React, { useEffect } from 'react'
import { useState } from 'react'
import { motion, LayoutGroup, AnimatePresence } from "framer-motion";
import LoadingDots from "../components/LoadingDots";
import BG2 from '../components/BG2';
import RandomButton from '../components/RandomButton';
import Card from '../components/Card';
import VideoComponent from '../components/VideoComponent';

const Index = () => {
    const [inp, setInp] = useState("")
    const [res, setRes] = useState(false)
    const [output, setOutput] = useState("")
    const [loading, setLoading] = useState(false)
    const [numswitch, setNumswitch] = useState(0)
    const [usedNums, setUsedNums] = useState(new Set([]))
    const [infoUp, setInfoUp] = useState(false)
    const [videoUrl, setVideoUrl] = useState('');
    const [time_range, setTimeRange] = useState([0, 10])

    // handle_search = () => {
    //     str = 'https://api.srvusd.net/semantic_search?query='
    //     setRes(str.repeat(10))
    // }

    const fetchVideo = async () => {
        try {
            const response = await fetch('http://localhost:8000/query', {
                method: 'POST', // *GET, POST, PUT, DELETE, etc.
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ start_time: 0, end_time: 10, query: inp }) 
            });

            // const response = await fetch('http://localhost:8000/get_video');


            const videoBlob = await response.blob();
            const url = URL.createObjectURL(videoBlob);
            console.log(url)
            setVideoUrl(url)
        } catch (error) {
            console.error('Error fetching the video', error);
        }
    };

    const search = async (query) => {

        // if quety is too long, alert user and return
        if (query.length > 70) {
            alert('Query too long')
            return
        }

        setLoading(true)

        fetchVideo().then(() => {
            setLoading(false)
            setRes(true)
        })

    };
    const [isHovering, setIsHovering] = useState(false);

    const handleMouseEnter = () => {
        setIsHovering(true);
    };

    const handleMouseLeave = () => {
        setIsHovering(false);
    };

    const random_switch = () => {
        setIsHovering(true);
        setTimeout(() => {
            setIsHovering(false);
        }, 500);
    };

    // get a random float between 1.5 and 2.5
    const randomFloat = (min, max) => {
        if (numswitch > 5) {
            console.log('rando')

            return Math.random() * (max - min) + min;
        } else {
            console.log('random float')
            return Math.random() * ((max + 10) - min) + min;
        }
    };
    useEffect(() => {
        // call random switch every 5 seconds
        const interval = setInterval(() => {
            random_switch();
        }, randomFloat(1, 2) * 1000);
        return () => clearInterval(interval);
    }, []);

    const random_prompts = [
        'who made teslas',
        'plastic cups',
        "What was Beethoven's favorite food",
        'Nvidia GeForce RTX 3090',
        'Indian Food',
        'Internal Combustion Engine',
        "Fighting among friends",
        'george washington',
        "I forgot to pay my taxes",
        "Biggie Smalls",
        "Drake",
        "Honey Bees",
        "Driving my spaceship into the sun",
        'Fortnite battle royale',
        'Warhammer 40k',
        'Taylor Swift',
        'JavaScript',
        'new red pen',
        'magic wand',
        'Youtube',
        'Britain and Zanzibar',
        'Pareidolia',
        "Schrödinger's cat"
    ]
    const get_random_prompt = () => {
        let unusedIndexes = random_prompts.map((val, ind) => ind).filter((val) => !usedNums.has(val));

        // If all indexes have been used, reset the set of used indexes
        if (unusedIndexes.length === 0) {
            setUsedNums(new Set([]));
            unusedIndexes = random_prompts.map((val, ind) => ind);
        }

        // Choose a random index from the unused indexes
        const randomIndex = unusedIndexes[Math.floor(Math.random() * unusedIndexes.length)];

        // Add the index to the set of used indexes
        setUsedNums(usedNums.add(randomIndex));

        // Return the random prompt
        return random_prompts[randomIndex];
    }
    const handleKeyDown = (event) => {
        if (event.keyCode === 13) {
            // The Enter key was pressed, so submit the input
            search(inp).then(() => {
                setRes(true)
            }
            )
        }
    }


    return (
        <div>
            <div className={!res ? 'text-white flex flex-col items-center justify-center w-screen h-screen' : 'flex flex-col text-white items-center justify-center w-screen h-full'}    >
                <BG2 />
                <AnimatePresence>
                    {/* {!res && (
                        <motion.div
                            transition={!res ? { duration: 2 } : { duration: 0.5 }}
                            initial={{ y: "-100%" }}
                            animate={{ y: 0 }}
                            exit={{ y: "-2500%" }}
                            className='flex md:hidden flex-col absolute items-center justify-center top-[4%]'
                        >
                            <div onClick = {() => setInfoUp(!infoUp)} className='w-11/12 md:w-8/12 text-center flex flex-col items-center justify-center rounded-xl p-4 bg_white'>
                                {!infoUp?(<h1  className="w-full mb-3 text-xl md:text-3xl font-bold ">
                                    What is a Semantic Search Engine?
                                </h1>):
                                (<h1 className=" md:block text-md md:text-sm text-center w-12/12 mb-3 ">
                                    
                                </h1>)}
                            </div>
                        </motion.div>)}
                        {!res && (
                        <motion.div
                            transition={!res ? { duration: 2 } : { duration: 0.5 }}
                            initial={{ y: "-100%" }}
                            animate={{ y: 0 }}
                            exit={{ y: "-2500%" }}
                            className='hidden md:flex flex-col absolute items-center justify-center top-[4%]'
                        >
                            <div className='w-11/12 md:w-8/12 text-center flex flex-col items-center justify-center rounded-xl p-4 bg_white'>
                                <h1 className="w-full mb-3 text-xl md:text-3xl font-bold ">
                                    What is a Semantic Search Engine?
                                </h1>
                                <h1 className=" hidden md:block text-xs md:text-sm text-center w-12/12 mb-3 ">
                                
                                </h1>
                            </div>
                        </motion.div>)} */}




                </AnimatePresence>

                <motion.div layout transition={{ duration: 0.5 }} >
                    <motion.div>
                        <div className='mt-10 flex flex-col items-center justify-center w-full'>
                            <h1 className="text-5xl md:text-6xl text-center mb-3 font-bold  rounded-xl p-4 bg_white">
                                <div className="px-80">AI CCTV Search</div>
                                <div className="pt-1 text-sm">A <span class="underline"><a target="_blank"
                                    rel="noreferrer"
                                    href="https://www.sunny-jay.com/">Sunny Jayaram</a></span> Production</div>
                            </h1>
                            {/* this div will ve a horizontal flex box */}
                            <div className="hidden mb-4 md:flex flex-row items-center justify-center w-full h-1/12 text-center ">
                                <button onMouseEnter={handleMouseEnter}
                                    onMouseLeave={handleMouseLeave}
                                    className=" m-4 p-4 w-1/12 bg_white font-bold text-center rounded-xl hover:bg-pink-800 search flex items-center justify-center"
                                    onClick={() => {

                                        // date range picker
                                        
                                    }}
                                >
                                    Time Range</button>
                                <input
                                    onKeyDown={handleKeyDown}
                                    className="p-4 w-6/12 text-center text-black rounded-xl border-0"
                                    value={inp}
                                    type="text"
                                    placeholder="Search using the power of AI"
                                    onChange={(e) => {
                                        setInp(e.target.value)
                                    }}
                                />
                                <button onClick={() => search(inp).then(() => {
                                    setRes(true)
                                })}
                                    className="bg_white search m-4 p-4 w-1/12 text-center font-bold rounded-xl flex items-center justify-center">
                                    {loading ? <LoadingDots color="white" style="large" /> : "Search"}
                                </button>
                            </div>
                            <div className="md:hidden mb-4 flex flex-col items-center justify-center w-full h-1/12">

                                <input
                                    onKeyDown={handleKeyDown}
                                    className="p-4 w-full text-center text-black rounded-xl border-0"
                                    value={inp}
                                    type="text"
                                    placeholder="Search using the power of AI"
                                    onChange={(e) => {
                                        setInp(e.target.value)
                                    }}
                                />
                                <div className='flex w-full items-center justify-center'>
                                    <button onMouseEnter={handleMouseEnter}
                                        onMouseLeave={handleMouseLeave}
                                        className={isHovering ? "go_crazy bg_white font-bold m-4 p-4 w-6/12 text-center  rounded-xl" :
                                            " m-4 p-4 w-6/12 bg_white font-bold text-center  rounded-xl"
                                        }
                                        onClick={() => {
                                            var x = get_random_prompt()
                                            setInp(x)
                                            search(x).then(() => {
                                                setRes(true)
                                            })
                                        }}
                                    >
                                        Random!</button>
                                    <button onClick={() => search(inp).then(() => {
                                        setRes(true)
                                    })}
                                        className="bg_white search m-4 p-4 w-6/12 text-center font-bold rounded-xl text-center">
                                        {loading ? <LoadingDots color="white" style="large" /> : "Search"}
                                    </button>

                                </div>
                            </div>



                        </div>
                    </motion.div>
                </motion.div >
                <div className=''>
                    {res && (
                        <motion.div
                            transition={{ duration: 0.5 }}
                            initial={{ y: "100%" }}
                            animate={{ y: 0 }}
                            exit={{ y: "100%" }}
                            className=''
                        >
                            <div className='flex items-center justify-center pb-16'>
                                <VideoComponent videoUrl={videoUrl} />
                                {/* hello */}
                            </div>
                        </motion.div>
                    )}
                </div>
                {/* <div className=' invisible w-6/12 text-center flex flex-col items-center justify-center rounded-xl p-4 bg_white'>
                    <h1 className="sm:text-3xl text-4xl mb-3 font-bold ">
                        What is a Semantic Search Engine?
                    </h1>

                    <h1 className="sm:text-xl text-4xl mb-3 ">
                        A semantic search engine is a search engine that uses semantic analysis to understand the meaning of the words in a query and the meaning of the words in the documents it indexes.
                    </h1>

                </div> */}
            </div>
        </div>

    )
}

export default Index
