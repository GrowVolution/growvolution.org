from flask import Blueprint, render_template

from .handling import your_endpoint


def init_routes(bp: Blueprint):
    @bp.route("/")
    def index():
        return render_template("index.html")


    @bp.route("/your-endpoint", methods=["GET", "POST"])
    def endpoint():
        return your_endpoint.handle_request()
