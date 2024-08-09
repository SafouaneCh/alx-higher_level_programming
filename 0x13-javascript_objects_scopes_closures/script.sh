#!/bin/bash
git add .

read -p "enter ur commit message: " commit_message

git commit -m $commit_message

git push
