@echo off


REM Stage all changes
git add .

REM Commit changes with a message
git commit -m "Update datetime.txt and other changes"

REM Push changes to the remote repository
git push origin main

echo Project has been added to GitHub successfully.