#!/bin/bash

git add .

read -p "enter commit mssage" commit_message

git commit -m "$commit_message"

git push
