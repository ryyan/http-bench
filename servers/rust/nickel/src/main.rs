extern crate uuid;
extern crate time;
#[macro_use] extern crate nickel;

use nickel::status::StatusCode;
use nickel::{Nickel, HttpRouter, QueryString, MediaType};
use uuid::Uuid;

fn main() {
    let mut server = Nickel::new();

    server.get("/api/echo/:words", middleware! { |request, mut response|
        // Log request
        println!("{} {} {} {}", time::now().rfc3339().to_string(), request.origin.remote_addr, request.origin.method, request.origin.uri);

        // Parse parameters
        let words = request.param("words").unwrap().to_string();
        let num = request.query().get("num").unwrap().parse::<i32>().unwrap();

        // Verify parameters
        response.set(MediaType::Json);
        if words.to_lowercase() != "helloworld" || num != 1234567890 {
            response.set(StatusCode::BadRequest);
            format!("{{\"error\": \"Invalid parameters\"}}")
        } else {
            // Return response
            response.set(StatusCode::Ok);
            format!("{{\"message\": {}}}", Uuid::new_v4().to_string())
        }
    });

    server.listen("0.0.0.0:8888").unwrap();
}
