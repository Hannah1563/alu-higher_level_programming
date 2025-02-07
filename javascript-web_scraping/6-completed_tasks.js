#!/usr/bin/node
const request = require('request');

// Get the API URL from the command-line argument
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  
  const tasks = JSON.parse(body);
  const completedTasks = {};

  // Loop through all tasks and count the completed ones per user
  tasks.forEach(task => {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId] += 1;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });

  // Print the result only for users with completed tasks
  console.log(completedTasks);
});
