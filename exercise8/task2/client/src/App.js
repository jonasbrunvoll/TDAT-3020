import React, {useState} from 'react';
import './App.css';
import './App.css'
const crypto = require('crypto');
const axios = require('axios').default;
const iterations = 2048;
const digest = 'sha1';
const keylen = 20;


function App() {
    const [logIn, setLogin] = useState(false);
    if (!logIn){
        return (
            <div>
                <LogIn loginCallback = {setLogin}/>
            </div>
        );
    } else {
        return(
            <div>
                <LoggedIn loggedInCallback = {setLogin}/>
            </div>
        );
    }


    function LogIn({loginCallback}) {

        const [name, setName] = useState("");
        const [password, setPassword] = useState("");

        function generateHash(salt){
            let hash = crypto.pbkdf2Sync(password, salt, iterations, keylen, digest).toString('hex');
            return hash;
        }

        function generateSalt(name) {
            let salt = name+name;
            return salt;
        }

        function findUser() {
            axios.get('/users')
                .then((response) => {
                    let message = "Password / username can not be null";
                    if (name !== "" || password !==""){
                        message = "Could not find user";
                        if (response.data != null){
                            for(let i = 0; i < response.data.length; i++){
                                if (name === response.data[i].name) {
                                    message = "The user: '"+response.data[i].name+ "' exist!";
                                    console.log(message);
                                    console.log(response.data[i]);
                                    return true;


                                }
                             message ="Could not find matching hash keys";
                            }
                        }
                    }
                    console.log(message);
                    return false;
                })
                .catch(error => {
                    console.log(error);
                    return false;
                });
            return false;
        }

        function addNewUser(){
            if (name !== "" && password!==""){
                if (!findUser()){
                    let salt = generateSalt(name);
                    let hash_key = generateHash(salt);
                    axios.post('/regUser', {name, hash_key})
                        .then(response => {
                            console.log(response);
                            console.log("Bruker lagt til. Nå kan du logge inn!");
                        })
                        .catch(error => {
                            console.log(error)
                        });
                } else {
                    console.log("User already exist!");
                }
            } else {
                console.log("Password and username cant be null");
            }

        }

        function logIn(){
            let message = "Password / username can not be null";
            if (name !== "" && password!==""){
                message = "could not find user ";
                if (findUser) {
                    let salt = generateSalt(name);
                    let hash_key = generateHash(salt);
                    axios.post('/login', {name, hash_key})
                        .then(response => {
                            //Saves token in localStorage
                            localStorage.setItem('token', response.data.Authorization);
                            //Adds the token to the header
                            const header = {
                                headers : {
                                    "Authorization": localStorage.getItem("token"),
                                    'Content-Type': 'application/json;charset=UTF-8',
                                    "Access-Control-Allow-Origin": "*",
                                }
                            };
                            console.log(header);
                            if(response.status === 200){
                                loginCallback(true);
                            }
                        })
                        .catch( error => {
                            console.log(error);
                        })
                } else {
                    console.log(message)
                }
            } else {
                console.log(message)
            }
        }
        return (
            <div className="App">
                <header className="App-header">
                    <h1>Registrer bruker eller logg inn</h1>
                    <input placeholder="Username" id="username" type="text" onChange={text => setName(text.target.value)}/>
                    <br/>
                    <input placeholder="Password" id="password" type="text" onChange={text => setPassword(text.target.value)}/>
                    <br/>
                    <button onClick={addNewUser}>Register ny bruker</button>
                    <br/>
                    <button onClick={logIn}>LogIn</button>
                </header>
            </div>
        );
    }



    function LoggedIn({loggedInCallback}) {

        const [displayText, setDisplayText] = useState("Hello World");

        function logOut(){
            loggedInCallback(false);
            console.log("You are no logged out");
        }

        function refresh(){
            //Adds the token to the header again.
            const header = {
                headers : {
                    "Authorization": localStorage.getItem("token"),
                    'Content-Type': 'application/json;charset=UTF-8',
                    "Access-Control-Allow-Origin": "*",
                }
            };
            console.log(header);
            axios.get("http://localhost:3000/", header).then(res => {
                if(res.status === 200){
                    setDisplayText("Access token: " + header.headers.Authorization);
                }
            }).catch(rej => console.log(rej));

        }
        return(
            <div className="App">
                <header className="App-header">
                    <h1>Du er logget inn</h1>
                    <br/>
                    <button onClick={refresh}>Refresh</button>
                    <br/>
                    <button onClick={logOut}>Log out</button><br/>
                    <br/>
                    {displayText}
                </header>
            </div>
        );

    }
}

export default App;

