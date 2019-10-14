deploy:
	pipenv run python setup.py bdist_wheel
	pipenv run python -m twine upload --skip-existing dist/*.whl
