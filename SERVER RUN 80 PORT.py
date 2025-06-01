import http.server
import socketserver
import os

# ✅ ফোল্ডার যেটা সার্ভ করতে চান:
FOLDER_TO_SERVE = r"C:\Users\DCL\Desktop\HTML\E Commerce 100%"  # ← এখানে আপনার ফোল্ডার দিন

# ✅ port 80 (admin/root privilege লাগবে)
PORT = 80

# চেক করুন ফোল্ডারটা আছে কিনা
if not os.path.isdir(FOLDER_TO_SERVE):
    print(f"[❌] Folder does not exist: {FOLDER_TO_SERVE}")
    exit()

# change working directory
os.chdir(FOLDER_TO_SERVE)

# HTTP handler
Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"[✅] Serving '{FOLDER_TO_SERVE}' at http://localhost:{PORT}")
        httpd.serve_forever()
except PermissionError:
    print(f"[❌] Permission denied! Try running as administrator or use sudo (for port {PORT})")
except OSError as e:
    print(f"[❌] OS Error: {e}")
