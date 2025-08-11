import io
import gzip
import sys
import shutil
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# محتوى نضغطه gzip
RAW = b"A" * 50000
buf = io.BytesIO()
with gzip.GzipFile(fileobj=buf, mode="wb") as gz:
    gz.write(RAW)
GZ = buf.getvalue()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/file.gz":
            self.send_error(404); return
        self.send_response(200)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("Content-Encoding", "gzip")
        self.send_header("Content-Length", str(len(GZ)))  # طول النسخة المضغوطة
        self.end_headers()
        self.wfile.write(GZ)

    def log_message(self, *args):
        pass  # نسكت اللوج

def start_server():
    srv = HTTPServer(("127.0.0.1", 0), Handler)  # بورت حر
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    return srv, th

def test_download_gzip_content_length(tmp_path):
    srv, _ = start_server()
    try:
        url = f"http://127.0.0.1:{srv.server_port}/file.gz"
        out = tmp_path / "out.gz"

        # نفضّل GET صراحةً ونستعمل --output
        exe = shutil.which("http")
        if exe:
            cmd = [exe, "GET", url, "--download", "--output", str(out)]
        else:
            cmd = [sys.executable, "-m", "httpie", "GET", url, "--download", "--output", str(out)]

        p = subprocess.run(cmd, capture_output=True, text=True)
        assert p.returncode == 0, f"stderr:\\n{p.stderr}\\nstdout:\\n{p.stdout}"
        assert out.exists(), "output file not created"

        size = out.stat().st_size
        assert size == len(GZ), f"saved size {size} != expected {len(GZ)}"

        # تحسّبي: نتأكد ماكو إشارات لتجاوز 100% أو incomplete
        combined = (p.stdout or "") + (p.stderr or "")
        assert ">100%" not in combined
        assert "Incomplete download" not in combined
    finally:
        srv.shutdown()
