#!/bin/bash
CRYPTOBOT_ENV=production
cd /home/oscar/git-repos/de-opa-1/collect-data/ && /home/oscar/.local/bin/poetry run python3 /home/oscar/git-repos/de-opa-1/collect-data/collect_data/main.py --type_data streaming --printer false
