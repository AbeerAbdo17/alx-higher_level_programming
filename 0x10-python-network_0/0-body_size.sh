#!/bin/bash

# Check if URL is provided as an argument
if [ $# -ne 1 ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi
response=$(curl -Is "$1")

if [ $? -ne 0 ]; then
	    echo "Error: Unable to retrieve headers from the URL."
	        exit 1
fi

content_length=$(echo "$response" | grep -w 'Content-Length' | cut -f2 -d' ')
if [ -n "$content_length" ]; then
	    echo "$content_length"
    else
	        echo "Content-Length header not found in the response."
fi
