#!/usr/bin/node

const request = require('request');
const async = require('async');

function fetchCharacterNames(movieId) {
  const movieEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  
  request(movieEndpoint, (error, response, body) => {
    if (error) {
      console.error(`Error fetching movie data: ${error.message}`);
      return;
    }

    try {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      if (!characterUrls || characterUrls.length === 0) {
        console.log('No character data found for this movie.');
        return;
      }

      async.each(
        characterUrls,
        (characterUrl, callback) => {
          request(characterUrl, (error, response, body) => {
            if (error) {
              console.error(`Error fetching character data: ${error.message}`);
              callback();
            } else {
              const characterData = JSON.parse(body);
              console.log(characterData.name);
              callback();
            }
          });
        },
        (err) => {
          if (err) {
            console.error(`Error: ${err}`);
          }
        }
      );
    } catch (error) {
      console.error(`Error parsing movie data: ${error.message}`);
    }
  });
}

// Check if a movie ID is provided as a command-line argument
if (process.argv.length !== 3) {
  console.log('Usage: node swapi_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
fetchCharacterNames(movieId);
