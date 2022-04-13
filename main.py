# importing the regular expression
import re
#from tkinter import *

# importing long responses file from the same folder
import long_responses as long

print('Namaste, I am Dr. Bot!')
print('How can I help you with? Common Diseases or Covid 19?')


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainity = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainity += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainity) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Response --------------------------------------------------------------------------------------------------------------
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'], single_response=True)

    # Common Diseases Code
    response(
        'Please tell me what do you want to know on Common Diseases? The common diseases with which I can help are - Flu, Backpain, Diarrhea, Fatigue, Hyper Tension, Knee Pain, Cough & Cold, Tuberculosis, Polio',
        ['common', 'disease', 'Common', 'Disease'], required_words=['common'])

    # Flu
    response('What do you want to know about Flu? 1. Symptoms 2. Cure 3. Medicine 4. Prevention', ['flu'],
             required_words=['flu'])
    response(
        'Symptoms of Flu are 1. Fever or feeling feverish/chills 2. Cough 3. Sore throat 4. Runny or stuffy nose 5. Muscle or body aches 6. Headaches 7. Fatigue (tiredness) 8. Some people may have vomiting and diarrhea, though this is more common in children than adults.',
        ['symptoms','flu'], required_words=['flu','symptoms'])

    response(
        'Cure of Flu is 1. Stay home and get plenty of rest. Mind your flu manners. 2. Drink plenty of fluids. Make sure you get more liquids. 3. Treat aches and fever. 4. Take care of your cough. Over-the-counter treatments can calm your hack. 5. Sit in a steamy bathroom. 6. Run the humidifier. 7. Try a lozenge.',
        ['cure','flu'], required_words=['cure', 'flu'])
    response(
        '(1). Baidyanath (Jhansi) Mrityunjay Ras Tablet (2). Baidyanath (Jhansi) Fevercut Tablet (3). Tansukh Sudarshanghan Vati.',
        ['ayurvedic', 'flu'], required_words=['ayurvedic', 'flu'])
    response(
        'Prevention of Flu is 1.Avoid close contact. Avoid close contact with people who are sick. 2. Cover your mouth and nose. 3. Clean your hands. 4. Avoid touching your eyes, nose or mouth. 5. Practice other good health habits.',
        ['home remedy', 'flu'], required_words=['home remedy', 'flu'])

    # Backpain
    response('What do you want to know about BackPain? 1. Symptoms 2. Cure 3. Medicine 4. Prevention', ['backpain'],
             required_words=['backpain'])
    response(
        'Symptoms of Backpain are 1. inflammation or swelling on the back. 2. persistent back pain where lying down or resting does not help. 3. a recent injury, blow, or trauma to the back 4. pain down the legs. 5. pain that reaches below the knees.',
        ['symptom', 'of', 'backpain'], required_words=['symptoms'])
    response(
        'Cure of Backpain is 1. Apply Ice and Heat. 2. Keep Exercising. 3. Strengthen Your Core. 4. Limit Bed Rest.',
        ['cure', 'backpain'], required_words=['cure', 'backpain'])
    response('Medicine used for Backpain are 1. ibuprofen (Advil) 2. naproxen (Aleve). 3. NSAIDs.',
             ['medicine', 'medicines', 'backpain'], required_words=['medicine', 'backpain'])
    response(
        'Prevention of Backpain is 1.  Avoid heavy lifting. 2.  Get active and eat a balanced diet. 3.  Do back-strengthening and stretching exercises at least 2 days a week.',
        ['prevention', 'backpain'], required_words=['prevention', 'backpain'])

    # Diarrhea
    response('What do you want to know about Diarrhea? 1. Symptoms 2. Cure 3. Medicine 4. Prevention', ['diarrhea'],
             required_words=['diarrhea'])
    response(
        'Symptoms of Diarrhea are 1.Frequent loose, watery stools. 2.Abdominal cramps. 3.Abdominal pain. 4.Fever. 5.Bleeding. 6.Lightheadedness or dizziness from dehydration.',
        ['symptom', 'symptoms', 'diarrhea'], required_words=['symptom', 'diarrhea'])
    response('Cure of Diarrhea is 1. Rehydrating. 2. Eating health diet. 3. Avoiding high fat and oily food.',
             ['cure', 'diarrhea'], required_words=['cure', 'diarrhea'])
    response(
        'Medicine used for Diarrhea are 1.  Loperamide (1 brand name: Imodium). 2.  Bismuth subsalicylate (2 brand names: Kaopectate, Pepto-Bismol).',
        ['medicine', 'medicines', 'diarrhea'], required_words=['medicine', 'diarrhea'])
    response(
        'Prevention of Diarrhea is 1. access to safe drinking-water. 2. use of improved sanitation. 3. hand washing with soap. 4. exclusive breastfeeding for the first six months of life. 5. good personal and food hygiene. 6. health education about how infections spread. 7. rotavirus vaccination.',
        ['prevention', 'diarrhea'], required_words=['prevention', 'diarrhea'])

    # Fatigue
    response('What do you want to know about Fatigue? 1. Symptoms 2. Cure 3. Medicine 4. Prevention', ['fatigue'],
             required_words=['fatigue'])
    response(
        'Symptoms of Fatigue are 1. Aching or sore muscles 2. Apathy and a lack of motivation 3. Daytime drowsiness 4. Difficulty concentrating or learning new tasks 5. Gastrointestinal problems, such as bloating, abdominal pain, constipation, or diarrhea 6. Headache 7. Irritability or moodiness 8. Slowed response time 9. Vision problems, such as blurriness',
        ['symptom', 'symptoms', 'fatigue'], required_words=['symptom', 'fatigue'])
    response(
        'Cure of Fatigue is 1. Get active 2. Sip Some Potato Water 3. Boost Red-Blood Cells 4. Perk-Up With Citrus 5. Make Your Own Energy Drink 6. Hello, Yoga. 7. Eat (and drink) good stuff.',
        ['cure', 'fatigue'], required_words=['cure', 'fatigue'])
    response(
        'Medicine used for Fatigue are 1. modafinil 2. methylphenidate 3. amantadine 4. amphetamine / dextroamphetamine',
        ['medicine', 'medicines', 'fatigue'], required_words=['medicine', 'fatigue'])
    response(
        'Prevention of Fatigue is 1. Manage stress and practice relaxation techniques. 2. Get exercise, but begin slowly and check with your health care practitioner before beginning any exercise program. 3. Check your medications with a health care practitioner or pharmacists to see if some medications could be responsible for fatigue.',
        ['prevention', 'fatigue'], required_words=['prevention', 'fatigue'])

    # HyperTension
    response('What do you want to know about Hypertension? 1. Symptoms 2. Cure 3. Medicine 4. Prevention',
             ['hypertension'], required_words=['hypertension'])
    response(
        'Symptoms of Hypertension are 1.Most people with high blood pressure have no signs or symptoms, even if blood pressure readings reach dangerously high levels. 2.A few people with high blood pressure may have headaches, shortness of breath or nosebleeds, but these signs and symptoms aren\'t specific and usually don\'t occur until high blood pressure has reached a severe or life-threatening stage.',
        ['symptom', 'symptoms', 'hypertension'], required_words=['symptom', 'hypertension'])
    response(
        'Cure of Hypertension is 1. Garlic 2. Cardamom 3.Hibiscus sabdariffa 4.Rauwolfia serpentina 5.Crataegus oxyacantha',
        ['cure', 'hypertension'], required_words=['cure', 'hypertension'])
    response(
        'Medicine used for Hypertension are There are several types of drugs used to treat high blood pressure, including: Angiotensin-converting enzyme (ACE) inhibitors, Angiotensin II receptor blockers (ARBs), Diuretics, Beta-blockers, Calcium channel blockers, Alpha-blockers, Alpha-agonists, Renin-inhibitors, Combination medications',
        ['medicine', 'medicines', 'hypertension'], required_words=['medicine', 'hypertension'])
    response(
        'Prevention of Hypertension is 1. Eat a Healthy Diet 2. Keep Yourself at a Healthy Weight 3. Be Physically Active 4. Do Not Smoke 5. Limit How Much Alcohol You Drink 6. Get Enough Sleep',
        ['prevention', 'hypertension'], required_words=['prevention', 'hypertension'])

    # Knee Pain
    response('What do you want to know about Knee Pain? 1. Symptoms 2. Cure 3. Medicine 4. Prevention', ['kneepain'],
             required_words=['kneepain'])
    response(
        'Symptoms of Knee Pain are Knee pain that appears out of nowhere may seem like it couldn’t be related to an injury. But the knee is a tricky body part. It consists of many parts that can become: stretched out, worn, aggravated, partially torn, fully ruptured',
        ['symptom', 'symptoms', 'kneepain'], required_words=['symptom', 'kneepain'])
    response(
        'Cure of Knee Pain is 1. Try RICE( Rest, Ice, Compression ,Elevation) for strains and sprains. 2. Daily exercise 3. Weight management 4.Heat and cold therapy 5.Herbal ointment 6. Willow bark 7.Ginger extract',
        ['cure', 'kneepain'], required_words=['cure', 'kneepain'])
    response(
        'Medicine used for Knee Pain are NSAIDs -- nonsteroidal anti-inflammatory drugs. They include: Aspirin, Ibuprofen (Advil, Motrin, Nuprin), Naproxen (Aleve, Anaprox, Naprosyn)',
        ['medicine', 'medicines', 'kneepain'], required_words=['medicine', 'kneepain'])
    response(
        'Prevention of Knee Pain is 1.  Don\'t skip the exercise, even if you have a structural problem. 2. Whether you\'re active or not, stretching is good for the knees. 3. Losing weight can improve knee pain. 4. Wearing the proper shoes is important for healthy knees. 5. Stand up straight to feel better.',
        ['prevention', 'kneepain'], required_words=['prevention', 'kneepain'])

    # Cough
    response('What do you want to know about Cough? 1. Symptoms 2. Cure 3. Medicine 4. Prevention', ['cough'],
             required_words=['cough'])
    response(
        'Symptoms of Cough are - A chronic cough can occur with other signs and symptoms, which may include: 1. A runny or stuffy nose 2. A feeling of liquid running down the back of your throat (postnasal drip) 3. Frequent throat clearing and sore throat 4. Hoarseness 5. Wheezing and shortness of breath 6. Heartburn or a sour taste in your mouth 7. In rare cases, coughing up blood.',
        ['symptom', 'symptoms', 'cough'], required_words=['symptom', 'cough'])
    response(
        'Cure of Cough is 1. Drinking plenty of fluids. 2. Resting. 3. Adjusting your room\'s temperature and humidity. 4. Soothing your throat. 5. Using saline nasal drops.',
        ['cure', 'cough'], required_words=['cure', 'cough'])
    response(
        'Medicine used for Cough are Pain relievers like aspirin or other mild relievers. Use caution when giving aspirin to children or teenagers. Consider giving your child over-the-counter (OTC) pain medications designed for infants or children. These include acetaminophen (Children\'s Tylenol, FeverAll, others) or ibuprofen (Children\'s Advil, Children\'s Motrin, others) to ease symptoms.',
        ['medicine', 'medicines', 'cough'], required_words=['medicine', 'cough'])
    response(
        'Prevention of Cough is 1. Wash Your Hands 2. Don\'t Cover Your Sneezes and Coughs With Your Hands 3)Don\'t Touch Your Face 4. Do Aerobic Exercise Regularly 5. Eat Foods Containing Phytochemicals 6. Don\'t Smoke',
        ['prevention', 'cough'], required_words=['prevention', 'cough'])

    # Cold
    response('What do you want to know about Cold? 1. Symptoms 2. Cure 3. Medicine 4. Prevention', ['cold'],
             required_words=['cold'])
    response(
        'Symptoms of Cold are A chronic cough or cold can occur with other signs and symptoms, which may include: 1. A runny or stuffy nose 2. A feeling of liquid running down the back of your throat (postnasal drip) 3. Frequent throat clearing and sore throat 4. Hoarseness 5. Wheezing and shortness of breath 6. Heartburn or a sour taste in your mouth 7. In rare cases, coughing up blood.',
        ['symptom', 'symptoms', 'cold'], required_words=['symptom', 'cold'])
    response(
        'Cure of Cold is 1. Drinking plenty of fluids. 2. Resting. 3. Adjusting your room\'s temperature and humidity. 4. Soothing your throat. 5. Using saline nasal drops.',
        ['cure', 'cold'], required_words=['cure', 'cold'])
    response(
        'Medicine used for Cold are Pain relievers like aspirin or other mild relievers. Use caution when giving aspirin to children or teenagers. Consider giving your child over-the-counter (OTC) pain medications designed for infants or children. These include acetaminophen (Children\'s Tylenol, FeverAll, others) or ibuprofen (Children\'s Advil, Children\'s Motrin, others) to ease symptoms.',
        ['medicine', 'medicines', 'cold'], required_words=['medicine', 'cold'])
    response(
        'Prevention of Cold is 1. Wash Your Hands 2. Don\'t Cover Your Sneezes and Coughs With Your Hands 3)Don\'t Touch Your Face 4. Do Aerobic Exercise Regularly 5. Eat Foods Containing Phytochemicals 6. Don\'t Smoke',
        ['prevention', 'cold'], required_words=['prevention', 'cold'])

    # Tuberculosis
    response('What do you want to know about Tuberculosis? 1. Symptoms 2. Cure 3. Medicine 4. Prevention',
             ['tuberculosis'], required_words=['tuberculosis'])
    response(
        'Symptoms of Tuberculosis are 1. A bad cough that lasts 3 weeks or longer 2. Pain in the chest 3. Coughing up blood or sputum (phlegm from deep inside the lungs) 4. Weakness or fatigue 5. Weight loss 6. No appetite 7. Sweating at night',
        ['symptom', 'symptoms', 'tuberculosis'], required_words=['symptom', 'tuberculosis'])
    response(
        'Cure of Tuberculosis is 1. keep regular follow-up with the doctor. 2. Take the medicines as prescribed. 3. Report any side effects of the medicine.',
        ['cure', 'tuberculosis'], required_words=['cure', 'tuberculosis'])
    response(
        'Medicine used for Tuberculosis are 1. Isoniazid. 2. Rifampin (Rifadin, Rimactane) 3. Ethambutol (Myambutol) 4. Pyrazinamide.',
        ['medicine', 'medicines', 'tuberculosis'], required_words=['medicine', 'tuberculosis'])
    response(
        'Prevention of Tuberculosis is 1. Stay away from work, school or college until your TB treatment team advises you it\'s safe to return. 2. Always cover your mouth – preferably with a disposable tissue – when coughing, sneezing or laughing 3. Carefully dispose of any used tissues in a sealed plastic bag 4. Open windows when possible to ensure a good supply of fresh air in the areas where you spend time 5. Not sleep in the same room as other people – you could cough or sneeze in your sleep without realising it',
        ['prevention', 'tuberculosis'], required_words=['prevention', 'tuberculosis'])

    # Polio
    response('What do you want to know about Polio? 1. Symptoms 2. Cure 3. Medicine 4. Prevention', ['polio'],
             required_words=['polio'])
    response(
        'Symptoms of Polio are Fever, Sore throat, Headache, Vomiting, Fatigue, Back pain or stiffness, Neck pain or stiffness, Pain or stiffness in the arms or legs.',
        ['symptom', 'symptoms', 'polio'], required_words=['symptom', 'polio'])
    response(
        'Cure of Polio is Heat and physical therapy is used to stimulate the muscles and antispasmodic drugs are given to relax the muscles. While this can improve mobility, it cannot reverse permanent polio paralysis. Polio can be prevented through immunization.',
        ['cure', 'polio'], required_words=['cure', 'polio'])
    response(
        'Medicine used for Polio are 1. IPOL® 2. Orimune® Trivalent 3. Kinrix® (containing Diphtheria, Tetanus Toxoids, Acellular Pertussis, Polio Vaccine) 4. Pentacel® (containing Diphtheria, Tetanus Toxoids, Acellular Pertussis, Haemophilus influenzae type b, Polio Vaccine)',
        ['medicine', 'medicines', 'polio'], required_words=['medicine', 'polio'])
    response(
        'Prevention of Polio is 1. Provision of clean water. 2. improved hygienic practices and sanitation are important for reducing the risk of transmission of polio virus.',
        ['prevention', 'polio'], required_words=['prevention', 'polio'])

    # COVID-19
    response('Please tell me what do you want to know about COVID-19? Symptoms, Prevention, or Immunity Boosters?',
             ['covid-19','covid', 'Covid', 'COVID' ], required_words=['covid'])
    response(
        'Symptoms of Covid are 1. Fever 2. Cough 3. Tiredness 4. Loss of taste or smell 5. Shortness of breath or difficulty breathing 6. Muscle aches, joint pains 7. Severe dizziness 8. Chills 9. Sore throat 10. Runny nose 11. Headache 12. Conjunctivitis 13. Chest pain 14. Skin rash 15. Nausea 16. Vomiting 17. Diarrhoea 18. Loss of speech 19. Loss of movement',
        ['symptom', 'symptoms', 'covid'], required_words=['symptom', 'covid'])
    response(
        'Prevention of Covid is 1. Clean your hands often. Use soap and water, or an alcohol-based hand rub. 2. Maintain a safe distance from anyone who is coughing or sneezing. 3. Wear a mask when physical distancing is not possible. 4. Don’t touch your eyes, nose or mouth. 5. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze. 6. Stay home if you feel unwell. 7. If you have a fever, cough and difficulty breathing, seek medical attention.',
        ['prevention', 'covid'], required_words=['prevention', 'covid'])
    response(
        'Immunity Boosters for Covid are 1. Take Immunity-Boosting Foods & Vitamins: fruits & vegetables contain vitamins A, C, D, and E, and minerals like magnesium, selenium, and zinc that acts as immunity-boosting vitamins. 2. Take Proper 7-8 Hours of Sleep:  Sleeping well is one of the easiest ways to increase immunity for COVID-19. 3. Drink up to 8-10 glasses of water every day:  Staying hydrated is the best way to increase immunity to fight Coronavirus because it flushes out all the toxins from the body. Immunity booster drink such as fresh fruit juices and coconut water, along with consuming enough water throughout the day helps in keeping the body hydrated. 4. Don’t skip these home workout exercises:  Home workout are another way of flushing out toxins from the body through sweat. Make sure not to skip exercises while staying home during the pandemic. Depending upon one’s stamina and routine, some of the easy workout exercises that can be done at home may include rope-skipping, push-ups, jogging on the spot, front plank, and forward lunges. 5. Practice These 3 Steps: A] Practice meditation:  Meditation is a mindful exercise that relaxes the mind of all external chaos and distractions. A mere 10 minutes of meditation every day can make a big difference not only throughout the day but also in life as a whole. A calm mind helps in better focus,  better decisions, and builds a sound body. B] Avoid Smoking and Alcohol:  Smoking and other substance abuse weaken the respiratory system, while alcohol reduces immunity. This makes the body susceptible to catching the virus and being infected. C] Avoid Non-essential travelling:  Social distancing is key to fighting novel coronavirus, and hence avoiding non-essential travel will help in protecting oneself and others from the virus.',
        ['immunity', 'boosters', 'covid'], required_words=['immunity', 'boosters', 'covid'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    # splitting the message into array so we can split each word seperately
    # the re split removes all the special characters which helps to recognise text easily
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Create an infinite while true loop so we can always get new responses
# Testing the response system
while True:
    # created a function get_response for taking the input from user
    print('Dr. Bot: ' + get_response(input('You: ')))

  