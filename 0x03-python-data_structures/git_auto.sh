#!/bin/bash

git add .
read -p "Enter commit message: " commit_message
git commit -m "$commit_message"
git push
echo "Changes committed and pushed successgully"
