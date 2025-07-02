from datetime import date
from db import db
from models import User, PersonalityResult

# Nutzer erstellen
users = [
    User(user_id=1, uni_id=1, name="Julia Carter", email="julia.carter@example.com", password="hashed_pw_1",
         birth_date=date(2000, 6, 14), created_at=date(2025, 7, 1), profile_picture=b"binary_data",
         description="I'm a Master's student in Psychology with a strong interest in social impact and mental health. Originally from the UK, I moved to Berlin to explore a more open and diverse culture. I enjoy deep conversations, quiet cafés, and volunteering with youth organizations. I'm using this app to find like-minded people who value empathy and authenticity. If you're into mindfulness, art therapy, or just want to take a walk in Tiergarten – let's connect!"),
    User(user_id=2, uni_id=2, name="Max Becker", email="max.becker@example.com", password="hashed_pw_2",
         birth_date=date(2002, 3, 9), created_at=date(2025, 7, 1), profile_picture=b"binary_data",
         description="Hey! I'm studying Mechanical Engineering and love anything hands-on – bikes, drones, gadgets, you name it. I'm usually out skating or checking out techno clubs on the weekends. I'm not great at small talk, but I’m always up for spontaneous adventures or random challenges. I'm here to meet energetic people who like to do stuff, not just talk about it."),
    User(user_id=3, uni_id=3, name="Leila Osman", email="leila.osman@example.com", password="hashed_pw_3",
         birth_date=date(1999, 11, 22), created_at=date(2025, 7, 1), profile_picture=b"binary_data",
         description="I'm a Literature student with a passion for poetry, feminism, and intercultural exchange. Berlin is a city where I can breathe creatively and politically. I spend my time in small bookshops, writing zines, or attending panel discussions. I'm looking to connect with people who have something to say – and who like rainy afternoons with good coffee and deeper meaning."),
    User(user_id=4, uni_id=4, name="Jonas Meier", email="jonas.meier@example.com", password="hashed_pw_4",
         birth_date=date(2003, 1, 15), created_at=date(2025, 7, 1), profile_picture=b"binary_data",
         description="I’m a Computer Science undergrad with a love for structure, logic, and chess. I’m pretty quiet at first, but enjoy loyal friendships and meaningful collaborations. In my free time I work on open-source software and explore Berlin's architecture. I’d like to meet people who respect boundaries, value consistency, and maybe want to start a study group."),
    User(user_id=5, uni_id=5, name="Clara Nguyen", email="clara.nguyen@example.com", password="hashed_pw_5",
         birth_date=date(2004, 8, 6), created_at=date(2025, 7, 1), profile_picture=b"binary_data",
         description="Design student and full-time daydreamer 🌈 I love color, music, and finding beauty in small things. I came to Berlin because I thrive in creative chaos and open spaces. I'm curious about everything – from urban gardening to improv theater. Here to meet people who don't take life too seriously and enjoy late-night bike rides, weird art, or talking about the future of the world."),
    User(user_id=6, uni_id=13, name="Amina Rahmani", email="amina.rahmani@example.com", password="hashed_pw_6",
         birth_date=date(2001, 10, 18), created_at=date(2025, 7, 1), profile_picture=b"binary_data",
         description="Social Work student with a heart for community building and intersectional feminism. I moved from Hamburg to Berlin to dive deeper into social justice work and inclusive education. I'm passionate about mutual care, language diversity, and public spaces. I'm looking for friends who are grounded, open-hearted, and maybe also looking for a break from the Berlin hustle. Let's go to community events or just hang out over tea."),
    User(user_id=7, uni_id=6, name="Lukas Schneider", email="lukas.schneider@example.com", password="hashed_pw_7",
         birth_date=date(1998, 12, 2), created_at=date(2025, 7, 1), profile_picture=b"binary_data",
         description="I'm doing a dual degree in IT & Management and mostly spend my time optimizing things – systems, workflows, even my daily routine. I like strategy games, geopolitics, and efficient apps. Some people say I'm intense, but I just really like ideas. I'd love to meet people who challenge me intellectually but also help me take things less seriously."),
    User(user_id=8, uni_id=7, name="Sara El-Masri", email="sara.elmasri@example.com", password="hashed_pw_8",
         birth_date=date(2003, 4, 27), created_at=date(2025, 7, 1), profile_picture=b"binary_data",
         description="I'm a medical student who loves working with people and believes in kindness as a core value. I’m into dance, baking, and mental health awareness. Berlin is home now, and I’m building my life one connection at a time. I’d love to find friends who enjoy brunch, helping others, or just sharing the little wins in life. Let's make some warm memories in a cold city :)"),
    User(user_id=9, uni_id=8, name="Tomás Rivera", email="tomas.rivera@example.com", password="hashed_pw_9",
         birth_date=date(2000, 9, 10), created_at=date(2025, 7, 1), profile_picture=b"binary_data",
         description="Originally from Argentina, I came to Berlin for philosophy, art theory, and (let's be honest) to argue about everything from Nietzsche to NFTs. I love building weird indie games and talking until 3am. Looking for fellow idea-hunters who enjoy creative chaos, cultural critique, and street food. Bonus points if you like paradoxes or dogs."),
    User(user_id=10, uni_id=1, name="Anna Petrova", email="anna.petrova@example.com", password="hashed_pw_10",
         birth_date=date(1997, 2, 5), created_at=date(2025, 7, 1), profile_picture=b"binary_data",
         description="I'm a Ukrainian-born Data Science PhD student, currently working on AI fairness and statistical bias. When I’m not coding or teaching, I climb, do photography, or lose track of time exploring flea markets. I tend to be direct and independent, but I enjoy sharing space with curious, grounded people. Friends who respect silence are always welcome.")
]

# Persönlichkeitsergebnisse
results = [
    PersonalityResult(result_id=1, user_id=1, vec_ei=0.21, vec_sn=0.34, vec_tf=0.39, vec_jp=0.78, mbti_type='INFJ', completed_at=date(2025, 6, 20)),
    PersonalityResult(result_id=2, user_id=2, vec_ei=0.89, vec_sn=0.77, vec_tf=0.64, vec_jp=0.12, mbti_type='ESTP', completed_at=date(2025, 6, 18)),
    PersonalityResult(result_id=3, user_id=3, vec_ei=0.18, vec_sn=0.42, vec_tf=0.27, vec_jp=0.51, mbti_type='INFP', completed_at=date(2025, 6, 22)),
    PersonalityResult(result_id=4, user_id=4, vec_ei=0.32, vec_sn=0.68, vec_tf=0.71, vec_jp=0.82, mbti_type='ISTJ', completed_at=date(2025, 6, 19)),
    PersonalityResult(result_id=5, user_id=5, vec_ei=0.86, vec_sn=0.38, vec_tf=0.29, vec_jp=0.35, mbti_type='ENFP', completed_at=date(2025, 6, 21)),
    PersonalityResult(result_id=6, user_id=6, vec_ei=0.27, vec_sn=0.66, vec_tf=0.33, vec_jp=0.79, mbti_type='ISFJ', completed_at=date(2025, 6, 23)),
    PersonalityResult(result_id=7, user_id=7, vec_ei=0.12, vec_sn=0.53, vec_tf=0.81, vec_jp=0.76, mbti_type='INTJ', completed_at=date(2025, 6, 20)),
    PersonalityResult(result_id=8, user_id=8, vec_ei=0.75, vec_sn=0.69, vec_tf=0.32, vec_jp=0.71, mbti_type='ESFJ', completed_at=date(2025, 6, 19)),
    PersonalityResult(result_id=9, user_id=9, vec_ei=0.84, vec_sn=0.41, vec_tf=0.54, vec_jp=0.29, mbti_type='ENTP', completed_at=date(2025, 6, 18)),
    PersonalityResult(result_id=10, user_id=10, vec_ei=0.35, vec_sn=0.72, vec_tf=0.67, vec_jp=0.25, mbti_type='ISTP', completed_at=date(2025, 6, 17)),
]

# In DB einfügen
db.session.bulk_save_objects(users)
db.session.bulk_save_objects(results)
db.session.commit()

print("Alle User und Personality-Daten wurden erfolgreich eingefügt.")
