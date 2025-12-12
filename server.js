const express = require("express");
const fs = require("fs");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// Load TODOS API
app.get("/api", (req, res) => {
  const file = fs.readFileSync("data.json", "utf-8");
  res.json(JSON.parse(file));
});

// Submit To-Do API
app.post("/submittodoitem", (req, res) => {
  const { itemName, itemDescription } = req.body;

  const todos = JSON.parse(fs.readFileSync("data.json", "utf-8"));

  const newTodo = {
    name: itemName,
    desc: itemDescription
  };

  todos.push(newTodo);

  fs.writeFileSync("data.json", JSON.stringify(todos, null, 2));

  res.json({ message: "Todo Added Successfully" });
});

// Server start
app.listen(8080, () => {
  console.log("Server running on http://localhost:8080");
});
git 