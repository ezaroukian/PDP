#Take a cvs of stimuli, make a js file containing a list of items

import csv, string

ont0A = "http://i1341.photobucket.com/albums/o753/ezaroukian/0A_zpslpinf2fi.png"
ont0Al = "http://i1341.photobucket.com/albums/o753/ezaroukian/0Al_zps1awoxvuz.png"
ont0B = "http://i1341.photobucket.com/albums/o753/ezaroukian/0B_zpsk5dn4xfl.png"
ont0Bl = "http://i1341.photobucket.com/albums/o753/ezaroukian/0Bl_zpsnhfil1sm.png"
ont0C = "http://i1341.photobucket.com/albums/o753/ezaroukian/0C_zpsgdjlzzvp.png"
ont0Cl = "http://i1341.photobucket.com/albums/o753/ezaroukian/0Cl_zpsclmfmgrs.png"
ont2A = "http://i1341.photobucket.com/albums/o753/ezaroukian/2A_zpsupnzz2ms.png"
ont2Al = "http://i1341.photobucket.com/albums/o753/ezaroukian/2Al_zpswfhoaulk.png"
ont2B = "http://i1341.photobucket.com/albums/o753/ezaroukian/2B_zpsjejd6spx.png"
ont2Bl = "http://i1341.photobucket.com/albums/o753/ezaroukian/2Bl_zpsk0rsjoio.png"
ont2C = "http://i1341.photobucket.com/albums/o753/ezaroukian/2C_zps3jmrm5lm.png"
ont2Cl = "http://i1341.photobucket.com/albums/o753/ezaroukian/2Cl_zpsj0pk83ox.png"
ont3A = "http://i1341.photobucket.com/albums/o753/ezaroukian/3A_zpsem2bpmkm.png"
ont3Al = "http://i1341.photobucket.com/albums/o753/ezaroukian/3Al_zpsbxkom9x9.png"
ont3B = "http://i1341.photobucket.com/albums/o753/ezaroukian/3B_zpssdog5hbw.png"
ont3Bl = "http://i1341.photobucket.com/albums/o753/ezaroukian/3Bl_zpsxsupqx7c.png"# "http://i1341.photobucket.com/albums/o753/ezaroukian/3Bl_zpsepjkv9je.png"
ont3C = "http://i1341.photobucket.com/albums/o753/ezaroukian/3C_zpsa2jieegn.png"
ont3Cl = "http://i1341.photobucket.com/albums/o753/ezaroukian/3Cl_zpsp2ljm9qv.png"



with open('ontSent.csv', 'rb') as csvfile:
        counter = 0
        items = []
        itemsNames01 = [] #practice
        itemsNames02 = [] #practice
        itemsNames1 = [] #block 1
        itemsNames2 = [] #block 2
        r = csv.reader(csvfile)
        r.next()
        for row in r:
                counter += 1
                ontograph = row[0]
                if row[0]=="0Al":
                        ontLink = ont0Al
                elif row[0]=="0Bl":
                        ontLink = ont0Bl
                elif row[0]=="0Cl":
                        ontLink = ont0Cl
                elif row[0]=="2Al":
                        ontLink = ont2Al
                elif row[0]=="2Bl":
                        ontLink = ont2Bl
                elif row[0]=="2Cl":
                        ontLink = ont2Cl
                elif row[0]=="3Al":
                        ontLink = ont3Al
                elif row[0]=="3Bl":
                        ontLink = ont3Bl
                elif row[0]=="3Cl":
                        ontLink = ont3Cl
                #Locally I can just do
                ontLink = "file:///M:/PDP/images/"+row[0]+".png"
                image = '<br/><img src="'+ontLink+'" height="360">'
                block = row[1]
                complexity = row[2] 
                truth = int(row[3])
                NL = row[4]
                CE = row[5]
                ident = row[6]
                an = row[7]
                neg = row[8]
                inan = row[9]

                #Add a switch of some sort for sentence and language
                #firstLang = NL
                #practice name...
                #secondLang = CE
                

                addToType = "." + ontograph + "." +  str(block) + "." + complexity + "." + str(truth)+ "." +str(counter) +"."+ident+"."+an+"."+neg+"."+inan
                if block == "0":
                        sentence01 = NL  #I arbitarily chose NL for block 1, other versions should do CE first, and should flip the blocks
                        itype01 = "NL_pract"+addToType
                        sentence02 = CE
                        itype02 = "CE_pract"+addToType              
                elif block == "1":
                        sentence = NL
                        itype = "NL"
                elif block == "2":
                        sentence = CE
                        itype = "CE"
                itype += "." + ontograph + "." +  str(block) + "." + complexity + "." + str(truth)+ "." +str(counter)+"."+ident+"."+an+"."+neg+"."+inan
                
                if block == "0":
                        item = [itype01, "PracticeQuestion", {"q": '<span class="q">'+sentence01+"</span>"+image, "hasCorrect": truth}  ]
                        items.append(item)
                        item = [itype02, "PracticeQuestion", {"q": '<span class="q">'+sentence02+"</span>"+image, "hasCorrect": truth} ]
                else:
                        item = [itype, "Question", {"q": '<span class="q">'+sentence+"</span>"+image, "hasCorrect": truth } ]
                        
                items.append(item)
                if block == "0":
                        itemsNames01.append(itype01)
                        itemsNames02.append(itype02)
                elif block == "1":
                        itemsNames1.append(itype)
                elif block == "2":
                        itemsNames2.append(itype)
                
                        
        #itemsNames1.pop()#so that there's no separator after the last item (how to randomize??)
        #itemsNames2.pop()
        csvfile.close()

with open('SUS.csv', 'rb') as csvfile:
        counter = 1
        sus1 = []
        sus2 = []
        susNames1 = []
        susNames2 = []
        r = csv.reader(csvfile)
        r.next()
        for row in r:
                order = row[0]
                statement = row[1]
                polarity = row[2]
                itype = polarity+"."+order
                itype1n = "NL.1."+itype
                itype1c = "CE.2."+itype
                itype2n = "NL.2."+itype
                itype2c = "CE.2."+itype
                #arbitrary order for lang/block right now (Latin square for which goes with which)
                item1n = [itype1n, "AcceptabilityJudgment", {"s": statement, "q": "", "as": ["1", "2", "3", "4", "5"], "leftComment": "strongly disagree", "rightComment": "strongly agree"} ]
                item1c = [itype1c, "AcceptabilityJudgment", {"s": statement, "q": "", "as": ["1", "2", "3", "4", "5"], "leftComment": "strongly disagree", "rightComment": "strongly agree"} ]
                item2n = [itype2n, "AcceptabilityJudgment", {"s": statement, "q": "", "as": ["1", "2", "3", "4", "5"], "leftComment": "strongly disagree", "rightComment": "strongly agree"} ]
                item2c = [itype2c, "AcceptabilityJudgment", {"s": statement, "q": "", "as": ["1", "2", "3", "4", "5"], "leftComment": "strongly disagree", "rightComment": "strongly agree"} ]
                sus1.append(item1n).append(item1c)
                sus2.append(item2n).append(item2c)
                susNames1.append(itype1)
                susNames2.append(itype2)
        csvfile.close()



#allItems = ["toPractice"] + itemsNames01 + ["endPractice"] + itemsNames1 +["toSUS"]+ susNames + ["break","toPractice"] + itemsNames02 + ["endPractice"] + itemsNames2 +["toSUS"]+ susNames +["endSurvey"] #add in conf and sep
#allItems = str(allItems)

with open('genItems.js', 'w') as writefile:
        #writefile.write('var ont0A = "http://i1341.photobucket.com/albums/o753/ezaroukian/0Al_zps1awoxvuz.png";\n var ont0Al = "http://i1341.photobucket.com/albums/o753/ezaroukian/0A_zpslpinf2fi.png";\n var ont0B = "http://i1341.photobucket.com/albums/o753/ezaroukian/0B_zpsk5dn4xfl.png";\n var ont0Bl = "http://i1341.photobucket.com/albums/o753/ezaroukian/0Bl_zpsnhfil1sm.png";\n var ont0C = "http://i1341.photobucket.com/albums/o753/ezaroukian/0C_zpsgdjlzzvp.png";\n var ont0Cl = "http://i1341.photobucket.com/albums/o753/ezaroukian/0Cl_zpsclmfmgrs.png";\n var ont2A = "http://i1341.photobucket.com/albums/o753/ezaroukian/2A_zpsupnzz2ms.png";\n var ont2Al = "http://i1341.photobucket.com/albums/o753/ezaroukian/2Al_zpswfhoaulk.png";\n var ont2B = "http://i1341.photobucket.com/albums/o753/ezaroukian/2B_zpsjejd6spx.png";\n var ont2Bl = "http://i1341.photobucket.com/albums/o753/ezaroukian/2Bl_zpsk0rsjoio.png";\n var ont2C = "http://i1341.photobucket.com/albums/o753/ezaroukian/2C_zps3jmrm5lm.png";\n var ont2Cl = "http://i1341.photobucket.com/albums/o753/ezaroukian/2Cl_zpsj0pk83ox.png";\n var ont3A = "http://i1341.photobucket.com/albums/o753/ezaroukian/3A_zpsem2bpmkm.png";\n var ont3Al = "http://i1341.photobucket.com/albums/o753/ezaroukian/3Al_zpsbxkom9x9.png";\n var ont3B = "http://i1341.photobucket.com/albums/o753/ezaroukian/3B_zpssdog5hbw.png";\n var ont3Bl = "http://i1341.photobucket.com/albums/o753/ezaroukian/3Bl_zpsepjkv9je.png";\n var ont3C = "http://i1341.photobucket.com/albums/o753/ezaroukian/3C_zpsa2jieegn.png";\n var ont3Cl = "http://i1341.photobucket.com/albums/o753/ezaroukian/3Cl_zpsp2ljm9qv.png";\n\n')
        writefile.write("var newTestItems = "+str(items)+";\n\n")
        writefile.write("var newSUSItems = "+str(sus1+sus2)+";\n\n\n")
        #writefile.write("var mySeq = seq('intro','"+"', '".join(allItems)+"');")
        writefile.write("var mySeq = seq('intro', 'toPractice', followEachWith('sepPractice',seq('"+"', '".join(itemsNames01)+"')), 'endPractice', followEachWith(seq('conf','sep'),rshuffle('"+"', '".join(itemsNames1)+"')), 'toSUS', '" + "', '".join(susNames1)+"', 'break', 'toPractice', followEachWith('sepPractice',seq('"+"', '".join(itemsNames02)+"')), 'endPractice', followEachWith(seq('conf','sep'),rshuffle('"+"', '".join(itemsNames2)+"')), 'toSUS', '"+"', '".join(susNames2)+"', 'endSurvey')")
        #writefile.write("var mySeq = seq( sepWith('sep', seq('" + "', '".join(itemsNames1) + "')));")
        writefile.close()


#write a few to file, then in js have random selection for which language starts

