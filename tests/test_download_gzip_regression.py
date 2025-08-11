# tests/test_download_gzip_regression.py
import gzip
import io
import shutil
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer


RAW = b"A" * 50000
buf = io.BytesIO()
with gzip.GzipFile(fileobj=buf, mode="wb") as gz:
    gz.write(RAW)
GZ = buf.getvalue()


class Handler(BaseHTTPRequestHandler):
    def _send_common_headers(self, content_length: int) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("Content-Encoding", "gzip")
        self.send_header("Content-Length", str(content_length))
        self.end_headers()

    def do_GET(self) -> None:
        if self.path != "/file.gz":
            self.send_error(404)
            return
        self._send_common_headers(len(GZ))
        self.wfile.write(GZ)

    def do_HEAD(self) -> None:
        if self.path != "/file.gz":
            self.send_error(404)
            return
        self._send_common_headers(len(GZ))

    def do_POST(self) -> None:
        if self.path != "/file.gz":
            self.send_error(404)
            return
        self._send_common_headers(len(GZ))
        self.wfile.write(GZ)

    def log_message(self, *args) -> None:
        pass


def start_server():
    srv = HTTPServer(("127.0.0.1", 0), Handler)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    return srv, th


def test_download_gzip_content_length(tmp_path):
    srv, _ = start_server()
    try:
        url = f"http://127.0.0.1:{srv.server_port}/file.gz"
        out = tmp_path / "out.gz"

        exe = shutil.which("http")
        if exe:
            cmd = [exe, "GET", url, "--download", "--output", str(out)]
        else:
            cmd = [sys.executable, "-m", "httpie", "GET", url, "--download", "--output", str(out)]

        p = subprocess.run(cmd, capture_output=True, text=True)

        assert p.returncode == 0, f"stderr:\n{p.stderr}\nstdout:\n{p.stdout}"
        assert out.exists(), "output file not created"
        size = out.stat().st_size
        assert size == len(GZ), f"saved size {size} != expected {len(GZ)}"

        combined = (p.stdout or "") + (p.stderr or "")
        assert ">100%" not in combined
        assert "Incomplete download" not in combined
    finally:
        srv.shutdown()
