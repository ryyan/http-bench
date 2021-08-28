<?php

use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\Exception\UnsatisfiedDependencyException;

$app->get('/api/echo/{words}', function (Request $request, Response $response) {
  # Log request
  # Automatically done by nginx

  # Get parameters
  $words = $request->getAttribute('words');
  $num = $request->getQueryParam('num');

  # Verify parameters
  if (strtolower($words) != 'helloworld' || intval($num) != 1234567890) {
    return $response->withJson(array('error' => 'Invalid parameters'), 400);
  }

  # Return response
  return $response->withJson(array('message' => Uuid::uuid4()->toString()));
});
