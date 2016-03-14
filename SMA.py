import copy

def matchmaker(guyprefers, galprefers):
    guys = sorted(guyprefers.keys())
    gals = sorted(galprefers.keys())
    guysfree = guys[:]
    engaged  = {}
    guyprefers2 = guyprefers.copy()
    galprefers2 = galprefers.copy()
    while guysfree:
        guy = guysfree.pop(0)
        print guy.name
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # She's free
            engaged[gal] = guy
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                # if guyprefers2[fiance]: # why is this needed? guy will always have preference list
                #     # Ex has more girls to try
                guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged
