.PHONY: python
python:
	python3 -m grpc_tools.protoc --proto_path=protos --python_out=python/pb --grpc_python_out=python/pb protos/*.proto