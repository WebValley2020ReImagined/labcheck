#!/bin/bash

bash -i <<EOF
conda activate py37_pytorch
jupyter lab --no-browser
EOF
