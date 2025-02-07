#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results || [];
    const count = films.reduce((acc, film) => {
      return acc + (film.characters.includes(characterUrl) ? 1 : 0);
    }, 0);
    console.log(count);
  }
});
