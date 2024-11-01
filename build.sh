#!/bin/bash

echo "Making novel draft files..."
DATE=$(date '+%Y-%m-%d')
GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
DRAFT_TITLE="${GIT_BRANCH}_${DATE}"

for book in $(ls -d content/*/ | xargs -n 1 basename)
do
    echo
    echo "Found book: content/${book}"
    DRAFT_PATH="drafts/${DRAFT_TITLE}/${book}"
    mkdir -p ${DRAFT_PATH}
    > ${DRAFT_PATH}/raw_content.md
    echo "Created/cleared: ${DRAFT_PATH}/raw_content.md"
    echo "Adding content to: ${DRAFT_PATH}/raw_content.md..."
    for file in $(ls content/${book})
    do
        if ! [[ ${file} =~ wip ]]; then
            cat content/${book}/${file} >> ${DRAFT_PATH}/raw_content.md
            echo "\n\n\n\n" >> ${DRAFT_PATH}/raw_content.md
        else
            echo "Excluding: content/${book}/${file}"
        fi
    done
done

for book in $(ls -d drafts/${DRAFT_TITLE}/*/ | xargs -n 1 basename)
do
    echo
    echo "Compiling: drafts/${DRAFT_TITLE}/${book}/JonahSpector_${book}.pdf..."
    if pandoc drafts/${DRAFT_TITLE}/${book}/raw_content.md \
    --toc --toc-depth=1 \
    --template style/book.tex \
    --metadata-file content/${book}/metadata.yml \
    -o drafts/${DRAFT_TITLE}/${book}/JonahSpector_${book}.pdf; then
        echo "Complete :)"
    else
        echo "Something went wrong :("
    fi
done