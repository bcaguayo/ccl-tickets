from app.app import create_app


# config = os.getenv('FLASK_ENV', 'production')  # fallback to 'production'
app = create_app('production')