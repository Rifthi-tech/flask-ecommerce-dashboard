from flask import Flask, render_template
from data_loader import load_data
from charts import restaurants_by_city, rating_by_city, cuisine_distribution

app = Flask(__name__)

df = load_data()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sales")
def sales():
    city_chart = restaurants_by_city(df)
    rating_chart = rating_by_city(df)

    return render_template(
        "sales.html",
        city_chart=city_chart,
        rating_chart=rating_chart
    )

@app.route("/products")
def products():
    cuisine_chart = cuisine_distribution(df)

    top_restaurants = (
        df.sort_values("Aggregate rating", ascending=False)
        .head(10)[["Restaurant Name", "City", "Aggregate rating", "Votes"]]
    )

    return render_template(
        "products.html",
        cuisine_chart=cuisine_chart,
        tables=top_restaurants.to_html(index=False)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)