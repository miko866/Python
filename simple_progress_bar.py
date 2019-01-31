# Python script to create a simple progress bar

import sys, time

def progress_bar(count, total, suffix=''):
    bar_length = 60
    filled_length = int(round(bar_length * count / float(total)))
    percent = round(100.0 * count / float(total), 1)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write(f'\n{[bar]} {percent}"%" ...{suffix}')
    sys.stdout.flush()

for i in range(20):
    time.sleep(1)
    progress_bar(i, 20)
