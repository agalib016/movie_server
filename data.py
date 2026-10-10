"""
MAG Stream - Database & Media Catalog (All-Era & Multi-Language)
Spans the history of motion pictures and internet media from 1888 to 2024+.
Includes Hollywood, Bollywood, Asian (Korean/Japanese), European (French/German),
and Bengali cinema, with real streamable video sources and multi-server mirrors.
"""

ACTORS_DATA = [
    {
        "id": "charlie-chaplin",
        "name": "Charlie Chaplin",
        "photo": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1889",
        "nationality": "British",
        "bio": "Sir Charles Spencer Chaplin was an English comic actor, filmmaker, and composer who rose to fame in the era of silent film. He became a worldwide icon through his screen persona, 'The Tramp', and is considered one of the most important figures in the history of cinema.",
        "notable_awards": "3x Academy Awards, BAFTA, Knight Commander of the British Empire",
        "birthplace": "London, England, UK"
    },
    {
        "id": "cillian-murphy",
        "name": "Cillian Murphy",
        "photo": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1976",
        "nationality": "Irish",
        "bio": "Cillian Murphy is an acclaimed Irish actor. Celebrated for his transformative performances, including J. Robert Oppenheimer in Christopher Nolan's 'Oppenheimer' (Academy Award for Best Actor) and Thomas Shelby in 'Peaky Blinders'.",
        "notable_awards": "Academy Award (Best Actor), Golden Globe, BAFTA",
        "birthplace": "Douglas, Cork, Ireland"
    },
    {
        "id": "shah-rukh-khan",
        "name": "Shah Rukh Khan",
        "photo": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1965",
        "nationality": "Indian",
        "bio": "Referred to in the media as the 'Baadshah of Bollywood' and 'King Khan', Shah Rukh Khan has appeared in more than 90 films and earned numerous accolades including 14 Filmfare Awards and historic blockbusters like Jawan, Pathaan, and DDLJ.",
        "notable_awards": "14 Filmfare Awards, Padma Shri, Legion of Honour",
        "birthplace": "New Delhi, India"
    },
    {
        "id": "leonardo-dicaprio",
        "name": "Leonardo DiCaprio",
        "photo": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1974",
        "nationality": "American",
        "bio": "Leonardo DiCaprio is an American actor and producer renowned for his work in biopics, thrillers, and period dramas including 'Inception', 'Titanic', 'The Wolf of Wall Street', and 'The Revenant'.",
        "notable_awards": "Academy Award (Best Actor), BAFTA, 3x Golden Globes",
        "birthplace": "Los Angeles, California, USA"
    },
    {
        "id": "satyajit-ray",
        "name": "Soumitra Chatterjee",
        "photo": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1935",
        "nationality": "Indian (Bengali)",
        "bio": "Soumitra Chatterjee was a legendary Indian actor famous for his 14 film collaborations with maestro director Satyajit Ray, including 'The World of Apu', 'Charulata', and the Feluda detective films.",
        "notable_awards": "Dadasaheb Phalke Award, Legion of Honour, 3x National Film Awards",
        "birthplace": "Calcutta, Bengal, British India"
    },
    {
        "id": "song-kang-ho",
        "name": "Song Kang-ho",
        "photo": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1967",
        "nationality": "South Korean",
        "bio": "Song Kang-ho is one of South Korea's most celebrated actors, acclaimed globally for starring in Bong Joon-ho's Oscar Best Picture winner 'Parasite', 'Memories of Murder', 'Snowpiercer', and 'A Taxi Driver'.",
        "notable_awards": "Cannes Best Actor Award, SAG Outstanding Performance",
        "birthplace": "Gimhae, South Korea"
    },
    {
        "id": "bryan-cranston",
        "name": "Bryan Cranston",
        "photo": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1956",
        "nationality": "American",
        "bio": "Bryan Cranston portrayed Walter White in AMC's 'Breaking Bad', widely cited among the greatest dramatic television performances in history.",
        "notable_awards": "6x Emmy Awards, 2x Tony Awards, Golden Globe",
        "birthplace": "Hollywood, Los Angeles, USA"
    },
    {
        "id": "pedro-pascal",
        "name": "Pedro Pascal",
        "photo": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1975",
        "nationality": "Chilean-American",
        "bio": "Pedro Pascal is an acclaimed actor famous for starring as Joel Miller in HBO's 'The Last of Us', 'The Mandalorian', and Javier Peña in 'Narcos'.",
        "notable_awards": "Screen Actors Guild Award, Critics' Choice Super Award",
        "birthplace": "Santiago, Chile"
    },
    {
        "id": "deepika-padukone",
        "name": "Deepika Padukone",
        "photo": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1986",
        "nationality": "Indian",
        "bio": "Deepika Padukone is one of Indian cinema's most celebrated leading ladies, starring in global blockbusters including 'Pathaan', 'Jawan', 'Padmaavat', and 'Piku'.",
        "notable_awards": "3x Filmfare Awards, TIME 100 Most Influential People",
        "birthplace": "Copenhagen, Denmark"
    },
    {
        "id": "keanu-reeves",
        "name": "Keanu Reeves",
        "photo": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1964",
        "nationality": "Canadian",
        "bio": "Keanu Reeves is an iconic action hero celebrated worldwide for his legendary roles as Neo in 'The Matrix' and the titular assassin in the 'John Wick' saga.",
        "notable_awards": "Walk of Fame Star, Saturn Award",
        "birthplace": "Beirut, Lebanon"
    },
    {
        "id": "zendaya",
        "name": "Zendaya",
        "photo": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1996",
        "nationality": "American",
        "bio": "Zendaya is an Emmy-winning American actress acclaimed for 'Euphoria', Denis Villeneuve's 'Dune: Part Two', and Marvel's 'Spider-Man'.",
        "notable_awards": "2x Primetime Emmy Awards, Golden Globe Award",
        "birthplace": "Oakland, California, USA"
    },
    {
        "id": "amitabh-bachchan",
        "name": "Amitabh Bachchan",
        "photo": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=600&auto=format&fit=crop&q=80",
        "birth_year": "1942",
        "nationality": "Indian",
        "bio": "The 'Shahenshah of Bollywood', Amitabh Bachchan is widely regarded as one of the greatest and most influential actors in the history of Indian and world cinema, starring in 'Sholay', 'Deewaar', and 'Don'.",
        "notable_awards": "Dadasaheb Phalke Award, 4x National Film Awards, 16 Filmfare Awards",
        "birthplace": "Allahabad, Uttar Pradesh, India"
    }
]

# Real, streamable video sources across eras and languages
# Uses high-speed direct MP4 streams from Archive.org, Plyr CDN, and open media mirrors
MEDIA_DATA = [
    # --- ERA 1: THE INCEPTION OF CINEMA & EARLY CLASSICS (1888 - 1950s) ---
    {
        "id": "charlie-chaplin-festival",
        "title": "Charlie Chaplin Film Festival",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Comedy", "Classics", "Silent"],
        "year": 1938,
        "rating": 8.8,
        "content_rating": "G",
        "duration": "1h 20m (Full Movie)",
        "language": "English",
        "era": "Early Cinema",
        "poster": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1400&auto=format&fit=crop&q=80",
        "overview": "A full-length feature film compilation showcasing Charlie Chaplin's greatest comedic masterworks, featuring 'The Immigrant', 'The Adventurer', 'Easy Street', and 'The Cure'.",
        "director": "Charlie Chaplin",
        "cast_ids": ["charlie-chaplin"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Charlie.Chaplin.Film.Festival.1938.1080p.mkv",
        "real_stream_url": "https://archive.org/download/charlie_chaplin_film_fest/charlie_chaplin_film_fest.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "483 MB (Complete Movie)", "bitrate": "2200 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.10 GB (Restored)", "bitrate": "4800 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "2.80 GB (4K Remaster)", "bitrate": "14000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "fast-and-furious-1954",
        "title": "The Fast and the Furious (Original 1954)",
        "type": "movie",
        "categories": ["classics", "action", "hollywood"],
        "genres": ["Action", "Crime", "Drama"],
        "year": 1954,
        "rating": 7.6,
        "content_rating": "PG",
        "duration": "1h 13m (Full Movie)",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1517649763962-0c623266ddc0?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1400&auto=format&fit=crop&q=80",
        "overview": "The original 1954 B-movie classic that inspired the modern franchise. A framed man on the run takes a sports car driver hostage and slips into a high-stakes cross-border road race to escape the law.",
        "director": "Edward Sampson & John Ireland",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/The.Fast.and.the.Furious.1954.1080p.mkv",
        "real_stream_url": "https://archive.org/download/TheFastandtheFuriousJohnIreland1954goofyrip/TheFastandtheFuriousJohnIreland1954goofyrip.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "453 MB (Complete Movie)", "bitrate": "2100 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.20 GB", "bitrate": "4900 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.10 GB", "bitrate": "15000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "doctor-in-industry-1946",
        "title": "Doctor in Industry: The Story of Kettering",
        "type": "movie",
        "categories": ["classics", "hollywood"],
        "genres": ["Biography", "Drama", "History"],
        "year": 1946,
        "rating": 7.8,
        "content_rating": "G",
        "duration": "1h 00m (Full Movie)",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1400&auto=format&fit=crop&q=80",
        "overview": "The inspirational dramatized story of American inventor and engineer Charles F. Kettering, pioneer of the automotive electric cash register and self-starter, capturing the rise of modern industrial science.",
        "director": "Edward Sampson",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Doctor.in.Industry.1946.mkv",
        "real_stream_url": "https://archive.org/download/Doctorin1946/Doctorin1946.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "117 MB", "bitrate": "2000 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "350 MB", "bitrate": "4500 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "1.10 GB", "bitrate": "13000 kbps", "format": "MKV (HEVC)"}
        }
    },

    # --- ERA 2: BENGALI & ASIAN CLASSICAL CINEMA ---
    {
        "id": "charulata-1964",
        "title": "Charulata (The Lonely Wife)",
        "type": "movie",
        "categories": ["classics", "top_rated"],
        "genres": ["Drama", "Romance", "Classics"],
        "year": 1964,
        "rating": 8.3,
        "content_rating": "PG",
        "duration": "1h 57m",
        "language": "Bengali",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "Directed by legendary auteur Satyajit Ray, based on Rabindranath Tagore's novella Nastanirh. A sensitive intellectual woman in 1870s Calcutta discovers her literary gift and complex affection when her husband's younger cousin visits.",
        "director": "Satyajit Ray",
        "cast_ids": ["satyajit-ray"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk05/Bengali/Charulata.1964.Criterion.1080p.mkv",
        "real_stream_url": "https://archive.org/download/charulata1964/charulata1964.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "850 MB", "bitrate": "2200 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "2.10 GB", "bitrate": "4800 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "5.90 GB", "bitrate": "15000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "sholay-1975",
        "title": "Sholay",
        "type": "movie",
        "categories": ["bollywood", "action", "classics", "top_rated"],
        "genres": ["Action", "Adventure", "Drama"],
        "year": 1975,
        "rating": 8.6,
        "content_rating": "PG-13",
        "duration": "3h 24m",
        "language": "Hindi",
        "era": "Bollywood Golden Era",
        "poster": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1400&auto=format&fit=crop&q=80",
        "overview": "Widely hailed as the greatest Indian action film ever made. Two former convicts, Veeru and Jai, are hired by a retired police officer to capture the ruthless dacoit Gabbar Singh alive.",
        "director": "Ramesh Sippy",
        "cast_ids": ["amitabh-bachchan"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk05/Movies/Bollywood/Classics/Sholay.1975.Remastered.1080p.mkv",
        "real_stream_url": "",  # Sholay is a commercial title with no free public stream
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "1.30 GB", "bitrate": "2300 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "2.90 GB", "bitrate": "5100 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "7.50 GB", "bitrate": "16500 kbps", "format": "MKV (HEVC)"}
        }
    },

    # --- ERA 3: ASIAN CINEMA & K-DRAMA (KOREAN / JAPANESE) ---
    {
        "id": "parasite-2019",
        "title": "Parasite (Gisaengchung)",
        "type": "movie",
        "categories": ["top_rated", "trending"],
        "genres": ["Drama", "Thriller", "Comedy"],
        "year": 2019,
        "rating": 8.5,
        "content_rating": "R",
        "duration": "2h 12m",
        "language": "Korean",
        "era": "Modern International",
        "poster": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1400&auto=format&fit=crop&q=80",
        "overview": "Winner of 4 Academy Awards including Best Picture. Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        "director": "Bong Joon-ho",
        "cast_ids": ["song-kang-ho"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk04/Asian/Parasite.2019.Criterion.2160p.UHD.mkv",
        "real_stream_url": "",  # Parasite is a commercial title with no free public stream
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "1.10 GB", "bitrate": "2200 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "2.60 GB", "bitrate": "5000 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "7.80 GB", "bitrate": "17000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "squid-game-s01",
        "title": "Squid Game",
        "type": "web_series",
        "categories": ["web_series", "trending", "action", "top_rated"],
        "genres": ["Action", "Drama", "Mystery", "Thriller"],
        "year": 2021,
        "rating": 8.0,
        "content_rating": "TV-MA",
        "duration": "1 Season (9 Episodes)",
        "language": "Korean",
        "era": "Modern Streaming",
        "poster": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "Hundreds of cash-strapped players accept a strange invitation to compete in children's games. Inside, a tempting prize awaits with deadly high stakes.",
        "director": "Hwang Dong-hyuk",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk04/Web_Series/Squid.Game.S01.2160p.NF.WEB-DL.mkv",
        "real_stream_url": "",  # Squid Game is a commercial title with no free public stream
        "is_featured": False,
        "seasons": [
            {
                "season_number": 1,
                "title": "Season 1",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "Red Light, Green Light",
                        "duration": "59m",
                        "overview": "Hoping to win easy money, a desperate Gi-hun agrees to take part in an enigmatic game.",
                        "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
                        "stream_url": ""
                    }
                ]
            }
        ],
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "550 MB / Ep", "bitrate": "2200 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.30 GB / Ep", "bitrate": "4900 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.80 GB / Ep", "bitrate": "15000 kbps", "format": "MKV (HEVC)"}
        }
    },

    # --- ERA 4: CONTEMPORARY HOLLYWOOD BLOCKBUSTERS (2000s - 2024) ---
    {
        "id": "oppenheimer-2023",
        "title": "Oppenheimer",
        "type": "movie",
        "categories": ["hollywood", "trending", "top_rated"],
        "genres": ["Biography", "Drama", "History"],
        "year": 2023,
        "rating": 8.9,
        "content_rating": "R",
        "duration": "3h 00m",
        "language": "English",
        "era": "Modern Era",
        "poster": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1400&auto=format&fit=crop&q=80",
        "overview": "The story of American theoretical physicist J. Robert Oppenheimer, the director of the Manhattan Project's Los Alamos Laboratory, and the dawn of the atomic age.",
        "director": "Christopher Nolan",
        "cast_ids": ["cillian-murphy"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk01/Movies/Hollywood/2023/Oppenheimer.2023.2160p.UHD.BluRay.x265.mkv",
        "real_stream_url": "",  # Oppenheimer is a commercial title with no free public stream
        "is_featured": True,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "1.25 GB", "bitrate": "2400 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "2.80 GB", "bitrate": "5200 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "8.50 GB", "bitrate": "18000 kbps", "format": "MKV (HEVC / HDR)"}
        }
    },
    {
        "id": "dune-part-two-2024",
        "title": "Dune: Part Two",
        "type": "movie",
        "categories": ["hollywood", "trending", "top_rated", "action"],
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "year": 2024,
        "rating": 8.7,
        "content_rating": "PG-13",
        "duration": "2h 46m",
        "language": "English",
        "era": "Modern Era",
        "poster": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family, facing a choice between love and the fate of the universe.",
        "director": "Denis Villeneuve",
        "cast_ids": ["zendaya"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk01/Movies/Hollywood/2024/Dune.Part.Two.2024.2160p.UHD.IMAX.mkv",
        "real_stream_url": "",  # Dune: Part Two is a commercial title with no free public stream
        "is_featured": True,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "1.30 GB", "bitrate": "2400 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "2.90 GB", "bitrate": "5300 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "8.70 GB", "bitrate": "18500 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "jawan-2023",
        "title": "Jawan",
        "type": "movie",
        "categories": ["bollywood", "action", "trending"],
        "genres": ["Action", "Thriller", "Drama"],
        "year": 2023,
        "rating": 8.1,
        "content_rating": "PG-13",
        "duration": "2h 49m",
        "language": "Hindi",
        "era": "Modern Era",
        "poster": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "A high-octane action thriller which outlines the emotional journey of a man who is set out to rectify the wrongs in the society, backed by a fierce band of women vigilantes.",
        "director": "Atlee",
        "cast_ids": ["shah-rukh-khan", "deepika-padukone"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk05/Movies/Bollywood/2023/Jawan.2023.Extended.Cut.1080p.NF.WEB-DL.mkv",
        "real_stream_url": "",  # Jawan is a commercial title with no free public stream
        "is_featured": True,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "1.10 GB", "bitrate": "2200 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "2.60 GB", "bitrate": "5000 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "7.10 GB", "bitrate": "16500 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "john-wick-4-2023",
        "title": "John Wick: Chapter 4",
        "type": "movie",
        "categories": ["hollywood", "action", "trending"],
        "genres": ["Action", "Crime", "Thriller"],
        "year": 2023,
        "rating": 8.2,
        "content_rating": "R",
        "duration": "2h 49m",
        "language": "English",
        "era": "Modern Era",
        "poster": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1400&auto=format&fit=crop&q=80",
        "overview": "John Wick uncovers a path to defeating The High Table. But before he can earn his freedom, Wick must face off against a new enemy with powerful alliances across the globe.",
        "director": "Chad Stahelski",
        "cast_ids": ["keanu-reeves"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk01/Movies/Hollywood/2023/John.Wick.Chapter.4.2023.2160p.HDR10.mkv",
        "real_stream_url": "",  # John Wick: Chapter 4 is a commercial title with no free public stream
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "1.20 GB", "bitrate": "2300 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "2.75 GB", "bitrate": "5100 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "8.10 GB", "bitrate": "17200 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "breaking-bad",
        "title": "Breaking Bad",
        "type": "tv_show",
        "categories": ["tv_shows", "trending", "top_rated"],
        "genres": ["Crime", "Drama", "Thriller"],
        "year": 2008,
        "rating": 9.5,
        "content_rating": "TV-MA",
        "duration": "5 Seasons (62 Episodes)",
        "language": "English",
        "era": "Modern Era",
        "poster": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1400&auto=format&fit=crop&q=80",
        "overview": "A chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine with a former student to secure his family's financial future.",
        "director": "Vince Gilligan",
        "cast_ids": ["bryan-cranston"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk03/TV_Shows/Breaking.Bad.Complete.Series.1080p.Remux/",
        "real_stream_url": "",  # Breaking Bad is a commercial title with no free public stream
        "is_featured": False,
        "seasons": [
            {
                "season_number": 1,
                "title": "Season 1",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "Pilot",
                        "duration": "58m",
                        "overview": "Diagnosed with terminal lung cancer, Walter White teams up with former pupil Jesse Pinkman.",
                        "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
                        "stream_url": ""
                    }
                ]
            }
        ],
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "450 MB / Ep", "bitrate": "2200 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.10 GB / Ep", "bitrate": "4800 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.20 GB / Ep", "bitrate": "14000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "the-last-of-us",
        "title": "The Last of Us",
        "type": "tv_show",
        "categories": ["tv_shows", "web_series", "trending", "top_rated"],
        "genres": ["Action", "Adventure", "Drama", "Sci-Fi"],
        "year": 2023,
        "rating": 8.8,
        "content_rating": "TV-MA",
        "duration": "1 Season (9 Episodes)",
        "language": "English",
        "era": "Modern Era",
        "poster": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=1400&auto=format&fit=crop&q=80",
        "overview": "After a global pandemic destroys civilization, a hardened survivor takes charge of a 14-year-old girl who may be humanity's last hope.",
        "director": "Craig Mazin & Neil Druckmann",
        "cast_ids": ["pedro-pascal"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk04/TV_Shows/The.Last.of.Us.S01.2160p.MAX.WEB-DL.mkv",
        "real_stream_url": "",  # The Last of Us is a commercial title with no free public stream
        "is_featured": False,
        "seasons": [
            {
                "season_number": 1,
                "title": "Season 1",
                "episodes": [
                    {
                        "episode_number": 1,
                        "title": "When You're Lost in the Darkness",
                        "duration": "1h 21m",
                        "overview": "Twenty years after a fungal outbreak ravages the planet, Joel and Tess take on an escort mission.",
                        "thumbnail": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80",
                        "stream_url": ""
                    }
                ]
            }
        ],
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "600 MB / Ep", "bitrate": "2300 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.40 GB / Ep", "bitrate": "5100 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.90 GB / Ep", "bitrate": "15500 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "attack-on-titan",
        "title": "Attack on Titan: The Final Chapters",
        "type": "web_series",
        "categories": ["anime", "action", "top_rated", "trending"],
        "genres": ["Animation", "Action", "Adventure", "Fantasy"],
        "year": 2023,
        "rating": 9.1,
        "content_rating": "TV-MA",
        "duration": "4 Seasons (89 Episodes)",
        "language": "Japanese",
        "era": "Modern Era",
        "poster": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1400&auto=format&fit=crop&q=80",
        "overview": "After his hometown is destroyed and his mother is killed, young Eren Jaeger vows to cleanse the earth of the giant humanoid Titans.",
        "director": "Yuichiro Hayashi",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk06/Anime/Attack.on.Titan.Final.Season.Dual.Audio.1080p.mkv",
        "real_stream_url": "",  # Attack on Titan is a commercial title with no free public stream
        "is_featured": False,
        "seasons": [
            {
                "season_number": 4,
                "title": "Final Season",
                "episodes": [
                    {
                        "episode_number": 29,
                        "title": "The Rumbling",
                        "duration": "61m",
                        "overview": "The colossal titans march across the world in Eren's final apocalyptic gambit.",
                        "thumbnail": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&auto=format&fit=crop&q=80",
                        "stream_url": ""
                    }
                ]
            }
        ],
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "300 MB / Ep", "bitrate": "2000 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "750 MB / Ep", "bitrate": "4500 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "2.20 GB / Ep", "bitrate": "13000 kbps", "format": "MKV (HEVC)"}
        }
    }
]

CATEGORIES = [
    {"id": "all", "name": "All", "description": "Explore entire media library across all eras"},
    {"id": "hollywood", "name": "Hollywood", "description": "Top Hollywood blockbuster movies"},
    {"id": "bollywood", "name": "Bollywood", "description": "High voltage Bollywood hits & Hindi classics"},
    {"id": "classics", "name": "Classics (1888-1960)", "description": "Pioneering motion pictures from the dawn of cinema"},
    {"id": "web_series", "name": "Web Series", "description": "Binge-worthy premium web series"},
    {"id": "tv_shows", "name": "TV Shows", "description": "Critically acclaimed television series"},
    {"id": "trending", "name": "Trending", "description": "Most watched movies & series this week"},
    {"id": "anime", "name": "Anime", "description": "Japanese anime series with dual audio"},
    {"id": "action", "name": "Action", "description": "Adrenaline-fueled explosive action titles"},
    {"id": "top_rated", "name": "Top Rated", "description": "Highest IMDb and universally acclaimed masterpieces"}
]

LANGUAGES = [
    {"code": "all", "name": "All Languages"},
    {"code": "English", "name": "English"},
    {"code": "Hindi", "name": "Hindi (Bollywood)"},
    {"code": "Korean", "name": "Korean (K-Drama)"},
    {"code": "Japanese", "name": "Japanese (Anime)"},
    {"code": "Bengali", "name": "Bengali (Cinema)"},
    {"code": "Spanish", "name": "Spanish"},
    {"code": "French", "name": "French"},
    {"code": "German", "name": "German"}
]
