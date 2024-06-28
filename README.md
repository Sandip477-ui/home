
jan = 500
feb = 600
mar = 700
apr = 800
may = 900
jun = 1000
jul = 1100
aug = 1200
sep = 1300
oct = 1400
nov = 1500
dec = 1000

expanses = {
    "jan": jan,
    "feb": feb,
    "mar": mar,
    "apr": apr,
    "may": may,
    "jun": jun,
    "jul": jul,
    "aug": aug,
    "sep": sep,
    "oct": oct,
    "nov": nov,
    "dec": dec
}

total = sum(expanses.values())
print(f"total expanses is {total}")
print(f"Average expanses is {total / 12}")