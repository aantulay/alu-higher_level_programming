#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    for (const film of films) {
      const characters = film.characters;
      for (const charUrl of characters) {
        if (charUrl.endsWith('/18/') || charUrl.endsWith('/18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
