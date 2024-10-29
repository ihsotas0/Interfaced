#!/bin/sh

echo "Making novel draft files..."
DATE=$(date '+%Y-%m-%d')
GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
DRAFT_TITLE="${GIT_BRANCH}_${DATE}"

for book in $(ls -d content/*/ | xargs -n 1 basename)
do
    echo "Found book: content/${book%%/}"
    DRAFT_PATH="drafts/${DRAFT_TITLE}/${book%%/}"
    mkdir -p ${DRAFT_PATH}
    > ${DRAFT_PATH}/raw_content.md
    echo "Created/cleared ${DRAFT_PATH}/raw_content.md"
    echo "Adding content to ${DRAFT_PATH}/raw_content.md..."
    for file in $(ls content/${book})
    do
        cat content/${book}/${file} >> ${DRAFT_PATH}/raw_content.md
        echo "\n\n\n" >> ${DRAFT_PATH}/raw_content.md
    done
done

for book in $(ls -d drafts/${DRAFT_TITLE}/*/ | xargs -n 1 basename)
do
    echo "Compiling drafts/${DRAFT_TITLE}/${book}/JonahSpector_${book}.pdf..."
    pandoc drafts/${DRAFT_TITLE}/${book}/raw_content.md \
    --metadata-file content/${book}/metadata.yml \
    -o drafts/${DRAFT_TITLE}/${book}/JonahSpector_${book}.pdf
done

echo "...Done!"

