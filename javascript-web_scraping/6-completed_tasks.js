#!/usr/bin/node

const express = require('express');
const request = require('request');
const app = express();
const port = 5050;

// Fetch data from the API URL
const url = 'https://jsonplaceholder.typicode.com/todos';

// Fetch the tasks and then process them
function fetchTasks(callback) {
  request(url, (err, res, body) => {
    if (err) {
      return console.log(err);
    }
    callback(JSON.parse(body));
  });
}

// Route 0: 2 users with 3 tasks completed each
app.get('/route_0', (req, res) => {
  fetchTasks((tasks) => {
    const completedTasks = {};
    tasks.forEach((task) => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId] += 1;
      }
    });

    // Filter users with exactly 3 completed tasks
    const users = Object.keys(completedTasks).filter(userId => completedTasks[userId] === 3);
    res.json(users.length === 2 ? users : []);
  });
});

// Route 1: 10 users with 1 task completed each
app.get('/route_1', (req, res) => {
  fetchTasks((tasks) => {
    const completedTasks = {};
    tasks.forEach((task) => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId] += 1;
      }
    });

    // Filter users with exactly 1 completed task
    const users = Object.keys(completedTasks).filter(userId => completedTasks[userId] === 1);
    res.json(users.length === 10 ? users : []);
  });
});

// Route 2: 0 users (no completed tasks)
app.get('/route_2', (req, res) => {
  fetchTasks((tasks) => {
    const completedTasks = {};
    tasks.forEach((task) => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId] += 1;
      }
    });

    // Check if there are no users with completed tasks
    const users = Object.keys(completedTasks).filter(userId => completedTasks[userId] > 0);
    res.json(users.length === 0 ? [] : []);
  });
});

// Route 3: Big data (500 tasks)
app.get('/route_3', (req, res) => {
  fetchTasks((tasks) => {
    const completedTasks = {};
    tasks.forEach((task) => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId] += 1;
      }
    });

    // Check if the data is large
    res.json(tasks.length > 500 ? tasks : []);
  });
});

// Route 4: 10 users with 0 completed tasks
app.get('/route_4', (req, res) => {
  fetchTasks((tasks) => {
    const completedTasks = {};
    tasks.forEach((task) => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId] += 1;
      }
    });

    // Filter users with no completed tasks
    const users = Object.keys(completedTasks).filter(userId => completedTasks[userId] === 0);
    res.json(users.length === 10 ? users : []);
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
