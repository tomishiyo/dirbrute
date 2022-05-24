import sys
import threading
import time

import requests


def make_request(url):
    try:
        answer = requests.get(url)
        if answer.status_code != 404:
            print(f'{url} --> {answer.status_code}')
    except Exception as error:
        print('Error: ', error)


def main():
    domain = sys.argv[1]
    wordlist_filename = sys.argv[2]

    wordlist = [line.strip() for line in open(wordlist_filename)]

    number_of_threads = 10

    start_time = time.time()
    while wordlist:
        threads = []
        for _ in range(number_of_threads):
            word = wordlist.pop(0)
            url = f'{domain}/{word}'
            threads.append(threading.Thread(target=make_request, args=[url]))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
    end_time = time.time()

    print(f'Time elapsed: {end_time - start_time}')


if __name__ == '__main__':
    main()
