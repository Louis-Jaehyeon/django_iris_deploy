# from django.apps import AppConfig


# class IrisConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'iris'

import os

import joblib
import pickle
from django_iris_deploy import settings
from django.apps import AppConfig
import os


# class IrisConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'iris'
    
#     # for ai_model load
#     def ready(self):
#         # 전역 변수로 모델 로드
#         global ml_model
#         # model_path = os.path.join(settings.BASE_DIR, 'static/models/iris_model_rfc.pkl')
#         model_path = os.path.join(settings.BASE_DIR, 'static/models/iris_model_rfc.joblib')
#         with open(model_path, 'rb') as f:
#             # self.ml_model = pickle.load(f)
#             self.ml_model = joblib.load(f)
#         print("AI 모델 로딩 완료!")


from django.apps import AppConfig
import os
import pickle

class IrisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iris'

    def ready(self):
        # 모델 경로 설정
        model_path = os.path.join(os.path.dirname(__file__), 'static', 'models', 'iris_model_rfc.pkl')
        with open(model_path, 'rb') as f:
            self.ml_model = pickle.load(f)