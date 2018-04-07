package main

import (
	"encoding/json"
	"log"
	"net/http"
	"strconv"
	"strings"

	uuid "github.com/satori/go.uuid"
)

type Response struct {
	Message string `json:"message,omitempty"`
	Error   string `json:"error,omitempty"`
}

func EchoHandler(res http.ResponseWriter, req *http.Request) {
	// Log request
	log.Printf("%s %s %s", req.RemoteAddr, req.Method, req.URL)

	// Parse parameters
	words := strings.TrimLeft(req.URL.Path, "/api/echo/")
	numberString := req.URL.Query().Get("num")
	number, _ := strconv.Atoi(numberString)

	// Verify parameters
	if strings.ToLower(words) != "helloworld" || number != 1234567890 {
		response := &Response{"", "Invalid parameters"}
		responseJson, _ := json.Marshal(response)
		writeResponse(res, http.StatusBadRequest, responseJson)
		return
	}

	// Return response
	response := &Response{uuid.Must(uuid.NewV4()).String(), ""}
	responseJson, _ := json.Marshal(response)
	writeResponse(res, http.StatusOK, responseJson)
}

func writeResponse(res http.ResponseWriter, statusCode int, message []byte) {
	res.Header().Set("Content-Type", "application/json")
	res.WriteHeader(statusCode)
	res.Write(message)
}

func main() {
	http.HandleFunc("/api/echo/", EchoHandler) // Trailing slash at end for rooted subtree path
	log.Println("Starting serving on port 8888")
	log.Fatal(http.ListenAndServe(":8888", nil))
}
