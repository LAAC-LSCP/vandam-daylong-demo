# VanDam Demo

VanDam, Mark (2018). [VanDam Public Daylong HomeBank Corpus](https://homebank.talkbank.org/access/Public/VanDam-Daylong.html). doi:10.21415/T5388S.

## Installation instructions

You need [datalad](https://www.datalad.org/) and the [datalad osf extension](https://github.com/datalad/datalad-osf) in order to install the dataset. They can be installed with:

```bash
pip install datalad datalad-osf
```

The next step is to clone the dataset :

```bash
datalad install https://github.com/LAAC-LSCP/vandam-daylong-demo.git
cd vandam-daylong-demo
```

## Getting data

```bash
datalad get recordings # download all recordings
datalad get annotations # get annotations
```
