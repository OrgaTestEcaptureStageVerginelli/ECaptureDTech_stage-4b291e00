# ECaptureDTech_stage

Automatisation internship

How to run this project :
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt


To run FastAPI, go to EcaptureDTech_stage/local :
fastapi dev

To run the tests, go to EcaptureDTech/ :
python tests.py

For the Pre-Commit feature :
  if you use command line (git add . and git commit -m "...") you will see the errors froñ the hooks of the pre-commit, just add verbose: true on the hooks you want
  if you use the VSCode interface to commit, you can see the error in the OUTPUT section (Next to Debug Console and Terminal)
  for the VSCode interface, you need to go to the settings -> search "git command", section "Git: Commands To Log", Add Item -> write "commit"

You can use the command : pre-commit autoupdate to update all your repo in .pre-commit-config.yaml (auto fix)
