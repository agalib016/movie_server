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

# --- EXTRA PUBLIC-DOMAIN MOVIES (Archive.org — all freely streamable) ---
MEDIA_DATA += [
    {
        "id": "metropolis-1927",
        "title": "Metropolis (1927)",
        "type": "movie",
        "categories": ["classics", "sci_fi", "top_rated"],
        "genres": ["Science Fiction", "Drama", "Classics"],
        "year": 1927,
        "rating": 8.3,
        "content_rating": "NR",
        "duration": "2h 33m",
        "language": "German",
        "era": "Silent Era",
        "poster": "https://images.unsplash.com/photo-1519666216370-6fe2b0b6c0e8?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1400&auto=format&fit=crop&q=80",
        "overview": "Fritz Lang's landmark sci-fi epic about a futuristic city sharply divided between the ruling class and workers who toil underground.",
        "director": "Fritz Lang",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Metropolis.1927.mkv",
        "real_stream_url": "https://archive.org/download/Metropolis_1927/Metropolis_1927.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "700 MB", "bitrate": "2100 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.5 GB", "bitrate": "4800 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.2 GB", "bitrate": "15000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "night-of-the-living-dead-1968",
        "title": "Night of the Living Dead (1968)",
        "type": "movie",
        "categories": ["horror", "classics", "hollywood"],
        "genres": ["Horror", "Thriller", "Classics"],
        "year": 1968,
        "rating": 8.0,
        "content_rating": "R",
        "duration": "1h 36m",
        "language": "English",
        "era": "Cult Classics",
        "poster": "https://images.unsplash.com/photo-1496104679565-6e5c5f8e4cfb?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1556228724-9e7c5faeb2f2?w=1400&auto=format&fit=crop&q=80",
        "overview": "George Romero's landmark horror masterpiece. A small group of people shelter in a farmhouse against flesh-eating zombies. The film that invented the modern zombie genre.",
        "director": "George A. Romero",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Night_of_the_Living_Dead.1968.mkv",
        "real_stream_url": "https://archive.org/download/night_of_the_living_dead/night_of_the_living_dead_512kb.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "750 MB", "bitrate": "2200 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.6 GB", "bitrate": "5000 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.5 GB", "bitrate": "15500 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "nosferatu-1922",
        "title": "Nosferatu (1922)",
        "type": "movie",
        "categories": ["horror", "classics", "top_rated"],
        "genres": ["Horror", "Fantasy", "Silent"],
        "year": 1922,
        "rating": 8.1,
        "content_rating": "NR",
        "duration": "1h 34m",
        "language": "German",
        "era": "Silent Era",
        "poster": "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=1400&auto=format&fit=crop&q=80",
        "overview": "The vampire Count Orlok expresses interest in a new residence and in his estate agent's wife. The quintessential vampire film and one of the greatest horror movies ever made.",
        "director": "F.W. Murnau",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Nosferatu.1922.mkv",
        "real_stream_url": "https://archive.org/download/Nosferatu_the_Vampire_1922/Nosferatu_the_Vampire_1922.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "620 MB", "bitrate": "2000 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.3 GB", "bitrate": "4500 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.0 GB", "bitrate": "14000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "the-general-1926",
        "title": "The General (1926)",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Comedy", "Action", "Adventure"],
        "year": 1926,
        "rating": 8.2,
        "content_rating": "NR",
        "duration": "1h 19m",
        "language": "English",
        "era": "Silent Era",
        "poster": "https://images.unsplash.com/photo-1517649763962-0c623266ddc0?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=1400&auto=format&fit=crop&q=80",
        "overview": "Buster Keaton's masterpiece. During the Civil War, a Southern train engineer pursues his stolen locomotive deep into enemy territory to rescue both his train and his sweetheart.",
        "director": "Buster Keaton & Clyde Bruckman",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/The_General_1926.mkv",
        "real_stream_url": "https://archive.org/download/TheGeneral1926BusterKeaton/TheGeneral1926BusterKeaton.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "580 MB", "bitrate": "1900 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.2 GB", "bitrate": "4400 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "2.8 GB", "bitrate": "13500 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "city-lights-1931",
        "title": "City Lights (1931)",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Comedy", "Drama", "Romance"],
        "year": 1931,
        "rating": 8.5,
        "content_rating": "NR",
        "duration": "1h 27m",
        "language": "English",
        "era": "Silent Era",
        "poster": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1400&auto=format&fit=crop&q=80",
        "overview": "Charlie Chaplin's romantic comedy masterpiece. The Tramp falls in love with a beautiful blind flower girl and tries to raise money for an operation to restore her sight.",
        "director": "Charlie Chaplin",
        "cast_ids": ["charlie-chaplin"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/City_Lights_1931.mkv",
        "real_stream_url": "https://archive.org/download/city-lights-1931-charlie-chaplin/city-lights-1931-charlie-chaplin.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "640 MB", "bitrate": "2000 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.3 GB", "bitrate": "4500 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.0 GB", "bitrate": "14000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "modern-times-1936",
        "title": "Modern Times (1936)",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Comedy", "Drama"],
        "year": 1936,
        "rating": 8.5,
        "content_rating": "G",
        "duration": "1h 27m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1533488765986-dfa2a9939acd?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1400&auto=format&fit=crop&q=80",
        "overview": "Chaplin's The Tramp struggles to survive in the modern industrialized world, working on an assembly line and facing the chaos of technology run amok.",
        "director": "Charlie Chaplin",
        "cast_ids": ["charlie-chaplin"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Modern_Times_1936.mkv",
        "real_stream_url": "https://archive.org/download/modern-times-1936/modern-times-1936.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "650 MB", "bitrate": "2000 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.35 GB", "bitrate": "4500 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.1 GB", "bitrate": "14000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "his-girl-friday-1940",
        "title": "His Girl Friday (1940)",
        "type": "movie",
        "categories": ["classics", "hollywood"],
        "genres": ["Comedy", "Romance", "Drama"],
        "year": 1940,
        "rating": 8.0,
        "content_rating": "NR",
        "duration": "1h 32m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "A fast-talking newspaper editor tries to win back his ex-wife and star reporter by involving her in a story about an escaped murderer. One of the fastest screwball comedies ever made.",
        "director": "Howard Hawks",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/His_Girl_Friday_1940.mkv",
        "real_stream_url": "https://archive.org/download/HisGirlFriday/HisGirlFriday.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "680 MB", "bitrate": "2000 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.4 GB", "bitrate": "4600 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.2 GB", "bitrate": "14500 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "mr-smith-goes-to-washington-1939",
        "title": "Mr. Smith Goes to Washington (1939)",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Drama", "Comedy"],
        "year": 1939,
        "rating": 8.2,
        "content_rating": "NR",
        "duration": "2h 09m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1400&auto=format&fit=crop&q=80",
        "overview": "Frank Capra's classic. A naive, idealistic man is appointed to the US Senate. When he fights corruption he faces the full force of the political establishment.",
        "director": "Frank Capra",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Mr_Smith_Goes_to_Washington.mkv",
        "real_stream_url": "https://archive.org/download/MrSmithGoesToWashington1939/MrSmithGoesToWashington1939.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "900 MB", "bitrate": "2200 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.9 GB", "bitrate": "4800 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "4.2 GB", "bitrate": "15000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "plan-9-from-outer-space-1957",
        "title": "Plan 9 from Outer Space (1957)",
        "type": "movie",
        "categories": ["classics", "sci_fi", "hollywood"],
        "genres": ["Science Fiction", "Horror", "Cult"],
        "year": 1957,
        "rating": 4.0,
        "content_rating": "NR",
        "duration": "1h 19m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=1400&auto=format&fit=crop&q=80",
        "overview": "Often called the worst movie ever made, aliens use resurrected humans to prevent humans from creating a doomsday weapon. A classic cult B-movie experience.",
        "director": "Ed Wood",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Plan9FromOuterSpace.mkv",
        "real_stream_url": "https://archive.org/download/plan_9_from_outer_space_ipod/plan_9_from_outer_space.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "420 MB", "bitrate": "1800 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "900 MB", "bitrate": "4000 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "2.0 GB", "bitrate": "12000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "the-great-dictator-1940",
        "title": "The Great Dictator (1940)",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Comedy", "Drama", "War"],
        "year": 1940,
        "rating": 8.4,
        "content_rating": "G",
        "duration": "2h 05m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1533488765986-dfa2a9939acd?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=1400&auto=format&fit=crop&q=80",
        "overview": "Charlie Chaplin's first true sound film. A timeless satirical comedy in which Chaplin plays both a Jewish barber and a Hitler-like dictator, culminating in one of cinema's greatest speeches.",
        "director": "Charlie Chaplin",
        "cast_ids": ["charlie-chaplin"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/The_Great_Dictator.1940.mkv",
        "real_stream_url": "https://archive.org/download/the-great-dictator-1940/the-great-dictator-1940.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "870 MB", "bitrate": "2200 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.9 GB", "bitrate": "4900 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "4.3 GB", "bitrate": "15000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "his-majesty-the-scarecrow-of-oz-1914",
        "title": "The Scarecrow of Oz (1914)",
        "type": "movie",
        "categories": ["classics", "hollywood"],
        "genres": ["Fantasy", "Adventure", "Family"],
        "year": 1914,
        "rating": 6.8,
        "content_rating": "NR",
        "duration": "1h 05m",
        "language": "English",
        "era": "Early Cinema",
        "poster": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?w=1400&auto=format&fit=crop&q=80",
        "overview": "An early silent fantasy film based on L. Frank Baum's Oz books. A magical adventure through the land of Oz with the beloved Scarecrow character.",
        "director": "J. Farrell MacDonald",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Scarecrow_of_Oz_1914.mkv",
        "real_stream_url": "https://archive.org/download/HisMajestyTheScarecrowOfOz/HisMajestyTheScarecrowOfOz.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "400 MB", "bitrate": "1700 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "850 MB", "bitrate": "3800 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "1.8 GB", "bitrate": "11000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "sherlock-jr-1924",
        "title": "Sherlock Jr. (1924)",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Comedy", "Mystery", "Action"],
        "year": 1924,
        "rating": 8.2,
        "content_rating": "NR",
        "duration": "44m",
        "language": "English",
        "era": "Silent Era",
        "poster": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1526986472364-f9bb6fbab0e5?w=1400&auto=format&fit=crop&q=80",
        "overview": "Buster Keaton's visionary short film. A film projectionist dreams himself into a movie he's screening. A genre-defining masterpiece featuring stunning physical comedy and pioneering editing.",
        "director": "Buster Keaton",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Sherlock_Jr_1924.mkv",
        "real_stream_url": "https://archive.org/download/SherlockJr.1924/SherlockJr.1924.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "280 MB", "bitrate": "1500 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "580 MB", "bitrate": "3500 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "1.3 GB", "bitrate": "10000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "the-gold-rush-1925",
        "title": "The Gold Rush (1925)",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Comedy", "Adventure", "Drama"],
        "year": 1925,
        "rating": 8.2,
        "content_rating": "G",
        "duration": "1h 35m",
        "language": "English",
        "era": "Silent Era",
        "poster": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "Charlie Chaplin's beloved adventure comedy. The Little Tramp seeks gold in the Klondike during the 1890s gold rush, facing hardship, starvation, and romance.",
        "director": "Charlie Chaplin",
        "cast_ids": ["charlie-chaplin"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/The_Gold_Rush_1925.mkv",
        "real_stream_url": "https://archive.org/download/the-gold-rush-1925-charlie-chaplin/the-gold-rush-1925.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "660 MB", "bitrate": "2000 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.4 GB", "bitrate": "4500 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.1 GB", "bitrate": "14000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "the-cabinet-of-dr-caligari-1920",
        "title": "The Cabinet of Dr. Caligari (1920)",
        "type": "movie",
        "categories": ["horror", "classics", "top_rated"],
        "genres": ["Horror", "Mystery", "Thriller"],
        "year": 1920,
        "rating": 8.1,
        "content_rating": "NR",
        "duration": "1h 16m",
        "language": "German",
        "era": "Silent Era",
        "poster": "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1496104679565-6e5c5f8e4cfb?w=1400&auto=format&fit=crop&q=80",
        "overview": "Widely considered the first true horror film. A mad doctor uses a somnambulist to commit murders in a German mountain village. A masterpiece of expressionist cinema.",
        "director": "Robert Wiene",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Cabinet_of_Dr_Caligari.mkv",
        "real_stream_url": "https://archive.org/download/TheCabinetOfDrCaligari/TheCabinetOfDrCaligari.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "520 MB", "bitrate": "1900 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.1 GB", "bitrate": "4300 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "2.6 GB", "bitrate": "13000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "birth-of-a-nation-1915",
        "title": "The Birth of a Nation (1915)",
        "type": "movie",
        "categories": ["classics", "hollywood"],
        "genres": ["Drama", "History", "War"],
        "year": 1915,
        "rating": 6.9,
        "content_rating": "NR",
        "duration": "3h 10m",
        "language": "English",
        "era": "Early Cinema",
        "poster": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1400&auto=format&fit=crop&q=80",
        "overview": "D.W. Griffith's historically significant but deeply controversial epic about the American Civil War and Reconstruction. A landmark in cinema technique despite its harmful content.",
        "director": "D.W. Griffith",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Birth_of_a_Nation_1915.mkv",
        "real_stream_url": "https://archive.org/download/dw_griffith_birth_of_a_nation_1915/dw_griffith_birth_of_a_nation_1915.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "1.2 GB", "bitrate": "2300 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "2.5 GB", "bitrate": "5000 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "5.5 GB", "bitrate": "15000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "little-shop-of-horrors-1960",
        "title": "The Little Shop of Horrors (1960)",
        "type": "movie",
        "categories": ["classics", "horror", "hollywood"],
        "genres": ["Comedy", "Horror", "Sci-Fi"],
        "year": 1960,
        "rating": 6.8,
        "content_rating": "NR",
        "duration": "1h 10m",
        "language": "English",
        "era": "Cult Classics",
        "poster": "https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "Roger Corman's cult comedy-horror filmed in two days. A dim-witted florist's assistant raises a plant that feeds on blood, starring a young Jack Nicholson in an early role.",
        "director": "Roger Corman",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Little_Shop_of_Horrors_1960.mkv",
        "real_stream_url": "https://archive.org/download/TheLittleShopOfHorrors/TheLittleShopOfHorrors.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "430 MB", "bitrate": "1700 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "920 MB", "bitrate": "4000 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "2.1 GB", "bitrate": "12000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "charade-1963",
        "title": "Charade (1963)",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Comedy", "Mystery", "Romance"],
        "year": 1963,
        "rating": 7.9,
        "content_rating": "G",
        "duration": "1h 53m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1526986472364-f9bb6fbab0e5?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=1400&auto=format&fit=crop&q=80",
        "overview": "A stylish romantic comedy thriller. Audrey Hepburn and Cary Grant star in this Hitchcock-style Parisian adventure involving cold war spies, buried gold, and shifting identities.",
        "director": "Stanley Donen",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Charade.1963.mkv",
        "real_stream_url": "https://archive.org/download/charade-1963/charade-1963.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "780 MB", "bitrate": "2100 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.65 GB", "bitrate": "4700 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "3.7 GB", "bitrate": "14500 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "the-kids-1921",
        "title": "The Kid (1921)",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Comedy", "Drama", "Family"],
        "year": 1921,
        "rating": 8.3,
        "content_rating": "NR",
        "duration": "1h 08m",
        "language": "English",
        "era": "Silent Era",
        "poster": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=1400&auto=format&fit=crop&q=80",
        "overview": "Charlie Chaplin's first feature-length film. The Tramp cares for an abandoned child (played by Jackie Coogan), in a deeply moving blend of comedy and social drama.",
        "director": "Charlie Chaplin",
        "cast_ids": ["charlie-chaplin"],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/The_Kid_1921.mkv",
        "real_stream_url": "https://archive.org/download/TheKid1921/TheKid1921.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "500 MB", "bitrate": "1900 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.1 GB", "bitrate": "4300 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "2.5 GB", "bitrate": "13000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "invasion-of-the-body-snatchers-1956",
        "title": "Invasion of the Body Snatchers (1956)",
        "type": "movie",
        "categories": ["sci_fi", "classics", "horror", "hollywood"],
        "genres": ["Science Fiction", "Horror", "Thriller"],
        "year": 1956,
        "rating": 7.7,
        "content_rating": "NR",
        "duration": "1h 20m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=1400&auto=format&fit=crop&q=80",
        "overview": "A small-town doctor discovers that townspeople are being replaced by emotionless alien duplicates grown from plant-like pods. A chilling Cold War allegory and sci-fi masterpiece.",
        "director": "Don Siegel",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Invasion_Body_Snatchers_1956.mkv",
        "real_stream_url": "https://archive.org/download/InvasionOfTheBodySnatchers1956/InvasionOfTheBodySnatchers1956.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "560 MB", "bitrate": "1900 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.2 GB", "bitrate": "4300 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "2.7 GB", "bitrate": "13000 kbps", "format": "MKV (HEVC)"}
        }
    },
    {
        "id": "the-39-steps-1935",
        "title": "The 39 Steps (1935)",
        "type": "movie",
        "categories": ["classics", "hollywood", "top_rated"],
        "genres": ["Thriller", "Mystery", "Action"],
        "year": 1935,
        "rating": 7.7,
        "content_rating": "NR",
        "duration": "1h 26m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=1400&auto=format&fit=crop&q=80",
        "overview": "Alfred Hitchcock's early thriller masterpiece. A man gets embroiled in a spy ring trying to steal British military secrets and must race to expose them while being hunted himself.",
        "director": "Alfred Hitchcock",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/The_39_Steps_1935.mkv",
        "real_stream_url": "https://archive.org/download/TheThirtyNineSteps/TheThirtyNineSteps.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {"resolution": "720p HD", "size": "590 MB", "bitrate": "1900 kbps", "format": "MP4 (H.264)"},
            "1080p": {"resolution": "1080p Full HD", "size": "1.25 GB", "bitrate": "4300 kbps", "format": "MP4 (H.264)"},
            "4k": {"resolution": "4K Ultra HD", "size": "2.8 GB", "bitrate": "13000 kbps", "format": "MKV (HEVC)"}
        }
    },
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
