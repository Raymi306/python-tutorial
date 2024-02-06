.PHONY: default
default: clean lint
	python3 -m app

.PHONY: clean
clean:
	rm -rf dist
.PHONY: lint
lint:
	pylint app
rsync:
	echo "rsync -rvz --progress -e 'ssh -p 57018' ./dist/* andrew@let-them.cyou:/srv/www/lt/andrew/tutorials/python"
