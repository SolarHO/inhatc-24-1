from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommend_product_list(df, product):
    """ 사용자 착용 제품에서 유사도 상위 제품 추천
    Args:
        df: 상품 CSV 파일
        product: 감지된 제품

    Returns:
        추천 제품
    """
    df = df.copy()
    df['Combined'] = df['Product'] + ' ' + df['Keywords'].fillna('')
    df = df.reset_index(drop=True)

    # 텍스트 벡터화
    count_vector = CountVectorizer(ngram_range=(1, 3))
    c_vector_combined = count_vector.fit_transform(df['Combined'])

    # 코사인 유사도 계산 및 정렬
    combined_c_sim = cosine_similarity(c_vector_combined, c_vector_combined).argsort()[:, ::-1]

    # 입력한 제품에 해당하는 인덱스 찾기
    if product not in df['Product'].values:
        return print("없는 제품")

    target_index = df[df['Product'] == product].index.values[0]

    # 자기 자신을 제외하고 상위 2개의 유사한 제품 추천
    sim_index = combined_c_sim[target_index, 1:3]  # 상위 2개 유사 제품의 인덱스 추출

    # 추천 제품 출력
    recommended_products = df['Product'].iloc[sim_index].values    
    return recommended_products