#!/bin/bash

git add *
git commit -am "$1"
git pull origin main
git push origin main
git status
