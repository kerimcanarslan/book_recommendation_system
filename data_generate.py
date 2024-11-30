import pandas as pd
import numpy as np
import random
from faker import Faker 
from datetime import datetime, timedelta

def build_data(random_state):
    # Seeding for consistency
    np.random.seed(random_state)
    random.seed(random_state)
    Faker.seed(random_state)

    fake = Faker()

    # Customer IDs
    customer_ids = [np.random.randint(1, 101) for _ in range(10000)]

    # Book IDs
    np.random.seed(random_state+1)
    book_id = [np.random.randint(1, 31) for _ in range(10000)]

    # Page Views
    np.random.seed(random_state+2)
    page_views = [np.random.randint(1, 2) for _ in range(10000)]

    # View Dates
    Faker.seed(random_state+3)
    view_dates = [fake.date_between(start_date=datetime(2023, 6, 1), end_date=datetime(2023, 12, 31)) 
                  for _ in range(10000)]

    customer_interactions_df = pd.DataFrame({
        'customer_id': customer_ids,
        'book_id': [np.random.randint(1, 31) for _ in range(10000)],
        'page_views': page_views,
        'view_dates': view_dates
    })

    # Purchase Dates
    Faker.seed(random_state+4)  # Different seed for purchase dates
    purchase_dates = [fake.date_between(start_date=datetime(2023, 6, 1), end_date=datetime(2023, 12, 31)) 
                      for _ in range(10000)]

    # Purchase History
    random.seed(random_state+5)  # Reset seed for reproducibility
    purchase_history_df = pd.DataFrame({
        'customer_id': random.choices(customer_ids, k=10000),
        'book_id': [np.random.randint(1, 31) for _ in range(10000)],
        'purchase_dates': purchase_dates
    })

    # Book Titles and Details
    Faker.seed(random_state+6)
    book_titles = [f"{fake.catch_phrase()} of {fake.word().capitalize()}" for _ in range(1, 31)]

    np.random.seed(random_state+7)
    prices = [round(np.random.uniform(10, 500), 2) for _ in range(30)]

    np.random.seed(random_state+8)
    ratings = [round(np.random.uniform(1, 5), 1) for _ in range(30)]

    product_details_df = pd.DataFrame({
        'book_id': list(range(1, 31)),
        'book_name': book_titles,
        'price': prices,
        'rating':ratings
    })

    return customer_interactions_df, purchase_history_df, product_details_df
