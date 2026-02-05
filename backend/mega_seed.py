"""
Comprehensive Quiz & Questions Seeder
Creates 50 quizzes (6-10 grades × 5 subjects × 2 difficulty levels)
With 10 questions each = 500+ questions total
"""
import requests
import json
import time

API_BASE = "http://127.0.0.1:8000/api"

# Quiz metadata
GRADES = [6, 7, 8, 9, 10]
SUBJECTS = {
    'Tamil': 'தமிழ்',
    'English': 'ஆங்கிலம்',
    'Maths': 'கணிதம்',
    'Science': 'அறிவியல்',
    'SS': 'சामூது பயிற்சி'
}
LEVELS = ['Easy', 'Medium', 'Hard']

# Sample questions for each subject (will repeat for all grades)
SAMPLE_QUESTIONS = {
    'Tamil': [
        {'q': 'தமிழ் மொழி எந்த நாட்டின் முக்கிய மொழி?', 'a': 'தென்னாட்டு', 'b': 'வடக்கு', 'c': 'நடுப்பு', 'd': 'மேல்', 'ans': 'a'},
        {'q': 'தமிழ் மொழியின் தந்தை என அழைக்கப்படுபவர் யார்?', 'a': 'பாணினி', 'b': 'சிவக்கை', 'c': 'பாணனீ', 'd': 'இப்.பி.எ', 'ans': 'b'},
        {'q': 'சங்ககால இலக்கியத்தின் மிகப் பழமையான தொல்காப்பியம் எப்போது எழுதப்பட்டது?', 'a': '1000 ஆண்டுக்கு முன்', 'b': '2000 ஆண்டுக்கு முன்', 'c': '1500 ஆண்டுக்கு முன்', 'd': '500 ஆண்டுக்கு முன்', 'ans': 'b'},
        {'q': 'தமிழின் முதல் அச்சுப் பதிப்பு எஸ் செந்தமிழ் என்று யாரால் எழுதப்பட்டது?', 'a': 'கும்மணன்', 'b': 'மெய்ப்பாவணன்', 'c': 'நெருளவர்', 'd': 'வாக்கார', 'ans': 'a'},
        {'q': 'பெரியாழ்வாரின் பெயர் என்ன?', 'a': 'விஷ்ணுசித்தன்', 'b': 'வாலராயன்', 'c': 'பரிய', 'd': 'வாலி', 'ans': 'a'},
        {'q': 'கம்பராமாயண உபாகேசிதம் பொருந்தும் காண்டம் எது?', 'a': 'பாலகாண்டம்', 'b': 'மந்திரகாண்டம்', 'c': 'களங்தகாண்டம்', 'd': 'இராவணகாண்டம்', 'ans': 'c'},
        {'q': 'பெரியாழ்வாரின் பக்திபக்கம் என்பது...', 'a': 'வெறுமனை பேச்சு', 'b': 'கண்ணன் பக்திக் குறிப்பு', 'c': 'தெய்வ உணர்வு', 'd': 'விஷ்ணு வழிபாடு', 'ans': 'd'},
        {'q': 'சிலப்பதிகாரம் கூறும் ஐயகஇலக்கணம் எது?', 'a': 'ஐம்பது', 'b': 'ஆறு', 'c': 'ஐந்து', 'd': 'நான்கு', 'ans': 'c'},
        {'q': 'மணிமேகலை சொல்வது...', 'a': 'இளங்கோவின் கதை', 'b': 'கண்ணகியின் மகளான மதুரையின் கதை', 'c': 'மணிமேகலையின் புத்த பக்தி', 'd': 'சீவக சிந்தாமணியின் ஒரு பகுதி', 'ans': 'c'},
        {'q': 'மாணிக்கவாசகரின் திருவாசகம் செய்யப்பட்ட முக்கிய முறை எது?', 'a': 'புலவரேனும் பொதிய', 'b': 'தெய்வ பக்தி', 'c': 'சிவபக்தி', 'd': 'சாதாரண கவிதை', 'ans': 'c'}
    ],
    'English': [
        {'q': 'Who is the author of "To Kill a Mockingbird"?', 'a': 'Harper Lee', 'b': 'Jane Austen', 'c': 'Mark Twain', 'd': 'Charles Dickens', 'ans': 'a'},
        {'q': 'What is the opposite of "benevolent"?', 'a': 'Kind', 'b': 'Malevolent', 'c': 'Generous', 'd': 'Helpful', 'ans': 'b'},
        {'q': 'Which sentence is grammatically correct?', 'a': 'She go to school', 'b': 'She goes to school', 'c': 'She going to school', 'd': 'She gone to school', 'ans': 'b'},
        {'q': 'What does "eloquent" mean?', 'a': 'Silent', 'b': 'Clear and expressive in speech', 'c': 'Angry', 'd': 'Confused', 'ans': 'b'},
        {'q': 'Identify the adjective in: "The quick brown fox"', 'a': 'fox', 'b': 'brown', 'c': 'quick and brown', 'd': 'the', 'ans': 'c'},
        {'q': 'What is a metaphor?', 'a': 'A comparison using "like" or "as"', 'b': 'A direct comparison without "like"', 'c': 'A type of poem', 'd': 'A figure of speech', 'ans': 'b'},
        {'q': 'Which word is a noun?', 'a': 'Run', 'b': 'Beautiful', 'c': 'Dog', 'd': 'Quickly', 'ans': 'c'},
        {'q': 'What tense is "has been running"?', 'a': 'Simple past', 'b': 'Present perfect continuous', 'c': 'Past continuous', 'd': 'Future tense', 'ans': 'b'},
        {'q': 'What is the plural of "child"?', 'a': 'Childs', 'b': 'Childes', 'c': 'Children', 'd': 'Childes', 'ans': 'c'},
        {'q': 'Which is a synonym for "happy"?', 'a': 'Sad', 'b': 'Joyful', 'c': 'Angry', 'd': 'Tired', 'ans': 'b'}
    ],
    'Maths': [
        {'q': 'What is 15 + 23?', 'a': '37', 'b': '38', 'c': '39', 'd': '40', 'ans': 'b'},
        {'q': 'What is 50 - 18?', 'a': '30', 'b': '31', 'c': '32', 'd': '33', 'ans': 'c'},
        {'q': 'What is 7 × 8?', 'a': '54', 'b': '55', 'c': '56', 'd': '57', 'ans': 'c'},
        {'q': 'What is 144 ÷ 12?', 'a': '11', 'b': '12', 'c': '13', 'd': '14', 'ans': 'b'},
        {'q': 'What is 3² (3 squared)?', 'a': '6', 'b': '8', 'c': '9', 'd': '12', 'ans': 'c'},
        {'q': 'What is √25?', 'a': '4', 'b': '5', 'c': '6', 'd': '7', 'ans': 'b'},
        {'q': 'What is the LCM of 4 and 6?', 'a': '12', 'b': '10', 'c': '8', 'd': '20', 'ans': 'a'},
        {'q': 'What is the area of a rectangle with length 5 and width 3?', 'a': '8', 'b': '15', 'c': '16', 'd': '20', 'ans': 'b'},
        {'q': 'What is 1/2 + 1/3?', 'a': '2/5', 'b': '3/5', 'c': '5/6', 'd': '3/6', 'ans': 'c'},
        {'q': 'What is 20% of 50?', 'a': '10', 'b': '15', 'c': '20', 'd': '25', 'ans': 'a'}
    ],
    'Science': [
        {'q': 'What is the chemical formula for water?', 'a': 'H2O', 'b': 'CO2', 'c': 'O2', 'd': 'H2SO4', 'ans': 'a'},
        {'q': 'What is the smallest unit of life?', 'a': 'Atom', 'b': 'Molecule', 'c': 'Cell', 'd': 'Tissue', 'ans': 'c'},
        {'q': 'What planet is closest to the Sun?', 'a': 'Venus', 'b': 'Mercury', 'c': 'Earth', 'd': 'Mars', 'ans': 'b'},
        {'q': 'How many bones does a human have?', 'a': '186', 'b': '206', 'c': '256', 'd': '306', 'ans': 'b'},
        {'q': 'What gas do plants absorb to make food?', 'a': 'Oxygen', 'b': 'Nitrogen', 'c': 'Carbon dioxide', 'd': 'Hydrogen', 'ans': 'c'},
        {'q': 'What is the speed of light?', 'a': '300,000 km/s', 'b': '150,000 km/s', 'c': '450,000 km/s', 'd': '200,000 km/s', 'ans': 'a'},
        {'q': 'What is photosynthesis?', 'a': 'Breakdown of glucose', 'b': 'Production of food using sunlight', 'c': 'Respiration', 'd': 'Fermentation', 'ans': 'b'},
        {'q': 'What is the SI unit of force?', 'a': 'Newton', 'b': 'Joule', 'c': 'Pascal', 'd': 'Watt', 'ans': 'a'},
        {'q': 'What is DNA?', 'a': 'Protein', 'b': 'Genetic material', 'c': 'Carbohydrate', 'd': 'Lipid', 'ans': 'b'},
        {'q': 'How many chambers does a human heart have?', 'a': '2', 'b': '3', 'c': '4', 'd': '5', 'ans': 'c'}
    ],
    'SS': [
        {'q': 'Who is the current Prime Minister of India?', 'a': 'Narendra Modi', 'b': 'Rahul Gandhi', 'c': 'Amit Shah', 'd': 'Arvind Kejriwal', 'ans': 'a'},
        {'q': 'What is the capital of Tamil Nadu?', 'a': 'Coimbatore', 'b': 'Chennai', 'c': 'Madurai', 'd': 'Salem', 'ans': 'b'},
        {'q': 'In which year did India gain independence?', 'a': '1945', 'b': '1946', 'c': '1947', 'd': '1948', 'ans': 'c'},
        {'q': 'Who was the first President of India?', 'a': 'Jawaharlal Nehru', 'b': 'Dr. Rajendra Prasad', 'c': 'Sardar Vallabhbhai Patel', 'd': 'Subhas Chandra Bose', 'ans': 'b'},
        {'q': 'What is the national currency of India?', 'a': 'Dollar', 'b': 'Pound', 'c': 'Rupee', 'd': 'Yen', 'ans': 'c'},
        {'q': 'How many states are there in India?', 'a': '26', 'b': '28', 'c': '29', 'd': '30', 'ans': 'c'},
        {'q': 'What is the longest river in India?', 'a': 'Godavari', 'b': 'Brahmaputra', 'c': 'Ganges', 'd': 'Yamuna', 'ans': 'c'},
        {'q': 'Who was the first Chief Minister of Tamil Nadu?', 'a': 'M. Karunanidhi', 'b': 'C. Rajagopalachari', 'c': 'J. Jayalalithaa', 'd': 'Periyar', 'ans': 'b'},
        {'q': 'What is the national anthem of India?', 'a': 'Vande Mataram', 'b': 'Jana Gana Mana', 'c': 'Padma Sampadah', 'd': 'Hindustan Hamara', 'ans': 'b'},
        {'q': 'Which is the largest state by area in India?', 'a': 'Rajasthan', 'b': 'Maharashtra', 'c': 'Madhya Pradesh', 'd': 'Andhra Pradesh', 'ans': 'a'}
    ]
}

def get_auth_token():
    """Create test user and get auth token"""
    # Try to signup
    signup_response = requests.post(
        f"{API_BASE}/auth/signup",
        json={
            "email": "admin@mystudylife.com",
            "password": "Admin@123456",
            "full_name": "Admin User"
        }
    )
    
    # Try to login
    login_response = requests.post(
        f"{API_BASE}/auth/login",
        params={
            "email": "admin@mystudylife.com",
            "password": "Admin@123456"
        }
    )
    
    if login_response.status_code != 200:
        print(f"❌ Login failed: {login_response.text}")
        return None
    
    token = login_response.json().get("access_token")
    return token

def create_quiz(token, grade, subject, difficulty):
    """Create a quiz"""
    headers = {"Authorization": f"Bearer {token}"}
    
    quiz_data = {
        "title": f"{subject} - Grade {grade} - {difficulty}",
        "subject": subject,
        "grade": grade,
        "description": f"{subject} questions for Grade {grade} ({difficulty} level)",
        "total_questions": 10
    }
    
    response = requests.post(
        f"{API_BASE}/quiz/create",
        json=quiz_data,
        headers=headers
    )
    
    if response.status_code == 200:
        return response.json().get("id")
    else:
        print(f"❌ Failed to create quiz: {response.text}")
        return None

def add_question(token, quiz_id, question_data):
    """Add a question to a quiz"""
    headers = {"Authorization": f"Bearer {token}"}
    
    payload = {
        "quiz_id": quiz_id,
        "question_text": question_data['q'],
        "option_a": question_data['a'],
        "option_b": question_data['b'],
        "option_c": question_data['c'],
        "option_d": question_data['d'],
        "correct_answer": question_data['ans']
    }
    
    response = requests.post(
        f"{API_BASE}/quiz/add-question",
        json=payload,
        headers=headers
    )
    
    return response.status_code == 200

def main():
    print("🚀 Starting Quiz Seeder...")
    print("=" * 60)
    
    # Get auth token
    print("\n📝 Authenticating user...")
    token = get_auth_token()
    if not token:
        print("❌ Authentication failed!")
        return
    
    print(f"✅ Authenticated! Token: {token[:20]}...")
    
    # Create quizzes and add questions
    quiz_count = 0
    question_count = 0
    
    for grade in GRADES:
        for subject in SUBJECTS.keys():
            for difficulty in LEVELS:
                print(f"\n📚 Creating: {subject} - Grade {grade} - {difficulty}")
                
                # Create quiz
                quiz_id = create_quiz(token, grade, subject, difficulty)
                if not quiz_id:
                    continue
                
                quiz_count += 1
                print(f"   ✅ Quiz created (ID: {quiz_id})")
                
                # Add 10 questions
                questions = SAMPLE_QUESTIONS.get(subject, [])
                for idx, q in enumerate(questions[:10]):
                    if add_question(token, quiz_id, q):
                        question_count += 1
                        print(f"   ✅ Q{idx+1}: Added")
                    else:
                        print(f"   ❌ Q{idx+1}: Failed")
                
                time.sleep(0.2)  # Small delay to avoid rate limiting
    
    print("\n" + "=" * 60)
    print(f"\n✅ SEEDING COMPLETED!")
    print(f"   📊 Quizzes created: {quiz_count}")
    print(f"   ❓ Questions added: {question_count}")
    print(f"\n🎯 You can now:")
    print(f"   1. Visit: http://127.0.0.1:8080/pages/quiz_selection.html")
    print(f"   2. View API at: http://127.0.0.1:8000/docs")
    print(f"   3. Login with:")
    print(f"      Email: admin@mystudylife.com")
    print(f"      Password: Admin@123456")

if __name__ == "__main__":
    main()
