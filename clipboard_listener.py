import sys
import time
import tkinter
import argparse
import logging

# logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                    format='[%(asctime)s] - PID: %(process)d - TID: %(thread)d - %(levelname)s - %(message)s')

def process_content(content):
    logging.debug('Processing content: {}'.format(content))
    pass

def listener():
    """
    Function to run loop to continuously check for clipboard changes.
    Copying twice the same content will be ignored.
    """
    content = ''            # Clipboard content
    wait_time = 3           # Seconds to wait between each clipboard check
    tk = tkinter.Tk()       # Use Standard Library tkinter approach to read clipboard
    while 1:
        try:
            if content != tk.clipboard_get():
                content = tk.clipboard_get()
                process_content(content)
        except Exception as e:
            logging.error(e)
        finally:
            logging.debug('Waiting for {} seconds.'.format(wait_time))
            time.sleep(wait_time)

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--version', action='version', version='0.1')
        parser.add_argument('-q', '--quick', help='Listen with default configuration', action='store_true')
        args = parser.parse_args()

        if len(sys.argv) < 2:
            parser.print_help()
            sys.exit(0)

        logging.info('Starting Clipboard Listener...')
        if args.quick:
            listener()

    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    main()