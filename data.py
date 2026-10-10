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
        "real_stream_url": "https://archive.org/download/charulata-1964-bengali-full-movie-hd-a-film-by-satyajit-ray/%E0%A6%9A%E0%A6%BE%E0%A6%B0%E0%A7%81%E0%A6%B2%E0%A6%A4%E0%A6%BE%20-%20Charulata%20%281964%29%20Bengali%20Full%20Movie%20%28HD%29%20-%20a%20film%20by%20Satyajit%20Ray.mp4",
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

# --- EXTRA VERIFIED STREAMING MOVIES (All verified HTTP 200/302 video/mp4) ---
MEDIA_DATA += [
    {
        "id": "jungle-book-1942",
        "title": "Jungle Book (1942)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood",
            "top_rated",
            "action"
        ],
        "genres": [
            "Action",
            "Adventure",
            "Family",
            "Classics"
        ],
        "year": 1942,
        "rating": 8.2,
        "content_rating": "PG",
        "duration": "1h 48m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "Mowgli, raised by wolves in the jungles of India, discovers human greed and ancient wonders. Nominated for 4 Academy Awards, Alexander Korda's stunning Technicolor adaptation of Rudyard Kipling's masterwork.",
        "director": "Zoltan Korda",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Jungle_Book_1942.mkv",
        "real_stream_url": "https://archive.org/download/JungleBook/Jungle_Book_512kb.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "650 MB",
                "bitrate": "2200 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.4 GB",
                "bitrate": "4600 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "3.1 GB",
                "bitrate": "13500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "his-girl-friday-1940",
        "title": "His Girl Friday (1940)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood",
            "top_rated"
        ],
        "genres": [
            "Comedy",
            "Drama",
            "Romance",
            "Classics"
        ],
        "year": 1940,
        "rating": 8.4,
        "content_rating": "NR",
        "duration": "1h 32m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?w=1400&auto=format&fit=crop&q=80",
        "overview": "Howard Hawks' legendary screwball comedy starring Cary Grant and Rosalind Russell. Rapid-fire dialog and unmatched wit as a newspaper publisher tries to win back his ace reporter ex-wife on a breaking murder scoop.",
        "director": "Howard Hawks",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/His_Girl_Friday_1940.mkv",
        "real_stream_url": "https://archive.org/download/his_girl_friday/his_girl_friday_512kb.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "580 MB",
                "bitrate": "2000 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.2 GB",
                "bitrate": "4300 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.8 GB",
                "bitrate": "12500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "house-on-haunted-hill-1959",
        "title": "House on Haunted Hill (1959)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood",
            "trending"
        ],
        "genres": [
            "Horror",
            "Mystery",
            "Classics"
        ],
        "year": 1959,
        "rating": 8.0,
        "content_rating": "PG-13",
        "duration": "1h 15m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "Vincent Price stars as an eccentric millionaire who offers five strangers $10,000 each if they can survive a night locked in his notoriously haunted house. A spine-tingling horror landmark.",
        "director": "William Castle",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/House_on_Haunted_Hill_1959.mkv",
        "real_stream_url": "https://archive.org/download/house_on_haunted_hill_ipod/house_on_haunted_hill_512kb.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "520 MB",
                "bitrate": "1900 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.1 GB",
                "bitrate": "4200 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.5 GB",
                "bitrate": "12000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "fast-and-furious-1954",
        "title": "The Fast and the Furious (1955)",
        "type": "movie",
        "categories": [
            "action",
            "hollywood",
            "classics"
        ],
        "genres": [
            "Action",
            "Crime",
            "Thriller"
        ],
        "year": 1955,
        "rating": 7.6,
        "content_rating": "PG",
        "duration": "1h 13m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=1400&auto=format&fit=crop&q=80",
        "overview": "A wrongly accused fugitive on the run takes a beautiful driver and her fast sports car hostage, racing cross-country to Mexico in a high-stakes cross-border competition.",
        "director": "John Ireland & Edward Sampson",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk01/Movies/Hollywood/1954/Fast_Furious_1954.1080p.mkv",
        "real_stream_url": "https://archive.org/download/TheFastandtheFuriousJohnIreland1954goofyrip/TheFastandtheFuriousJohnIreland1954goofyrip_512kb.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "530 MB",
                "bitrate": "1900 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.15 GB",
                "bitrate": "4100 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.6 GB",
                "bitrate": "12000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "charlie-chaplin-festival",
        "title": "Charlie Chaplin Film Festival",
        "type": "movie",
        "categories": [
            "classics",
            "top_rated"
        ],
        "genres": [
            "Comedy",
            "Classics"
        ],
        "year": 1938,
        "rating": 8.5,
        "content_rating": "G",
        "duration": "1h 20m",
        "language": "English",
        "era": "Silent Era",
        "poster": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1400&auto=format&fit=crop&q=80",
        "overview": "Timeless collection of Charlie Chaplin's most celebrated comedic tours de force: The Adventurer, The Cure, Easy Street and The Immigrant with full orchestrated score.",
        "director": "Charlie Chaplin",
        "cast_ids": [
            "charlie-chaplin"
        ],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Chaplin_Festival.1080p.mkv",
        "real_stream_url": "https://archive.org/download/charlie_chaplin_film_fest/charlie_chaplin_film_fest_512kb.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "550 MB",
                "bitrate": "1900 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.2 GB",
                "bitrate": "4200 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.7 GB",
                "bitrate": "12500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "sita-sings-the-blues-2008",
        "title": "Sita Sings the Blues (2008)",
        "type": "movie",
        "categories": [
            "anime",
            "trending",
            "top_rated"
        ],
        "genres": [
            "Animation",
            "Comedy",
            "Musical",
            "Fantasy"
        ],
        "year": 2008,
        "rating": 8.6,
        "content_rating": "PG-13",
        "duration": "1h 22m",
        "language": "English",
        "era": "Modern Era",
        "poster": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "A dazzling, award-winning animated masterwork weaving the Indian epic Ramayana with 1920s jazz songs by Annette Hanshaw and modern relationship comedy.",
        "director": "Nina Paley",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk06/Anime/Sita_Sings_the_Blues.mkv",
        "real_stream_url": "https://archive.org/download/Sita_Sings_the_Blues/Sita_Sings_the_Blues_DVD_NTSC3.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "600 MB",
                "bitrate": "2100 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.3 GB",
                "bitrate": "4500 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "3.0 GB",
                "bitrate": "13000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "the-stranger-1946",
        "title": "The Stranger (Orson Welles 1946)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood",
            "top_rated"
        ],
        "genres": [
            "Crime",
            "Drama",
            "Film-Noir",
            "Thriller"
        ],
        "year": 1946,
        "rating": 8.1,
        "content_rating": "NR",
        "duration": "1h 35m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=1400&auto=format&fit=crop&q=80",
        "overview": "Orson Welles directs and stars alongside Edward G. Robinson in this electrifying cat-and-mouse film noir about a war crimes investigator tracking down a fugitive living under a false identity in a quiet town.",
        "director": "Orson Welles",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/The_Stranger_1946.mkv",
        "real_stream_url": "https://archive.org/download/TheStranger_0/The_Stranger_512kb.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "620 MB",
                "bitrate": "2000 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.35 GB",
                "bitrate": "4400 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "3.1 GB",
                "bitrate": "13000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "dressed-to-kill-1946",
        "title": "Sherlock Holmes: Dressed to Kill (1946)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood"
        ],
        "genres": [
            "Mystery",
            "Crime",
            "Thriller"
        ],
        "year": 1946,
        "rating": 7.9,
        "content_rating": "NR",
        "duration": "1h 11m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=1400&auto=format&fit=crop&q=80",
        "overview": "Basil Rathbone and Nigel Bruce star as Sherlock Holmes and Dr. Watson, investigating three seemingly harmless music boxes sold at auction that conceal a secret code to stolen currency plates.",
        "director": "Roy William Neill",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Dressed_To_Kill_1946.mkv",
        "real_stream_url": "https://archive.org/download/dressed_to_kill/dressed_to_kill_512kb.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "500 MB",
                "bitrate": "1900 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.1 GB",
                "bitrate": "4200 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.4 GB",
                "bitrate": "12000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "suddenly-1954",
        "title": "Suddenly (1954 - Frank Sinatra)",
        "type": "movie",
        "categories": [
            "action",
            "hollywood",
            "classics"
        ],
        "genres": [
            "Crime",
            "Drama",
            "Film-Noir",
            "Thriller"
        ],
        "year": 1954,
        "rating": 7.8,
        "content_rating": "NR",
        "duration": "1h 17m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=1400&auto=format&fit=crop&q=80",
        "overview": "Frank Sinatra gives a chilling, career-defining performance as a psychopathic assassin who takes over a family home overlooking a train station to assassinate the visiting President of the United States.",
        "director": "Lewis Allen",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk01/Movies/Hollywood/Suddenly_1954.mkv",
        "real_stream_url": "https://archive.org/download/suddenly/suddenly_512kb.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "540 MB",
                "bitrate": "1950 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.18 GB",
                "bitrate": "4250 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.6 GB",
                "bitrate": "12500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "pather-panchali-1955",
        "title": "Pather Panchali (Song of the Little Road)",
        "type": "movie",
        "categories": [
            "classics",
            "top_rated"
        ],
        "genres": [
            "Drama",
            "Classics"
        ],
        "year": 1955,
        "rating": 8.8,
        "content_rating": "PG",
        "duration": "2h 05m",
        "language": "Bengali",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "Satyajit Ray's monumental directorial debut and winner of the Best Human Document award at Cannes. An unforgettable lyrical portrait of childhood, poverty, and wonder in rural Bengal.",
        "director": "Satyajit Ray",
        "cast_ids": [
            "satyajit-ray"
        ],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk05/Bengali/Pather_Panchali_1955.720p.mkv",
        "real_stream_url": "https://archive.org/download/PatherPanchali1955720p/Pather%20Panchali%20%281955%29%20%5B720p%5D.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "780 MB",
                "bitrate": "2200 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.75 GB",
                "bitrate": "4700 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "4.2 GB",
                "bitrate": "14000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "voyage-prehistoric-women-1967",
        "title": "Voyage to the Planet of Prehistoric Women",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood"
        ],
        "genres": [
            "Science Fiction",
            "Adventure",
            "Cult"
        ],
        "year": 1967,
        "rating": 7.0,
        "content_rating": "G",
        "duration": "1h 18m",
        "language": "English",
        "era": "Cult Classics",
        "poster": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1519666216370-6fe2b0b6c0e8?w=1400&auto=format&fit=crop&q=80",
        "overview": "Astronauts crash-land on Venus and encounter volcanic hazards, alien monsters, and telepathic sirens worshiping a pterodactyl deity. An essential piece of vintage space pulp cinema.",
        "director": "Peter Bogdanovich",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Voyage_Prehistoric_Women.mkv",
        "real_stream_url": "https://archive.org/download/VoyagetothePlanetofPrehistoricWomen/VoyagetothePlanetofPrehistoricWomen_512kb.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "530 MB",
                "bitrate": "1900 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.15 GB",
                "bitrate": "4100 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.5 GB",
                "bitrate": "12000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "return-kung-fu-dragon-1976",
        "title": "Return of the Kung Fu Dragon (1976)",
        "type": "movie",
        "categories": [
            "action",
            "trending"
        ],
        "genres": [
            "Action",
            "Martial Arts",
            "Adventure"
        ],
        "year": 1976,
        "rating": 7.7,
        "content_rating": "R",
        "duration": "1h 29m",
        "language": "English",
        "era": "Cult Classics",
        "poster": "https://images.unsplash.com/photo-1517649763962-0c623266ddc0?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=1400&auto=format&fit=crop&q=80",
        "overview": "High-octane golden era martial arts adventure packed with furious fist-fighting, acrobatics, and revenge showdowns across ancient temples.",
        "director": "Chung-Kwang Pao",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk01/Movies/Action/Return_Kung_Fu_Dragon.mkv",
        "real_stream_url": "https://archive.org/download/Return_of_the_Kung_Fu_Dragon/Return_of_the_Kung_Fu_Dragon_512kb.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "590 MB",
                "bitrate": "2050 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.3 GB",
                "bitrate": "4400 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.9 GB",
                "bitrate": "13000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "utopia-1951",
        "title": "Utopia (Atoll K - Laurel & Hardy)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood"
        ],
        "genres": [
            "Comedy",
            "Adventure",
            "Classics"
        ],
        "year": 1951,
        "rating": 7.5,
        "content_rating": "G",
        "duration": "1h 22m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?w=1400&auto=format&fit=crop&q=80",
        "overview": "The final feature film made by Stan Laurel and Oliver Hardy together. The duo inherits an uninhabited Pacific island and sets off on a hilarious maritime misadventure.",
        "director": "Leo Joannon",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Utopia_1951.mkv",
        "real_stream_url": "https://archive.org/download/utopia/Utopia.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "540 MB",
                "bitrate": "1950 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.2 GB",
                "bitrate": "4250 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.7 GB",
                "bitrate": "12500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "escape-from-sobibor-1987",
        "title": "Escape From Sobibor (1987)",
        "type": "movie",
        "categories": [
            "action",
            "hollywood",
            "top_rated"
        ],
        "genres": [
            "Action",
            "Drama",
            "History",
            "War"
        ],
        "year": 1987,
        "rating": 8.3,
        "content_rating": "R",
        "duration": "2h 23m",
        "language": "English",
        "era": "Modern Era",
        "poster": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=1400&auto=format&fit=crop&q=80",
        "overview": "Alan Arkin and Rutger Hauer star in this gripping, Emmy and Golden Globe winning historical drama detailing the audacious, successful mass escape of prisoners from the Sobibor camp.",
        "director": "Jack Gold",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk01/Movies/War/Escape_From_Sobibor.1080p.mkv",
        "real_stream_url": "https://archive.org/download/Escape_From_Sobibor.avi/Escape_from_Sobibor_512kb.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "790 MB",
                "bitrate": "2200 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.75 GB",
                "bitrate": "4700 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "4.1 GB",
                "bitrate": "14000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "abraham-lincoln-1930",
        "title": "Abraham Lincoln (1930 - D.W. Griffith)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood"
        ],
        "genres": [
            "Biography",
            "Drama",
            "History"
        ],
        "year": 1930,
        "rating": 7.5,
        "content_rating": "NR",
        "duration": "1h 36m",
        "language": "English",
        "era": "Early Cinema",
        "poster": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=1400&auto=format&fit=crop&q=80",
        "overview": "D.W. Griffith's first sound feature film, an epic biographical chronicle of the life of the 16th US President from his log cabin beginnings through the Civil War to his martyrdom.",
        "director": "D.W. Griffith",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Abraham_Lincoln_1930.mkv",
        "real_stream_url": "https://archive.org/download/abraham_lincoln/abraham_lincoln_512kb.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "610 MB",
                "bitrate": "2000 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.3 GB",
                "bitrate": "4300 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.9 GB",
                "bitrate": "12500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "carnival-of-souls-1962",
        "title": "Carnival of Souls (1962)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood",
            "top_rated"
        ],
        "genres": [
            "Horror",
            "Mystery",
            "Cult"
        ],
        "year": 1962,
        "rating": 8.1,
        "content_rating": "PG",
        "duration": "1h 24m",
        "language": "English",
        "era": "Cult Classics",
        "poster": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "A church organist emerges as the sole survivor of a drag-racing accident and finds herself drawn to an abandoned lakeside pavilion, haunted by apparitions in this hypnotic horror masterpiece.",
        "director": "Herk Harvey",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Carnival_of_Souls_1962.mkv",
        "real_stream_url": "https://archive.org/download/carnival_of_souls/carnival_of_souls.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "560 MB",
                "bitrate": "1950 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.25 GB",
                "bitrate": "4300 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.8 GB",
                "bitrate": "13000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "nosferatu-1922",
        "title": "Nosferatu: A Symphony of Horror (1922)",
        "type": "movie",
        "categories": [
            "classics",
            "top_rated"
        ],
        "genres": [
            "Horror",
            "Fantasy",
            "Silent"
        ],
        "year": 1922,
        "rating": 8.3,
        "content_rating": "NR",
        "duration": "1h 34m",
        "language": "German",
        "era": "Silent Era",
        "poster": "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=1400&auto=format&fit=crop&q=80",
        "overview": "F.W. Murnau's immortal Gothic masterpiece. The eerie vampire Count Orlok terrorizes a town and covets his estate agent's bride in the defining film of cinematic expressionism.",
        "director": "F.W. Murnau",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Nosferatu.1922.mkv",
        "real_stream_url": "https://archive.org/download/nosferatu_1922/nosferatu_1922.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "640 MB",
                "bitrate": "2050 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.35 GB",
                "bitrate": "4400 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "3.1 GB",
                "bitrate": "13500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "the-39-steps-1935",
        "title": "The 39 Steps (Alfred Hitchcock 1935)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood",
            "top_rated"
        ],
        "genres": [
            "Thriller",
            "Mystery",
            "Action"
        ],
        "year": 1935,
        "rating": 8.2,
        "content_rating": "NR",
        "duration": "1h 26m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=1400&auto=format&fit=crop&q=80",
        "overview": "Alfred Hitchcock's early British espionage masterpiece. An innocent man is drawn into a shadowy ring of international spies and must race across Scotland handcuffed to a woman who suspects him.",
        "director": "Alfred Hitchcock",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/The_39_Steps_1935.mkv",
        "real_stream_url": "https://archive.org/download/the_39_steps_1935/the_39_steps_1935.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "580 MB",
                "bitrate": "1950 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.25 GB",
                "bitrate": "4300 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.8 GB",
                "bitrate": "12500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "doctor-in-industry-1946",
        "title": "Doctor in Industry (1946)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood"
        ],
        "genres": [
            "Drama",
            "Classics"
        ],
        "year": 1946,
        "rating": 7.4,
        "content_rating": "G",
        "duration": "1h 00m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=1400&auto=format&fit=crop&q=80",
        "overview": "A pioneering historical drama dramatizing the struggle of a dedicated physician to introduce modern safety and occupational healthcare into early industrial factories.",
        "director": "Ben Blake",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Doctor_In_Industry.mkv",
        "real_stream_url": "https://archive.org/download/Doctorin1946/Doctorin1946_edit.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "450 MB",
                "bitrate": "1800 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "980 MB",
                "bitrate": "3900 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.2 GB",
                "bitrate": "11500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "about-bananas-1935",
        "title": "About Bananas (1935 Vintage Cinema)",
        "type": "movie",
        "categories": [
            "classics"
        ],
        "genres": [
            "Documentary",
            "Classics"
        ],
        "year": 1935,
        "rating": 7.2,
        "content_rating": "G",
        "duration": "15m",
        "language": "English",
        "era": "Early Cinema",
        "poster": "https://images.unsplash.com/photo-1528825871115-3581a5387919?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "A captivating archival travelogue and early sound documentary chronicling life, agriculture, and transportation through Central America in the 1930s.",
        "director": "United Fruit Archives",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/About_Bananas_1935.mkv",
        "real_stream_url": "https://archive.org/download/AboutBan1935/AboutBan1935_edit.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "220 MB",
                "bitrate": "1700 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "480 MB",
                "bitrate": "3600 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "1.1 GB",
                "bitrate": "10000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "pied-piper-1957",
        "title": "The Pied Piper of Hamelin (1957)",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood"
        ],
        "genres": [
            "Musical",
            "Fantasy",
            "Family"
        ],
        "year": 1957,
        "rating": 7.8,
        "content_rating": "G",
        "duration": "1h 27m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=1400&auto=format&fit=crop&q=80",
        "overview": "Van Johnson and Claude Rains star in this vibrant musical fantasy adapted from Robert Browning's poem, set to the timeless music of Edvard Grieg.",
        "director": "Bretaigne Windust",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Pied_Piper_1957.mkv",
        "real_stream_url": "https://archive.org/download/The_Pied_Piper_of_Hamelin/pied_512kb.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "560 MB",
                "bitrate": "1950 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.2 GB",
                "bitrate": "4200 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.7 GB",
                "bitrate": "12500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "three-stooges-1950",
        "title": "Three Stooges: The Golden Shorts",
        "type": "movie",
        "categories": [
            "classics",
            "hollywood"
        ],
        "genres": [
            "Comedy",
            "Slapstick",
            "Classics"
        ],
        "year": 1950,
        "rating": 8.4,
        "content_rating": "G",
        "duration": "1h 10m",
        "language": "English",
        "era": "Golden Age",
        "poster": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1400&auto=format&fit=crop&q=80",
        "overview": "Moe, Larry, and Curly at their uproarious peak! Featuring the legendary comedy routines from Disorder in the Court, Brideless Groom, and Sing a Song of Six Pants.",
        "director": "Jules White & Del Lord",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Three_Stooges_Collection.mkv",
        "real_stream_url": "https://archive.org/download/3stooges/3stooges_NewApants2_512kb.mp4",
        "is_featured": True,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "520 MB",
                "bitrate": "1900 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.15 GB",
                "bitrate": "4200 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.6 GB",
                "bitrate": "12500 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "godzillas-revenge-1969",
        "title": "Godzilla's Revenge (All Monsters Attack 1969)",
        "type": "movie",
        "categories": [
            "action",
            "anime",
            "classics"
        ],
        "genres": [
            "Action",
            "Science Fiction",
            "Kaiju"
        ],
        "year": 1969,
        "rating": 7.5,
        "content_rating": "G",
        "duration": "1h 10m",
        "language": "Japanese",
        "era": "Cult Classics",
        "poster": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=1400&auto=format&fit=crop&q=80",
        "overview": "Ishiro Honda directs this beloved Showa-era Toho Kaiju fantasy about a young boy in Tokyo who dreams of visiting Monster Island to learn bravery from Minilla and the mighty Godzilla.",
        "director": "Ishiro Honda",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk06/Anime/Godzillas_Revenge_1969.mkv",
        "real_stream_url": "https://archive.org/download/RecurringDinosaurInfestationFilms/10.GodzillasRevenge1969.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "540 MB",
                "bitrate": "1950 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.18 GB",
                "bitrate": "4250 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.7 GB",
                "bitrate": "13000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "bloody-pit-of-horror-1965",
        "title": "Bloody Pit of Horror (1965)",
        "type": "movie",
        "categories": [
            "classics"
        ],
        "genres": [
            "Horror",
            "Cult",
            "Thriller"
        ],
        "year": 1965,
        "rating": 7.1,
        "content_rating": "R",
        "duration": "1h 27m",
        "language": "English",
        "era": "Cult Classics",
        "poster": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1400&auto=format&fit=crop&q=80",
        "overview": "Mickey Hargitay plays the psychotic Crimson Executioner in this legendary Italian gothic horror cult film set inside an ominous castle filled with sinister contraptions.",
        "director": "Massimo Pupillo",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Bloody_Pit_of_Horror.mkv",
        "real_stream_url": "https://archive.org/download/BloodyPitOfHorror/BloodyPitOfHorror.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "590 MB",
                "bitrate": "2000 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.3 GB",
                "bitrate": "4400 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.9 GB",
                "bitrate": "13000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "sex-madness-1938",
        "title": "Sex Madness (1938 Cult Vintage)",
        "type": "movie",
        "categories": [
            "classics"
        ],
        "genres": [
            "Drama",
            "Cult",
            "Classics"
        ],
        "year": 1938,
        "rating": 7.2,
        "content_rating": "NR",
        "duration": "59m",
        "language": "English",
        "era": "Early Cinema",
        "poster": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=1400&auto=format&fit=crop&q=80",
        "overview": "A rare 1930s exploitation and melodrama curiosity exploring the underground nightlife of Broadway and the perils of taboo city escapades.",
        "director": "Dwain Esper",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Sex_Madness_1938.mkv",
        "real_stream_url": "https://archive.org/download/sex_madness/sex_madness_512kb.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "420 MB",
                "bitrate": "1800 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "950 MB",
                "bitrate": "3900 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.1 GB",
                "bitrate": "11000 kbps",
                "format": "MKV (HEVC)"
            }
        }
    },
    {
        "id": "reefer-madness-1938",
        "title": "Reefer Madness (1938 Cult Classic)",
        "type": "movie",
        "categories": [
            "classics",
            "trending"
        ],
        "genres": [
            "Drama",
            "Cult",
            "Classics"
        ],
        "year": 1938,
        "rating": 7.4,
        "content_rating": "NR",
        "duration": "1h 06m",
        "language": "English",
        "era": "Early Cinema",
        "poster": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=700&auto=format&fit=crop&q=80",
        "backdrop": "https://images.unsplash.com/photo-1509281373149-e957c6296406?w=1400&auto=format&fit=crop&q=80",
        "overview": "The archetypal sensationalized cult classic made to capitalize on mid-century melodrama, following innocent youths drawn into chaotic jazz-age escapades.",
        "director": "Louis J. Gasnier",
        "cast_ids": [],
        "icc_ftp_path": "ftp://icc-stream.bd/Disk02/Classics/Reefer_Madness_1938.mkv",
        "real_stream_url": "https://archive.org/download/reefer_madness1938/reefer_madness1938_512kb.mp4",
        "is_featured": False,
        "downloads": {
            "720p": {
                "resolution": "720p HD",
                "size": "480 MB",
                "bitrate": "1850 kbps",
                "format": "MP4 (H.264)"
            },
            "1080p": {
                "resolution": "1080p Full HD",
                "size": "1.05 GB",
                "bitrate": "4100 kbps",
                "format": "MP4 (H.264)"
            },
            "4k": {
                "resolution": "4K Ultra HD",
                "size": "2.4 GB",
                "bitrate": "12000 kbps",
                "format": "MKV (HEVC)"
            }
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
