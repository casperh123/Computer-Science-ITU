def dot_product(v1, v2):
    sum = 0;


    for i in range(len(v1)):
        sum = sum + v1[i] * v2[i]

    return sum


testcases = int(input());

for i in range(testcases):
    vector_length = int(input())
    vector_1 = [int(point) for point in input().split(" ")]
    vector_2 = [int(point) for point in input().split(" ")]

    vector_1.sort();
    vector_2.sort(reverse=True);

    product = dot_product(vector_1, vector_2)

    print(f"Case #{i+1}: {product}")