from sklearn.base import BaseEstimator, TransformerMixin
import pickle
import numpy as np
import pandas as pd

class DateTransformer(BaseEstimator, TransformerMixin):
            def fit(self, X, y=None):
                return self
            
            
            def transform(self, X, y=None):
                X['joining_date'] = pd.to_datetime(X.joining_date, format="%Y/%m/%d")
                X['joining_day'] = X.joining_date.dt.day
                X['joining_month'] = X.joining_date.dt.month
                X['joining_year'] = X.joining_date.dt.year
                

                # extract hour, minutes and seconds
                X[['last_visit_time_hour','last_visit_time_minutes','last_visit_time_seconds']] = X['last_visit_time'].astype(str).str.split(':', expand=True).astype(int)
                
                X["avg_frequency_login_days"] = X["avg_frequency_login_days"].astype(float).fillna(round(X["avg_frequency_login_days"].astype(float).mean()))

                return np.c_[X.drop(['joining_date', 'last_visit_time'], axis=1)]
            
            
            def fit_transform(self, X, y=None):
                return self.fit(X, y).transform(X, y)


def predict_test(data):
    age = int(data['age'])
    gender = data['gender']
    region_category = data['region_category']
    membership_category = data['membership_category']
    joining_date = data['date']
    joined_through_referral = data['joined_through_referral']
    preferred_offer_types = data['preferred_offer_types']
    medium_of_operation = data['medium_of_operation']
    internet_option = data['internet_option']
    last_visit_time = data['time']
    days_since_last_login = int(data['last_login'])
    avg_time_spent = float(data['avg_time_spent'])
    avg_transaction_value = float(data['avg_transaction_value'])
    avg_frequency_login_days = float(data['avg_frequency_login_days'])
    points_in_wallet = float(data['points_in_wallet'])
    used_special_discount = data['used_special_discount']
    offer_application_preference = data['offer_application_preference']
    past_complaint = data['past_complaint']
    feedback = data['feedback']

    test = pd.DataFrame(
                    [[age, gender, region_category, membership_category, joining_date, joined_through_referral, 
                    preferred_offer_types, medium_of_operation, internet_option, last_visit_time, days_since_last_login, 
                    avg_time_spent, avg_transaction_value, avg_frequency_login_days, points_in_wallet, used_special_discount, 
                    offer_application_preference, past_complaint, feedback]],             
                    
                    columns=['age', 'gender', 'region_category', 'membership_category', 'joining_date', 'joined_through_referral', 
                            'preferred_offer_types', 'medium_of_operation', 'internet_option', 'last_visit_time', 'days_since_last_login', 
                            'avg_time_spent', 'avg_transaction_value', 'avg_frequency_login_days', 'points_in_wallet', 'used_special_discount',
                            'offer_application_preference', 'past_complaint', 'feedback']
    )

    # load saved model
    model = pickle.load(open('classifier.pkl', 'rb'))

    return model.predict(test)[0]