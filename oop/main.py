from oop.class_static_methods_demo import Calculator

def main():
    #use nstatic method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    #use classmethod
    product_result = Calculator.muliply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
