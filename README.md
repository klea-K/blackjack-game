# Blackjack Game

A web-based Blackjack game built with Python, Flask, HTML, CSS, and JavaScript.

## About the Project

This project is a simple interactive Blackjack game where the player can play against the dealer through a web interface.

The project is divided into a **backend** and a **frontend**:

- **Backend** — handles the game logic and provides the API using Flask.
- **Frontend** — provides the user interface and communicates with the backend using JavaScript.

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- REST API / JSON

## Project Structure

```text
blackjack-game/
│
├── app.py        # Flask application and API endpoints
├── game.py       # Blackjack game logic
├── index.html    # User interface
├── style.css     # Styling
├── script.js     # Frontend functionality and API requests
└── .gitignore    # Files excluded from Git
```

## Features

- Start a new Blackjack game
- Deal cards to the player and dealer
- Calculate card scores
- Handle Blackjack game rules
- Determine the winner
- Interactive web interface
- Frontend and backend communication through API requests

## How It Works

The frontend sends requests to the Flask backend when the player interacts with the game.

The backend processes the request using the Blackjack game logic in `game.py` and returns the relevant game data as JSON.

The JavaScript in `script.js` then updates the interface based on the response.

## Author

Klea Gega
