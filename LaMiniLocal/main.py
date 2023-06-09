#! /usr/bin/env python

########### GUI IMPORTS ################
import streamlit as st
#### IMPORTS FOR AI PIPELINES ###############
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
from transformers import AutoModel, T5Tokenizer, T5Model
from transformers import T5ForConditionalGeneration
from langchain.llms import HuggingFacePipeline
import torch


# SET THE MODEL PATH
checkpoint = "./model/"  #it is actually LaMini-Flan-T5-248M
# INITIALIZE TOKENIZER AND MODEL
tokenizer = T5Tokenizer.from_pretrained(checkpoint)

base_model = T5ForConditionalGeneration.from_pretrained(
    checkpoint,
    device_map='auto',
    torch_dtype=torch.float32)

# INITIALIZE THE PIPELINE
pipe_sum = pipeline('summarization', 
                    model = base_model,
                    tokenizer = tokenizer,
                    max_length = 350, 
                    min_length = 25)


text = " Automatic text summarization with machine learning is the task of condensing a piece of text to a shorter version, reducing the size of the initial text while at the same time preserving key informational elements and the meaning of content. It is a challenging task that requires extensive research in the NLP area. There are two different approaches for automatic text summaryization: extraction and abstraction. The extraction method involves identifying important sections of the text and stitching together portions of the content to produce a condensed version. The scoring function assigns a value to each sentence denoting the probability with which it will get picked up in the summary. The process involves constructing an intermediate representation of the input text and scoring the sentences based on the representation. A typical flow of extractive summarization systems involves constructing intermediate representations of the input text, scoring sentences based on the representation, and using Latent semantic analysis (LSA) to identify semantically important sentences. Recent studies have also applied deep learning in extractive text summaryization, such as Sukriti's approach for factual reports using a deep learning model, Yong Zhang's document summarizing framework using convolutional neural networks, and Y. Kim's regression process for sentence ranking. The neural architecture used in the paper is compounded by one single convolution layer built on top of pre-trained word vectors followed by a max-pooling layer. Experiments have shown the proposed model achieved competitive or even better performance compared with baselines. Abstractive summarization methods aim to produce summary by interpreting the text using advanced natural language techniques to generate a new shorter text that conveys the most critical information from the original text. They take advantage of recent developments in deep learning and use an attention-based encoder-decoder method for generating abstractive summaries. Recent studies have argued that attention to sequence models can suffer from repetition and semantic irrelevance, causing grammatical errors and insufficient reflection of the main idea of the source text. Junyang Lin et al proposes a gated unit on top of the encoder outputs at each time step to tackle this problem. The code to reproduce the experiments from the NAMAS paper can be found here. The Pointer Network is a neural attention-based sequence-to-sequence architecture that learns the conditional probability of an output sequence with elements that are discrete tokens corresponding to positions in an input sequence. Other methods for abstractive summarization include Pointer-Generator, which allows copying words from the input sequence via pointing of specific positions, and a generator that generates words from a fixed vocabulary of 50k words. To overcome repetition problems, the paper adapts the coverage model of Tu et al. to overcome the lack of coverage of source words in neural machine translation models. To train the extractor on available document-summary pairs, the model uses a policy-based reinforcement learning (RL) with sentence-level metric rewards to connect both extractor and abstractor networks and to learn sentence saliency. The abstractor network is an emphasis-based encoder-decoder which compresses and paraphrases an extracted document sentence to a concise summary sentence. An RNN encoder computes context-aware representation and then an RNN decoder selects sentence at time step t. The extractor agent is a convolutional sentence encoder that computes representations for each sentence based on input embedded word vectors. An RNN encoder computes context-aware representation and then an RNN decoder selects sentence at time step t. The method incorporates abstractive approach advantages of concisely rewriting sentences and generating novel words from the full vocabulary, while adopting intermediate extractive behavior to improve the overall model's quality, speed, and stability. Recent studies have proposed a combination of adversarial processes and reinforcement learning to abstractive summarization. The extractive approach is easier because copying large chunks of text from the source document ensures good levels of grammaticality and accuracy, while the abstractive model generates new phrases, rephrasing or using words that were not in the original text. Recent developments in the deep learning area have allowed for more sophisticated abilities to be generated."
# RUN THE PIPELINE ON THE TEXT AND PRINT RESULT
result = pipe_sum(text)
print(result[0]['summary_text'])

