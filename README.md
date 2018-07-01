# Summarizer (PyTeaser) in Lambda

### Requirements
- Python2
- Serverless
- Docker

### Develop
```
virtualenv -p python2 s
. s/bin/activate
pip install -r requirements.txt
sls wsgi serve
sls invoke local --function summarize --path local.json
sls logs --function summarize
```

### Deploy
```
pip freeze > requirements.txt
sls deploy
sls invoke --function summarize --path local.json
```

### Learnings
- Used virtualenv over conda because some libraries are not readily accessible via conda, or I wasn't sure how to import them manually with proper versions
- Installed Python 2.7 as I was getting module errors on 3.6
- Ultimate solution was to bypass module dependencies by setting a docker option flag in serverless.yml that packages everything and uploads to lambda.
- Don't forget to update requirements.txt (aka package.json) on every deploy
- You also need serverless-wsgi to serve up endpoints via Flask. This overrides Lambda's event/context

### Resources
- https://serverless.com/blog/serverless-python-packaging/
- https://dzone.com/articles/serverless-and-virtualenv-unable-to-import-module
- https://serverless.com/framework/docs/providers/aws/examples/hello-world/python/
- https://github.com/xiaoxu193/PyTeaser
- https://github.com/IndigoResearch/textteaser
- https://github.com/miso-belica/sumy
- https://stackoverflow.com/questions/419163/what-does-if-name-main-do
- https://stackoverflow.com/questions/990754/how-to-leave-exit-deactivate-a-python-virtualenv
- https://stackoverflow.com/questions/11005457/how-do-i-remove-delete-a-virtualenv
- https://stackoverflow.com/questions/33175827/what-version-of-python-is-on-my-mac
- http://docs.python-guide.org/en/latest/starting/install/osx/
- https://serverlesscode.com/post/python-3-on-serverless-framework/
- https://github.com/logandk/serverless-wsgi
- https://serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/
- https://serverless.com/framework/docs/providers/aws/cli-reference/invoke-local/
- https://serverless.com/blog/quick-tips-for-faster-serverless-development/
