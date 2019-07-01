import numpy as np
from sklearn.preprocessing import normalize, scale
from sklearn.covariance import ledoit_wolf

# Step 1 : Data Normalization
def mean_normalization(data):
    normed_matrix = scale(data, axis = 0, with_mean=True, with_std=False)
    return normed_matrix

# Step 2 : Calculating covariance matrix
def cov_matrix(normed_matrix):
    return np.cov(normed_matrix)

# Step 3 : Calculating eigenvalues and eigenvectors
def eigenvalues_eigenvectors(_cov_matrix):
    return np.linalg.eig(_cov_matrix)

# Step 4 : Construct the feature matrix
def feature_matrix(eigenvectors,dim=None):
    if (dim == None):
        dim = len(eigenvectors)
    elif(dim > len(eigenvectors)):
        print('Error out of dimention')
        return
    feature_matrix_ = eigenvectors[:,:dim]
    return feature_matrix_

# Step 5 : create new data 
def create_new_data(data,feature_matrix_):
    return np.matmul(np.array(feature_matrix_).T ,np.array(data).T)

if __name__ == "__main__":
    matrix = [
        [3,5,-1],
        [4,-3,-4],
        [12,9,2]
        ]
    
    normed_matrix = mean_normalization(matrix)
    print('Normalized matrix :\n {} \n'.format(normed_matrix))

    cov_matrix_ = cov_matrix(normed_matrix)
    print('Covarance matrix :\n {} \n'.format(cov_matrix_))

    eigenvalues, eigenvectors = eigenvalues_eigenvectors(cov_matrix_)
    print('Eigenvalues :\n {} \n'.format(eigenvalues))
    print('Eigenvectors :\n {} \n'.format(eigenvectors))

    feature_matrix_ = feature_matrix(eigenvectors,dim=2)
    print('Feature matrix :\n {} \n'.format(feature_matrix_))

    new_data = create_new_data(normed_matrix,feature_matrix_)
    print('new data matrix :\n {} \n'.format(new_data))