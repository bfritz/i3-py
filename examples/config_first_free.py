#!/usr/bin/python3

"""
Find the first free workspace and configure it with two
side-by-side containers with stacked windows.  Start browser
on left side and terminal on right.

Add this to your i3 config file:
    bindsym <key-combo> exec python /path/to/this/script.py
"""
import i3
import os
import time

term = os.environ.get('TERM', 'xterm')
if 'rxvt-unicode' in term:
    term = 'urxvt'

browser = os.environ.get('BROWSER', 'firefox')

# TODO: try replacing sleep() with subscription to window event
def main():
    i3.workspace(str(first_free()))
    i3.layout('default')
    i3.exec(browser)
    time.sleep(1)   # give browser window time to spawn
    i3.exec(term)
    time.sleep(0.5) # give terminal window time to spawn
    i3.split('v')
    i3.layout('stacking')
    i3.focus('left')
    i3.split('v')
    i3.layout('stacking')

def first_free():
    workspaces = i3.get_workspaces()
    workints = list()
    for w in workspaces:
        workints.append(w['num'])
    for i in range(1,11):
        if i not in workints:
            return i

if __name__ == '__main__':
    main()
