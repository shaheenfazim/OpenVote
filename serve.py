import sys
import http.server
import socketserver
import os

# Change the working directory to "server"
os.chdir("server")

# Check if an argument was passed
if len(sys.argv) > 1:
    # Get the argument value
    argument_value = sys.argv[1]
    
    # Create a file called "smartcontract" in the same directory
    with open("./smartcontract", "w") as file:
        file.write(argument_value)

# Start an HTTP server on port 8080
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 8080), handler) as httpd:
    print("HTTP server started on port 8080, visit http://localhost:8080")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Keyboard interrupt received, stopping server")
        httpd.shutdown()
