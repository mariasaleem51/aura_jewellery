from pymongo import MongoClient

# =======================================================
# --- PROPER & GUARANTEED MONGODB CONNECTION SETUP ---
# =======================================================
try:
    # 1. Standard Local Loopback URL with Direct Connection parameters
    CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true"
    
    # 2. Initialize Client with a 5-second selective timeout
    client = MongoClient(CONNECTION_STRING, serverSelectionTimeoutMS=5000)
    
    # 3. CRITICAL: Database aur Collection ko explicitly bind karna
    db = client["aura_jewelry_db"]
    products_collection = db["products"]

    # 4. Connection Test (Ping Command)
    client.admin.command('ping')
    print("\n=======================================================")
    print(" STATUS: MONGODB CONNECTION IS PROPERLY ACTIVE! 🎉")
    print("=======================================================")

    # --- OLD RECORDS CLEAR ---
    # Naye batch se pehle purana data wipe out karne ke liye
    deletion_result = products_collection.delete_many({})
    print(f"-> Purane records successfully clear kar diye gaye hain.")

    # --- INVENTORY DATA (Unchanged & Secured) ---
    inventory_data = [
        # --- PENDANTS CATEGORY (16 Products) ---
        {"name": "Aura Solitaire Pendant", "category": "pendants", "price": 2899, "image": "collection/pendent1.jpg", "description": "Classic shimmering single diamond finish pendant with a sleek chain."},
        {"name": "Empress Ruby Drop Chain", "category": "pendants", "price": 3600, "image": "collection/pendant2.jpg", "description": "Stunning ruby core stone suspended on fine sterling silver chain."},
        {"name": "Minimalist Golden Bar Locket", "category": "pendants", "price": 1999, "image": "collection/pandant3.jpg", "description": "Sleek layered geometric bar pendant with a 24k gold wash finish."},
        {"name": "Vintage Emerald Cushion Pendant", "category": "pendants", "price": 4200, "image": "collection/pendant4.jpg", "description": "Royal cushion-cut green emerald piece with micro zircon borders."},
        {"name": "Infinity Bond Pendant", "category": "pendants", "price": 2499, "image": "collection/pendant5.jpg", "description": "Elegant infinity loop symbolic necklace for timeless regular styling."},
        {"name": "Sapphire Horizon Choker", "category": "pendants", "price": 4500, "image": "collection/pendant6.jpg", "description": "Deep ocean blue teardrop sapphire centered on an elegant link chain."},
        {"name": "Princess Hexagon Diamond Piece", "category": "pendants", "price": 3100, "image": "collection/pendant7.jpg", "description": "Modern hexagon design holding a highly reflective cluster of stones."},
        {"name": "Twisted Vine Botanical Pendant", "category": "pendants", "price": 2250, "image": "collection/pendant8.jpg", "description": "Delicately crafted leaf vine details winding around a pearl base."},
        {"name": "Modern Cushion Halo Charm", "category": "pendants", "price": 3800, "image": "collection/pendant9.jpg", "description": "Beautiful statement cushion cut zircon piece for heavy dress matching."},
        {"name": "Golden Sunburst Medallion", "category": "pendants", "price": 2700, "image": "collection/pendant10.jpg", "description": "Engraved premium metallic sunburst design for retro street styling."},
        {"name": "Freshwater Pearl Drop Necklace", "category": "pendants", "price": 3299, "image": "collection/pendant11.jpg", "description": "Selected premium white freshwater pearl locked in gold wiring."},
        {"name": "Marquise Luxury Cascade", "category": "pendants", "price": 4999, "image": "collection/pendant12.jpg", "description": "High end marquise crystals cascading downwards in an artisan fashion."},
        {"name": "Aura Chevron Minimal Layer", "category": "pendants", "price": 1850, "image": "collection/pendant13.jpg", "description": "Trendy V-shaped geometric sleek layering chain for college wear."},
        {"name": "Celestial Half Moon Pendant", "category": "pendants", "price": 2150, "image": "collection/pendant14.jpg", "description": "Delicate crescent moon layout detailed with tiny crystal alignment."},
        {"name": "Royal Crown Crest Locket", "category": "pendants", "price": 4100, "image": "collection/pendant15.jpg", "description": "Exquisite crown structure designed meticulously for party wear."},
        {"name": "Ethereal Heartbeat Lock Piece", "category": "pendants", "price": 2350, "image": "collection/pendant16.jpg", "description": "Heart line silhouette detailed beautifully with platinum polish."},

        # --- RINGS CATEGORY (13 Products) ---
        {"name": "Aura Solitaire Ring", "category": "rings", "price": 2499, "image": "collection/ring1.jpg", "description": "Elegant daily wear silver solitaire ring."},
        {"name": "Empress Ruby Ring", "category": "rings", "price": 3500, "image": "collection/ring2.jpg", "description": "Stunning ruby finish stone set in delicate silver wiring."},
        {"name": "Minimalist Rose Gold Band", "category": "rings", "price": 1499, "image": "collection/ring3.jpg", "description": "Sleek and stackable lightweight daily band."},
        {"name": "Vintage Emerald Halo Ring", "category": "rings", "price": 3999, "image": "collection/ring4.jpg", "description": "Beautiful green emerald crystal with a tiny stone halo."},
        {"name": "Infinity Eternal Band", "category": "rings", "price": 2999, "image": "collection/ring5.jpg", "description": "Continuous delicate rows of crystal zircons."},
        {"name": "Sapphire Royalty Ring", "category": "rings", "price": 4200, "image": "collection/ring6.jpg", "description": "Deep blue sapphire finish crystal for party wear."},
        {"name": "Princess Cut Glamour Ring", "category": "rings", "price": 3150, "image": "collection/ring7.jpg", "description": "Bold square-cut central diamond zircon piece."},
        {"name": "Twisted Vine Diamond Ring", "category": "rings", "price": 1850, "image": "collection/ring8.jpg", "description": "Intertwining beautiful silver design with micro-stones."},
        {"name": "Modern Cushion Cut Ring", "category": "rings", "price": 3600, "image": "collection/ring9.jpg", "description": "Contemporary cushion stone setting on platinum polish."},
        {"name": "Golden Sunburst Signet Ring", "category": "rings", "price": 2200, "image": "collection/ring10.jpg", "description": "Solid gold plated classic signet statement ring."},
        {"name": "Floral Pearl Cluster Ring", "category": "rings", "price": 1950, "image": "collection/ring12.jpg", "description": "Freshwater pearl beautifully clustered with crystals."},
        {"name": "Marquise Statement Ring", "category": "rings", "price": 4500, "image": "collection/ring13.jpg", "description": "Eye-catching marquise cut luxury festive band."},
        {"name": "Aura Chevron Diamond Ring", "category": "rings", "price": 1650, "image": "collection/ring14.jpg", "description": "V-shaped beautiful sleek chevron thumb or finger ring."},

        # --- BRACELETS CATEGORY (11 Products) ---
        {"name": "Aura Delicate Chain Bracelet", "category": "bracelets", "price": 1899, "image": "collection/bracelet1.jpg", "description": "Sleek silver chain perfect for layering."},
        {"name": "Premium Zircon Tennis Bracelet", "category": "bracelets", "price": 4500, "image": "collection/bracelet2.jpg", "description": "Classic row of brilliant-cut shiny zircon crystals."},
        {"name": "Minimalist Rose Gold Cuff", "category": "bracelets", "price": 2200, "image": "collection/bracelet3.jpg", "description": "Modern and smooth adjustable rose gold wrist cuff."},
        {"name": "Vintage Emerald Charm Bangle", "category": "bracelets", "price": 3800, "image": "collection/bracelet4.jpg", "description": "Stunning green charm accent on a silver lock bangle."},
        {"name": "Empress Golden Link Bracelet", "category": "bracelets", "price": 2999, "image": "collection/bracelet5.jpg", "description": "Thick premium golden textures for festive statement looks."},
        {"name": "Infinity Love Crystal Bracelet", "category": "bracelets", "price": 2400, "image": "collection/bracelet6.jpg", "description": "Beautiful intertwined infinity shape with micro stones."},
        {"name": "Floral Pearl Drop Bracelet", "category": "bracelets", "price": 2650, "image": "collection/bracelet7.jpg", "description": "Delicate chain accented with beautiful white pearls."},
        {"name": "Modern Geometric Line Bangle", "category": "bracelets", "price": 3100, "image": "collection/bracelet8.jpg", "description": "Minimalist cutwork design for contemporary styling."},
        {"name": "Twisted Silver Vine Bracelet", "category": "bracelets", "price": 1999, "image": "collection/bracelet9.jpg", "description": "Nature-inspired textured silver daily wrist wear."},
        {"name": "Royal Sapphire Accent Chain", "category": "bracelets", "price": 4150, "image": "collection/bracelet10.jpg", "description": "Gorgeous blue crystal gemstone centered on standard chain."},
        {"name": "Aura Sweetheart Charm Band", "category": "bracelets", "price": 1750, "image": "collection/bracelet11.jpg", "description": "Lovely hanging heart charm on an adjustable high-polish band."},

        # --- EARRINGS CATEGORY (14 Products) ---
        {"name": "Aura Classic Studs", "category": "earrings", "price": 1250, "image": "collection/earing1.jpg", "description": "Minimalist crystal studs for daily casual outfit rotation."},
        {"name": "Royal Drop Chandelier Earrings", "category": "earrings", "price": 3800, "image": "collection/earing2.jpg", "description": "Luxurious dangling stones for evening festive wear."},
        {"name": "Sleek Silver Huggies", "category": "earrings", "price": 1499, "image": "collection/earing3.jpg", "description": "Comfortable premium silver hoops for effortless daily use."},
        {"name": "Vintage Emerald Tassel Droppers", "category": "earrings", "price": 3400, "image": "collection/earing4.jpg", "description": "Vibrant emerald green gems beautifully framed with zircons."},
        {"name": "Golden Geo Statement Hoops", "category": "earrings", "price": 1950, "image": "collection/earing5.jpg", "description": "Thick metallic gold-plated statement structural statement loops."},
        {"name": "Freshwater Pearl Dangles", "category": "earrings", "price": 2600, "image": "collection/earing6.jpg", "description": "Timeless clean white baroque pearls matching fine silver pins."},
        {"name": "Sparkling Cushion Solitaire Drop", "category": "earrings", "price": 2999, "image": "collection/earing7.jpg", "description": "High brilliance square stones capturing maximal ambient light."},
        {"name": "Delicate Rose Gold Leaf Climbers", "category": "earrings", "price": 1850, "image": "collection/earing8.jpg", "description": "Organic leafy design tracing along the contour of the ear lobe."},
        {"name": "Minimalist Floating Linear Chain", "category": "earrings", "price": 1600, "image": "collection/earing9.jpg", "description": "Ultra fine threader chains with small starburst details."},
        {"name": "Midnight Sapphire Stud Halo Pieces", "category": "earrings", "price": 3150, "image": "collection/earing10.jpg", "description": "Deep blue sapphire core surrounding by crystal ring accents."},
        {"name": "Aura Elegant Blossom Clusters", "category": "earrings", "price": 2100, "image": "collection/earing11.jpg", "description": "Petal patterns sculpted in premium hypoallergenic alloys."},
        {"name": "Opulent Festive Jhumka Studs", "category": "earrings", "price": 4250, "image": "luxury gold."},
        {"name": "Asymmetrical Crescent Moon Hanging", "category": "earrings", "price": 1799, "image": "collection/earing13.jpg", "description": "Bohemian cosmic charm designs highlighting cubic zirconia lines."},
        {"name": "Empress Royal Crown Drops", "category": "earrings", "price": 3900, "image": "collection/earing14.jpg", "description": "Exquisite statement design for weddings or bridal parties."}
    ]

    # --- DATA INSERTION ---
    products_collection.insert_many(inventory_data)
    print("Mubarak ho! All 16 Pendants, 13 Rings, 11 Bracelets, and 14 Earrings synchronized into storage.")
    print("=======================================================\n")

except Exception as e:
    print("\n=======================================================")
    print(f" DATABASE CONNECTION ISSUE: {e}")
    print("=======================================================")
    print("Quick Check: Please make sure MongoDB Compass / Service is started in Windows Services.")
    print("Proceeding with active template architecture.\n")