# GPT4All Chatbot

2023-06-04: code here is based on this Medium post:
<https://levelup.gitconnected.com/free-open-source-alternative-to-chatgpt-gpt4all-ad5828e4dcae>


2023-06-11:  
- seems to require two pip installs: gpt4all, gradio (these two modules bring in many more)

- this code uses a smaller model than specified in the Medium post (to work well on my PC)
  (and the model will be downloaded if not previously installed.
     this *may* require the use of a HUGGINGFACE API_TOKEN)  
	 
- one way to manage these environment variables is to copy
  `../../env.sh-template` to `.env.sh`; add your key information; and
  `source env.sh` before running any programs.  
  N.B.: make sure your actual key values are *not* stored in a public
  repository.  See `../../gitignore`.  
  
2023-06-11:  
- added a way to terminate (without grace) the gradio interface

2023-06-17:
- observations about performance in terms of reliability and
  reproducability
  - reliability: responses constructed to questions may be wrong, even
    when information is attributed to an outside institution
  - reproducibilty: the same query yields the same answer (small test
    sample size)

--------
## Notes on running this program:  

- install a Python virtual environment:  
`$ python3 -m venv venv`  

- activate that environment and update the pip module:  
```
$ source venv/bin/activate`  
(venv) $ pip install --upgrade pip  
```  

- install the PyPi modules (these bring many modules with them):  
```
(venv) $ pip install gpt4all  
(venv) $ pip install gradio  
```  

- to run the program:  
`(venv) $ python gradioChat.py`  

  - this will install the specified model if needed, and this
  installation may require that the HUGGINGFACE_API_TOKEN be
  available.  
  - if successful an http server will be running on `localhost:7860`  
  - questions and requests can be entered on the web page; Prompt and
    Response will be shown on the web page and displayed in the
    Terminal  
  - the server can be terminated with the "Close Chatbot" button on
    the web page.  

