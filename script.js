document.querySelectorAll(".filter-btn").forEach(button => {
    button.addEventListener("click", () => {
        const filter = button.getAttribute("data-filter");
        document.querySelectorAll(".card").forEach(card => {
            if (filter === "all" || card.dataset.category === filter) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    });
});