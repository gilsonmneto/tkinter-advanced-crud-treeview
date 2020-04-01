git init
git add .
git commit -m "first commit"
for %%I in (.) do set CurrDirName=%%~nxI
git remote add origin https://github.com/gilsonmneto/%CurrDirName%
git push -u origin master
