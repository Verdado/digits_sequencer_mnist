#Build image
docker-compose build

# Bring up container
docker-compose up -d

# Get inside the container
docker exec -it digits_sequencer_mnist_mnist_app_1 bash

# Go to WORKDIR
cd /MNIST

# Run Job
python digits_sequencer_cli.py [3,2,3,4] "(0,10)" 200

#Output under MNIST folder
/MNIST