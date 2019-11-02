.PHONY: setup
setup:
	pip install -r requirements.txt

.PHONY: run
run:
	python app.py

.PHONY: drun
drun:
	docker build -t simpleapp .
	docker run -ti -p 5555:5555 simpleapp