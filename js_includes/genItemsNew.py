#Take a cvs of stimuli, make a js file containing a list of items
countdownP = '<div id="clockdiv">seconds remaining: -</div>'+'<script> var timeInSeconds = 10; var currentTime = Date.parse(new Date()); var deadline = new Date(currentTime + timeInSeconds*1000); function getTimeRemaining(endtime){  var t = Date.parse(endtime) - Date.parse(new Date());  var seconds = Math.floor( (t/1000) );  return {    "total": t,    "seconds": seconds  };}</script>'+'<script>var t = getTimeRemaining(deadline);    try{document.getElementById("clockdiv").innerHTML = "seconds remaining: " + t.seconds;} catch(err){}</script>'+'<script> var timeinterval = setInterval(function(){    var t = getTimeRemaining(deadline);    try{document.getElementById("clockdiv").innerHTML = "seconds remaining: " + t.seconds;} catch(err){}      },1000);</script>'
countdown = '<div id="clockdiv">seconds remaining: -</div>'+'<script> var timeInSeconds = 10; var currentTime = Date.parse(new Date()); var deadline = new Date(currentTime + timeInSeconds*1000); function getTimeRemaining(endtime){  var t = Date.parse(endtime) - Date.parse(new Date());  var seconds = Math.floor( (t/1000) % 60 ); if(seconds<0){seconds=0;}  return {    "total": t,    "seconds": seconds  };}</script>'+'<script>var t = getTimeRemaining(deadline);    try{document.getElementById("clockdiv").innerHTML = "seconds remaining: " + t.seconds;} catch(err){}</script>'+'<script> var intervalId  = setInterval(function(){    var t = getTimeRemaining(deadline);    try{ if(t.seconds<=5){clearInterval(intervalId );} else{document.getElementById("clockdiv").innerHTML = "seconds remaining: " + t.seconds;}} catch(err){}     },1000);</script>'


##put back in to stop timer at 0
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
        itemsNames0n = [] #practice
        itemsNames0c = [] #practice
        itemsNames1n = [] #block 1
        itemsNames1c = []
        itemsNames2n = [] #block 2
        itemsNames2c = []
        r = csv.reader(csvfile)
        r.next()
        for row in r:
                counter += 1
                ontograph = row[0]
##                if row[0]=="0Al":
##                        ontLink = ont0Al
##                elif row[0]=="0Bl":
##                        ontLink = ont0Bl
##                elif row[0]=="0Cl":
##                        ontLink = ont0Cl
##                elif row[0]=="2Al":
##                        ontLink = ont2Al
##                elif row[0]=="2Bl":
##                        ontLink = ont2Bl
##                elif row[0]=="2Cl":
##                        ontLink = ont2Cl
##                elif row[0]=="3Al":
##                        ontLink = ont3Al
##                elif row[0]=="3Bl":
##                        ontLink = ont3Bl
##                elif row[0]=="3Cl":
##                        ontLink = ont3Cl
                #Locally I can just do
                ontLink = row[0]+".png"
                #online I do
                ontLink = "http://ezaroukian.github.io/pdp/"+row[0]+".png"
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

##                addToType = "." + ontograph + "." +  str(block) + "." + complexity + "." + str(truth)+ "." +str(counter) +"."+ident+"."+an+"."+neg+"."+inan
##                if block == "0":
##                        sentence01 = NL  #I arbitarily chose NL for block 1, other versions should do CE first, and should flip the blocks
##                        itype01 = "NL_pract"+addToType
##                        itype01c = "CE_pract"+addToType
##                        sentence02 = CE
##                        itype02n = "NL_pract"+addToType
##                        itype02 = "CE_pract"+addToType
                        
                sentenceN = NL
                sentenceC = CE
                itypeN = itypeC = "." + ontograph + "." +  str(block) + "." + complexity + "." + str(truth)+ "." +str(counter)+"."+ident+"."+an+"."+neg+"."+inan
                itypeN = "NL" + itypeN
                itypeC = "CE" + itypeC
                
                if block == "0":#practice items
                        itemN = [itypeN, "PracticeQuestion", {"q": countdownP+'<br/><br/>'+'<span class="q">'+sentenceN+"</span>"+image, "hasCorrect": truth}  ]
                        itemC = [itypeC, "PracticeQuestion", {"q": countdownP+'<br/><br/>'+'<span class="q">'+sentenceC+"</span>"+image, "hasCorrect": truth}  ]
                else:
                        itemN = [itypeN, "Question", {"q": countdown+'<br/><br/>'+'<span class="q">'+sentenceN+"</span>"+image, "hasCorrect": truth, "timeout": 11000 } ]
                        itemC = [itypeC, "Question", {"q": countdown+'<br/><br/>'+'<span class="q">'+sentenceC+"</span>"+image, "hasCorrect": truth, "timeout": 11000 } ]
                        
                items.extend([itemN,itemC])
                if block == "0":
                        itemsNames0n.append(itypeN)
                        itemsNames0c.append(itypeC)
                elif block == "1":
                        itemsNames1n.append(itypeN)
                        itemsNames1c.append(itypeC)
                elif block == "2":
                        itemsNames2n.append(itypeN)
                        itemsNames2c.append(itypeC)
        
        csvfile.close()

with open('SUS.csv', 'rb') as csvfile:
        counter = 1
        sus = []
        susNames1n = []
        susNames1c = []
        susNames2n = []
        susNames2c = []
        r = csv.reader(csvfile)
        r.next()
        for row in r:
                order = row[0]
                statement = row[1]
                polarity = row[2]
                itype = polarity+"."+order
                itype1n = "NL.1."+itype
                itype1c = "CE.1."+itype
                itype2n = "NL.2."+itype
                itype2c = "CE.2."+itype
                #arbitrary order for lang/block right now (Latin square for which goes with which)
                item1n = [itype1n, "AcceptabilityJudgment", {"s": statement, "q": "", "as": ["1", "2", "3", "4", "5"], "leftComment": "strongly disagree", "rightComment": "strongly agree"} ]
                item1c = [itype1c, "AcceptabilityJudgment", {"s": statement, "q": "", "as": ["1", "2", "3", "4", "5"], "leftComment": "strongly disagree", "rightComment": "strongly agree"} ]
                item2n = [itype2n, "AcceptabilityJudgment", {"s": statement, "q": "", "as": ["1", "2", "3", "4", "5"], "leftComment": "strongly disagree", "rightComment": "strongly agree"} ]
                item2c = [itype2c, "AcceptabilityJudgment", {"s": statement, "q": "", "as": ["1", "2", "3", "4", "5"], "leftComment": "strongly disagree", "rightComment": "strongly agree"} ]
                sus.extend([item1n,item1c,item2n,item2c])
                susNames1n.append(itype1n)
                susNames1c.append(itype1c)
                susNames2n.append(itype2n)
                susNames2c.append(itype2c)
                
        csvfile.close()



with open('genItems.js', 'w') as writefile:
        writefile.write("var newTestItems = "+str(items)+";\n\n")
        writefile.write("var newSUSItems = "+str(sus)+";\n\n\n")

        writefile.write("var mySeqNC = seq('intro', 'toPractice', followEachWith('sepPractice',seq('"+"', '".join(itemsNames0n)+"')), 'endPractice', followEachWith(seq('conf','sep'),rshuffle('"+"', '".join(itemsNames1n)+"')), 'toSUS', '" + "', '".join(susNames1n)+"', 'break', 'toPractice', followEachWith('sepPractice',seq('"+"', '".join(itemsNames0c)+"')), 'endPractice', followEachWith(seq('conf','sep'),rshuffle('"+"', '".join(itemsNames2c)+"')), 'toSUS', '"+"', '".join(susNames2c)+"', 'endSurvey');\n\n")
        writefile.write("var mySeqCN = seq('intro', 'toPractice', followEachWith('sepPractice',seq('"+"', '".join(itemsNames0c)+"')), 'endPractice', followEachWith(seq('conf','sep'),rshuffle('"+"', '".join(itemsNames1c)+"')), 'toSUS', '" + "', '".join(susNames1c)+"', 'break', 'toPractice', followEachWith('sepPractice',seq('"+"', '".join(itemsNames0n)+"')), 'endPractice', followEachWith(seq('conf','sep'),rshuffle('"+"', '".join(itemsNames2n)+"')), 'toSUS', '"+"', '".join(susNames2n)+"', 'endSurvey');")
        
        writefile.close()


#write a few to file, then in js have random selection for which language starts

