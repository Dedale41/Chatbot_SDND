from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
import pandas as pd
import pickle
import os 


def create_model(queries_dataset, path_to_model) : 
    model = make_pipeline(TfidfVectorizer(), MLPClassifier(activation= 'relu', alpha= 0.001, hidden_layer_sizes= (50, 100, 50), solver= 'lbfgs'))
    queries = pd.read_csv(queries_dataset, sep = ",") 

    X = queries["Query"]
    y = queries["Label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    model.fit(X_train, y_train) 

    test_predictions = model.predict(X_test)

    print("--Accuracy--")
    print(accuracy_score(y_test, test_predictions))
    print("--Classification Report--")
    print(classification_report(y_test, test_predictions))

    with open(path_to_model, 'wb') as model_file:
        pickle.dump(model, model_file)


def import_model (path_to_model) : 
    with open(path_to_model, 'rb') as model_file:
        model = pickle.load(model_file)
        return model 


def predict_query (model, query) : 
    prediction = model.predict([query])[0]
    proba = model.predict_proba([query])[0]

    best_prob = max(proba)
    threshold = 0.5
    tab_of_features = []
    for idx, elem in enumerate(proba) :
        if elem > threshold*best_prob : 
            tab_of_features.append(model.classes_[idx])

    return(tab_of_features)



def get_all_proba(model, query) :
    proba = model.predict_proba([query])[0]
    for idx, elem in enumerate(proba) : 
        print(model.classes_[idx], elem)




def tune_model(data_path, quiet=False):
    queries = pd.read_csv(data_path, sep = ",") 

    X = queries["Query"][0:50000]
    y = queries["Label"][0:50000]

    param_grid = {
             'hidden_layer_sizes': [(50,50,50), (50,100,50), (100,)],
             'activation': ['tanh', 'relu', 'logistic'],
             'solver': ['sgd', 'adam'],
             'alpha': [0.0001, 0.05],
             'learning_rate': ['constant','adaptive']
            }

    transformer = TfidfVectorizer() 
    X_trans = transformer.fit_transform(X)

    if not quiet:
        print("Spliting dataset into k consecutive folds.")

    cv = KFold(n_splits=2, random_state=None, shuffle=False)

    if not quiet:
        print("done.")
        print("Starting GridSearchCV() - this might take a while...")

    grid_search = GridSearchCV(estimator=MLPClassifier(), param_grid=param_grid,
                               cv=cv, scoring='accuracy', error_score=0,
                               verbose=4)

    grid_search.fit(X_trans, y)

    if not quiet:
        print("done.")
        print("\n\nBest: %f using %s\n\n" % (grid_search.best_score_,
              grid_search.best_params_))

    print("best estimator :", grid_search.best_estimator_)

    return grid_search.best_estimator_




if __name__ == "__main__":
    queries_path = os.path.join("Queries", "queries.csv")
    model_path = os.path.join("Model", "model.pickle")
    create_model(queries_path, model_path)
    # model = import_model("model.pickle")
    # query = "pourrais-je imprimer doc1 de 100 pages ?"
    # get_all_proba(model, query) 
    # tab = predict_query(model, query)
    # print(tab)


