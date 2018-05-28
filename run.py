import os
import download as dw


dw.download_stats()
print(os.listdir(os.path.join('.', "data")))
