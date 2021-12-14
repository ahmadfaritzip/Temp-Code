import pyautogui as gui
from time import sleep, time
import string, random, sys
import argparse
import configparser


def parse_arguments():
    parser = argparse.ArgumentParser(description='Spam Chat Sosmed (wa, fb, ig, tw, telegram, dll)')
    parser.add_argument('-n','--number', type=int, metavar='', required=True, default=50, help='Panjang text yang akan dikirim.')
    parser.add_argument('-t','--time_running', type=int, metavar='', default=2, help='Lama waktu jalankan program.')
    parser.add_argument('-p','--pause', type=int, metavar='', default=2, help='Jeda waktu jalankan program.')

    args = parser.parse_args()
    return args

def main():
    arguments = parse_arguments()
    panjang_text = arguments.number
    time_running = arguments.time_running
    pause = arguments.pause

    #jeda waktu ketika program dijalankan
    sleep(pause)

    start_time = time()

    while 1:
        string_random = ''.join(random.choices(
            string.ascii_lowercase + string.digits, 
            k=panjang_text))
        gui.write(string_random) #paste
        gui.press('enter') #tekan enter

        # berhentikan program ketika sudah mencapai time-running
        if (int(time() - start_time)) == time_running:
            break

if __name__=='__main__':
    main()

