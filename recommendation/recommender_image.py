import pandas as pd
import algorithm_image
import random

df = pd.read_csv('data/recommender.csv', encoding='euc-kr')
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
        goods, img = algorithm_image.get_recommend_product_list(ageGroupProductList, Item)
        if(len(ageGroupProductList) == 0):
            ageGroupProductList = df['index'].to_list()
            index = random.sample(ageGroupProductList, 1)
            goods = df.loc[(df.index == index[0]), 'Product'].tolist()
            img = df.loc[(df.index == index[0]), 'Image'].tolist()
            goods = goods[0]
            img = img[0]
        return goods, img

    elif Age_Group is not None and Item is not None and Sex is None :
        """
            인식 상태
            연령대 O 제품 O 성별 X
        """
        ageGroupProductList = df.loc[df.Age_Group == Age_Group]
        goods, img = algorithm_image.get_recommend_product_list(ageGroupProductList, Item)
        if(len(ageGroupProductList) == 0):
            ageGroupProductList = df['index'].to_list()
            index = random.sample(ageGroupProductList, 1)
            goods = df.loc[(df.index == index[0]), 'Product'].tolist()
            img = df.loc[(df.index == index[0]), 'Image'].tolist()
            goods = goods[0]
            img = img[0]
        return goods, img
    
    elif Age_Group is not None and Sex is None and Item is None :
        """
            인식 상태
            연령대 O 제품 X 성별 X 
        """
        ageGroupProductList = df.loc[(df.Age_Group == Age_Group), 'index'].tolist()
        if(len(ageGroupProductList) == 0):
            ageGroupProductList = df['index'].to_list()
            index = random.sample(ageGroupProductList, 1)
            goods = df.loc[(df.index == index[0]), 'Product'].tolist()
            img = df.loc[(df.index == index[0]), 'Image'].tolist()
        elif len(ageGroupProductList) >= 2:
            index = random.sample(ageGroupProductList, 1)
            goods = df.loc[(df.index == index[0]), 'Product'].tolist()
            img = df.loc[(df.index == index[0]), 'Image'].tolist()
        else:
            goods = df.loc[(df.index == ageGroupProductList[0]), 'Product'].tolist()
            img = df.loc[(df.index == ageGroupProductList[0]), 'Image'].tolist()

        return goods[0], img[0]
    
    elif Age_Group is not None and Item is None and Sex is not None:
        """
            인식 상태
            연령대 O 제품 X 성별 O
        """
        ageGroupProductList = df.loc[(df.Age_Group == Age_Group) & (df.Sex == Sex), 'index'].tolist()
        if(len(ageGroupProductList) == 0):
            ageGroupProductList = df['index'].to_list()
            index = random.sample(ageGroupProductList, 1)
            goods = df.loc[(df.index == index[0]), 'Product'].tolist()
            img = df.loc[(df.index == index[0]), 'Image'].tolist()
        elif len(ageGroupProductList) >= 2:
            index = random.sample(ageGroupProductList, 1)
            goods = df.loc[(df.index == index[0]), 'Product'].tolist()
            img = df.loc[(df.index == index[0]), 'Image'].tolist()
        else:
            goods = df.loc[(df.index == ageGroupProductList[0]), 'Product'].tolist()
            img = df.loc[(df.index == ageGroupProductList[0]), 'Image'].tolist()

        return goods[0], img[0]
    
    elif Age_Group is None and Item is None and Sex is None:
        """
            인식 상태
            연령대 X 제품 X 성별 X
        """
        ageGroupProductList = df['index'].to_list()
        index = random.sample(ageGroupProductList, 1)
        goods = df.loc[(df.index == index[0]), 'Product'].tolist()
        img = df.loc[(df.index == index[0]), 'Image'].tolist()

        return goods[0], img[0]

