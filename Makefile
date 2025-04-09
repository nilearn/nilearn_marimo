PYTHON ?= python

all: clean

clean:
	rm -fr _site

build:
	python scripts/build.py

serve:
	python -m http.server -d _site
