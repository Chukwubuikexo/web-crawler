I selected carsdirect(dot)come as the ecommerce website for car listings and prices. 
In my analysis of the HTML structure and DOM elements of the website, revealed that Selenium would be the best tool for a crawler.
To avoid rate limiting and IP blocking, I used User-Agents to randomize my access and mimick human access. I also introduced request delays.
To schedule the daily scraping process, i utilized Github Actions, creating a yml file with the instruction to run at 12am daily.
The yml file also contained instructions and required permissions to load the car_list results incrementally into the lig query warehouswe
In Github Actions i set up notifcations to my email to monitor and alert for successful scraping operations, as well as for errors or failures.