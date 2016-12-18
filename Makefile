help:
	@echo '   make clean                       clean output directory'
	@echo '   make generate                    generate the site'
	@echo '   make upload                      upload to S3'
	@echo '   make publish                     all of the above'

clean:
	rm -rf output/*

generate: clean
	python generate.py && cp main.css output/main.css

upload:
	aws s3 sync --acl=public-read --delete output/ s3://zen-of-python.info/

publish: clean generate upload
