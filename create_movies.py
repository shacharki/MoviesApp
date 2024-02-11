from app import db, Movie, app 

movies_data = [
    {
        'title': "The Lion King",
        'description': "A young lion prince flees his kingdom only to learn the true meaning of responsibility and bravery.",
        'director': "Roger Allers, Rob Minkoff",
        'actors': "Matthew Broderick, Jeremy Irons, James Earl Jones",
        'year': 1994,
        'poster_url': "https://lumiere-a.akamaihd.net/v1/images/image_fc5cb742.jpeg?region=0%2C0%2C540%2C810"
    },
    {
        'title': "Toy Story",
        'description': "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
        'director': "John Lasseter",
        'actors': "Tom Hanks, Tim Allen, Don Rickles",
        'year': 1995,
        'poster_url': "https://lumiere-a.akamaihd.net/v1/images/p_toystory_19639_424d94a0.jpeg"
    },
    {
        'title': "Finding Nemo",
        'description': "After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.",
        'director': "Andrew Stanton, Lee Unkrich",
        'actors': "Albert Brooks, Ellen DeGeneres, Alexander Gould",
        'year': 2003,
        'poster_url': "https://lumiere-a.akamaihd.net/v1/images/p_findingnemo_19752_05271d3f.jpeg?region=0%2C0%2C540%2C810"
    },
    {
        'title': "Shrek",
        'description': "A mean lord exiles fairytale creatures to the swamp of a grumpy ogre, who must go on a quest and rescue a princess for the lord in order to get his land back.",
        'director': "Andrew Adamson, Vicky Jenson",
        'actors': "Mike Myers, Eddie Murphy, Cameron Diaz",
        'year': 2001,
        'poster_url': "https://m.media-amazon.com/images/M/MV5BOGZhM2FhNTItODAzNi00YjA0LWEyN2UtNjJlYWQzYzU1MDg5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"
    },
    {
        'title': "Frozen",
        'description': "When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister Anna teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.",
        'director': "Chris Buck, Jennifer Lee",
        'actors': "Kristen Bell, Idina Menzel, Jonathan Groff",
        'year': 2013,
        'poster_url': "https://lumiere-a.akamaihd.net/v1/images/p_frozen_18373_3131259c.jpeg?region=0%2C0%2C540%2C810"
    },
    {
        'title': "Harry Potter and the Sorcerer's Stone",
        'description': "An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.",
        'director': "Chris Columbus",
        'actors': "Daniel Radcliffe, Rupert Grint, Emma Watson",
        'year': 2001,
        'poster_url': "https://m.media-amazon.com/images/I/91wKDODkgWL._AC_UF1000,1000_QL80_.jpg"
    },
    {
        'title': "The Incredibles",
        'description': "A family of undercover superheroes, while trying to live the quiet suburban life, are forced into action to save the world.",
        'director': "Brad Bird",
        'actors': "Craig T. Nelson, Samuel L. Jackson, Holly Hunter",
        'year': 2004,
        'poster_url': "https://m.media-amazon.com/images/I/716RrNAAMQL._AC_UF894,1000_QL80_.jpg"
    },
    {
        'title': "The Little Mermaid",
        'description': "A mermaid princess makes a Faustian bargain in an attempt to become human and win a prince's love.",
        'director': "Ron Clements, John Musker",
        'actors': "Jodi Benson, Samuel E. Wright, Rene Auberjonois",
        'year': 1989,
        'poster_url': "https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p11958_p_v13_ab.jpg"
    },
    {
        'title': "Aladdin",
        'description': "A kind-hearted street urchin and a power-hungry Grand Vizier vie for a magic lamp that has the power to make their deepest wishes come true.",
        'director': "Ron Clements, John Musker",
        'actors': "Scott Weinger, Robin Williams, Linda Larkin",
        'year': 1992,
        'poster_url': "https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9780794443511/disney-aladdin-9780794443511_hr.jpg"
    },
    {
        'title': "The Jungle Book",
        'description': "Bagheera the Panther and Baloo the Bear have a difficult time trying to convince a boy to leave the jungle for human civilization.",
        'director': "Wolfgang Reitherman",
        'actors': "Phil Harris, Sebastian Cabot, Louis Prima",
        'year': 1967,
        'poster_url': "https://lumiere-a.akamaihd.net/v1/images/p_thejunglebook1967_19869_f10b5016.jpeg"
    },
        {
        'title': "Moana",
        'description': "In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches Moana's island, she answers the Ocean's call to seek out the Demigod to set things right.",
        'director': "Ron Clements, John Musker",
        'actors': "Auli'i Cravalho, Dwayne Johnson, Rachel House",
        'year': 2016,
        'poster_url': "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg"
    },
    {
        'title': "Coco",
        'description': "Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.",
        'director': "Lee Unkrich, Adrian Molina",
        'actors': "Anthony Gonzalez, Gael García Bernal, Benjamin Bratt",
        'year': 2017,
        'poster_url': "https://m.media-amazon.com/images/M/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGdeQXVyODIxMzk5NjA@._V1_.jpg"
    },
    {
        'title': "Beauty and the Beast",
        'description': "A selfish Prince is cursed to become a monster for the rest of his life, unless he learns to fall in love with a beautiful young woman he keeps prisoner.",
        'director': "Gary Trousdale, Kirk Wise",
        'actors': "Paige O'Hara, Robby Benson, Richard White",
        'year': 1991,
        'poster_url': "https://m.media-amazon.com/images/M/MV5BMTUwNjUxMTM4NV5BMl5BanBnXkFtZTgwODExMDQzMTI@._V1_.jpg"
    },
    {
        'title': "Peter Pan",
        'description': "Wendy and her brothers are whisked away to the magical world of Neverland with the hero of their stories, Peter Pan.",
        'director': "Clyde Geronimi, Wilfred Jackson",
        'actors': "Bobby Driscoll, Kathryn Beaumont, Hans Conried",
        'year': 1953,
        'poster_url': "https://m.media-amazon.com/images/M/MV5BMzIwMzUyYTUtMjQ3My00NDc3LWIyZjQtOGUzNDJmNTFlNWUxXkEyXkFqcGdeQXVyMjA0MDQ0Mjc@._V1_.jpg"
    },
    {
        'title': "The Sound of Music",
        'description': "A woman leaves an Austrian convent to become a governess to the children of a Naval officer widower.",
        'director': "Robert Wise",
        'actors': "Julie Andrews, Christopher Plummer, Eleanor Parker",
        'year': 1965,
        'poster_url': "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg"
    },
    {
        'title': "The Wizard of Oz",
        'description': "Dorothy Gale is swept away from a farm in Kansas to a magical land of Oz in a tornado and embarks on a quest with her new friends to see the Wizard who can help her return home to Kansas and help her friends as well.",
        'director': "Victor Fleming",
        'actors': "Judy Garland, Frank Morgan, Ray Bolger",
        'year': 1939,
        'poster_url': "https://upload.wikimedia.org/wikipedia/en/1/1d/Wiz_of_oz_london.jpg"
    },
    {
    'title': "Sleeping Beauty",
    'description': "After being snubbed by the royal family, a malevolent fairy places a curse on a princess which only a prince can break, along with the help of three good fairies.",
    'director': "Clyde Geronimi",
    'actors': "Mary Costa, Bill Shirley, Eleanor Audley",
    'year': 1959,
    'poster_url': "https://lumiere-a.akamaihd.net/v1/images/p_sleepingbeauty_20525_0cc9243a.jpeg"
},
{
    'title': "Bambi",
    'description': "The story of a young deer growing up in the forest after his mother is shot by hunters.",
    'director': "James Algar, Samuel Armstrong",
    'actors': "Hardie Albright, Stan Alexander, Bobette Audrey",
    'year': 1942,
    'poster_url': "https://lumiere-a.akamaihd.net/v1/images/p_bambi_19754_990e0e5a.jpeg"
},
{
    'title': "The Princess Bride",
    'description': "While home sick in bed, a young boy's grandfather reads him the story of a farmboy-turned-pirate who encounters numerous obstacles, enemies and allies in his quest to be reunited with his true love.",
    'director': "Rob Reiner",
    'actors': "Cary Elwes, Mandy Patinkin, Robin Wright",
    'year': 1987,
    'poster_url': "https://m.media-amazon.com/images/I/7116Aa2ZkRL._AC_UF894,1000_QL80_.jpg"
},
{
    'title': "Willy Wonka & the Chocolate Factory",
    'description': "A poor but hopeful boy seeks one of the five coveted golden tickets that will send him on a tour of Willy Wonka's mysterious chocolate factory.",
    'director': "Mel Stuart",
    'actors': "Gene Wilder, Jack Albertson, Peter Ostrum",
    'year': 1971,
    'poster_url': "https://play-lh.googleusercontent.com/nJviG_JqwxnPJlIT9yA5cImb-dV3jXLpWlU-kk5VKYEdTFtonrui6UENnyqqkM6yMuav8WhF9U8QCiLa2mI"
}
]



with app.app_context():
    db.create_all()  
    for movie_data in movies_data:
        movie = Movie(**movie_data)  
        db.session.add(movie)  
    db.session.commit()  



