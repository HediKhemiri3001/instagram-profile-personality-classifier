
import instaloader
from datetime import datetime
#fernandez
#fett
#feudejoieco
#fhercisner
""""fizzyfi",
"flahes",
"flokke",
"formfett",
"freedom23833jsd",
"frosty",
"fverloop",
"gabry46",
"gardenstatehiker",
"gavan",
"gavinporter",
"giulio",
"gizmosachin",
"glitzerpopitzer",
"goateegram",
"grahamcase",
"greatwhite",
"grumpy.kel",
"hankword",
"happychap",
"hawkeye",
"helgie",
"heratus",
"heyitsdiggy",
"heystack",
"hishamsaidak",
"hishboy"
"hiswork",
"hiteck",
"hootsieroll",
"hubartt",
"huguesh",
"iamneven",
"iamsawhneygautam",
"ibob_90",
    "ibvanmat",
"igrovac",
"imsobe",
"iridesce",
"iru.sbc",
"itsmgz",
"itswilder",
"iwanesk",
"j4m1eb",
"jakeblunsford",
"jakevance",
"jameswagner",
"jamiemonster",
"jan1878",
"janeinging",
"janetmobrien6",
"jankorbel",
"jaybird82",
"jazza",
"jbenjaminsson",
"jboat1",
"jbs_ribs_n_whiskey",
"jchristopher",
"jeeeeeeess",
"jeffwms",
"jenapic",
"jenniferploogphotographie",
"jeremyflint",
"jevasshaug",
"jfoser",
"jgclarke",
"jknuutila",
"johandelfs",
"johanprag",
"johngrogg",
"johnnietheblack",
"jolanta",
"jon2512chua",
"jonascarlsson",
"jonathan.muth",

"jonathandavidk",
"""
#"jamielarea",
persons=[
"jonguerin",
"jonheidib",
"jonmagic",
"jonrowe",
"jorgevalencia",
"josh.r.bancroft",
"joshdavey",
"joshnippon",
"josiahwiebe",
"josietevebaugh22",
"jotkali",
"jotong",
"jrome",
"jsa007",
"jsizzl",
"juanford",
"juicedus",
"julianhinz",
"juliusschaeper",
"juningham",
"jusantin",
"justinreid",
"k8therine",
"kabirh",
"kaethend",
"kari_ray",
"karmadude",
"karmiccycle",
"katherineyiu",
"kawham93",
"kdraper72",
"keir",
"kelllp",
"kelsifernie_",
"kennylong",
"kenton",
"keverett",
"kevinsharon",
"kevinthompson",
"kiki_t123",
"kirko",
"kirsten_pg",
"kjetilsveen",
"koevet",
"kpich",
"kreshinjo",
"krisarruda",
"kurtzchong",
"kuschti",
"kviksilver",
]
#kviksilve

L = instaloader.Instaloader()
L.load_session_from_file("hedihedi.hedi")
UNTIL = datetime(2021, 3, 30)
SINCE = datetime(2017, 3, 30)

done_list = open("done.txt","a")
no_posts_in_range_file = open("no_posts.txt","a")
for person in persons:
    print("Downloading for person: "+ person+"\n")
    posts = instaloader.Profile.from_username(L.context, person).get_posts()
    filtered = filter(lambda post: SINCE<post.date<UNTIL, posts)
    if not filtered:
        #Person has no posts in specified date range.
        print(person, " has no posts in specified range, passing to next person.")
        no_posts_in_range_file.write(person+"\n")
        continue
    for post in list(filtered):
        print(SINCE<post.date<UNTIL)
        output = L.download_post(post, person)
        print(output)
    print("Done downloading for ", person, ". Adding to done list.")
    #File that keeps track of scrapped profiles.
    
    done_list.write(person+"\n")
no_posts_in_range_file.close()
done_list.close()