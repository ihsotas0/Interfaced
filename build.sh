#!/bin/bash

# Initalize variables for a new draft
echo "Making novel draft files..."
DATE=$(date '+%Y-%m-%d')
GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
DRAFT_TITLE="${GIT_BRANCH}_${DATE}"


# Create raw content file(s) containing all writing for book(s)
for book in $(ls -d content/*/ | xargs -n 1 basename)
do
    # Initalize things for specific book draft
    echo # New line
    echo "Found book: content/${book}"
    DRAFT_PATH="drafts/${DRAFT_TITLE}/${book}"
    mkdir -p ${DRAFT_PATH}

    # Start making raw draft file
    > ${DRAFT_PATH}/raw_content.md
    echo "Created/cleared: ${DRAFT_PATH}/raw_content.md"
    echo "Adding sections to: ${DRAFT_PATH}/raw_content.md..."

    # Add the sections one by one
    for file in $(ls content/${book})
    do
        if ! [[ ${file} =~ wip ]]; then # Check if the section is WIP
            cat content/${book}/${file} >> ${DRAFT_PATH}/raw_content.md
            echo "\n\n\n\n" >> ${DRAFT_PATH}/raw_content.md
        else
            echo "Excluding section: content/${book}/${file}"
        fi
    done

done

# Compile the raw content file(s) into PDF and EPUB file(s)
for book in $(ls -d drafts/${DRAFT_TITLE}/*/ | xargs -n 1 basename)
do
    # Make PDF
    echo # New line
    echo "Compiling: drafts/${DRAFT_TITLE}/${book}/JonahSpector_${book}.pdf..."
    
    # Compilation command and error handling
    if pandoc drafts/${DRAFT_TITLE}/${book}/raw_content.md \
    --toc --toc-depth=1 \
    --template style/book.tex \
    --metadata-file content/${book}/metadata.yml \
    -o drafts/${DRAFT_TITLE}/${book}/JonahSpector_${book}.pdf; then
        echo "PDF complete :)"
    else
        echo "PDF failed :("
    fi

    # Make EPUB
    echo "Compiling: drafts/${DRAFT_TITLE}/${book}/JonahSpector_${book}.epub..."

    # Compilation command and error handling
    if pandoc drafts/${DRAFT_TITLE}/${book}/raw_content.md \
    # TODO: Put EPUB options here
    -o drafts/${DRAFT_TITLE}/${book}/JonahSpector_${book}.epub; then
        echo "EPUB complete :)"
    else
        echo "EPUB failed :("
    fi

done