def format_poems(lst):
    #highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
    #print(highlighted_poems)
    highlighted_poems_list = lst.split(',')
    #print(highlighted_poems_list)
    highlighted_poems_stripped = []
    for poem in highlighted_poems_list:
      highlighted_poems_stripped.append(poem.strip())
    #print(highlighted_poems_stripped)
    highlighted_poems_details = []
    for poem in highlighted_poems_stripped:
      highlighted_poems_details.append(poem.split(':'))
    #print(highlighted_poems_details)
    #titles = []
    #poets = []
    #dates = []
    titles = [poem[0] for poem in highlighted_poems_details]
    poets = [poem[1] for poem in highlighted_poems_details]
    dates = [poem[2] for poem in highlighted_poems_details]

    #for poem in highlighted_poems_details:
      #titles.append(poem[0])
      #poets.append(poem[1])
      #dates.append(poem[2])

    for i in range(len(titles)):
      #print("The poem {title} was published by {poet} in {date}".format(title = titles[i], poet = poets[i], date = dates[i]))
      print(f"The poem {titles[i]} was published by {poets[i]} in {dates[i]}")

lst = input("")
format_poems(lst)
