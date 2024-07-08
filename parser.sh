#!/bin/bash
/usr/bin/python3 /opt/pars/habr.py > /opt/pars/feed.txt
/usr/bin/python3 /opt/pars/send.py
sleep 15
/usr/bin/python3 /opt/pars/habr_bl.py > /opt/pars/feed.txt
/usr/bin/python3 /opt/pars/send.py
sleep 15
/usr/bin/python3 /opt/pars/HN.py > /opt/pars/feed.txt
/usr/bin/python3 /opt/pars/send.py
sleep 15
/usr/bin/python3 /opt/pars/xakep.py > /opt/pars/feed.txt
/usr/bin/python3 /opt/pars/send.py
sleep 15
/usr/bin/python3 /opt/pars/SP.py > /opt/pars/feed.txt
/usr/bin/python3 /opt/pars/send.py
