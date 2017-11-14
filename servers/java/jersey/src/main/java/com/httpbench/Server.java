package com.httpbench;

import java.io.IOException;
import java.net.URI;

import org.glassfish.grizzly.http.server.HttpServer;
import org.glassfish.jersey.grizzly2.httpserver.GrizzlyHttpServerFactory;
import org.glassfish.jersey.server.ResourceConfig;

public class Server {

	public static final String BASE_URI = "http://localhost:8888/api/";

	public static HttpServer startServer() {
		final ResourceConfig rc = new ResourceConfig().packages("com.httpbench");
		return GrizzlyHttpServerFactory.createHttpServer(URI.create(BASE_URI), rc);
	}

	public static void main(String[] args) throws IOException {
		final HttpServer server = startServer();
		System.out.println(String.format("Server started at %s", BASE_URI));
		System.in.read();
		server.shutdownNow();
	}
}