def is_prime(n):
    if n <= 1:
        print(False)
    else:
        prime_check = True  # establish variable to hold prime status
        for i in range(2, int(n**0.5) + 1): # run loop only up to square root because of how division and multiplication work. which i can sort of conceptualize in my head, but maybe lack the skill to describe in english?
            if n % i == 0: # modulo to see if n (the number we are testing) divides evenly by i (um, definition of prime?)
                prime_check = False
                break
        print(prime_check)


is_prime(2)     #Output: True 
is_prime(11)  #Output: True  
is_prime(15)  #Output: False  
is_prime(1)  #Output:  False  
is_prime(0) #Output:  False  
