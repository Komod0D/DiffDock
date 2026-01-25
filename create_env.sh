#!/usr/bin/env bash

conda create -n diffdock python=3.10
conda activate diffdock
pip install torch==2.3.1
pip install -r requirements.txt
pip install -e . --config-settings editable_mode=strict
