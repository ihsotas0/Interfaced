#!/bin/sh

echo "Making novel draft files..."
DATE=$(date '+%Y-%m-%d')
GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
DRAFT_TITLE="${GIT_BRANCH}_${DATE}"

mkdir -p drafts/${DRAFT_TITLE}
echo "Made directory: drafts/${DRAFT_TITLE}"

touch drafts/${DRAFT_TITLE}/raw_content.md
echo "Made raw content file: drafts/${DRAFT_TITLE}/raw_content.md"



