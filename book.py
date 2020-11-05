
myText = """Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey Xylophone Yankee Zulu. Breezily jingling $3,416,857,209, wise advertiser ambles to the bank, his exchequer amplified. Jackdaws love my big sphinx of quartz. Victors flank gypsy who mixed up on job quiz. Wolves exit quickly as fanged zoo chimps jabber. Five jumbo oxen graze quietly with packs of dogs. Grumpy wizards make toxic brew for the evil queen and jack. Lazy movers quit hard packing of jewelry boxes. Ban foul, toxic smogs which quickly jeopardize lives. Hark! Toxic jungle water vipers quietly drop on zebras for meals! New farm hand, picking just six quinces, proves strong but lazy. Back in my quaint garden, jaunty zinnias vie with flaunting phlox. Waltz, nymph, for quick jigs vex Bud. Crazy Fredericka bought many very exquisite opal jewels. Jolly housewives made inexpensive meals using quick-frozen vegetables. Sixty zippers were quickly picked from the woven jute bag. Call 1 (800) 435 8293 Jaded zombies acted quaintly but kept driving their oxen forward. Six big juicy steaks sizzled in a pan as five workmen left the quarry. Will Major Douglas be expected to take this true-false quiz very soon? A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent. Jimmy and Zack, the police explained, were last seen diving into a field of buttered quahogs. Monique, the buxom coed, likes to fight for Pez with the junior varsity team. The jukebox music puzzled a gentle visitor from a quaint valley town. Just work for improved basic techniques to maximize your typing skills. When we go back to Juarez, Mexico, do we fly over picturesque Arizona? Murky haze enveloped a city as jarring quakes broke forty-six windows. Nancy Bizal exchanged vows with Robert J. Kumpf at Quincy Temple. The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs. Brick quiz whangs jumpy veldt fox. Quick wafting zephyrs vex bold Jim. Sphinx of black quartz, judge my vow. The five boxing wizards jump quickly. Pickled, Gorbachev jumps tawny fax quiz. Sympathizing would fix Quaker objectives. Doxy with charming buzz quaffs vodka julep. Raving zibet chewed calyx of pipsqueak major. J. Hoefler cabled: “puzzling over waxy kumquats.” Oozy quivering jellyfish expectorated by mad hawk. By Jove, my quick study of lexicography won a prize. Lazy jackal from raiding xebec prowls the quiet cove. Six boys guzzled cheap raw plum vodka quite joyfully. Six big devils from Japan quickly forgot how to waltz. Quixotic knights’ wives are found on jumpy old zebras. Guzzling of jaunty exile wrecks havoc at damp banquet. How razorback-jumping frogs can level six piqued gymnasts! When waxing parquet decks, Suez sailors vomit jauntily abaft. Frozen buyer just quickly keyed shocking weaver’s complexion. Qu’est-ce c’est chez le vieux forgerondu coin J’ai pu boire le meilleur whisky? Fabled reader with jaded, roving eye seized by quickened impulse to expand budget. Breezily jingling $3,416,857,209, wise advertiser ambles to the bank, his exchequer amplified. Six big devils from Japan quickly forgot how to waltz. Quixotic knights’ wives are found on jumpy old zebras. Guzzling of jaunty exile wrecks havoc at damp banquet. How razorback-jumping frogs can level six piqued gymnasts! When waxing parquet decks, Suez sailors vomit jauntily abaft. Frozen buyer just quickly keyed shocking weaver’s complexion. Qu’est-ce c’est chez le vieux forgerondu coin J’ai pu boire le meilleur whisky? Fabled reader with jaded, roving eye seized by quickened impulse to expand budget. Breezily jingling $3,416,857,209, wise advertiser ambles to the bank, his exchequer amplified. Six big devils from Japan quickly forgot how to waltz. Quixotic knights’ wives are found on jumpy old zebras. Guzzling of jaunty exile wrecks havoc at damp banquet. How razorback-jumping frogs can level six piqued gymnasts! When waxing parquet decks, Suez sailors vomit jauntily abaft. Frozen buyer just quickly keyed shocking weaver’s complexion. Qu’est-ce c’est chez le vieux forgerondu coin J’ai pu boire le meilleur whisky? 

Fabled reader with jaded, roving eye seized by quickened impulse to expand budget. Breezily jingling $3,416,857,209, wise advertiser ambles to the bank, his exchequer amplified. Six big devils from Japan quickly forgot how to waltz. Quixotic knights’ wives are found on jumpy old zebras. Guzzling of jaunty exile wrecks havoc at damp banquet. How razorback-jumping frogs can level six piqued gymnasts! When waxing parquet decks, Suez sailors vomit jauntily abaft. Frozen buyer just quickly keyed shocking weaver’s complexion. Qu’est-ce c’est chez le vieux forgerondu coin J’ai pu boire le meilleur whisky? Fabled reader with jaded, roving eye seized by quickened impulse to expand budget. Breezily jingling $3,416,857,209, wise advertiser ambles to the bank, his exchequer amplified. Six big devils from Japan quickly forgot how to waltz. Quixotic knights’ wives are found on jumpy old zebras. Guzzling of jaunty exile wrecks havoc at damp banquet. How razorback-jumping frogs can level six piqued gymnasts! When waxing parquet decks, Suez sailors vomit jauntily abaft. Frozen buyer just quickly keyed shocking weaver’s complexion. Qu’est-ce c’est chez le vieux forgerondu coin J’ai pu boire le meilleur whisky? Fabled reader with jaded, roving eye seized by quickened impulse to expand budget. Breezily jingling $3,416,857,209, wise advertiser ambles to the bank, his exchequer amplified. Six big devils from Japan quickly forgot how to waltz. Quixotic knights’ wives are found on jumpy old zebras. Guzzling of jaunty exile wrecks havoc at damp banquet. How razorback-jumping frogs can level six piqued gymnasts! When waxing parquet decks, Suez sailors vomit jauntily abaft. Frozen buyer just quickly keyed shocking weaver’s complexion. Qu’est-ce c’est chez le vieux forgerondu coin J’ai pu boire le meilleur whisky? Fabled reader with jaded, roving eye seized by quickened impulse to expand budget. Breezily jingling $3,416,857,209, wise advertiser ambles to the bank, his exchequer amplified."""

font('Gimlet Variable')
print(listFontVariations())



fs = FormattedString(myText, 
    font='Gimlet Variable', 
    fontSize=20, 
    lineHeight=40,
    fill=(1, 0, 0), 
    openTypeFeatures={
        'smcp': False,
        'ss01': True
        },
    fontVariations={
        'wght': 900,
        'ital': 1
        }
        )

margin = 50

while fs:
    newPage('A4')
    fill(1)
    rect(margin, margin, width()-margin*2, height()-margin*2)

    fs = textBox(fs, (margin, margin, width()-margin*2, height()-margin*2))

