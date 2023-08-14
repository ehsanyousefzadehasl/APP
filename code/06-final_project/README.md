# Final Project
The main process of this project, which is consisted of two parts, is:
1. Scraping an online shop and filling database with appropriate data for machine learning purposes
2. Training phase (using the gathered data in the part 1)

**Note**: This project can be applied to other websites just by changing the regexes.

## [Part 1](final_project.py)
1. Reading a number of pages from the [/bama.ir/](https://bama.ir/)
2. Ggoing into each post (by generating the link) to extract the data
3. If the data set of each post is not complete it will be ignored, otherwise, they will be mapped to numbers to be able to be used by machine learning model, which only works with numbers
4. Finally, filling the database table, which is going to provide training data, with just numbers (this is the first version, it needs refactoring and rethinking its efficiency)


## [Part 2](learning_phase.py)
(1) Reading from the prepared table
(2) Using them for training
(3) Its functionality tested according to the inserted data (it is mentioned because auto-increment is not same for everybody based on what he had done to his table (because of different number of manual inserts and deletes)). So, if you want to test it manually, test it appropriately with regard to your table content.

## More to do
1. Building an interface for easy interaction with the model
   - Using Django would be nice => We can use our designed tables to map the data to be easily choose among them and give them to the ML part (in a form)
2. It is not required for the model and the scraping part to be run based on each request. so using cronetab for scheduling a timely run can be useful for keeping the app update, and also saving processing power
3. Another suggestion is separating testing part from training.