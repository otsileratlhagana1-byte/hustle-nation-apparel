from flask import Flask, render_template, request, jsonify
from urllib.parse import quote

app = Flask(__name__)

PRODUCTS = [
    # Mind Full of Money
    {"id": 1, "name": "Mind Full of Money Hoodie", "category": "Mind Full of Money", "type": "Hoodies", "price": 290, "image": "tee-collection.jpg", "tag": "Streetwear"},
    {"id": 2, "name": "Mind Full of Money Sweatshirt", "category": "Mind Full of Money", "type": "Sweatshirts", "price": 250, "image": "tee-collection.jpg", "tag": "Streetwear"},
    {"id": 3, "name": "Mind Full of Money T-Shirt", "category": "Mind Full of Money", "type": "T-shirts", "price": 150, "image": "tee-collection.jpg", "tag": "Graphic Tee"},
    {"id": 4, "name": "Mind Full of Money Sweatpants", "category": "Mind Full of Money", "type": "Sweatpants", "price": 150, "image": "sweatpants.jpg", "tag": "Bottoms"},

    # Young Money
    {"id": 5, "name": "Young Money Hoodie", "category": "Young Money Design", "type": "Hoodies", "price": 290, "image": "tee-collection.jpg", "tag": "Streetwear"},
    {"id": 6, "name": "Young Money Sweatshirt", "category": "Young Money Design", "type": "Sweatshirts", "price": 250, "image": "tee-collection.jpg", "tag": "Streetwear"},
    {"id": 7, "name": "Young Money T-Shirt", "category": "Young Money Design", "type": "T-shirts", "price": 150, "image": "tee-collection.jpg", "tag": "Graphic Tee"},
    {"id": 8, "name": "Young Money Sweatpants", "category": "Young Money Design", "type": "Sweatpants", "price": 150, "image": "sweatpants.jpg", "tag": "Bottoms"},

    # Classic
    {"id": 9, "name": "Classic Design Hoodie", "category": "Classic Design", "type": "Hoodies", "price": 290, "image": "24-raglan-front.jpg", "tag": "Classic"},
    {"id": 10, "name": "Classic Design Sweatshirt", "category": "Classic Design", "type": "Sweatshirts", "price": 250, "image": "24-raglan-front.jpg", "tag": "Classic"},
    {"id": 11, "name": "Classic Design T-Shirt", "category": "Classic Design", "type": "T-shirts", "price": 150, "image": "24-raglan-tees.jpg", "tag": "Graphic Tee"},
    {"id": 12, "name": "Classic Design Sweatpants", "category": "Classic Design", "type": "Sweatpants", "price": 150, "image": "sweatpants.jpg", "tag": "Bottoms"},

    # Boys & Girls Club
    {"id": 13, "name": "Boys & Girls Club Hoodie", "category": "Boys and Girls Club Design", "type": "Hoodie", "price": 300, "image": "girls-club.jpg", "tag": "Girls Club"},
    {"id": 14, "name": "Boys & Girls Club Sweatshirt", "category": "Boys and Girls Club Design", "type": "Sweatshirts", "price": 250, "image": "girls-club.jpg", "tag": "Girls Club"},
    {"id": 15, "name": "Boys & Girls Club T-Shirt", "category": "Boys and Girls Club Design", "type": "T-shirts", "price": 200, "image": "girls-club.jpg", "tag": "Girls Club"},
    {"id": 16, "name": "Boys & Girls Club Sweatpants", "category": "Boys and Girls Club Design", "type": "Sweatpants", "price": 190, "image": "sweatpants.jpg", "tag": "Girls Club"},

    # Newspaper
    {"id": 17, "name": "Newspaper Design Hoodie", "category": "Newspaper Design", "type": "Hoodies", "price": 340, "image": "tee-collection.jpg", "tag": "Newspaper"},
    {"id": 18, "name": "Newspaper Design Sweatshirt", "category": "Newspaper Design", "type": "Sweatshirts", "price": 250, "image": "tee-collection.jpg", "tag": "Newspaper"},
    {"id": 19, "name": "Newspaper Design T-Shirt", "category": "Newspaper Design", "type": "T-shirts", "price": 200, "image": "newspaper-tees.jpg", "tag": "Newspaper"},
    {"id": 20, "name": "Newspaper Design Sweatpants", "category": "Newspaper Design", "type": "Sweatpants", "price": 190, "image": "sweatpants.jpg", "tag": "Bottoms"},

    # HN
    {"id": 21, "name": "HN Design Hoodie", "category": "HN Design", "type": "Hoodies", "price": 340, "image": "24-raglan-front.jpg", "tag": "Hustle Nation"},
    {"id": 22, "name": "HN Design Sweatshirt", "category": "HN Design", "type": "Sweatshirts", "price": 250, "image": "24-raglan-front.jpg", "tag": "Hustle Nation"},
    {"id": 23, "name": "HN Design T-Shirt", "category": "HN Design", "type": "T-shirts", "price": 200, "image": "24-raglan-tees.jpg", "tag": "Hustle Nation"},
    {"id": 24, "name": "HN Design Sweatpants", "category": "HN Design", "type": "Sweatpants", "price": 190, "image": "sweatpants.jpg", "tag": "Bottoms"},

    # Classic Edition
    {"id": 25, "name": "Classic Edition Hoodie", "category": "Classic Edition Design", "type": "Hoodies", "price": 340, "image": "24-raglan-front.jpg", "tag": "Edition"},
    {"id": 26, "name": "Classic Edition Sweatshirt", "category": "Classic Edition Design", "type": "Sweatshirts", "price": 250, "image": "24-raglan-front.jpg", "tag": "Edition"},
    {"id": 27, "name": "Classic Edition T-Shirt", "category": "Classic Edition Design", "type": "T-shirts", "price": 200, "image": "24-raglan-tees.jpg", "tag": "Edition"},
    {"id": 28, "name": "Classic Edition Sweatpants", "category": "Classic Edition Design", "type": "Sweatpants", "price": 190, "image": "sweatpants.jpg", "tag": "Bottoms"},
    {"id": 29, "name": "Classic Edition School Bag", "category": "Classic Edition Design", "type": "School bags", "price": 200, "image": "backpack.jpg", "tag": "Accessories"},

    # Headwear
    {"id": 30, "name": "Hustle Nation Panel Cap", "category": "Headwear", "type": "Panel caps", "price": 70, "image": "backpack.jpg", "tag": "Headwear"},
    {"id": 31, "name": "Hustle Nation Slouchy Beanie", "category": "Headwear", "type": "Slouchy beanies", "price": 80, "image": "girls-club.jpg", "tag": "Headwear"},
    {"id": 32, "name": "Hustle Nation Beanie", "category": "Headwear", "type": "Beanies", "price": 70, "image": "girls-club.jpg", "tag": "Headwear"},
    {"id": 33, "name": "Hustle Nation Knitted Beanie", "category": "Headwear", "type": "Knitted beanies", "price": 150, "image": "girls-club.jpg", "tag": "Headwear"},

    # Mafia Tracksuits
    {"id": 34, "name": "Mafia Tracksuit Top", "category": "Mafia Tracksuits", "type": "Mafia top", "price": 400, "image": "mafia-tracksuit.jpg", "tag": "Tracksuit"},
    {"id": 35, "name": "Mafia Tracksuit Pants", "category": "Mafia Tracksuits", "type": "Mafia pants", "price": 300, "image": "mafia-tracksuit.jpg", "tag": "Tracksuit"},
    {"id": 36, "name": "Mafia Shorts", "category": "Mafia Tracksuits", "type": "Mafia shorts", "price": 150, "image": "mafia-tracksuit.jpg", "tag": "Tracksuit"},
    {"id": 37, "name": "Mafia Two Piece Tracksuit", "category": "Mafia Tracksuits", "type": "Two piece tracksuits", "price": 650, "image": "mafia-tracksuit.jpg", "tag": "Tracksuit"},

    # Mafia 2nd Edition
    {"id": 38, "name": "Mafia Tracksuits 2nd Edition Top", "category": "Mafia Tracksuits 2nd Edition", "type": "Mafia top", "price": 450, "image": "mafia-tracksuit.jpg", "tag": "2nd Edition"},
    {"id": 39, "name": "Mafia Tracksuits 2nd Edition Trackpants", "category": "Mafia Tracksuits 2nd Edition", "type": "Mafia Trackpants", "price": 350, "image": "mafia-tracksuit.jpg", "tag": "2nd Edition"},
    {"id": 40, "name": "Mafia Tracksuits 2nd Edition Two Piece", "category": "Mafia Tracksuits 2nd Edition", "type": "Two piece", "price": 750, "image": "mafia-tracksuit.jpg", "tag": "2nd Edition"},
]

CATEGORIES = [
    "All", "Mind Full of Money", "Young Money Design", "Classic Design",
    "Boys and Girls Club Design", "Newspaper Design", "HN Design",
    "Classic Edition Design", "Headwear", "Mafia Tracksuits",
    "Mafia Tracksuits 2nd Edition"
]

@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS, categories=CATEGORIES)

@app.route("/api/products")
def api_products():
    return jsonify(PRODUCTS)

@app.route("/api/order", methods=["POST"])
def order():
    data = request.get_json(silent=True) or {}
    customer = data.get("customer", {})
    items = data.get("items", [])
    total = data.get("total", 0)

    lines = ["HUSTLE NATION APPAREL ORDER", ""]
    lines.append(f"Customer: {customer.get('name','')}")
    lines.append(f"Phone: {customer.get('phone','')}")
    lines.append(f"Address: {customer.get('address','')}")
    lines.append("")
    for item in items:
        lines.append(f"{item.get('qty',1)} x {item.get('name','')} - R{item.get('price',0)} each")
    lines.append("")
    lines.append(f"TOTAL: R{total}")
    message = quote("\n".join(lines))
    return jsonify({"whatsapp": f"https://wa.me/27698881104?text={message}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
