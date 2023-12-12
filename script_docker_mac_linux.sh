#!/bin/bash

# Vérifier si Docker est installé
if ! command -v docker &> /dev/null; then
    echo "Docker n'est pas installé. Veuillez installer Docker Desktop."
    exit 1
fi



# Cloner le projet depuis GitHub
git clone https://github.com/Zzappy24/Application_Big_Data.git
cd Application_Big_Data/BigDataProject


# Construire l'image Docker
docker build -t big_data_image .

cd ../

# Exécuter le conteneur Docker
docker run -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" -v "$(pwd)/model:/app/model" big_data_image

