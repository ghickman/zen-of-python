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
	s3cmd sync output/ s3://zen-of-python --acl-public --delete-removed --guess-mime-type --cf-invalidate

publish: clean generate upload
