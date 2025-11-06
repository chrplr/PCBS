import itertools
import pandas as pd

def expand_grid(data_dict):
    """Create a dataframe from every combination of given values."""
    rows = itertools.product(*data_dict.values())
    return pd.DataFrame.from_records(rows, columns=data_dict.keys())



N_SUBJECTS_NATIVE = 54
N_SUBJECTS_FOREIGN = 46
N_SUBJECTS = N_SUBJECTS_NATIVE + N_SUBJECTS_FOREIGN

subject_id = pd.Series([f'sub{i:02}' for i in range(N_SUBJECTS)])
group = pd.Series(['native'] * N_SUBJECTS_NATIVE
                  + ['foreign'] * N_SUBJECTS_FOREIGN)



# a dataframe can be viewed as a list of columns. Each column is a pd.Series. To give names to them we use a dict;


pd.DataFrame(dict(subject_id=subject_id,
                  group=group))





N_SUBJECTS_NATIVE = 54
N_SUBJECTS_FOREIGN = 46
N_SUBJECTS = N_SUBJECTS_NATIVE + N_SUBJECTS_FOREIGN

subject_id = pd.Series([f'sub{i:02}' for i in range(N_SUBJECTS)])
group = pd.Series(['native'] * N_SUBJECTS_NATIVE
                  + ['foreign'] * N_SUBJECTS_FOREIGN)

SUBJECTS = pd.DataFrame({'Subject_id': subject_id,
                         'Group': group})


N_TEXTS_FICTION = 5
N_TEXTS_NONFICTION = 5
N_TEXTS = N_TEXTS_FICTION + N_TEXTS_NONFICTION
text_id = pd.Series(f'text{i}' for i in range(N_TEXTS))
texttype = pd.Series(['fiction'] * N_TEXTS_FICTION
                    + ['nonfiction'] * N_TEXTS_NONFICTION)

TEXTS = pd.DataFrame({'Text_id': text_id,
                      'Text_type': texttype})

print(expand_grid({'subject': SUBJECTS, 'texts:': TEXTS}))
