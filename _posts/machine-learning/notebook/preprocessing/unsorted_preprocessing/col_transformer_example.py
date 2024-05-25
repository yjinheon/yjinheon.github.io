import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.feature_extraction.text import _VectorizerMixin
from sklearn.feature_selection._base import SelectorMixin
from sklearn.feature_selection import SelectKBest
from sklearn.feature_extraction.text import CountVectorizer

train = pd.DataFrame({'age': [23,12, 12, np.nan],
                      'Gender': ['M','F', np.nan, 'F'],
                      'income': ['high','low','low','medium'],
                      'sales': [10000, 100020, 110000, 100],
                      'foo' : [1,0,0,1],
                      'text': ['I will test this',
                               'need to write more sentence',
                               'want to keep it simple',
                               'hope you got that these sentences are junk'],
                      'y': [0,1,1,1]})
numeric_columns = ['age']
cat_columns     = ['Gender','income']

numeric_pipeline = make_pipeline(SimpleImputer(strategy='median'), StandardScaler())
cat_pipeline     = make_pipeline(SimpleImputer(strategy='most_frequent'), OneHotEncoder())
text_pipeline = make_pipeline(CountVectorizer(), SelectKBest(k=5))

transformers = [
    ('num', numeric_pipeline, numeric_columns),
    ('cat', cat_pipeline, cat_columns),
    ('text', text_pipeline, 'text'),
    ('simple_transformer', MinMaxScaler(), ['sales']),
]

combined_pipe = ColumnTransformer(
    transformers, remainder='passthrough')

transformed_data = combined_pipe.fit_transform(
    train.drop('y',1), train['y'])
