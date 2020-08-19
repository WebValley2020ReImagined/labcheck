#!/bin/bash

bash -i <<EOF
cd ~
conda activate py37_pytorch
jupyter lab --no-browser
EOF
