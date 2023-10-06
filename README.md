<div align="center">

<h3 align="center">Instagram Profile Personality Classifier</h3>

  <p align="center">
    Notebooks studying personality traits classification from Instagram profiles.
    <br />
  </p>
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#challenges">Challenges</a></li>
      </ul>
    </li>
    <li><a href="#libraries">Libraries</a></li>
    <li><a href="#todos">Todos</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



## About The Project
This project is our try at training NLP and Image Processing models to be able to classify personality traits (using the 16 personality trait model) from the textual (captions) and media (pictures and videos) data scrapped from Instagram, starting from a CSV file which contains Instagram usernames and their personality classification that previous students made after long and tiring work, this wouldn't have been possible without them so we are truly grateful. 

To get the full details, analysis and results of our work you can check out [this report](https://drive.google.com/file/d/1nKqIeuZ9hluFpKxQmCGqYy9PUM1LOYh7/view?usp=sharing). 

### Challenges
- The first hurdle we had to overcome in order to pursue this project was how do we gather the data knowing that Meta now has strict control over scrapping and gathering of data on their platforms. For this we used a python module called Instaloader, which took a username and time period as a parameter and was able to download all media of that username within that specific timeframe to the local machine. it was rather easy to make a script that read the usernames from the csv and ran this function iteratively. We seperated this work on all members of our group as it took time and bandwith to complete the task.
- The second hurdle was adjusting the bert model which we expected to have the best results for the textual data and training it knowing we had limited computational ressources.


## Libraries
 - [ScikitLearn](https://scikit-learn.org/)
 - [Tensorflow](https://www.tensorflow.org/)
 - [Pandas](https://pandas.pydata.org/)
 - [Numpy](https://numpy.org/)
 - [Keras](https://keras.io/)
 - [OpenCV](https://opencv.org/)
 - [seaborn](https://seaborn.pydata.org/)

## Todos
- [x] Write Thesis containing all details of work.
- [x] Try different NLP Models not just Bert.
- [x] Package models.
- [ ] Deploy Models.
- [ ] Find hosting and computing solutions.
- [ ] Build pipeline to improve data.

## Acknowledgements

We acknowledge and thank the students who made the dataset before us, without them this wouldn't have been possible.

We also acknowledge and thank our mentor during this project [Dr. Sana HAMDI](https://www.researchgate.net/profile/Sana-Hamdi-2) for their invaluable theoritical guidance and time.

