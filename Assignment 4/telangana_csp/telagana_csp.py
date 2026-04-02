import networkx as nx
import matplotlib.pyplot as plt

neighbors = {

'Adilabad': ['Nirmal','KomaramBheem'],
'Nirmal': ['Adilabad','Nizamabad','Mancherial'],
'Mancherial': ['Nirmal','Peddapalli','Jayashankar'],
'KomaramBheem': ['Adilabad','Mancherial'],

'Nizamabad': ['Nirmal','Kamareddy','Jagtial'],
'Kamareddy': ['Nizamabad','Medak','RajannaSircilla'],

'Karimnagar': ['Jagtial','Peddapalli','RajannaSircilla'],
'Peddapalli': ['Karimnagar','Mancherial','Jayashankar'],
'Jagtial': ['Karimnagar','Nizamabad'],
'RajannaSircilla': ['Karimnagar','Kamareddy','Siddipet'],

'Medak': ['Kamareddy','Sangareddy','Siddipet'],
'Sangareddy': ['Medak','Rangareddy','Vikarabad'],
'Siddipet': ['Medak','RajannaSircilla','WarangalUrban'],

'WarangalUrban': ['Siddipet','WarangalRural','Jangaon'],
'WarangalRural': ['WarangalUrban','Jangaon','Mahabubabad'],
'Jangaon': ['WarangalUrban','WarangalRural','Suryapet'],

'Mahabubabad': ['WarangalRural','Khammam'],
'Khammam': ['Mahabubabad','BhadradriKothagudem'],
'BhadradriKothagudem': ['Khammam','Jayashankar'],

'Jayashankar': ['Mancherial','Peddapalli','BhadradriKothagudem'],
'Mulugu': ['Jayashankar','WarangalRural'],

'Hyderabad': ['Rangareddy','Medchal'],
'Medchal': ['Hyderabad','Rangareddy'],
'Rangareddy': ['Hyderabad','Medchal','Vikarabad','Sangareddy'],

'Vikarabad': ['Rangareddy','Mahabubnagar','Sangareddy'],

'Mahabubnagar': ['Vikarabad','Nagarkurnool','Narayanpet'],
'Nagarkurnool': ['Mahabubnagar','Nalgonda','Wanaparthy'],
'Wanaparthy': ['Nagarkurnool','JogulambaGadwal'],
'JogulambaGadwal': ['Wanaparthy','Narayanpet'],
'Narayanpet': ['Mahabubnagar','JogulambaGadwal'],

'Nalgonda': ['Nagarkurnool','Suryapet','Yadadri'],
'Suryapet': ['Nalgonda','Jangaon'],
'Yadadri': ['Nalgonda']
}

districts = list(neighbors.keys())

colors = ['red','green','blue','yellow','orange','cyan','magenta','purple']

def is_valid(d,c,a):
    for n in neighbors[d]:
        if n in a and a[n]==c:
            return False
    return True

def solve(a):
    if len(a)==len(districts):
        return a
    for d in districts:
        if d not in a:
            for c in colors:
                if is_valid(d,c,a):
                    a[d]=c
                    r=solve(a)
                    if r:
                        return r
                    del a[d]
            return None

solution = solve({})

print("Telangana Map Coloring:\n")
for d in districts:
    print(d,"->",solution[d])

G = nx.Graph()
for d in neighbors:
    for n in neighbors[d]:
        G.add_edge(d,n)

node_colors = [solution[n] for n in G.nodes()]

plt.figure(figsize=(12,10))
pos = nx.spring_layout(G,seed=10)

nx.draw(G,pos,with_labels=True,node_color=node_colors,node_size=1500,font_size=6)

plt.title("Telangana CSP")

plt.savefig("telangana_csp.png")
plt.show()