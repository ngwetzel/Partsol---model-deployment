# gunicorn_config.py
workers = 4
bind = "0.0.0.0:8000"
loglevel = "info"
timeout = 120
