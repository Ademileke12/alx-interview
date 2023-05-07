const request = require('request');

// Retrieve the movie ID from command-line arguments
const movieId = process.argv[2];

// Send a request to the Star Wars API to retrieve the movie data
request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(`Error retrieving movie data: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error retrieving movie data: API returned status code ${response.statusCode}`);
    return;
  }

  // Parse the movie data and retrieve the character URLs
  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Send requests to the Star Wars API to retrieve each character data
  characterUrls.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(`Error retrieving character data: ${error}`);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Error retrieving character data: API returned status code ${response.statusCode}`);
        return;
      }

      // Parse the character data and print the name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
