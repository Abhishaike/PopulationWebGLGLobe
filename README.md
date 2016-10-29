# PopulationWebGLGLobe

This is a data visualization program utilizing the WebGLGlobe created by the Google Data Arts Team.
The included Heroku link will launch an application that will build three things: 

1. Using the included globe.js Javascript, graph the global population (on a city-by-city basis) from 1950-2050 in five year increments onto the globe. Each year has around 590 datapoints, and with 17 segements of years, there are just over 10,000 data points all together. 

2. Estimates the population (which uses average population growth rates and current time) and displays it in the top-right hand corner.
3. Creates a small menu of buttons which, when clicked on the corresponding year, will launch an image frame (Heat Map) created using Google Fusion Tables and the corresponding population data from that year. 

To begin with, I wrote the DataParser.py Python program I included in this repository to take data from an included .csv file and convert the relevant sections of it to a .json format, while I placed in the population909500.json file. The magnitudes of population included in the .json file were also normalized to a number between 0 and 1 by the DataParser.py program.

Next, I individually loaded each of the year-specific data sets into Google Fusion Tables, which created heat maps weighted with the population of a specific year. I then wrote the required CSS/HTML to take these year-specific image frames and display them with a button press in a non-intrusive and aesthetic way. By default, no image frames are displayed before a button has been pressed. To remove the presence of image frames from the Heroku application after any buttons have been pressed, simply reload the page. 

Finally, for fun, I found some existing code that can take in the existing time, along with previously recorderd rates of population growth, and spit out an estimation of the current population. This estimation is displayed in the top left hand corner. 
