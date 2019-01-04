#!/usr/bin/env bash

set -ex

pipenv run python -m pytest
pipenv run behave