# book ID
$bookId = 6

# API endpoint
$apiEndpoint = "http://127.0.0.1:8000/api/books/$bookId/"

# Make DELETE request
$response = Invoke-RestMethod -Uri $apiEndpoint -Method Delete

# Display
$response
