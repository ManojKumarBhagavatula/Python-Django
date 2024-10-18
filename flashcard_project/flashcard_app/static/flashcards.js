let currentFlashcardId = null;  // To track which flashcard is open
let flipState = {};  // To track flip state for each flashcard

// Function to open the modal and load flashcard data
function openModal(flashcardId) {
    if (currentFlashcardId === flashcardId) {
        return;  // No action if the same flashcard is clicked
    }

    // Close previously opened modal
    if (currentFlashcardId !== null) {
        closeModal(currentFlashcardId);
    }

    currentFlashcardId = flashcardId;
    const modal = document.getElementById('flashcard-modal-' + flashcardId);
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';  // Disable scrolling on background

    // Reset the flip state and content for reopening
    flipState[flashcardId] = false;  // Set to false since the card will start as flipped to the question

    // Fetch flashcard data (question and answer) when modal opens
    fetch(`/flashcard/${flashcardId}/`)
        .then(response => response.json())
        .then(data => {
            modal.querySelector('.flashcard-question').innerHTML = "<strong>Question:</strong> " + data.question;
            modal.querySelector('.flashcard-answer').innerHTML = "<strong>Answer:</strong> " + data.answer;
            modal.querySelector('.flashcard-answer').style.display = 'none';  // Hide the answer initially
        });
}

// Function to flip the modal to show the answer
function flipCard(flashcardId) {
    const modal = document.getElementById('flashcard-modal-' + flashcardId);
    const content = modal.querySelector('.modal-content');

    // Add the flip class to trigger the animation
    modal.classList.add('flip');

    // Fetch both question and answer (once) if not already loaded
    fetch(`/flashcard/${flashcardId}/`)
        .then(response => response.json())
        .then(data => {
            const questionElement = modal.querySelector('.flashcard-question');
            const answerElement = modal.querySelector('.flashcard-answer');

            // If we are flipping to the answer, hide the question and show the answer
            if (!flipState[flashcardId]) {
                questionElement.style.display = 'none';
                answerElement.style.display = 'block';
                flipState[flashcardId] = true;  // Set flip state to true
            } 
            // If we are flipping back to the question, hide the answer and show the question
            else {
                answerElement.style.display = 'none';
                questionElement.style.display = 'block';
                flipState[flashcardId] = false;  // Set flip state to false
            }
        });

    // Reset the flip animation after the animation ends
    content.addEventListener('animationend', () => {
        modal.classList.remove('flip');  // Remove flip animation class
    });
}

// Function to close the modal
function closeModal(flashcardId) {
    const modal = document.getElementById('flashcard-modal-' + flashcardId);
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';  // Re-enable scrolling

    // Clear the flashcardId tracking
    currentFlashcardId = null;

    // Reset the flip state for the card so that it starts with the question next time
    flipState[flashcardId] = false;

    // Ensure the modal is reset to show the question
    modal.querySelector('.flashcard-question').style.display = 'block';
    modal.querySelector('.flashcard-answer').style.display = 'none';
}
