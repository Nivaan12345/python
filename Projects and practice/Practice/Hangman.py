print("Choose a category for hangman \n1.Geography\n2.History\n3.Sports")
category=int(input("your choice is: "))
if category==1:
    x=["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria",
    "Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo (Congo-Brazzaville)","Costa Rica","Croatia","Cuba","Cyprus","Czechia","Democratic Republic of the Congo","Denmark",
    "Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji"
    ,"Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras",
    "Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kuwait",
    "Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands",
    "Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","North Macedonia","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea",
    "Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia"
    ,"Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia",
    "Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands",
    "Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria","Tajikistan","Tanzania"
    ,"Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates",
    "United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]
elif category==2:
    x=["Chandragupta Maurya","Bindusara","Ashoka","Dasharatha Maurya","Samprati","Chandragupta I","Samudragupta","Chandragupta II","Kumaragupta I",
       "Skandagupta","Harsha","Pulakeshin II","Vikramaditya (Chandragupta II)","Yashodharman","Rajaraja Chola I","Rajendra Chola I","Kulothunga Chola I",
       "Karikala Chola","Krishnadevaraya","Harihara I","Bukka Raya I","Devaraya II","Prithviraj Chauhan","Vigraharaja IV","Rana Kumbha","Rana Sanga",
       "Maharana Pratap","Udai Singh II","Rana Amar Singh I","Shivaji Maharaj","Sambhaji Maharaj","Rajaram Maharaj","Shahu Maharaj","Balaji Vishwanath",
       "Baji Rao I","Balaji Baji Rao","Madhavrao I","Raghuji Bhonsle","Ahilyabai Holkar","Malhar Rao Holkar","Ranjit Singh","Kharak Singh","Duleep Singh",
       "Anangpal Tomar","Qutb-ud-din Aibak","Iltutmish","Razia Sultan","Ghiyas-ud-din Balban","Alauddin Khilji","Muhammad bin Tughlaq","Firoz Shah Tughlaq"
       ,"Sikandar Lodi","Ibrahim Lodi","Babur","Humayun","Akbar","Jahangir","Shah Jahan","Aurangzeb","Bahadur Shah I",
       "Muhammad Shah","Bahadur Shah Zafar","Sher Shah Suri","Islam Shah Suri","Hemu Vikramaditya","Krishna Deva Raya","Tipu Sultan","Hyder Ali","Krishnaraja Wodeyar III",
       "Chikka Devaraja Wodeyar","Serfoji II","Shahaji Bhonsle","Lachit Borphukan","Rudrama Devi","Ganapati Deva",
       "Prataparudra II","Narasimhadeva I","Anantavarman Chodaganga","Yayati I","Bhoja","Munja","Dantidurga","Krishna I (Rashtrakuta)","Amoghavarsha I",
       "Govinda III","Tailapa II","Someshvara I","Vikramaditya VI","Ballala II","Veera Ballala III","Nizam-ul-Mulk Asaf Jah I",
       "Salabat Jung","Mir Osman Ali Khan"]
elif category==3:
    x=["Sachin Tendulkar","Virat Kohli","MS Dhoni","Rohit Sharma","Kapil Dev","Sunil Gavaskar","Rahul Dravid","Sourav Ganguly","Anil Kumble","Virender Sehwag","Yuvraj Singh","Jasprit Bumrah","Ravichandran Ashwin","Ravindra Jadeja","Hardik Pandya","KL Rahul","Shikhar Dhawan",
       "Mohammed Shami","Ishant Sharma","Zaheer Khan","Harbhajan Singh","Gautam Gambhir","VVS Laxman","Mohammad Azharuddin","Ajinkya Rahane","Cheteshwar Pujara","Rishabh Pant","Suryakumar Yadav","Shubman Gill","David Warner","Steve Smith","Ricky Ponting","Glenn McGrath","Shane Warne","Adam Gilchrist","Muttiah Muralitharan",
       "Kumar Sangakkara","Mahela Jayawardene","Sanath Jayasuriya","Wasim Akram","Waqar Younis","Imran Khan","Babar Azam","Shaheen Afridi","Kane Williamson","Brendon McCullum","Ross Taylor","Ben Stokes","Joe Root",
       "James Anderson","Stuart Broad","Alastair Cook","Jacques Kallis","AB de Villiers","Dale Steyn","Graeme Smith","Chris Gayle","Brian Lara","Curtly Ambrose",
       "Courtney Walsh","Kieron Pollard","Andre Russell","Lasith Malinga","Shakib Al Hasan","Tamim Iqbal","Mashrafe Mortaza","Angelo Mathews","Thisara Perera","Dinesh Chandimal","Faf du Plessis",
       "Quinton de Kock","Hashim Amla","Mitchell Starc","Pat Cummins","Josh Hazlewood","Travis Head","Aaron Finch","Glenn Maxwell","Shane Watson",
       "Michael Clarke","Brett Lee","Matthew Hayden","Mark Waugh","Steve Waugh","Allan Border","Dennis Lillee","Ian Botham","Michael Vaughan","Kevin Pietersen",
       "Eoin Morgan","Jofra Archer","Jos Buttler","Saeed Anwar","Inzamam-ul-Haq","Shoaib Akhtar","Younis Khan","Misbah-ul-Haq","Mohammad Hafeez"]
else:
    print("Error please choose a number between 1 and 3")


import random
hangman=random.choice(x)
answer=""
for i in range(len(hangman)+1):
    answer=answer+"-"
lives=7
while lives==0:
    y=input("Enter the letter ")
    if y or y.upper in hangman:
        print("--------congratulations------------")
        print(f"the letter {y} is in the answer")
        l=hangman(enumerate(y))
        answer[l]=y
        print(answer)
