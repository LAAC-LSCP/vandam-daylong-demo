# VanDam Demo

VanDam, Mark (2018). [VanDam Public Daylong HomeBank Corpus](https://homebank.talkbank.org/access/Public/VanDam-Daylong.html). doi:10.21415/T5388S.

## Installation instructions

You need [datalad](https://www.datalad.org/) and the [datalad osf extension](https://github.com/datalad/datalad-osf) in order to install the dataset. They can be installed with:

```bash
pip install datalad datalad-osf
```

If anything goes wrong, please check fuller instructions for [installing ChildProject](https://childproject.readthedocs.io/en/latest/install.html), and that you are in the right environment, which may mean doing `source ~/ChildProjectVenv/bin/activate`

The next step is to clone the dataset:

```bash
datalad install https://github.com/LAAC-LSCP/vandam-daylong-demo.git
cd vandam-daylong-demo
```

## Getting data

```bash
datalad get recordings # download all recordings
datalad get annotations # get annotations
```
Should you get an error like `get(error): annotations/its/converted/BN32_010007_0_0.csv (file) [not available; (Note that these git remotes have annex-ignore set: origin)]`, try the following:

```bash
pip install datalad-osf
git annex enableremote osf-annex-storage
datalad get recordings # download all recordings
datalad get annotations # get annotations
```
