.PHONY: setup
setup:
	pip3 install -r requirements.txt

.PHONY: run
run:
	python3 app.py

.PHONY: drun
drun:
	docker build -t simpleapp .
	docker run -ti -p 5555:5555 simpleapp

.PHONY: test
test:
	pytest -v --junitxml=report.xml --cov=app --cov-report xml

.PHONY: buildci
buildci:
	docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG .
         