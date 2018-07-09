test:
	python -m pytest tests/

PORT = 8000
run:
	#gunicorn --bind 0.0.0.0:$(PORT) -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker hardwarecheckout:app
	gunicorn --bind 0.0.0.0:$(PORT) --worker-class eventlet -w 1 hardwarecheckout:app

