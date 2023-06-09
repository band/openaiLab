#! /usr/bin/env python

#### IMPORTS FOR AI PIPELINES ###############
#from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
#from transformers import AutoModel, T5Tokenizer, T5Model
#from langchain.llms import HuggingFacePipeline
### IMPORTS NEEDED FOR THIS PROGRAM
from transformers import pipeline
from transformers import T5Tokenizer
from transformers import T5ForConditionalGeneration

import torch
import datetime

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

######################################################################
#     SUMMARIZATION FROM TEXT STRING WITH HUGGINGFACE PIPELINE       #
######################################################################
def AI_SummaryPL(checkpoint, text, chunks, overlap):
    """
    checkpoint is in the format of relative path
    example:  checkpoint = "./model/"  #it is actually LaMini-Flan-T5-248M 
    text: a long string; or an input long string; or a document read into a string
    chunks: integer, length of the split chunks
    overlap: integer, overlap for attention and focus retreival
    RETURNS full_summary (str), delta(str) and reduction(str)

    ? post_summary14 = AI_SummaryPL(LaMini,doc2,3700,500)
    USAGE EXAMPLE:
    post_summary, post_time, post_percentage = AI_SummaryPL(LaMini,originalText,3700,500)
    """
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.? for example ???
        chunk_size = chunks,
        chunk_overlap  = overlap,
        length_function = len,
    )
    texts = text_splitter.split_text(text)
    checkpoint = checkpoint
    tokenizer = T5Tokenizer.from_pretrained(checkpoint)
    base_model = T5ForConditionalGeneration.from_pretrained(checkpoint,
                                                            device_map='auto',
                                                            torch_dtype=torch.float32)
    ### INITIALIZING PIPELINE
    pipe_sum = pipeline('summarization', 
                        model = base_model,
                        tokenizer = tokenizer,
                        max_length = 350, 
                        min_length = 25,
                        truncation=True
                        )
    ## START TIMER
    start = datetime.datetime.now()
    ## START CHUNKING
    full_summary = ''
    for chunk in range(len(texts)):
      result = pipe_sum(texts[chunk])
      full_summary = full_summary + ' '+ result[0]['summary_text']
    stop = datetime.datetime.now()
    ## TIMER STOPPED AND RETURN DURATION
    duration = stop-start  
    ### Calculating Summarization PERCENTAGE
    reduction = '{:.1%}'.format(len(full_summary)/len(text))
    print(f"Completed in {duration}")
    print(f"Reduction percentage: ", reduction)
    
    return full_summary, duration, reduction

def main():
    # read a large-ish text file
    originalText = open_file('input.txt')
    # RUN THE SUMMARIZATION PIPELINE ON THE TEXT AND PRINT RESULT
    LaMini = './model/'
    post_summary, post_time, post_percentage = AI_SummaryPL(LaMini,originalText,3700,500)

    from pprint import pprint
    pprint(post_summary)

if __name__ == "__main__":
    exit(main())
