#!/bin/bash
git add .

read -p "Enter ur commit message: " commit_message

git commit -m $commit_message

git push
