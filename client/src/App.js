import React, { useState, useEffect } from "react";

function App() {

  const [text, setText] = useState(""); // React state to store the textbox input
  const [email, setEmail] = useState("") // React state to store the email input
  const [status, setStatus] = useState(false) // Checks if Emails are being sent
  const [res, setRes] = useState(null) // Sends over response from backend

  // Handle input changes
  const handleInputChange = (event) => {
    setText(event.target.value);
  };

  const handleInputChangeEmail = (event) => {
    setEmail(event.target.value)
  } 

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();
    setStatus(true);

    // Send the input data to the Flask backend
    const response = await fetch("http://localhost:5000/api/text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: text, email: email }), // Send the text as JSON
    });

    const result = await response.json(); // Parse the JSON response
    setRes(result) // Brings response to Frontend
    console.log(result); // Handle the response from Flask
  };

  let Content
  if (status === false) {
    Content = <>
    <div>
      <form onSubmit={handleSubmit}>
        <p>
        <input
          placeholder="Search Query"
          type="text"
          value={text}
          onChange={handleInputChange} // Update the state text when the user types
        ></input>
        Stick to One Word Searchs
        </p>
        <p>
        <input
          placeholder="Email"
          type="text"
          value={email}
          onChange={handleInputChangeEmail} // Update the state email when the user types
          ></input>
          </p>
          <p>
        <button type="submit" >Submit</button>
        </p>
      </form>
    </div>
    <div>
      
    </div>
    </>
  } else if (res === null){
    Content = <>
    <h3>Email is Being Sent, Check the Inbox of the Email given.</h3>
    <p>Email sent to: {email}</p>
    </>
  } else {
    Content = <>
    <h3>{res}</h3>
    <p>Email sent to: {email}</p>
    </>
  }

  return (
    <>
    {Content}
    </>
    
  );
}

export default App