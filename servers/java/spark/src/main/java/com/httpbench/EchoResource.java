package com.httpbench;

import java.util.Date;
import java.util.UUID;

import spark.Request;
import spark.Response;

public class EchoResource {

	public static String echo(Request req, Response res) {
		// Log request
		System.out.printf("%s %s %s %s\n", new Date(), req.ip(), req.requestMethod(), req.pathInfo());

		// Parse parameters
		String words = req.params("words");
		Integer num = Integer.decode(req.queryParams("num"));

		// Verify parameters
		if (!words.toLowerCase().equals("helloworld") || !num.equals(1234567890)) {
			res.status(400);
			res.type("application/json");
			return "{\"error\": \"invalid parameters\"}";
		}

		// Return response
		res.status(200);
		res.type("application/json");
		return String.format("{\"message\":\"%s\"}", UUID.randomUUID());
	}
}
