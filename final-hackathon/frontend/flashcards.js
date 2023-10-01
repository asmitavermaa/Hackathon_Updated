// flashcards.js

const flashcardData = [
    { front: "Front of Card 1", back: "Back of Card 1" },
    { front: "Front of Card 2", back: "Back of Card 2" },
];

const flashcardContainer = document.getElementById("flashcard-container");

function createFlashcards() {
    flashcardData.forEach((card, index) => {
        const flashcard = document.createElement("div");
        flashcard.classList.add("flashcard");
        flashcard.dataset.index = index;

        const front = document.createElement("div");
        front.classList.add("front");
        front.textContent = card.front;

        const back = document.createElement("div");
        back.classList.add("back");
        back.textContent = card.back;

        flashcard.appendChild(front);
        flashcard.appendChild(back);

        flashcard.addEventListener("click", () => {
            flashcard.classList.toggle("flipped");
        });

        flashcardContainer.appendChild(flashcard);
    });
}

createFlashcards();
