"""
routes/public_assets.py
------------------------
On Vercel, everything inside the public/ folder is automatically served
straight from the CDN — Flask never even sees those requests.

Locally (when you run `python app.py`), Flask needs a little help to serve
those same files, so this blueprint does that. This keeps local
development behaving exactly like the live site, with no extra setup.
"""

import os
from flask import Blueprint, send_from_directory

PUBLIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public")

public_assets_bp = Blueprint("public_assets", __name__)


@public_assets_bp.route("/css/<path:filename>")
def css_files(filename):
    return send_from_directory(os.path.join(PUBLIC_DIR, "css"), filename)


@public_assets_bp.route("/js/<path:filename>")
def js_files(filename):
    return send_from_directory(os.path.join(PUBLIC_DIR, "js"), filename)


@public_assets_bp.route("/img/<path:filename>")
def img_files(filename):
    return send_from_directory(os.path.join(PUBLIC_DIR, "img"), filename)
