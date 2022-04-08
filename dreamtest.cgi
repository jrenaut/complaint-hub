#!/bin/sh

GIT_REPO=https://github.com/jrenaut/complaint-hub.git
TMP_GIT_CLONE=/home/jrenaut/new.complainthub.com/tmp
PUBLIC_WWW=/home/jrenaut/new.complainthub.com/public

git clone $GIT_REPO $TMP_GIT_CLONE
cp /home/jrenaut/new.complainthub.com/mynt.yml /home/jrenaut/new.complainthub.com/tmp/mynt.yml
source /home/jrenaut/new.complainthub.com/myntenvnew/bin/activate
mynt gen -f $TMP_GIT_CLONE $PUBLIC_WWW
rm -rf $TMP_GIT_CLONE
deactivate

echo "All done!"




