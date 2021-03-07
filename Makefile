
build:
	python -m pip install --upgrade pip
	pip install setuptools wheel twine build
	python -m build

release:
	python3 -m twine upload --repository testpypi dist/*

clean:
	rm -rf build dist *.egg-info
