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

