const express = require('express');
const app = express();
const port = 3000; // Choose a port number (e.g., 3000)

// Define a route for the home page
app.get('/', (req, res) => {
  res.send('Hello, World! This is my web server!');
});

// Start the server and listen on the chosen port
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
