const bodyParser = require("express");
const crypto = require('crypto');
const express = require('express');
const path = require('path');
const app = express();
let jsonParser = bodyParser.json();
app.use(jsonParser);

const iterations = 2048;
const digest = 'sha1';
const keylen = 20;


//Acts like dummy databases
let users =[];
let tokens = [];


function chechIfUserExist(name){
    for (let i = 0; i < users.length; i++){
        if (name === users[i].name){
            console.log("The username: '" + name+"' already exist");
            return true;
        }
    }
    return false;
}

function chechHash_Key(hash_key){
    for (let i = 0; i < users.length; i++){
        let salt = users[i].salt;
        let tryHash = crypto.pbkdf2Sync(hash_key,salt, iterations, keylen, digest).toString('hex');
        if (tryHash === users[i].hash_key){
            console.log("The username: '" + hash_key+"' already exist");
            return true;
        }
    }
    return false;
}

app.get('/users', jsonParser, (request, response) => {
    console.log("Returning list of users from server");
    response.send(users);
});

    //Retrives all tokens. Handy for testing in postman.
app.get('/tokens', jsonParser, (request, response) => {
    if (tokens !== null){
        console.log(response);
        response.send(tokens);
    } else {
        console.log("Token list is empty");
    }
});


app.post('/regUser', jsonParser, (request, response) => {
    console.log("Register request...");
    if (!chechIfUserExist(request.body.name)){
        let salt = request.body.name + request.body.name;
        let hash_key = crypto.pbkdf2Sync(request.body.hash_key,salt, iterations, keylen, digest).toString('hex');
        let newUser = {
            name : request.body.name,
            salt : salt,
            hash_key : hash_key
        };
        users.push(newUser);
        console.log('New user registered: ' + request.body.name);
        response.send('You are now registered!');
    }
});

app.post('/login', (request, response) => {
    console.log('Login request...');
    if (chechIfUserExist(request.body.name)){
        if (chechHash_Key(request.body.hash_key)){
            const randomToken = Math.random().toString(36).substring(2);
            const newToken = {
                token: randomToken
            };
            tokens.push(newToken);
            response.send({"Authorization" : "Bearer " + newToken.token});

        }
    } else {
    console.log('Invalid request');
    response.sendStatus(404);
    }
});

//Set the port that you want the server to run on
const port = process.env.PORT || 8080;
app.listen(port);
console.log('App is listening on port ' + port);

