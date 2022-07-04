import numpy as np
import numpy.linalg as la
np.set_printoptions(precision=4, suppress=True)
# a = np.array([[1,2,3,4],[1,1,2,3],[0,1,1,0]])
# print(a)
# print()
# u,s,vh = la.svd(a, full_matrices=True)
# # print(u)
# # print()
# # print(u.dot(u.T))
# # print()
# # print(vh)
# # print()
# # print(vh.dot(vh.T))
# # print()
# # print(s)
# # print()
# sd = np.diag(s)
# print(sd)
# print()
# b=np.zeros((3,4))
# b[:,:-1]=sd
# sigma=b
# print(sigma)
# print()
# print(np.dot(np.dot(u,sigma),vh))
# print()

# # Doing Low-Rank Approximation
# # Replacing s[2] with zero as it is pretty close to zero
# s[2] = 0
# print(s)
# print()
# sd = np.diag(s)
# print(sd)
# print()
# b=np.zeros((3,4))
# b[:,:-1]=sd
# sigma=b
# print(sigma)
# print()
# print(np.dot(np.dot(u,sigma),vh))

# Example: 2
an = np.array([[1,2,3,4],[1,1,2,3],[0,1,1,0],[0,2,2,0],[0,5,5,0]])
print(an)
print()
u,s,vh = la.svd(an, full_matrices=True)
# print(u)
# print()
# print(u.dot(u.T))
# print()
# print(vh)
# print()
# print(vh.dot(vh.T))
# print()
# print(s)
# print()

# [9.2296 4.4454 0.2312 0.    ]

s[2]=0
sd = np.diag(s)
sigma = np.zeros((5,4))
sigma[:4,:] = sd
print(sigma)
print()
print(np.dot(np.dot(u,sigma),vh))