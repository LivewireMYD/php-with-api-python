<?php

header("Content-Type: application/json");

// Define a simple password for authentication
$auth_password = "123456"; // Change this to the password you want

// Check if password is provided in the Authorization header
$headers = apache_request_headers();
if (!isset($headers['Authorization']) || $headers['Authorization'] !== $auth_password) {
    // If the password is missing or incorrect, return an error
    echo json_encode(array("status" => "error", "message" => "Unauthorized access. Invalid password."));
    http_response_code(401); // Unauthorized status
    exit;
}

// Database connection (assuming MySQL)
$host = "localhost";
$user = "root";      // Default MySQL user for XAMPP
$password = "";      // Default MySQL password (leave empty if no password)
$dbname = "myapi";   // Name of your database

// Create a MySQL connection
$conn = new mysqli($host, $user, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die(json_encode(array("status" => "error", "message" => "Connection failed: " . $conn->connect_error)));
}

// Handle the GET request
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Define the query to get users
    $yesterday = date("Y-m-d", strtotime("-1 day")); // Get yesterday's date
    $nextDay = date("Y-m-d", strtotime("+2 days")); // Get the day after tomorrow

    $sql = "SELECT * FROM users WHERE duedate BETWEEN '$yesterday' AND '$nextDay'";

    $result = $conn->query($sql);

    // Check if records exist
    if ($result->num_rows > 0) {
        $users = array();

        // Fetch data from the database
        while ($row = $result->fetch_assoc()) {
            $users[] = $row;
        }

        // Send JSON response
        echo json_encode(array("status" => "success", "data" => $users));
    } else {
        echo json_encode(array("status" => "success", "data" => [], "message" => "No users found."));
    }
} else {
    // If not a GET request, send a 405 Method Not Allowed response
    http_response_code(405);
    echo json_encode(array("status" => "error", "message" => "Method not allowed"));
}

// Close the database connection
$conn->close();
?>
