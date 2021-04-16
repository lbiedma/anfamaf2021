def horn(coefs,x):
	# coefs = [a_n, a_{n-1}, ... , a_1, a_0]
	#		   0    1              n-1  , n
	n = len(coefs)-1 # n = grado del polinomio

	# p = a_n
	p = coefs[0]

#	for k in range(1,n+1):
#		# p <- a_k + x * p
#		p = coefs[k] + x*p

	for coef in coefs[1:]:
		p = coef + x*p

	return p
