#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    tasks.forEach(task => {
      if (task.completed) {
        completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
      }
    });

    console.log(completedTasks);
  }
});
