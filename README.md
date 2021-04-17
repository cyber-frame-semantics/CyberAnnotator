# CyberAnnotator (Turning Cyber Data into Language)

Github Repo for CKIDS DataFest Spring 2021: Turning Cyber Data into Language Project. This web app annotates through JSON formatted cyber threat material via Wordnet, FrameNet and supported using Streamlit. 
</br>

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

Run the streamlit program with the following command:
```python
streamlit run main.py
```
This first run will take a few minutes to download all the required peices. For future runs comment out the above mentioned lines and re-run the app. 

## TODO
- JSON Path Indexing Issue
- Cannot find all keys in some JSON file
- Need to handle case that some keys' synsets are empty
- Possible warning when initially run the code, after file is loaded error is gone

## Future Improvements
- Improve code efficiency
- Improve UI
