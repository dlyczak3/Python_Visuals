import pandas as pd
import matplotlib.pyplot as plt
from pySankey.sankey import sankey

file = "Major Change Viz.csv"
df = pd.read_csv(file, sep=",", names=["College", "Initial", "Confirmed", "New_College"])

#df1 = df.loc[df['Confirmed'] == "Computer Science"]
df1 = df.loc[df['College'] == "College of Design"]

colors = {
    ##College of Computing Majors
    "College of Computing": "#64CCC9",
    "Computer Science": "#64CCC9",

    ##College of Design Majors
    ##This is an example of a change to make when isolating a college
    "Industrial Design": "#B3A369",
    "Music Technology": "#003057",
    "Architecture": "#EAAA00",
    "Building Construction": "#54585A",
    
    
    
    "College of Design": "#5F249F",
    #"Industrial Design": "#5F249F",
    #"Music Technology": "#5F249F",
    #"Architecture": "#5F249F",
    #"Building Construction": "#5F249F",

    ##College of Engineering Majors
    "College of Engineering": "#FFCD00",
    "Aerospace Engineering": "#FFCD00",
    "Electrical Engineering": "#FFCD00",
    "Mechanical Engineering": "#FFCD00",
    "Computer Engineering": "#FFCD00",
    "Environmental Engineering": "#FFCD00",
    "Civil Engineering": "#FFCD00",
    "Materials Science and Engineering": "#FFCD00",
    "Biomedical Engineering": "#FFCD00",
    "Nuclear and Radiological Engineering": "#FFCD00",
    "Industrial Engineering": "#FFCD00",
    "Chemical and Biomolecular Engineering": "#FFCD00",
    
    ##College of Science Majors
    "College of Sciences": "#3A5DAE",
    "Applied Physics": "#3A5DAE",
    "Biochemistry": "#3A5DAE",
    "Biology": "#3A5DAE",
    "Chemistry": "#3A5DAE",
    "Earth & Atmospheric Sciences": "#3A5DAE",
    "Solid Earth and Planetary Sciences": "#3A5DAE",
    "Environmental Science": "#3A5DAE",
    "Mathematics": "#3A5DAE",
    "Neuroscience": "#3A5DAE",
    "Physics": "#3A5DAE",
    "Psychology": "#3A5DAE",

    ##Ivan Allen Majors
    "Ivan Allen College": "#A4D233",
    "Applied Languages & Intercultural Studies": "#A4D233",
    "Computational Media": "#A4D233",
    "Economics": "#A4D233",
    "Global Economics & Modern Languages": "#A4D233",
    "Economics & International Affairs": "#A4D233",
    "History, Technology & Society": "#A4D233",
    "International Affairs": "#A4D233",
    "International Affairs & Modern Languages": "#A4D233",
    "Literature, Media & Communication": "#A4D233",
    "Public Policy": "#A4D233",

    ##Scheller Majors
    "Scheller College of Business": "#E04F39",
    "Business Administration": "#E04F39",

}

sankey(df1["Initial"], df1["Confirmed"], aspect=20, colorDict=colors, fontsize=18, figure_name = 'Major Changes')
fig = plt.gcf()
fig.set_size_inches(30, 30)
fig.set_facecolor("w")
fig.savefig("Sankey_COD_From.png", bbox_inches="tight", dpi=150)