from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import json
import multipart


HOST = "0.0.0.0"
PORT = 8080

# Project folders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RECEIVED_FOLDER = os.path.join(BASE_DIR, "received")
WEB_FOLDER = os.path.join(BASE_DIR, "web")

os.makedirs(RECEIVED_FOLDER, exist_ok=True)

# Serve website from /web
os.chdir(WEB_FOLDER)


class Cyb3rShareHandler(SimpleHTTPRequestHandler):

    def do_POST(self):

        if self.path != "/upload":
            self.send_error(404, "Not Found")
            return

        content_type = self.headers.get("Content-Type")
        content_length = self.headers.get("Content-Length")

        if not content_type or "multipart/form-data" not in content_type:
            self.send_error(400, "Invalid upload type")
            return

        if not content_length:
            self.send_error(400, "Missing content length")
            return

        try:
            content_length = int(content_length)

            if content_length < 0:
                self.send_error(400, "Invalid content length")
                return

        except ValueError:
            self.send_error(400, "Invalid content length")
            return

        uploaded_filename = None
        uploaded_file = None

        def on_field(field):
            pass

        def on_file(file):

            nonlocal uploaded_filename
            nonlocal uploaded_file

            # Get filename
            filename = file.file_name

            if isinstance(filename, bytes):
                filename = filename.decode("utf-8", errors="replace")

            # Security: remove any path information
            uploaded_filename = os.path.basename(filename)

            uploaded_file = file.file_object

        try:

            # Headers required by python-multipart
            headers = {
                "Content-Type": content_type,
                "Content-Length": str(content_length)
            }

            # Parse the upload
            multipart.parse_form(
                headers,
                self.rfile,
                on_field,
                on_file
            )

        except Exception as error:

            print(f"Upload error: {error}")

            self.send_error(400, "Failed to process upload")
            return

        if not uploaded_filename or uploaded_file is None:
            self.send_error(400, "No file received")
            return

        # Save file
        file_path = os.path.join(
            RECEIVED_FOLDER,
            uploaded_filename
        )

        try:

            uploaded_file.seek(0)

            with open(file_path, "wb") as output:

                while True:

                    chunk = uploaded_file.read(1024 * 1024)

                    if not chunk:
                        break

                    output.write(chunk)

        except Exception as error:

            print(f"Save error: {error}")

            self.send_error(500, "Could not save file")
            return

        print(f"Received: {uploaded_filename}")

        # Success response
        response = {
            "message": f"{uploaded_filename} received successfully"
        }

        response_bytes = json.dumps(response).encode("utf-8")

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.send_header(
            "Content-Length",
            str(len(response_bytes))
        )

        self.end_headers()

        self.wfile.write(response_bytes)


print("=================================")
print("       CYB3RSHARE")
print("=================================")
print(f"Server running on port {PORT}")
print("Press CTRL+C to stop the server")
print("=================================")

server = HTTPServer(
    (HOST, PORT),
    Cyb3rShareHandler
)

server.serve_forever()