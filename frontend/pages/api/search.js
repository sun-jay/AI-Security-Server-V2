const { Configuration, OpenAIApi } = require("openai");
import { PineconeClient } from "@pinecone-database/pinecone";


export default async function handler(req, res) {
    
        const wait = ms => new Promise(resolve => setTimeout(resolve, ms))
        // wait 2 seconds
        await wait(2000)
        .then(response => response.json())
        .then(data => {console.log(data)
        return res.status(200).json(['hello', 'world']);
        }
        
        
        )
        .catch(error => {console.error(error)
        return res.status(500).json({error: error});
        });

}



// const sendTwilio = async (perscription) => {
//     const res = await fetch("/api/twilio", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify({ drug: perscription, phone: FBuser.phone }),
//     });
// };