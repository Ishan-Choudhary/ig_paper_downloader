# IGCSE Paper Downloader
A simple python script that will download past papers qp and ms for IGCSE, from papers.gceguide.com

# INSTALLATION
```
git clone https://github.com/Ishan-Choudhary/ig_paper_downloader.git
cd ig_paper_downloader
```
# USAGE
```
$ python3 main.py -h
WELCOME CLI PAPER DOWNLOADER
--------------------
(I)CT, (C)hemistry, (B)iology, (P)hysics, (M)athematics, (E)nglish
(F)eb/March, (M)ay/June, (O)ctober/November
Type -h or --help for me information
--------------------
usage: main.py [-h] -s SUBJECT -y YEAR -m MONTH -pv [PAPER_VARIANT [PAPER_VARIANT ...]]

optional arguments:
  -h, --help            show this help message and exit
  -s SUBJECT, --subject SUBJECT
                        Initials of subject
  -y YEAR, --year YEAR  Full year
  -m MONTH, --month MONTH
                        Initials of month
  -pv [PAPER_VARIANT [PAPER_VARIANT ...]], --paper_variant [PAPER_VARIANT [PAPER_VARIANT ...]]
                        Paper number with variant
```
# EXAMPLES
```
python3 main.py -s i -y 2020 -m o -pv 12
python3 main.py -s b -y 2016 -m m -pv 22 23 62
```
