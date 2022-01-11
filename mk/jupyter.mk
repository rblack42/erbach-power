.PHONY: jb_init
jb_init:	## init jupyter-book directory
	jb create book
	mkdir -p docs
	touch docs/.nojekyll

.PHONY: jb_build
jb_build:	## Build Jupyter book
	jb build book/
	cp -R book/_build/html/* docs


.PHONY: nb
nb:	## start Jupyter Notebook web browser
	jupyter notebook book
