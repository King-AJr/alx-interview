#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Define the movie endpoint URL
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Function to send requests to retrieve character names
function sendRequest(characterUrls, index) {
  // Check if all character URLs have been processed
  if (characterUrls.length === index) {
    return;
  }

  // Send a request to fetch character data
  request(characterUrls[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      // Parse the character data and print the name
      const characterData = JSON.parse(body);
      console.log(characterData.name);

      // Recursively call sendRequest for the next character
      sendRequest(characterUrls, index + 1);
    }
  });
}

// Send a request to retrieve movie data
request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Parse the movie data and extract character URLs
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Start fetching character names
    sendRequest(characterUrls, 0);
  }
});
