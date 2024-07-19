const express = require('express');
const request = require('request');
const cors = require('cors');
const app = express();

app.use(express.json());
app.use(cors()); 

app.post('/proxy/jigyasa', (req, res) => {
    const url = 'http://10.152.2.137:7777/api/jigyasa';
    request.post({ url, json: req.body }, (error, response, body) => {
        if (error) {
            return res.status(500).send(error);
        }
        res.send(body);
    });
});

const PORT = 3002;
app.listen(PORT, () => {
    console.log(`Proxy server is running on port ${PORT}`);
});
