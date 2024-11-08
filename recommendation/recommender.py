import pandas as pd
import algorithm
import random

df = pd.read_csv('data/recommender.csv', encoding='cp949')
def recommender(Age_Group = None, Sex = None, Item = None):
    """사용자 추천 알고리즘
    
    Args:
        Age_Group: 연령대
        Sex: 성별
        Item: 제품

    Returns:
        추천 상품
    """

    if Age_Group is not None and Item is not None and Sex is not None :
        """
            인식 상태
            연령대 O 제품 O 성별 O
        """
        ageGroupProductList = df.loc[(df.Age_Group == Age_Group) & (df.Sex == Sex)]
        goods = algorithm.get_recommend_product_list(ageGroupProductList, Item)
        return goods

    elif Age_Group is not None and Item is not None and Sex is None :
        """
            인식 상태
            연령대 O 제품 O 성별 X
        """
        ageGroupProductList = df.loc[df.Age_Group == Age_Group]
        goods = algorithm.get_recommend_product_list(ageGroupProductList, Item)
        return goods
    
    elif Age_Group is not None and Sex is None and Item is None :
        """
            인식 상태
            연령대 O 제품 X 성별 X 
        """
        ageGroupProductList = df.loc[(df.Age_Group == Age_Group), 'Product'].tolist()

        if len(ageGroupProductList) >= 2:
            goods = random.sample(ageGroupProductList, 2)
        else:
            goods = ageGroupProductList

        return goods
    
    elif Age_Group is not None and Item is None and Sex is not None:
        """
            인식 상태
            연령대 O 제품 X 성별 O
        """
        ageGroupProductList = df.loc[(df.Age_Group == Age_Group) & (df.Sex == Sex), 'Product'].tolist()

        if len(ageGroupProductList) >= 2:
            goods = random.sample(ageGroupProductList, 2)
        else:
            goods = ageGroupProductList

        return goods
    
    elif Age_Group is None and Item is None and Sex is None:
        """
            인식 상태
            연령대 X 제품 X 성별 X
        """
        ageGroupProductList = df['Product'].to_list()

        if len(ageGroupProductList) >= 2:
            goods = random.sample(ageGroupProductList, 2)
        else:
            goods = ageGroupProductList

        return goods
    
product = recommender(Age_Group='8-12', Sex='Female', Item="가방")
print(product)