import pandas as pd
import random
import string

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# DATASET I

data = {
    'Text': [
        'Bagaimana kabarmu?', 'Where are you?', 'It is animal?', 'How do you do', 'If you like it',
        'Kurang ajar', 'Bagaimana mungkin', 'Kurasa tidak masalah untuk itu', 'Not bad at all',
        'Permisi, apakah disini rumahnya?', 'Cukup tau', 'So you have a mother?', 'Just for fun men',
        'Malas sekali rasanya', 'Aku juga mau', 'Maafkan aku', "How? that's impossible", 'Maybe next day',
        'Aku punya ini', 'That what i say', 'How much man?', 'No, dont get serious iil just kidding',
        'Kenapa hanya kau dan aku?', 'Its yours', 'Beraninya kau sialan', 'Mau bagaimana lagi kamu ini',
        'Its okay dont mind', 'I dunno how to repair this', 'Maybe the thief is her', 'One soup please!',
        'Jadi bagaimana ceritanya?', 'Kurasa tidak masalah untuk melakukannya', 'Kalau kamu mau aku juga mau',
        'One more time please!', 'I should go home now', 'Sampai jumpa lagi', 'Aku berhasil memenangkannya',
        'Uhh kau tidak apa apa?', 'Itu suara yang indah kawan', 'Will you be my friend?', 'Of course sir!',
        'Can i sit here boy?', 'Jadi bagaimana kemajuannya', 'Kurasa bos akan marah dengan ini', 'Can you take my water?',
        'Jangan dia,dia tidak bersalah', 'Sudah waktunya', 'I am just a postman', 'Excuse me,it is your package?',
        'How much it is?', 'Kamu ini sudah melampau!', 'Its time to shine', 'Can i get the rice mom?',
        'Burung apa tuh? burung puyuh', 'Tempat itu merah', 'Ya kau benar,itu terlihat masuk akal',
        'Bagaimana mungkin dia melakukan itu', "Nah i'd win!!!", 'Why you always late!', 'Mana buktinya? Ini buktinya',
    ],
    'Language': [
        'Indonesia', 'English', 'English', 'English', 'English', 'Indonesia', 'Indonesia', 'Indonesia',
        'English', 'Indonesia', 'Indonesia', 'English', 'English', 'Indonesia', 'Indonesia',
        'Indonesia', 'English', 'English', 'Indonesia', 'English', 'English', 'English', 'Indonesia', 'English',
        'Indonesia', 'Indonesia', 'English', 'English', 'English', 'English', 'Indonesia', 'Indonesia',
        'Indonesia', 'English', 'English', 'Indonesia', 'Indonesia', 'Indonesia', 'Indonesia', 'English', 'English',
        'English', 'Indonesia', 'Indonesia', 'English', 'Indonesia', 'Indonesia', 'English', 'English',
        'English', 'Indonesia', 'English', 'English', 'Indonesia', 'Indonesia', 'Indonesia', 'Indonesia',
        'English', 'English', 'Indonesia'
    ]
}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# DATASET II

# Indonesia text
data_id = [
    'Bagaimana kabarmu?', 'Dimana kamu?', 'Apakah itu binatang?', 'Apa kabar', 'Jika kamu suka',
    'Kurang ajar', 'Bagaimana mungkin', 'Kurasa tidak masalah', 'Tidak buruk sama sekali',
    'Permisi, apakah ini rumahmu?', 'Cukup tahu', 'Jadi kamu punya ibu?', 'Hanya untuk bersenang-senang',
    'Sangat malas rasanya', 'Aku juga mau', 'Maafkan aku', 'Bagaimana? itu tidak mungkin', 'Mungkin hari lain',
    'Aku punya ini', 'Itu yang kukatakan', 'Berapa harganya?', 'Jangan bercanda, aku hanya bercanda',
    'Kenapa hanya kamu dan aku?', 'Ini milikmu', 'Beraninya kau', 'Apa yang akan kamu lakukan?',
    'Tidak apa-apa, jangan dipikirkan', 'Aku tidak tahu cara memperbaikinya', 'Mungkin pencurinya dia',
    'Satu sup, tolong!', 'Jadi bagaimana ceritanya?', 'Kurasa tidak masalah melakukannya', 'Jika kamu mau, aku juga mau',
    'Satu kali lagi, tolong!', 'Aku harus pulang sekarang', 'Sampai jumpa lagi', 'Aku berhasil menang',
    'Kamu tidak apa-apa?', 'Itu suara yang indah', 'Maukah kamu menjadi temanku?', 'Tentu saja, pak!',
    'Bolehkah aku duduk di sini?', 'Jadi bagaimana kemajuannya?', 'Kurasa bos akan marah dengan ini', 'Bisa ambilkan airku?',
    'Jangan dia, dia tidak bersalah', 'Sudah waktunya', 'Aku hanya seorang tukang pos', 'Permisi, ini paketmu?',
    'Berapa harganya?', 'Kamu ini sudah melampaui batas!', 'Saatnya bersinar', 'Bolehkah aku mendapatkan nasi, ibu?',
    'Burung apa itu? burung puyuh', 'Tempat itu merah', 'Ya, kamu benar, itu masuk akal',
    'Bagaimana mungkin dia melakukan itu', "Nah aku menang!!!", 'Kenapa kamu selalu terlambat!', 'Mana buktinya? Ini buktinya'
]

# English text
data_en = [
    'How are you?', 'Where are you?', 'Is it an animal?', 'How do you do?', 'If you like it',
    'Damn', 'How is that possible?', 'I think it\'s okay', 'Not bad at all',
    'Excuse me, is this your house?', 'Just know', 'So you have a mother?', 'Just for fun',
    'Feeling very lazy', 'I want it too', 'Forgive me', 'How? that\'s impossible', 'Maybe another day',
    'I have this', 'That\'s what I said', 'How much is it?', 'No, don\'t get serious, just kidding',
    'Why is it just you and me?', 'It\'s yours', 'How dare you', 'What are you going to do?',
    'It\'s okay, don\'t mind it', 'I don\'t know how to fix it', 'Maybe the thief is her',
    'One soup, please!', 'So how\'s the story?', 'I think it\'s okay to do it', 'If you want, I want it too',
    'One more time, please!', 'I should go home now', 'See you again', 'I managed to win',
    'Are you okay?', 'That\'s a beautiful voice', 'Will you be my friend?', 'Of course, sir!',
    'Can I sit here?', 'So how\'s the progress?', 'I think the boss will be angry with this', 'Can you take my water?',
    'Not him, he\'s innocent', 'It\'s time', 'I am just a postman', 'Excuse me, is this your package?',
    'How much is it?', 'You have crossed the line!', 'It\'s time to shine', 'Can I get the rice, mom?',
    'What bird is that? quail', 'That place is red', 'Yes, you are right, it makes sense',
    'How could he do that?', "Nah, I win!!!", 'Why are you always late!', 'Where is the proof? Here it is'
]

data = data_id + data_en

# Labeling
labels = ['Indonesia'] * len(data_id) + ['English'] * len(data_en)

# Declare dataframe
df = pd.DataFrame({'Text': data, 'Language': labels})

# Randomize index
df = df.sample(frac=1).reset_index(drop=True)
df = pd.concat([df] * 5, ignore_index=True)

# df.to_csv('data_train.csv')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# DATASET III

# Generate random text function
def generate_text(language, length):
    words = {
        'Indonesia' : ['ini', 'adalah', 'contoh', 'kalimat', 'dalam', 'bagaimana', 'bisa', 'mungkin',
                        'betul', 'tujuan', 'perlu', 'cukup', 'masalah', 'bermain', 'juga'],
        'English' : ['this', 'is', 'example', 'text', 'in', 'how', 'can', 'possible', 'correct',
                     'objective', 'need', 'enough', 'trouble', 'playing', 'to']
    }
    sentence = ' '.join(random.choices(words[language], k=length))
    return sentence

# Add feature function
def add_features(text):
    features = {}
    features['Length'] = len(text)
    features['Word Count'] = len(text.split())
    features['Has Number'] = 'yes' if any(char.isdigit() for char in text) else 'no'
    features['Has Special Character'] = 'yes' if any(char in string.punctuation for char in text) else 'no'
    return features

# Generate dataset
data = []
languages = ['Indonesia', 'English']
for _ in range(250):
    for language in languages:
        text = generate_text(language, random.randint(5, 15))
        features = add_features(text)
        data.append({'Text': text, 'Language': language, **features})

# Create dataset
df = pd.DataFrame(data)

# Shuffle the DF
df = df.sample(frac=1).reset_index(drop=False)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# DATASET IV

# Dataset
data_4 = {
    'Text': [
        'Hari ini sangat cerah dan indah.',
        'I am feeling great today!',
        'Saya suka belajar bahasa pemrograman.',
        'Programming languages are fun to learn.',
        'Apakah kamu suka membaca buku?',
        'Do you like to read books?',
        'Aku akan pergi ke pasar nanti sore.',
        'I will go to the market this evening.',
        'Bisakah kamu membantu saya?',
        'Can you help me?',
        'Saya ingin membeli beberapa buah.',
        'I want to buy some fruits.',
        'Teman-teman saya sangat baik.',
        'My friends are very kind.',
        'Kucing saya sangat lucu.',
        'My cat is very cute.',
        'Dia bermain gitar dengan baik.',
        'He plays guitar well.',
        'Apakah kamu lapar?',
        'Are you hungry?',
        'Malam ini kita akan menonton film.',
        'Tonight we will watch a movie.',
        'Saya suka kopi hitam.',
        'I like black coffee.',
        'Kita akan pergi ke pantai besok.',
        'We will go to the beach tomorrow.',
        'Apa rencanamu akhir pekan ini?',
        'What are your plans for the weekend?',
        'Bunga-bunga di taman sangat cantik.',
        'The flowers in the garden are beautiful.',
        'Dia adalah seorang dokter.',
        'She is a doctor.',
        'Anjing itu menggonggong keras.',
        'The dog is barking loudly.',
        'Musik membuatku merasa tenang.',
        'Music makes me feel calm.',
        'Dia berlari sangat cepat.',
        'He runs very fast.',
        'Apakah kamu percaya pada cinta?',
        'Do you believe in love?',
        'Ini adalah sebuah buku yang bagus.',
        'This is a good book.',
        'Mereka sedang bermain sepak bola.',
        'They are playing soccer.',
        'Aku ingin pergi berlibur.',
        'I want to go on vacation.',
        'Apakah kamu pernah ke luar negeri?',
        'Have you ever been abroad?',
        'Hari ini saya belajar banyak.',
        'I learned a lot today.',
        'Kami akan makan malam bersama keluarga.',
        'We will have dinner with the family.',
        'Film ini sangat menarik.',
        'This movie is very interesting.',
        'Saya perlu tidur lebih awal malam ini.',
        'I need to sleep early tonight.',
        'Bisakah kamu berbicara bahasa Inggris?',
        'Can you speak English?',
        'Dia sedang membaca koran.',
        'He is reading a newspaper.',
        'Apakah kamu punya waktu luang besok?',
        'Do you have free time tomorrow?',
        'Saya harus pergi ke kantor sekarang.',
        'I have to go to the office now.',
        'Ini adalah tempat yang indah.',
        'This is a beautiful place.',
        'Saya senang bertemu denganmu.',
        'I am happy to meet you.',
        'Kita akan bertemu lagi besok.',
        'We will meet again tomorrow.',
        'Apakah kamu percaya pada takdir?',
        'Do you believe in destiny?',
        'Dia menyukai seni dan musik.',
        'She likes art and music.',
        'Pekerjaan ini sangat menantang.',
        'This job is very challenging.',
        'Saya ingin menjadi seorang insinyur.',
        'I want to be an engineer.',
        'Buku ini sangat informatif.',
        'This book is very informative.'
    ],
    'Language': [
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English',
        'Indonesia', 'English'
    ]
}

df = pd.DataFrame(data_4)

# Shuffle index
df = df.sample(frac=1).reset_index(drop=True)

# df.to_csv('data_test_3.csv')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# DATASET V

data_5 = {
    'Text': [
            'Aku', 'We', 'Biji', 'Purple', 'Semangka', 'Spesificly', 'Kuliah', 'Flying', 'Tidur',
             'Personal', 'Agustus', 'Consider', 'Malam', 'Profession', 'Mangga', 'Red', 'Panci', 'Awake',
             'Membangun', 'Soup', 'Undangan', 'Promise', 'Payung', 'Sword', 'Waktu', 'Meat', 'Upacara',
             'Lawyer', 'Minuman', 'Giant', 'Kucing', 'Road', 'Rem', 'Hair', 'Nampak', 'Trust',
             'Jiwa', 'Coffee', 'Dokter', 'Architect', 'Ikan', 'Rest', 'Pulang', 'Come', 'Sepertinya',
             'Lamp', 'Listrik', 'Buffalo', 'Tertawa', 'Meat', 'Berpikir', 'Closed', 'Lulusan', 'Meeting',
             'Pancingan', 'Mark', 'Papan', 'Knife', 'Palu', 'Services', 'Meja', 'From', 'Berputar',
             'Toast', 'Babi', 'Waterfall', 'Hijau', 'Queen', 'Rumput', 'Expensive', 'Kurang', 'King',
             'Ternak', 'Butterfly', 'Mentega', 'Corn', 'Bayi', 'Third', 'Sendiri', 'Number', 'Pribadi',
             'Always', 'Timah', 'Coal', 'Jubah', 'Fox', 'Warung', 'Present', 'Kelahiran', 'Againts'
             ],

    
    'Language': [
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia',
        'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English',
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia',
        'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English',
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia',
        'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English',
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia',
        'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English',
        'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia',
        'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English', 'Indonesia', 'English'
        ]
}

df = pd.DataFrame(data_5)

# Shuffle the index
df = df.sample(frac=1).reset_index(drop=True)

# df.to_csv('data_test_4.csv')
