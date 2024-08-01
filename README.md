# A Large-Scale Longitudinal Study of Evolution in URL Length using Common Crawl

There are many characteristics of the web
unknown to the world and very little in-depth studies are available on how the web has
changed. My research aims to analyse how the length of URL has changed in a span of nineteen
years using data from Common Crawl.

The dataset is extremely large. It can be retrieved from using S3 or HTTP by adding the prefix s3://commoncrawl/ resp. https://data.commoncrawl.org/ to the file path. Directories raw, timestamp, combine, merge_10_seg pre-process data. The code was run on Cirrus, a High Computing Platform using slurm - a job scheduler. Each code is run separately. Lastly Plot folder contains python codes to build graphs and summaries necessary for analysis.
