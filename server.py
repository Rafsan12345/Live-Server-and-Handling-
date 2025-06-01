import http.server
import socketserver
import os

# নির্দিষ্ট ফোল্ডারের পাথ সেট করুন
FIRMWARE_FOLDER = r"C:\Users\DCL\Desktop\HTML\Host"  # এখানে আপনার ফোল্ডারের পাথ লিখুন
PORT = 8080  # পোর্ট নম্বর সেট করুন

# বর্তমান ডিরেক্টরি পরিবর্তন করুন
os.chdir(FIRMWARE_FOLDER)

# HTTP সার্ভার চালু করুন
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT} from {FIRMWARE_FOLDER}")
    httpd.serve_forever()
