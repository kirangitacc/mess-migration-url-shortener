from flask import Flask, jsonify, request, redirect
from app.models import save_url, get_original_url, get_stats
from app.utils import is_valid_url

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url or not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_id = save_url(original_url)
    return jsonify({
        "short_code": short_id,
        "short_url": f"http://localhost:5000/{short_id}"
    })

@app.route('/<short_id>')
def redirect_to_original(short_id):
    original_url = get_original_url(short_id)
    if original_url:
        return redirect(original_url)
    return jsonify({"error": "URL not found"}), 404

@app.route('/api/stats/<short_id>')
def stats(short_id):
    data = get_stats(short_id)
    if not data:
        return jsonify({"error": "Short code not found"}), 404
    return jsonify({
        "url": data["url"],
        "clicks": data["clicks"],
        "created_at": data["created_at"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

