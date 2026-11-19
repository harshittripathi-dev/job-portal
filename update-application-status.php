<?php

session_start();

if (!isset($_SESSION["user_id"])) {
    header("Location: login.php");
    exit();
}

if (strtolower($_SESSION["role"] ?? "") !== "admin") {
    http_response_code(403);
    $_SESSION["application_error"] = "Only administrators can update application statuses.";
    header("Location: applications.php");
    exit();
}

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    http_response_code(405);
    header("Allow: POST");
    exit("Method not allowed.");
}

$csrf_token = $_POST["csrf_token"] ?? "";

if (
    empty($_SESSION["csrf_token"]) ||
    !is_string($csrf_token) ||
    !hash_equals($_SESSION["csrf_token"], $csrf_token)
) {
    http_response_code(403);
    $_SESSION["application_error"] = "Your session expired. Please try again.";
    header("Location: applications.php");
    exit();
}

$application_id = filter_input(INPUT_POST, "application_id", FILTER_VALIDATE_INT);
$status = $_POST["status"] ?? "";
$allowed_statuses = ["Applied", "Shortlisted", "Selected", "Rejected"];
$job_id = filter_input(INPUT_POST, "job_id", FILTER_VALIDATE_INT);

$redirect = "applications.php";
if ($job_id !== false && $job_id !== null && $job_id > 0) {
    $redirect .= "?job_id=" . $job_id;
}

if ($application_id === false || $application_id === null || $application_id <= 0) {
    $_SESSION["application_error"] = "Invalid application.";
    header("Location: " . $redirect);
    exit();
}

if (!is_string($status) || !in_array($status, $allowed_statuses, true)) {
    $_SESSION["application_error"] = "Invalid application status.";
    header("Location: " . $redirect);
    exit();
}

require_once "config/database.php";

$stmt = $conn->prepare("UPDATE applications SET status = ? WHERE id = ?");

if (!$stmt) {
    $_SESSION["application_error"] = "Unable to update the application right now.";
    header("Location: " . $redirect);
    exit();
}

$stmt->bind_param("si", $status, $application_id);

if (!$stmt->execute()) {
    $_SESSION["application_error"] = "Unable to update the application right now.";
} elseif ($stmt->affected_rows === 0) {
    $_SESSION["application_error"] = "Application not found or status was unchanged.";
} else {
    $_SESSION["application_success"] = "Application status updated to " . $status . ".";
}

$stmt->close();
$conn->close();

header("Location: " . $redirect);
exit();
