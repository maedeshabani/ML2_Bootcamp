def find(num1, num2, num3):
    main_set={1,2,3,4}
    test_set={num1, num2, num3}
    for num in test_set:
        result= main_set.symmetric_difference(test_set)
    for x in result:
        print(x)
find(1,2,3)
find(2,4,1)
find(3,2,4)
