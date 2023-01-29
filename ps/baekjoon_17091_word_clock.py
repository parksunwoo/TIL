# h = int(input())
# m = int(input())

h = 7
m = 25

alpha_m = alpha_h = ""
connect = "past"

d = { 0 : "o' clock", 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 
      5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
     11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
     15 : 'quarter', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
     19 : 'nineteen', 20 : 'twenty', 30 : 'half'}

if m > 30:
    h = h + 1
    m = 60 - m
    connect = "to"

if h > 12:
    h = h - 12

if m < 30 and m > 20:
    mod_m = m - 20
    alpha_m = d[20] + " " + d[mod_m]
else:
    alpha_m = d[m]

if m == 0:
    print(d[h]+ " " + d[m])
elif m == 1:
    print(d[m]+ " minute " + connect + " " + d[h])
elif m in [15, 30]:
    print(d[m]+ " " + connect + " " + d[h])
else:
    print(alpha_m+ " minutes " + connect + " " + d[h])
