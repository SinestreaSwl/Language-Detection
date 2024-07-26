import pandas as pd

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

df = pd.DataFrame(data)
df.to_csv('data_train.csv')