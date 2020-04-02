# -*- coding: utf-8 -*-
# Copyright: (C) 2019-2020 Lovac42
# Support: https://github.com/lovac42/SmallPotatoes
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


import aqt
import aqt.deckconf
from anki.hooks import wrap

from anki import version
ANKI21 = version.startswith("2.1.")


def listToUser(deckConf, steps, _old):
    arr=[]
    for i in steps:
        if i>=1440 and i%1440==0:
            i=str(i//1440)+'d'
        arr.append(str(i))
    return " ".join(arr)


def updateList(deckConf, conf, key, w, minSize=1, _old=None):
    if ANKI21:
        steps=str(w.text()).split(" ")
    else: #for older python 2.6 and 2.7
        steps=unicode(w.text()).split(" ")

    arr=[]
    for i in steps:
        if not i: continue
        if i.endswith('d'):
            i=i[:-1]
            i=int(i)*1440
        arr.append(i)
    w.setText(" ".join([str(x) for x in arr]))
    _old(deckConf, conf, key, w, minSize)


aqt.deckconf.DeckConf.updateList = wrap(aqt.deckconf.DeckConf.updateList, updateList, pos="around")
aqt.deckconf.DeckConf.listToUser = wrap(aqt.deckconf.DeckConf.listToUser, listToUser, pos="around")


