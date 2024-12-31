from flask import Flask, render_template, jsonify, request
import datetime
import platform
import logging

# Create Flask application
app = Flask(__name__)

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Our logger instance
logger = logging.getLogger(__name__)


@app.route("/")
def hello():
    logger.info(f"Home page accessed by user from {request.remote_addr}")
    message = "Hello, World!"
    return render_template("index.html", message=message)


@app.route("/health")
def health():
    logger.info("Health check endpoint called")
    return jsonify(
        {
            "status": "healthy",
            "timestamp": datetime.datetime.now().isoformat(),
            "service": "flask-demo",
        }
    )


@app.route("/system")
def system():
    logger.info("System information requested")
    try:
        return jsonify(
            {
                "python_version": platform.python_version(),
                "platform": platform.platform(),
                "architecture": platform.architecture()[0],
            }
        )
    except Exception as e:
        logger.error(f"Error getting system info: {str(e)}")
        return jsonify({"error": "System information unavailable"}), 500


if __name__ == "__main__":
    logger.info("Starting Flask application")
    app.run(host="0.0.0.0", port=5050)
