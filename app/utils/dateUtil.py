def findTimeFrame(df):

    if len(df.index) > 2:
        dtDiff = df.index[1] - df.index[0]

        if dtDiff.seconds == 60:
            return "M1"
        elif dtDiff.seconds == 300:
            return "M5"
        elif dtDiff.seconds == 900:
            return "M15"
        elif dtDiff.seconds == 1800:
            return "M30"
        elif dtDiff.seconds == 3600:
            return "H1"
        elif dtDiff.seconds == 14400:
            return "H4"
        elif dtDiff.seconds == 86400:
            return "D"
        elif dtDiff.seconds == 604800:
            return "W"

    pass