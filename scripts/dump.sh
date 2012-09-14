#!/bin/sh

BASEDIR=$(dirname $0)
TARGETFILE=$BASEDIR/../fixtures/initial_data.xml
MANAGER=$BASEDIR/../manage.py

#echo $TARGETFILE
#echo $MANAGER
python $MANAGER dumpdata --format=xml --indent 2 --natural --exclude contenttypes.contenttype --exclude portlets.portletregistration --exclude sites.site --exclude export.script --exclude auth.permission > $TARGETFILE