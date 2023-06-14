# Notes - regarding observations and learnings

2023-06-12: some vocabulary notes  
- checkpoint: A checkpoint is an intermediate dump of a model’s entire
  internal state (its weights, current learning rate, etc.) so that
  the framework can resume the training from this point whenever
  desired.  
  <https://towardsdatascience.com/ml-design-pattern-2-checkpoints-e6ca25a4c5fe>  
  - so a checkpoint is like a VM snapshot (but do not push the analogy
    too far)  
  - my next questions include: what format are checkpoint files? is
    the checkpoint info contained in one file or several?  
	
