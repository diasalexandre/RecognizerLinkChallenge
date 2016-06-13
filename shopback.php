<?php

$host    = "localhost";
$port    = 9094;
$url = "";

if (isset($_GET['url'])) {
	$url = $_GET['url'];
}

$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create socket\n");
$result = socket_connect($socket, $host, $port) or die("Could not connect to server\n");  
socket_write($socket, $url, strlen($url)) or die("Could not send data to server\n");

$result = socket_read ($socket, 1024) or die("Could not read server response\n");

echo $result;

socket_close($socket);