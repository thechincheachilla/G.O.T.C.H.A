import pandas as pd
import csv

class Legislator:

    def parseLegislator(csvfile):
    df = pd.read_csv(csvfile).T.to_dict()
    print(df[0].get("middle_name"))
    
    with open ('parsed_legislators.txt', 'w') as outfile:
        json.dump(df, outfile)
    

    if __name__ == '__main__':
        main()
