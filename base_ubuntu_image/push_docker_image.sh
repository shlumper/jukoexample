az acr login --name deepcontainerregistry.azurecr.io
docker push deepcontainerregistry.azurecr.io/basic_python_image:$1
