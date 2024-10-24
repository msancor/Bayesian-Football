# Using Bayesian Modeling to Predict Football Matches after the COVID-19 Pandemic

This is a Github repository created to submit the final project of the **Statistical Methods in Data Science and Laboratory II (SDS)** course for the MSc. in Data Science at the Sapienza University of Rome. The main goal of this project was to reproduce and extend some of the results presented by the published article: *Lee, Jaemin & Kim, Juhuhn & Kim, Hyunho & Lee, Jong-Seok. (2022). A Bayesian Approach to Predict Football Matches with Changed Home Advantage in Spectator-Free Matches after the COVID-19 Break. Entropy. 24. 366. 10.3390/e24030366.*

We acknowledge the authors as the full responsibles of this project and this reproduction is made only for didactic purposes. If you attempt to reproduce the results presented on this repository, please cite the original article:

```markdown
@article{article,
author = {Lee, Jaemin and Kim, Juhuhn and Kim, Hyunho and Lee, Jong-Seok},
year = {2022},
month = {03},
pages = {366},
title = {A Bayesian Approach to Predict Football Matches with Changed Home Advantage in Spectator-Free Matches after the COVID-19 Break},
volume = {24},
journal = {Entropy},
doi = {10.3390/e24030366}
}
```


--- 
## What's inside this repository?

1. `README.md`: A markdown file that explains the content of the repository.

2. `data/data_scraper.py`: A Python file containing all the relevant code to scrape data from football matches for all the relevant seasons and leagues used in the project.

3. ``modules/``: A folder including 5 Python modules used to make simulations and plotting in `main.ipynb`. The files included are:

    - `final_project/final_project.Rmd`: An RMarkdown file containing all the relevant code and Markdown text to create the final report of the project.

    - `final_project/DBDA2E-utilities.py`: An R file including utility functions used in the book *Kruschke, J. K. (2015). Doing Bayesian Data Analysis, Second Edition: A Tutorial with R, JAGS, and Stan. Academic Press / Elsevier.*

    - `final_project/master.bib`: A .bib file containing the bibliography of the report.

    - `final_project/final_project.pdf`: Final report of the project in pdf format.

4. ``.gitignore``: A python gitignore file.

5. `LICENSE`: A file containing an MIT permissive license.

## Datasets

The data used to work in this repository was obtained via simulations by running the `data/data_scraper.py` file. In order to obtain the data used for the analysis follow the steps below:

**1.** Make sure you modify the saving path accordingly to where you want to obtain the data.

**2.** Run the `data/data_scraper.py` file using the following command:

```bash
python3 data/data_scraper.py
```

---

**Author:** Miguel Ángel Sánchez Cortés

**Email:** sanchezcortes.2049495@studenti.uniroma1.it

*MSc. in Data Science, Sapienza University of Rome*
