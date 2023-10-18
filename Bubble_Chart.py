import circlify
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.legend_handler import HandlerPatch

def College(name, short = True):
    name = "".join(i.lower() for i in name if i.isalpha())
    if name in ('a', 'collegeofdesign', 'cod', 'design'):
        if short:
            return 'COD'
        else:
            return 'College of Design'
    if name in ('s', 'collegeofsciences', 'cos', 'sciences'):
        if short:
            return 'COS'
        else:
            return 'College of Sciences'
    if name in ('c', 'collegeofcomputing', 'coc', 'computing'):
        if short:
            return 'COC'
        else:
            return 'College of Computing'
    if name in ('e', 'collegeofengineering', 'coe', 'engineering'):
        if short:
            return 'COE'
        else:
            return 'College of Engineering'
    if name in ('m', 'schellercollegeofbusiness', 'scob', 'business'):
        if short:
            return 'SCOB'
        else:
            return 'Scheller College of Business'
    if name in ('i', 'ivanallencollege', 'iac', 'ivan'):
        if short:
            return 'IAC'
        else:
            return 'Ivan Allen College'
    else:
        return 'Other'
    
def Children (source, school):
    data = source[school]
    alist = ['COD', 'COE', 'COC', 'IAC', 'SCOB', 'COS']
    l_dict = {}
    return_dict = {}
    return_dict['id'] = College(school, False)
    return_dict['datum'] = data['Enroll']
    children = []
    lost = 0
    gained = 0
    for i in data.keys():
        if i == 'Admit':
            temp_dict = {}
            temp_dict['id'] = 'Admitted'
            temp_dict['datum'] = data[i]
            children.append(temp_dict)
        if i in alist and i != school:
            lost -= data[i]
        if i == 'Enroll':
            temp_dict = {}
            temp_dict['id'] = 'Enroll'
            temp_dict['datum'] = data[i]
            children.append(temp_dict)
        if i == school:
            temp_dict = {}
            temp_dict['id'] = 'Gained'
            temp_dict['datum'] = data['Enroll'] - data[i]
            children.append(temp_dict)     
    l_dict['id'] = 'Lost'
    l_dict['datum'] = abs(lost)
    children.append(l_dict)
    return_dict['children'] = children
    return return_dict
                    
def get_data(source_file):
    infile = open(source_file , 'r')
    header = infile.readline()
    data = infile.readlines()
    data_list = []
    return_list = []
    enrollment_dict = {}
    school_set = set()
    for line in data:
        line_pieces = line.strip().split(',')
        in_college = line_pieces[1]
        out_college = line_pieces[-1]
        in_code = College(in_college, True)
        school_set.add(in_code)
        out_code = College(out_college, True)
        if in_code not in enrollment_dict:
            enrollment_dict[in_code] = {}
            enrollment_dict[in_code]['COD'] = 0
            enrollment_dict[in_code]['COS'] = 0
            enrollment_dict[in_code]['COE'] = 0
            enrollment_dict[in_code]['IAC'] = 0
            enrollment_dict[in_code]['SCOB'] = 0
            enrollment_dict[in_code]['COC'] = 0
            enrollment_dict[in_code][out_code] += 1
            enrollment_dict[in_code]['Admit'] = 1
            enrollment_dict[in_code]['Enroll'] = 0
        else:
            enrollment_dict[in_code][out_code] += 1
            enrollment_dict[in_code]['Admit'] += 1
    for line in data:
        line_pieces = line.strip().split(',')
        out_code = College(line_pieces[-1], True)
        enrollment_dict[out_code]['Enroll'] += 1
    for school in enrollment_dict.keys():
        data_list.append(Children(enrollment_dict, school))
    return_dict = {}
    return_dict['id'] = 'Georgia Tech'
    return_dict['datum'] = 9000
    return_dict['children'] = data_list
    return_list.append(return_dict)
    return return_list

def Format(name, Color = True):
    if name == 'College of Design':
        if Color:
            return '#B2BEB5'
        else:
            return (x-0.005,y+0.185)
    if name == 'College of Sciences':
        if Color:
            return '#36454F'
        else:
            return (x-0.01,y+0.345)
    if name == 'College of Computing':
        if Color:
            return '#7393B3'
        else:
            return (x-0.02,y-0.43)
    if name == 'College of Engineering':
        if Color:
            return '#6082B6'
        else:
            return (x,y-0.6)
    if name == 'Scheller College of Business':
        if Color:
            return '#A9A9A9'
        else:
            return (x,y-0.24)
    if name == 'Ivan Allen College':
        if Color:
            return '#818589'
        else:
            return (x-0.01,y+0.22)
    if name == 'Admitted':
        return '#B3A369'
    if name == 'Enroll':
        return '#003057'
    if name == 'Gained':
        return '#2961FF'
    if name == 'Lost':
        return '#E04F39'
    else:
        return '#003057'

file = 'Major Change Viz.csv'
data = get_data(file)

circles = circlify.circlify(
    data, 
    show_enclosure=False, 
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

fig, ax = plt.subplots(figsize=(20,20))
fig.patch.set_facecolor('#F9F6E5')

ax.set_title('Incoming First-Year Students AY2024 by College', fontsize = 36)

ax.axis('off')

lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

for circle in circles:
    if circle.level != 2:
      continue
    x, y, r = circle
    ax.add_patch( plt.Circle((x, y), r, alpha=0.25, linewidth=2, color= Format(circle.ex['id'])))

for circle in circles:
    if circle.level != 3:
      continue
    x, y, r = circle
    label = circle.ex["id"]
    label2 = circle.ex['datum']
    ax.add_patch( plt.Circle((x, y), r, alpha=1, linewidth=2, color= Format(label)))
    plt.annotate(label2, (x,y-0.01 ), ha='center', color="white", fontsize=22)

for circle in circles:
    if circle.level != 2:
      continue
    x, y, r = circle
    label = circle.ex["id"]
    plt.annotate(label, Format(label, False) ,va='center', ha='center', fontsize = 18, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.5))


colors = ["#B3A369", "#003057", "#E04F39", "#2961FF"]
texts = ["Admitted Into College", "Confirmed in College", "Students Lost", "Students Gained"]
class HandlerEllipse(HandlerPatch):
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        center = 0.5 * width - 0.5 * xdescent, 0.5 * height - 0.5 * ydescent
        p = mpatches.Ellipse(xy=center, width=height + xdescent,
                             height=height + ydescent)
        self.update_prop(p, orig_handle, legend)
        p.set_transform(trans)
        return [p]


c = [mpatches.Circle((1, 1), radius = 0.5, facecolor=colors[i], edgecolor="none" ) for i in range(len(texts))]
plt.legend(c, texts,bbox_to_anchor=(0.2, 0.86), edgecolor = '#003057', loc='lower right', ncol=1, fontsize = 18, labelcolor = ["#B3A369", "#003057", "#E04F39", "#2961FF"], handler_map={mpatches.Circle: HandlerEllipse()}).get_frame().set_facecolor('white')
ax.annotate('"Lost" refers to a student who was admitted into that College but confirmed a major in another College', xy = (0.18, 0), xycoords='axes fraction', fontsize = 14)
plt.savefig('bubbles.png', bbox_inches='tight')