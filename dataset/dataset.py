import pandas as pd
import random

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

# DATASET II

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

# Contoh kalimat bahasa Inggris
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

df = pd.DataFrame({'Text': data})
df = df.sample(frac=1).reset_index(drop=True)
df = pd.concat([df] * 5, ignore_index=True)