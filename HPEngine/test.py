from HPEngine.Helpers import DataReader
from HPEngine.Helpers import config

df_train = DataReader.read(config.data_root / 'train.csv')
df_test = DataReader.read(config.data_root / 'test.csv')

df_train.info()
df_test.info()