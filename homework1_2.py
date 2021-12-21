while True:
    sec = input('Please, enter seconds:')

    if sec.isdigit():
        break

sec = int(sec)

hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = ((sec % 3600) % 60) % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
