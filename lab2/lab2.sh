#!/bin/bash

# Lab 2 - Dana Harper
# Reads OverTheWire Bandit passwords, prints them alphabetically,
# and writes each one to its own file.

passwordFile="passwords.txt"
outputDir="password_files"

if [[ ! -f "$passwordFile" ]]; then
    echo "Error: $passwordFile not found"
    exit 1
fi

mkdir -p "$outputDir"

count=1
for password in $(sort "$passwordFile"); do
    echo "$password"
    echo "$password" > "$outputDir/password_${count}.txt"
    ((count++))
done

echo "Wrote $((count - 1)) files to $outputDir/"
