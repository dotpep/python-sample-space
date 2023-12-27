# book ID
$bookId = 10

# API endpoint
$apiEndpoint = "http://127.0.0.1:8000/api/books/$bookId/"

# updated data
$data = @{
    "title" = "Thinks"
    "author" = "Aleksandr"
    "price" = "29.99"
}
#$data = @{
#    "title" = "UpdatedTitle"
#    "author" = "UpdatedAuthor"
#    "price" = "29.99"
#}


# Convert data to JSON
$jsonData = $data | ConvertTo-Json

# Make PUT request
$response = Invoke-RestMethod -Uri $apiEndpoint -Method Put -Body $jsonData -ContentType 'application/json'

# Display
$response
