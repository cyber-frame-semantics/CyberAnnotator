# CyberAnnotator

Github Repo for CKIDS DataFest Spring 2021: Turning Cyber Data into Language Project. This web app annotates through JSON formatted cyber threat material via Wordnet, FrameNet and supported using Streamlit. 
Presentation: [Final Presentation](https://docs.google.com/presentation/d/1mhpxF4cnY0QpxWW-K0TgMlsAKG_97fRDCA9gQ81c2Ho/edit?usp=sharing)


#### Students Participants: 
Chuqi Liu, MS, 1st year
</br>
Carol Varkey, MS, 1st year
</br>
Ruoyu Li, MS, 1st year
</br>
Rengapriya Aravindan MS, 1st year
</br>

#### Advisor: 
Jeremy Abrahamson, Viterbi School of Engineering

## Installation 
For first time running WordNet and FrameNet, please uncomment the following lines:
```python
import nltk
nltk.download("all")
```
This first run will take a few minutes to download all the required peices. For future runs comment out the above mentioned lines and re-run the app. 

## Demo


## TODO
- output meaningful text
- cannot find all keys in some JSON file
- The output shown by streamlit is kind messy (improve UI)
- Need to handle case that some keys' synsets are empty
- For shortcircuit option, what to do w/ keys that contain underscore (input as is, seperate?)

## Future Improvements
- improve code efficiency
- updated UI
