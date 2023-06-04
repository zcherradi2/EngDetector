from scipy.stats import beta
from scipy.special import erf
from math import log10
import random
import string


def letterDist(string,letter):
    lettersFrequency = {
    'a': 8.2,
    'b': 1.5,
    'c': 2.8,
    'd': 4.3,
    'e': 13.0,
    'f': 2.2,
    'g': 2.0,
    'h': 6.1,
    'i': 7.0,
    'j': 0.15,
    'k': 0.77,
    'l': 4.0,
    'm': 2.4,
    'n': 6.7,
    'o': 7.5,
    'p': 1.9,
    'q': 0.095,
    'r': 6.0,
    's': 6.3,
    't': 9.1,
    'u': 2.8,
    'v': 0.98,
    'w': 2.4,
    'x': 0.15,
    'y': 2.0,
    'z': 0.074}
    letter = letter.lower()
    k = len(string)
    if k ==0:
        k = 1
    p = lettersFrequency[letter]/100
    a = p*k
    b = (1-p)*k
    beta_dist = beta(a, b)
    x = round(string.count(letter)/k,4)
    V=(a*b)/((a+b)**2*(a+b+1))
    V= V**0.5
    res = beta_dist.cdf(x+V)-beta_dist.cdf(x-V)
    return abs(res)*k

def engDetecter(string):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    string = string.lower()
    string  = ''.join([char for char in string if char in chars])
    lst = []
    res = 0
    res0 = 0
    res2 = 1
    for ch in chars:
        lst.append(letterDist(string,ch))
        res += lst[-1]
        res0 += 1/lst[-1]
        res2 *= lst[-1]
    p = 0
    #print(res)
    #print(res0)
    #print(res2)
    #print('--')
    if(abs(log10(res2))<17):
        return False
    if(res0>10):
        return False
    return True
    if(res<25):
        p+= 0.25
    if p >= 0.74:
        return False
    return True



if __name__ =='__main__':
    isEnglish = ['i see red',
    'English is a widely spoken language, known for its global reach and influence. It has evolved over centuries, absorbing words from different cultures and languages. English plays a significant role in academia, business, and international communication. It enables people from diverse backgrounds to connect and understand each other. Learning English opens doors to various opportunities and enhances cultural understanding.',
    'The English language originated from the Germanic tribes in England and gradually developed into its modern form. It has a vast vocabulary, including words from Latin, French, and other languages. English grammar follows a relatively flexible structure, allowing for creativity and expression. As a lingua franca, English bridges gaps between different nations and facilitates trade, diplomacy, and cultural exchange.',
    'English has become the language of technology and innovation. Many scientific advancements and research papers are published in English, fostering collaboration and knowledge-sharing worldwide. Fluency in English can boost career prospects and open doors to international job markets. It enables individuals to access a vast range of literature, films, and music, expanding their horizons and enriching their cultural experiences.',
    'English is not just a means of communication but also a gateway to understanding diverse cultures. It helps build connections, break down barriers, and foster empathy. With its widespread usage and accessibility through the internet, English has become a language of global citizenship. It empowers individuals to engage with people from different backgrounds and contribute to a more interconnected world.',
    'English language skills are highly valued in education systems globally. Many universities and academic institutions offer programs taught in English. Proficiency in English can enhance educational opportunities, facilitate international student exchanges, and broaden intellectual horizons. It equips learners with the ability to access and understand a wealth of academic resources and research from around the world.',
    'English is a language that continues to evolve and adapt to the changing needs of society. It reflects the dynamic nature of human communication and the influence of cultural exchanges. From literature and poetry to films and music, English has made a significant impact on various art forms. It has the power to captivate and inspire people through its richness and expressive possibilities.',
    'English has a strong presence in the media and entertainment industry. Many popular books, movies, and songs are in English, reaching global audiences. English-language films dominate the international box office, enabling people from different countries to enjoy shared cinematic experiences. It has also influenced popular culture, shaping trends and expressions that resonate across borders.',
    'English proficiency can enhance travel experiences by enabling communication with people from different regions. Whether exploring a new city, navigating transportation systems, or engaging with locals, knowing English can facilitate interactions and make the journey smoother. It allows travelers to immerse themselves in new cultures, seek assistance when needed, and create meaningful connections along the way.',
    'English has a rich literary tradition that spans centuries. It has produced renowned authors, poets, and playwrights whose works have shaped the literary canon. From the plays of Shakespeare to the novels of Jane Austen and the poetry of William Wordsworth, English literature offers a vast array of literary masterpieces that continue to captivate readers and inspire generations.',
    'English has a significant influence on the world of business and commerce. Many multinational companies use English as their primary language for internal and external communication. Proficiency in English can enhance career prospects, as it is often a requirement for many job positions, particularly in international organizations. It facilitates collaboration, negotiation, and networking in the global marketplace.',    'English language proficiency opens doors to a world of literature, where classic novels, poetry, and plays come to life. From the works of Charles Dickens to the sonnets of William Shakespeare, English literature showcases the beauty of language and the power of storytelling, capturing the imagination of readers throughout history.',
    'English language skills enable effective communication in the digital era. With social media, online forums, and virtual communities, English acts as a universal language, connecting individuals from different corners of the world. It allows for the exchange of ideas, collaboration on global projects, and the sharing of diverse perspectives and experiences.',
    'English language learning provides access to a wealth of online resources. The internet is teeming with educational materials, tutorials, and courses in English, allowing individuals to acquire knowledge on a wide range of subjects. Online platforms provide interactive learning experiences, enabling self-paced language acquisition and personal growth opportunities.',
    'English proficiency fosters cultural appreciation and understanding. Through literature, films, and music, individuals can explore different cultures and gain insights into their traditions, values, and perspectives. English language skills facilitate cross-cultural interactions, enabling people to connect, respect differences, and cultivate global friendships based on shared interests and mutual respect.',
    'English language proficiency is an asset in the global job market. Many international companies seek employees with strong English skills to facilitate communication and collaboration across borders. English fluency can broaden career opportunities, enabling professionals to work in diverse industries, participate in international projects, and pursue global career paths.'
]

    uncoherent = []
    for _ in range(15):
        random_text = ''.join(random.choices(string.ascii_lowercase + ' ', k=20))
        uncoherent.append(random_text)
    random_text = ''.join(random.choices(string.ascii_lowercase + ' ', k=20))
    uncoherent.append(random_text)
    eng = 0
    notEng = 0


    for i in range(len(isEnglish)):
        if(engDetecter(isEnglish[i])):
            print('eng')
            eng += 1
        if(engDetecter(uncoherent[i])):
            notEng += 1
    eng /= len(isEnglish)
    notEng /= len(isEnglish)
    print('isenglish',eng)
    print('isNot english',notEng)