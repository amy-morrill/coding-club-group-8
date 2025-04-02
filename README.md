# coding-club-group-8

## Downloading Python:

Before developing in this repo you will need to download python. To do so you must do the following:
- Request local admin access using SNOW: https://tempus.service-now.com/esc?id=sc_cat_item&sys_id=35ee47391bfae410f3b48730604bcbe1
- Follow the instructions once local admin access has been granted
- Once you have local admin access, install brew: https://brew.sh/
- Run the following commands:
```
brew install pyenv
pyenv install 3.12.8
```

## Running tkinter test script
From the root folder of this repo, run the following command:
```
python test_script.py
```

## Running streamlit test script
Make sure you have streamlit downloaded by running:
```
python -m pip install -r requirements.txt
```
Then run the following command from the root folder of this repo:
```
streamlit run test_script_streamlit.py
```
This will open a browser rendering the test script.

## Streamlit docs:
Streamlit playground to test out code (but doesn't get saved anywhere): https://streamlit.io/playground
Streamlit documentation: https://docs.streamlit.io/
Streamlit cheat sheet: https://docs.streamlit.io/develop/quick-reference/cheat-sheet
