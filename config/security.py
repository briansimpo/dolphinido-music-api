"""Security Related Config"""

# Cross-Origin Resource Sharing
CORS = {
    "paths": ["api/*"],
    "allowed_methods": ["GET", "POST", "DELETE", "PUT", "PATCH", "OPTIONS"],
    "allowed_origins": ["http://localhost", "http://localhost:3000"],
    "allowed_headers": ["Authorization", "Origin", "Content-Type", "Accept", "X-Requested-With"],
    "exposed_headers": [],
    "max_age": 60*60*24,
    "supports_credentials": True,
}
