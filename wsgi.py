from app.app import create_app

# fallback to 'production'
config = os.getenv('FLASK_ENV', 'production')  
app = create_app('production')