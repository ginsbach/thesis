#!/usr/bin/python

import sys

print("****************************************************************** FILTERED LATEX DEBUG BEGIN ******************************************************************")

for line in sys.stdin:

    stack = [""]
    skip = False
    for char in line:
        if char == '(':
            stack.append("(")
        elif char == ')' and len(stack) > 1:
            stack = stack[:-1]
            skip = True
        elif char == ' ' and skip:
            skip=False
        elif char == '\n':
            stack = ["".join(stack)+char]
        else:
            stack[-1] = stack[-1]+char
    line = stack[0]

    stack = [""]
    skip = False
    for char in line:
        if char == '[':
            stack.append("[")
        elif char == ']' and len(stack) > 1:
            stack = stack[:-1]
            skip = True
        elif char == ' ' and skip:
            skip=False
        elif char == '\n' or char == ' ':
            stack = ["".join(stack)+char]
        else:
            stack[-1] = stack[-1]+char
    line = stack[0]

    if line == "\n":
        continue

    if line in ["This is pdfTeX, Version 3.14159265-2.6-1.40.18 \n",
                " restricted \write18 enabled.\n",
                "entering extended mode\n",
                "){/usr/share/texlive/texmf-dist/fonts/enc/dvips/base/8r.enc}</usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/rsfs/rsfs10.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrro8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvro8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/symbol/usyr.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\n",
                "{/usr/share/texlive/texmf-dist/fonts/enc/dvips/base/8r.enc}</usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb></usr/share/texlive/texmf-dist/fonts/type1/public/rsfs/rsfs10.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrro8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvro8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/symbol/usyr.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb></usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\n",
                "Output written on thesis.pdf .\n",
                "Transcript written on thesis.log.\n"]:
        continue

    sys.stdout.write(line)

print("******************************************************************* FILTERED LATEX DEBUG END *******************************************************************")