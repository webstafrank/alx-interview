#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the first positional argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID.');
  process.exit(1); // Exit if no Movie ID is provided
}

// URL for the Star Wars API to get the film details
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to get the film data
request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  // Parse the response body to get the film data
  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Function to fetch and print character names in order
  function printCharacter(index) {
    if (index >= characters.length) return; // Base case: end of the list

    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.error(`Error: ${err.message}`);
        return;
      }
      if (res.statusCode !== 200) {
        console.error(`Failed to fetch character. Status code: ${res.statusCode}`);
        return;
      }
      const characterData = JSON.parse(charBody);
      console.log(characterData.name); // Print the character name
      printCharacter(index + 1); // Recursive call to print the next character
    });
  }

  // Start printing characters from the first one
  printCharacter(0);
});

