install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest --nbval *.ipynb && python -m pytest -cov=mylib test_script.py mylib/test_lib.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	python main.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	git add bar1.png bar2.png MTA.md
	git commit -m "Generate stats and plots" || true 
	git push
		
all: install lint test format deploy
