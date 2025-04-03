<?php
// Database configuration
$host = 'localhost'; // MySQL server hostname
$username = 'root'; // MySQL username
$password = 'Rudra@192004'; // MySQL password
$database = 'healthcare'; // Database name

// Create a database connection
$conn = new mysqli($host, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process form data
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = htmlspecialchars($_POST['name']);
    $phone = htmlspecialchars($_POST['phone']);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $dob = $_POST['dop'];
    $disease_type = htmlspecialchars($_POST['disease_type']);
    $appointment_date = $_POST['appointment_date'];
    $message = htmlspecialchars($_POST['messege']);

    // Insert data into the database
    $sql = "INSERT INTO appointments (name, phone, email, dob, disease_type, appointment_date, message)
            VALUES (?, ?, ?, ?, ?, ?, ?)";

    // Prepare and bind the statement
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sssssss", $name, $phone, $email, $dob, $disease_type, $appointment_date, $message);

    // Execute the statement
    if ($stmt->execute()) {
        echo "Appointment booked successfully!";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $conn->close();
}
?>