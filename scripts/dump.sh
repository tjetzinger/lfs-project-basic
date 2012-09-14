#!/bin/sh

BASEDIR=$(dirname $0)
TARGETFILE=$BASEDIR/../fixtures/initial_data.xml
MANAGER=$BASEDIR/../manage.py

#echo $TARGETFILE
#echo $MANAGER
python $MANAGER dumpdata --format=xml --indent 2 --exclude auth.user --exclude auth.permission --exclude contenttypes.contenttype --exclude sessions.session --exclude sites.site --exclude portlets.portletregistration --exclude export.script > $TARGETFILE