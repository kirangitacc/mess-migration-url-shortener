import uuid
import threading
from datetime import datetime

# Thread-safe in-memory store
url_store = {}
store_lock = threading.Lock()

def generate_short_id():
    return uuid.uuid4().hex[:6]

def save_url(original_url):
    short_id = generate_short_id()
    with store_lock:
        url_store[short_id] = {
            "url": original_url,
            "clicks": 0,
            "created_at": datetime.utcnow().isoformat()
        }
    return short_id

def get_original_url(short_id):
    with store_lock:
        data = url_store.get(short_id)
        if data:
            data["clicks"] += 1
            return data["url"]
        return None

def get_stats(short_id):
    with store_lock:
        return url_store.get(short_id)
