from http.server import BaseHTTPRequestHandler
import json
import re
import urllib.request
import urllib.error
from urllib.parse import urlparse, parse_qs

API_ENDPOINT = "https://srahitek-num-info-api-xi.vercel.app/FetchData?Number="


class handler(BaseHTTPRequestHandler):
    def _cors(self, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._cors(204)

    def do_GET(self):
        try:
            qs = parse_qs(urlparse(self.path).query)
            raw = (qs.get("n") or qs.get("number") or [""])[0]
            num = re.sub(r"\D", "", raw)

            if len(num) != 10:
                self._cors(400)
                self.wfile.write(json.dumps({
                    "status": "error",
                    "message": "Enter exactly 10 digits"
                }).encode())
                return

            req = urllib.request.Request(
                API_ENDPOINT + num,
                headers={
                    "Accept": "application/json",
                    "User-Agent": "Shaurya-OSINT-Web/1.0",
                },
            )
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            self._cors(200)
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

        except urllib.error.HTTPError as e:
            self._cors(502)
            self.wfile.write(json.dumps({
                "status": "error",
                "message": f"Upstream HTTP {e.code}"
            }).encode())
        except Exception as e:
            self._cors(500)
            self.wfile.write(json.dumps({
                "status": "error",
                "message": str(e)
            }).encode())
