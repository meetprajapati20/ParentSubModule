#!/bin/bash

set -e

git checkout main
git pull origin main

echo "==============================================================="
echo "🔄 Updating backend submodules..."

git submodule update --init --recursive --remote


echo "==============================================================="
echo "📝 Saving new release state to Git..."

if ! git diff-index --quiet HEAD; then
    git add .
    git commit -m "chore(release): update module pointers"
    git push origin main
else
    echo "⚡ No Git changes needed in shell."
fi

echo "==============================================================="
echo "✅ Server shell updated in CodeCommit."