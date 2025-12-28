New more basic try just to get this site working quickly

Started off with docker initially, but too many problems with SELinux
and permissions, so in order to save time we will do it like this and
slowly make it nicer.


""" bash
git clone <thisapp>
cd c3-edu-statistiken
python3 -m venv .venv(.fish)
. .venv/bin/activate
pip install flask
"""
