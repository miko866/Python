import sys
import calendar

view_calendar = lambda yy, mm: print(f"\n\n Calendar > \n {calendar.month(yy, mm)} \n")

while True:
    if str(input("[+] Start [Y/n] ? ")).strip().lower() == "y":
        try:
            view_calendar(int(input("\nYear: ")), int(input("Month: ")))
        except IndexError:
            print("  -> Try Again!\n")
    else:
        print("\nSee You Soon.")
        sys.exit(0)

        