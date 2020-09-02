## Glassdoor Project: Introduction into Data Science
### Project Overview
* This project was my first introduction into a full data science project. My goals going into the project were to obtain a basic understanding for the fundamentals of data science through data analysis and to gain direct practice in the technical skills needed to complete a project.
* A side benefit that came from this project was gaining a better understanding for the requirements real companies need from their Data Scientists. Creating a word cloud in the exploratory data analysis (EDA) section of this project based on the job descriptions allowed me to understand the core requirements. The key takeaways from the word cloud consisted of:
	* **Machine Learning** - This skillset made up the widest phrase in the word cloud. Additional focus on technical aspects companies look for will be an important part of progressing towards a career in Data Science. While my interests will ultimately dictate the roles I want to follow, I can use the information from this word cloud to gear my hands-on learning approach.
	* **Words that align with my background** - As I shift towards completing a Master’s Degree in Applied Data Science, the words that stand out in the word cloud like analytic, insight, research, customer, and solution make up a major part of my prior work. While my background is analyst-focused, I worried that my prior experience in designing products in support of the United States military and government might not translate over. However, the analytical thinking paired with more technical knowledge should translate well into a Data Science Career.
	* **Further Analysis** - I would like to analyze the exact number of companies using individual phrases based on the weight they carried in the word cloud. I also plan to limit certain words and phrases to capture a wider set of valuable information from the word cloud.
* This tool estimates possible salaries of Data Scientists to about an 11,000-dollar accuracy in mean absolute error (MAE). Designing this tool following the step-by-step project instructions from Ken Jee (see resources) and gave me insights into using linear regression, Lasso, and Random Forrest Regressors with GridsearchCV.
* The full scope of the tool scrapes Glassdoor looking to capture a wide variety of information on each job posting. In total, I scraped 1,000 different job postings with the web scrapper designed by arapfaik. With the help of the tutorials by Ken Jee, I learned techniques to pull specific words from the job descriptions to identify the number of companies looking for skillsets like Python, R, and other languages related to data science. Finally, the project also contains client a client facing API through the help of Flask.
### Resources
**1. Author: Ken Jee**
   - Followed guides to create first data science projects from beginning to end.
   - [Link to webpage](https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t)
   
**2. Author: arapfaik**
   - Relied on the scraper code to get data from Glassdoor.
   - [Link to webpage](https://github.com/arapfaik/scraping-glassdoor-selenium)
   
**3. Author: Ömer Sakarya**
   - Guide used for explaining how the scraper works.
   - [Link to webpage](https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905)
   
**4. Author: Chris I.**
   - Following guide for productionizing through Flask.
   - [Link to webpage](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2)
