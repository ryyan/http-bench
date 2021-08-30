package com.httpbench;

import static spark.Spark.get;
import static spark.Spark.port;

public class Server {

	public static void main(String[] args) {
		port(8888);
		get("/echo/:words", (req, res) -> EchoResource.echo(req, res));
	}
}
