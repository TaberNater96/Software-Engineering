#!/bin/bash

##################################################################################
#                                                                                #
#                               Build Automation                                 #
#                                                                                #
# Build Script - automate a build process                                        #
# This script copies files from the source directory to the build directory,     #
# handling exceptions and notifying the user. It extracts the version number     #
# from the changelog and prompts the user for confirmation before proceeding.    #
# Contains logic to ensure that a secret file is not copied from the source      #
# directory into the build directory.                                            #
##################################################################################

echo "Welcome to the Build Script!"

# Read the first line of changelog.md
firstline=$(head -n 1 source/changelog.md)

# Split the first line into an array
read -a splitfirstline <<< "$firstline"

# Set the version
version=${splitfirstline[1]}

# Notify user of the version
echo "You are building version $version"

# Ask user to continue
echo "Enter 1 to continue or 0 to exit:"
read versioncontinue

if [ "$versioncontinue" = "1" ]; then
    echo "OK, proceeding with the build..."
    
    # Iterate over files in source directory
    for file in source/*; do
        filename=$(basename "$file")

        # Add logic to not copy the secret file
        if [ "$filename" = "secretinfo.md" ]; then
            echo "Not copying $filename"
        else
            echo "Copying $filename to build directory"
            cp "$file" build/
        fi
    done

    # Change to build directory
    cd build

    # List files in build directory
    echo "Files in version $version build:"
    ls

    # Change back to original directory
    cd ..
else
    echo "Please come back when you are ready"
fi