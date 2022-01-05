from variables import SERIES_FULLFORMS, SUBJECT_DICT
import requests, argparse

parser = argparse.ArgumentParser()

print("WELCOME CLI PAPER DOWNLOADER")
print("-" * 20)
print("(I)CT, (C)hemistry, (B)iology, (P)hysics, (M)athematics, (E)nglish")
print("(F)eb/March, (M)ay/June, (O)ctober/November")
print("Type -h or --help for me information")
print("-" * 20)

def add_arguments():
    
    parser.add_argument("-s", "--subject", required=True, help="Initials of subject")
    parser.add_argument("-y", "--year", required=True, help="Full year", )
    parser.add_argument("-m", "--month", required=True, help="Initials of month")
    parser.add_argument("-pv", "--paper_variant", required=True, nargs="*",help="Paper number with variant")

    options = parser.parse_args() 
    return options

options = add_arguments()

subject_name = SUBJECT_DICT[options.subject]["name"]
subject_code = SUBJECT_DICT[options.subject]["code"]
year_real = SERIES_FULLFORMS[options.month]+options.year[2:]

for codes in options.paper_variant:
    url_qp = f"https://papers.gceguide.com/IGCSE/{subject_name}/{options.year}/{subject_code}_{year_real}_qp_{codes}.pdf"
    url_ms = f"https://papers.gceguide.com/IGCSE/{subject_name}/{options.year}/{subject_code}_{year_real}_ms_{codes}.pdf"
    r_qp = requests.get(url_qp, allow_redirects=True)
    r_ms = requests.get(url_ms, allow_redirects=True)

    open(f'{subject_code}_{year_real}_qp_{codes}.pdf', 'wb').write(r_qp.content)
    open(f'{subject_code}_{year_real}_ms_{codes}.pdf', 'wb').write(r_ms.content)