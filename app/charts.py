import plotly.express as px

def restaurants_by_city(df):
    city_count = df["City"].value_counts().head(10).reset_index()
    city_count.columns = ["City", "Restaurants"]

    fig = px.bar(
        city_count,
        x="City",
        y="Restaurants",
        title="Top Cities by Number of Restaurants",
        color="City"
    )
    return fig.to_html(full_html=False)


def rating_by_city(df):
    rating_city = (
        df.groupby("City")["Aggregate rating"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        rating_city,
        x="City",
        y="Aggregate rating",
        title="Average Rating by City",
        color="Aggregate rating",
        color_continuous_scale="Viridis"
    )
    return fig.to_html(full_html=False)


def cuisine_distribution(df):
    cuisines = df["Cuisines"].str.split(", ").explode()
    top_cuisines = cuisines.value_counts().head(10).reset_index()
    top_cuisines.columns = ["Cuisine", "Count"]

    fig = px.pie(
        top_cuisines,
        names="Cuisine",
        values="Count",
        title="Top Cuisines Distribution"
    )
    return fig.to_html(full_html=False)