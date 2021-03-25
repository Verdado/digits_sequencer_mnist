# MNIST DIGITS SEQUENCER API

# Build image
docker-compose build

# Bring up container
docker-compose up -d

# Go to WORKDIR
cd /MNIST

# Run Job
python digits_sequencer_cli.py [3,2,3,4] "(0,10)" 200

#Output under MNIST folder
/MNIST
