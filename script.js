document.getElementById('reviewForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const review = document.getElementById('review').value;

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ review: review })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('sentiment').textContent = data.sentiment;
    });
});