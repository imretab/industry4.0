# industry4.0
Project for the industry4.0 lecture
(written in Python)
## Used resources
[request didn't work](https://stackoverflow.com/questions/67660164/submitting-form-data-with-python-requests-post-not-working) \
[getting data from html table](https://stackoverflow.com/questions/11790535/extracting-data-from-html-table) \
[webscraping tutorial](https://www.geeksforgeeks.org/python-web-scraping-tutorial/) \
[TKinter GUI](https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/) \
[TKinter date picker](https://www.geeksforgeeks.org/create-a-date-picker-calendar-tkinter/)
### Packages
- requests
- bs4
- tkinter
- tkcalendar
- pandas 
- matplotlib
  - matplotlib.figure
  - matplotlib.backends.backend_tkagg
### What's the main goal of this program?
This program makes statistics from the lottery draws made on the given date (Putto).
### How does it work?
The user selects the date from the datepicker, presses the button, it'll send a request to the site, scrapes the useable data, then creates statistics from the data.
