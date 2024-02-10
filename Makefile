.PHONY: python
python:
	python3 -m grpc_tools.protoc --proto_path=protos --python_out=python --grpc_python_out=python protos/*.proto