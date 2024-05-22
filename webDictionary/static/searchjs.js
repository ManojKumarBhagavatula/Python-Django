function searchWord() {
    var searchInput = document.getElementById("searchInput").value.trim();
    var searchResult = document.getElementById("searchResult");

    if (searchInput) {
        fetch('/search/?q=' + searchInput)
            .then(response => response.json())
            .then(data => {
                if (data.result) {
                    searchResult.textContent = data.result;
                } else {
                    searchResult.textContent = "Word not found.";
                }
            })
            .catch(error => {
                console.error("An error occurred:", error);
            });
    } else {
        searchResult.textContent = "Please enter a word to search.";
    }
}

// Prevent form submission and call the searchWord function
document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();
    searchWord();
});
