Possible problems with the current setup:
    - Since I'm not using forms there's no url input validation (i.e illegal chars).
    - For every POST request there's a new entry in the database. I've added a time_created 
        attribute for the ShortLongUrl model so in the future we could check or prioritize url entries
        by date (essentially a timeout).
    - Another possible problem is integer overflow with incrementing the number of times a url had been 
        clicked.
    - Added posgresql integration instead of the default sqlite, changing between them is as simple as
        commenting in settings.py the configuration of postgresql and uncommenting the default configuration 
        for sqlite.
    - Containing in Postman folder is are examples of POST & GET HTTP requests.
   
