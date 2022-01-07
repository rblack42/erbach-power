.PHONY: docs
docs:  ## generate html documentation
	cd rst && \
		sphinx-build -b html -d _build/doctrees . ../docs

.PHONY:	spelling
spelling:	## spell check documentation
	cd rst && \
		sphinx-build -b spelling -d _build/doctrees . ../docs

.PHONY: docs-clean
docs-clean:	## remove sphinx docs html files
	cd rst && \
		sphinx-build -b clean
