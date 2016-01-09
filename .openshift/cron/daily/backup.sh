#!/bin/bash
# Backs up the OpenShift content - the uploaded media PostgreSQL database and related django code
# application's static files are expected to be "backed up" in the git repository
#
# Author: Radek Svarz radek@svarz.cz
#
# Requires cron cartridge
#
# if not installed, add to the application:
#   rhc app cartridge add -a yourapplication -c cron-1.4
#
# install the backup by putting into the cron/daily dir and list in the jobs.allow file
#
# adapted from http://nicaw.wordpress.com/2013/04/18/bash-backup-rotation-script/
# 

BACKUP_DIR=$OPENSHIFT_DATA_DIR/backup

# Create backup dirs
if [ ! -d $OPENSHIFT_DATA_DIR/backup ]; then
    mkdir $OPENSHIFT_DATA_DIR/backup
    mkdir $OPENSHIFT_DATA_DIR/backup/queue
    mkdir $OPENSHIFT_DATA_DIR/backup/daily
    mkdir $OPENSHIFT_DATA_DIR/backup/weekly
    mkdir $OPENSHIFT_DATA_DIR/backup/monthly
fi 
 
NOW="$(date +"%Y-%m-%d")"

# Collect DB dump
FILENAME="$BACKUP_DIR/queue/$OPENSHIFT_APP_NAME.$NOW.backup.sql.gz"
pg_dump $OPENSHIFT_APP_NAME | gzip > $FILENAME 

# Collect media files
if [ -d $OPENSHIFT_DATA_DIR/media ]; then
    cd  $OPENSHIFT_DATA_DIR
    tar -czvf $BACKUP_DIR/queue/$OPENSHIFT_APP_NAME.$NOW.backup.media.tgz  media/
fi 

# Collect real code snapshot
cd $OPENSHIFT_REPO_DIR
cd ..
tar -czvf $BACKUP_DIR/queue/$OPENSHIFT_APP_NAME.$NOW.backup.code.tgz repo/ 

# Get current month and week day number
month_day=`date +"%d"`
week_day=`date +"%u"`

# On first month day do
if [ "$month_day" -eq 1 ] ; then
  destination=$BACKUP_DIR/monthly
else
  # On saturdays do
  if [ "$week_day" -eq 6 ] ; then
    destination=$BACKUP_DIR/weekly
  else
    # On any regular day do
    destination=$BACKUP_DIR/daily
  fi
fi

# Move the files
mv -v $BACKUP_DIR/queue/* $destination

#
# Remove old backups
#

# daily - keep for 14 days
find $BACKUP_DIR/daily/ -maxdepth 1 -mtime +14 -type f -exec rm -rv {} \;

# weekly - keep for 60 days
find $BACKUP_DIR/weekly/ -maxdepth 1 -mtime +60 -type f -exec rm -rv {} \;

# monthly - keep for 400 days
find $BACKUP_DIR/monthly/ -maxdepth 1 -mtime +400 -type f -exec rm -rv {} \;
