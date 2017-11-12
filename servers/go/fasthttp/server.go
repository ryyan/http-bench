package main

import (
	"encoding/json"
	"log"
	"net/http"
	"strings"

	uuid "github.com/satori/go.uuid"
	fasthttp "github.com/valyala/fasthttp"
	reuseport "github.com/valyala/fasthttp/reuseport"
)

type Response struct {
	Message string `json:"message,omitempty"`
	Error   string `json:"error,omitempty"`
}

func EchoHandler(ctx *fasthttp.RequestCtx) {
	// Simulate routing
	path := string(ctx.Path())
	if strings.HasPrefix(path, "/api/echo/") == false {
		ctx.Error("Unsupported path", fasthttp.StatusNotFound)
	}

	// Log request
	log.Printf("%s %s %s", ctx.RemoteAddr(), ctx.Method(), ctx.URI())

	// Parse parameters
	words := strings.TrimLeft(path, "/api/echo/")
	number, _ := ctx.URI().QueryArgs().GetUint("num")

	// Verify parameters
	if strings.ToLower(words) != "helloworld" || number != 1234567890 {
		response := &Response{"", "Invalid parameters"}
		responseJson, _ := json.Marshal(response)
		writeResponse(ctx, http.StatusBadRequest, responseJson)
		return
	}

	// Return response
	response := &Response{uuid.NewV4().String(), ""}
	responseJson, _ := json.Marshal(response)
	writeResponse(ctx, http.StatusOK, responseJson)
}

func writeResponse(ctx *fasthttp.RequestCtx, statusCode int, message []byte) {
	ctx.Response.Header.Set("Content-Type", "application/json")
	ctx.SetStatusCode(statusCode)
	ctx.Write(message)
}

func main() {
	ln, err := reuseport.Listen("tcp4", "localhost:8888")
	if err != nil {
		log.Fatalf("Error starting listener: %s", err)
	}

	log.Println("Starting server on port 8888")
	log.Fatal(fasthttp.Serve(ln, EchoHandler))
}
