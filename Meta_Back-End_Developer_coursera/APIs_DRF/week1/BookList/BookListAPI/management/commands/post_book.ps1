# API endpoint
$apiEndpoint = "http://127.0.0.1:8000/api/books/"

# book data
$data = @{
    "title" = "Aleksandr"
    "author" = "Thinks"
    "price" = "19.99"
}

# Convert data to JSON
$jsonData = $data | ConvertTo-Json

# Make POST request
$response = Invoke-RestMethod -Uri $apiEndpoint -Method Post -Body $jsonData -ContentType 'application/json'

# Display
$response
