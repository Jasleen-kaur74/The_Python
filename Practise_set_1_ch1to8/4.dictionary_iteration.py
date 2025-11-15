"""Dictionary Iteration (Key-Value Pairing): You have the dictionary
hyperparams = {'batch_size': 32, 'learning_rate': 0.01, 'dropout': 0.5}.
 Write a for loop that iterates over this dictionary and
 prints both the hyperparameter name (key) and its setting (value)
 in the format: [Key] is set to [Value]."""


#dictionary
hyperparams = {'batch_size': 32,
               'learning_rate': 0.01,
               'dropout': 0.5}


#for printing
for j ,k in hyperparams.items():
    print(f"[{j}] is set to [{k}]")

