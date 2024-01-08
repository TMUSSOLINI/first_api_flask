import time

def duration_time(function):
    def wraper():
        init = time.time()
        function()
        final = time.time()

        print('O tempo total da função {} foi de {}'.format(function.__name__, float(final-init)))

    return wraper

@duration_time
def main():
    for i in range(1,1000000):
        pass

main()