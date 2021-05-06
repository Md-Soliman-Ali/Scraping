1. Download Scraping Folder
 
2. Go To Scraping Folder Using cmd
 
3. Now, Type ( pip install virtualenv ) Then ( virtualenv myenv ) Again Type ( myenv\scripts\activate ) [ myenv = you can use any environment name ]
 
4. Install Required Liberty
   1. pip install scrapy
   2. pip install pypiwin32
   
5. Again, Type ( scrapy startproject webscraping . )

6. Now, You Will Get Another Folder, Called webscraping. Copy ( quotes_spiders.py ) Files Into webscraping -> spiders Folder

7. Go To The spiders Folder using cmd 
   1. cd webscraping
   2. cd spiders

8. Now, Type ( scrapy runspider quotes_spiders.py -o quotes.xml ) [ also we can save csv & json ]   

9. Now, You Will Get ( quotes.xml ) That Contain The Values

10. Install Visual Studio Code For Editing ( quotes_spiders.py ) File.
