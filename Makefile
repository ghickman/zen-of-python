help:
	@echo '   make upload                      upload the web site via S3'

upload:
	s3cmd sync output/ s3://zen-of-python --acl-public --delete-removed --guess-mime-type --cf-invalidate
