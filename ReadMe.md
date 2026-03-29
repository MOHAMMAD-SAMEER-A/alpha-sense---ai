mkdir alphasense-ai && cd alphasense-ai
git init
echo "# AlphaSense AI" > README.md
git add README.md
git commit -m "initial: create repo and README"
git branch -M main
git remote add origin https://github.com/<your-username>/alphasense-ai.git
git push -u origin main
