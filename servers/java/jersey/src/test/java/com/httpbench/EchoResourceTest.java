package com.httpbench;

import static org.junit.Assert.assertTrue;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.Response;

import org.glassfish.grizzly.http.server.HttpServer;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class EchoResourceTest {

    private HttpServer server;
    private WebTarget target;

    @Before
    public void setUp() throws Exception {
        // start the server
        server = Server.startServer();

        // create the client
        Client c = ClientBuilder.newClient();
        target = c.target(Server.BASE_URI);
    }

    @After
    public void tearDown() throws Exception {
        server.shutdownNow();
    }

    @Test
    public void testHappyPath() {
    	Response response = target.path("echo/HelloWorld").queryParam("num", 1234567890).request().get(Response.class);
        assertTrue(response.getStatus() == 200);
    	assertTrue(response.readEntity(String.class).contains("message"));
    }

    @Test
    public void testErrorPath() {
        Response response = target.path("echo/GoodbyeWorld").queryParam("num", 321).request().get(Response.class);
        assertTrue(response.getStatus() == 400);
        assertTrue(response.readEntity(String.class).contains("error"));
    }
}
