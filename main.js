
const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();
require('dotenv').config();
// const cors = require('cors');

// const corsOptions = {
//   origin: '*',
//   methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
//   allowedHeaders: ['Content-Type', 'Authorization', 'Accept', 'Origin', 'X-Requested-With'],
//   // maxAge: 3600, // 1 hour
// };

app.use(express.json());
app.use(cors());

const PORT =5000;

app.get('/', (req, res) => {
  res.send("Hello I am active");
})
// app.use('/',(req,res)=>{
//   console.log("Hello bhaiya");
// })

app.post('/api/generate', async (req, res) => {
  // return res.json("Hello bro");
  console.log("hello" + process.env.GEMINI_KEY_ID);
  try {
    // console.log(req.body);

    const response = await axios.post(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=${process.env.GEMINI_KEY_ID}`,
      {"contents": [
          {
            "parts": [{ "text": "Please focus solely on answering the current question without referencing past responses. However, remember all previous questions in memory for context without repeating or addressing them unless directly relevant to the current query."+ req.body.question }]
          }
       ]}
    );
    console.log(response.data.candidates[0].content.parts[0].text);
    return res.json(response.data.candidates[0].content.parts[0].text);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching the answer' });
  }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));