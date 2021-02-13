module "lambda-box" {
	source = "/path/to/lambda_module"
	include = ["common_libs/*.py", "lambda-box/lambda-box.py"]
	exclude = ["*.pyc"]
}
module "lambda-circle" {
	source = "/path/to/lambda_module"
	include = ["common_libs/*.py", "lambda-circle/lambda-circle.py"]
	exclude = ["*.pyc"]
}
module "lambda-ext" {
	source = "/path/to/lambda_module"
	include = ["common_libs/*.py", "lambda-ext-deps/lambda-ext.py"]
	exclude = ["*.pyc"]
	requirements = "lambda-ext-deps/reqirements.txt"
}

