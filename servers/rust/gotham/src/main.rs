use gotham::handler::IntoResponse;
use gotham::helpers::http::response::create_response;
use gotham::hyper::{Body, Response, StatusCode};
use gotham::router::builder::*;
use gotham::router::Router;
use gotham::state::{FromState, State};
use gotham_derive::{StateData, StaticResponseExtender};
use mime::APPLICATION_JSON;
use serde::Deserialize;
use uuid::Uuid;

#[derive(Deserialize, StateData, StaticResponseExtender)]
struct PathExtractor {
    words: String,
}

#[derive(Deserialize, StateData, StaticResponseExtender)]
struct QueryStringExtractor {
    num: String,
}

struct Message {
    status_code: StatusCode,
    body: String,
}

impl IntoResponse for Message {
    fn into_response(self, state: &State) -> Response<Body> {
        create_response(state, self.status_code, APPLICATION_JSON, self.body)
    }
}

fn echo(state: State) -> (State, Message) {
    // Log request
    // TODO: log request
    println!("Log request");
    //println!("{} {} {} {}", time::now().rfc3339().to_string(), request.origin.remote_addr, request.origin.method, request.origin.uri);

    // Parse parameters
    let path_params = PathExtractor::borrow_from(&state);
    let words = &path_params.words;
    let query_params = QueryStringExtractor::borrow_from(&state);
    let num = query_params.num.parse::<i32>().unwrap();

    // Verify parameters
    let (body, status_code) = {
        if words.to_lowercase() != "helloworld" || num != 1234567890 {
            (
                format!("{{\"error\": \"Invalid parameters\"}}"),
                StatusCode::BAD_REQUEST,
            )
        } else {
            (
                format!("{{\"message\": {}}}", Uuid::new_v4().to_string()),
                StatusCode::OK,
            )
        }
    };

    // Return response
    let response = Message {
        status_code: status_code,
        body: body,
    };
    (state, response)
}

fn router() -> Router {
    build_simple_router(|route| {
        route
            .get("/echo/:words")
            .with_path_extractor::<PathExtractor>()
            .with_query_string_extractor::<QueryStringExtractor>()
            .to(echo);
    })
}

pub fn main() {
    let addr = "0.0.0.0:8888";
    println!("Starting server at http://{}", addr);
    gotham::start(addr, || Ok(router()))
}
