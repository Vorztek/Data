def convert_second(seconde):
    heure = seconde // 3600
    seconde = seconde - 3600 * heure
    minute = seconde  // 60
    seconde = seconde - 60 * minute
    print(heure, minute, seconde)

convert_second(3601)