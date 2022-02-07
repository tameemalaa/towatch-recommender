from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class recommender:
    def __init__(self, data : DataFrame , features_label : str):
        """[summary]

        Args:
            data (DataFrame): [description]
            features_label (str): [description]
        """
        self.data = data
        self.features_label = features_label
        self.count_vectorizer = CountVectorizer()
        self.count_matrix =self.vectorize()
        self.sim_matrix = self.fit()

    def vectorize(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        self.count_matrix = self.count_vectorizer.fit_transform(self.data[self.features_label])
        return self.count_matrix

    def print_count_matrix(self):
        print("Count Matrix:", self.count_matrix.toarray())

    def print_sim_matrix(self):
        """[summary]
        """
        print ("Sim Matrix:", self.sim_matrix)

    def fit(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        self.sim_matrix = cosine_similarity(self.count_matrix)
        return self.sim_matrix

    def recommend(self, id : int , n_recommendations : int = 1):
        """[summary]

        Args:
            id (int): [description]
            n_recommendations (int, optional): [description]. Defaults to 1.

        Returns:
            [type]: [description]
        """
        return (i[0] for i in list(enumerate(self.sim_matrix[id])).sort(key=lambda x:x[1], reverse=True)[:n_recommendations])

