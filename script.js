// =====================================
// Blackjack Frontend JavaScript
// Connects to Flask Backend API
// =====================================
// Backend URL

const API_URL = "http://localhost:5000/api";

// HTML elements

const playerCards = document.getElementById("player-cards");
const dealerCards = document.getElementById("dealer-cards");

const playerScore = document.getElementById("player-score");
const dealerScore = document.getElementById("dealer-score");

const message = document.getElementById("message");


const newButton = document.getElementById("new-btn");
const hitButton = document.getElementById("hit-btn");
const standButton = document.getElementById("stand-btn");

// =====================================
// API REQUEST HELPER
// =====================================

async function apiRequest(endpoint, method = "GET") {
    try {
        const response = await fetch(
            `${API_URL}/${endpoint}`,
            {
                method: method,
                credentials: "include"
            }
        );

        const data = await response.json();
        return data;

    } catch(error) {

        console.error(
            "Backend connection error:",
            error
        );

        message.innerHTML =
            "Cannot connect to server";
    }
}

// =====================================
// CREATE CARD ELEMENT
// =====================================

function createCard(card){
    const div = document.createElement("div");
    // Hidden dealer card
    if(card.hidden){
        div.className = "card hidden";
        return div;
    }
    div.className = "card";

    // Red suits
    if(
        card.suit === "♥" ||
        card.suit === "♦"
    ){
        div.classList.add("red");
    }

    div.innerHTML = `
        <div class="rank">
            ${card.rank}
        </div>

        <div class="suit">
            ${card.suit}
        </div>
    `;
    return div;
}

// =====================================
// DISPLAY CARDS
// =====================================

function renderCards(container, cards){
    container.innerHTML = "";
    cards.forEach(card => {
        const cardElement =
            createCard(card);
        container.appendChild(cardElement);
    });
}

// =====================================
// UPDATE GAME SCREEN
// =====================================

function updateGame(state){
    // Cards
    renderCards(
        playerCards,
        state.player_cards
    );

    renderCards(
        dealerCards,
        state.dealer_cards
    );

    // Scores

    playerScore.textContent =
        state.player_score;

    if(state.finished){
        dealerScore.textContent =
            state.dealer_score;
    }
    else{
        dealerScore.textContent =
            "?";
    }

    // Message

    message.textContent =
        state.message;

    // Buttons

    if(state.finished){
        hitButton.disabled = true;
        standButton.disabled = true;
    }
    else{
        hitButton.disabled = false;
        standButton.disabled = false;
    }
}

// =====================================
// NEW GAME
// =====================================

async function newGame(){
    const state =
        await apiRequest(
            "new-game",
            "POST"
        );
    updateGame(state);
}

// =====================================
// HIT
// =====================================

async function hit(){
    const state =
        await apiRequest(
            "hit",
            "POST"
        );
    updateGame(state);
}

// =====================================
// STAND
// =====================================

async function stand(){
    const state =
        await apiRequest(
            "stand",
            "POST"
        );
    updateGame(state);
}

// =====================================
// BUTTON EVENTS
// =====================================

newButton.addEventListener(
    "click",
    newGame
);

hitButton.addEventListener(
    "click",
    hit
);

standButton.addEventListener(
    "click",
    stand
);

// =====================================
// START GAME AUTOMATICALLY
// =====================================

window.onload = () => {
    newGame();
};