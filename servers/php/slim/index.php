<?php

require __DIR__ . '/vendor/autoload.php';

$settings = [
	'settings' => [
		'displayErrorDetails' => false,
		'addContentLengthHeader' => false,
		'outputBuffering' => false,
	]
];
$app = new \Slim\App($settings);

require __DIR__ . '/server.php';

$app->run();
