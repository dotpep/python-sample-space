# API endpoint
$apiEndpoint = "http://127.0.0.1:8000/api/books/"

# Make GET request for all books
$response = Invoke-RestMethod -Uri $apiEndpoint -Method Get

# Display
$response
