#!/bin/sh

GIT_REPO=https://github.com/jrenaut/complaint-hub.git
TMP_GIT_CLONE=/home/jrenaut/new.complainthub.com/tmp
PUBLIC_WWW=/home/jrenaut/new.complainthub.com/public

git clone $GIT_REPO $TMP_GIT_CLONE
source /home/jrenaut/new.complainthub.com/mynt/bin/activate
mynt gen -f $TMP_GIT_CLONE $PUBLIC_WWW
rm -rf $TMP_GIT_CLONE
deactivate

echo "Content-type: text/html"
echo ""
echo "Hello, world!"




