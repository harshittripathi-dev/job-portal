from flask import Flask, request, jsonify
from flask_cors import CORS

from system import recommend_jobs

app = Flask(__name__)
CORS(app)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "Job In India AI Recommendation Engine"
    })


@app.route("/recommend", methods=["POST"])
def recommend():

    try:
        data = request.get_json()

        candidate = data.get("candidate", {})
        jobs = data.get("jobs", [])

        if not candidate:
            return jsonify({
                "success": False,
                "message": "Candidate profile is required"
            }), 400

        if not jobs:
            return jsonify({
                "success": True,
                "recommendations": []
            })

        recommendations = recommend_jobs(
            candidate,
            jobs,
            top_n=10
        )

        return jsonify({
            "success": True,
            "count": len(recommendations),
            "recommendations": recommendations
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )