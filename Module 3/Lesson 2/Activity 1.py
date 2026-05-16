def total_calc(total_amount,tip_perc):
    total=total_amount*(1+0.01*tip_perc)
    print(f"Please pay BDT {total}")
total_calc(735.36,15)