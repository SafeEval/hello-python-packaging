setup:
	python3 -m pip install --upgrade pip
	pip install setuptools wheel twine build

build:
	python setup.py sdist bdist_wheel

release:
	@semantic-release publish

install:
	pip install .

this-version:
	@semantic-release print-version --current

next-version:
	@semantic-release print-version

clean:
	rm -rf build dist *.egg-info
