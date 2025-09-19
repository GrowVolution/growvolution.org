from eventlet import monkey_patch
monkey_patch()

from app import create_app
app = create_app()
