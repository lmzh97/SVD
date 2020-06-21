import numpy as np

matrix = input("Please input list as matrix:\n")

if matrix == "default":
    matrix = np.array([[0,1],[1,1],[1,0]])
else:
    matrix = np.array(eval(matrix))

transpose = matrix.T

m_mt = np.matmul(matrix, transpose)
mt_m = np.matmul(transpose, matrix)

eigen_left, feature_left = np.linalg.eig(m_mt)
eigen_right, feature_right = np.linalg.eig(mt_m)

[m, n] = matrix.shape
k = min(m,n)
sigma_list = []

for i in range(k):
    sig_element = np.matmul(matrix, feature_right[:, i])[0]/feature_left[0,i]
    sigma_list.append(sig_element)

sigma = np.zeros(matrix.shape)

for j in range(k):
    sigma[j, j] = sigma_list[j]


print(feature_left)
print(feature_right)
print(sigma)
