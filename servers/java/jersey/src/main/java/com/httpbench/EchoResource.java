package com.httpbench;

import java.util.Date;
import java.util.UUID;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Request;

@Path("echo/{words}")
public class EchoResource {

	@Context
	private Request request;

	/**
	 * Method handling HTTP GET requests. The returned object will be sent to the
	 * client as "application/json" media type.
	 *
	 * @return String that will be returned as a application/json response.
	 */
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public String echo(@PathParam("words") String words, @QueryParam("num") Integer num) {
		// Log request
		System.out.printf("%s %s\n", new Date(), request.getMethod());

		// Parse parameters
		// Done in function signature

		// Verify parameters
		if (!words.toLowerCase().equals("helloworld") || !num.equals(1234567890)) {
			return "{\"error\": \"Invalid parameters\"}";
		}

		// Return response
		return String.format("{\"message\": \"%s\"}", UUID.randomUUID());
	}
}
