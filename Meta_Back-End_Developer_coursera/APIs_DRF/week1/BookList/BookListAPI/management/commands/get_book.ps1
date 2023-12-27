# book ID
$bookId = 6

# API endpoint
$apiEndpoint = "http://127.0.0.1:8000/api/books/$bookId/"

# Make GET request for a specific book
$response = Invoke-RestMethod -Uri $apiEndpoint -Method Get

# Display
$response
