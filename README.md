# screenshot-pdf-converter

A python script that iterates through pages of a eBook, takes a screenshot and merges it to a pdf. 

## Dependencies

    -time
    -PIL
    -pyautogui
    -PyPDF2
    -pynput

pyautoui is used to take a cropped screenshot, then pynput simulates  space bar keypress to go to the next page. The location and size of the screenshot as well as the number of iterations can be editted in screenshot_keypress.py. The simulated key press can also be changed to a different key.

## Running

Clone repo and ensure all dependencies are installed, then run:
    
    python screenshot_keypress.py

The script will wait a few seconds before starting. When it's done it will create the merged master pdf 'result.pdf.' It also creates a pdf for every screenshot. to delete these, run:

    python clean.py

This is kinda jank for now, I'll clean it up and make it a single script later.


No copyright infringement intended.
