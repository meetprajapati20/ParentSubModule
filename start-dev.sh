#!/bin/bash

set -e

git checkout main
git pull origin main

echo "🔄 Updating backend submodules..."
git submodule update --init --recursive --remote

echo "📝 Saving new release state to Git..."

git add .
git commit -m "chore(release): update module pointers"
git push origin main

echo "✅ Server shell updated in CodeCommit."