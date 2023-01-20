#define the function to predict the maximum price
def findmaxprice(price):
    #take minumum_price
    min_price=float('inf')
    #take the max_price as 0
    max_price=0
    #define the loop for iteration to the entire the element's in the array
    for i in range(len(price)):
        #define the condition if the index of the price less then the store the min_price as that index
        if price[i]<min_price:
            min_price=price[i]
        #if the first condition not true check 
        elif price[i]-min_price>max_price:
            max_price=price[i]-min_price
    return max_price



price_stock=[7,22,52,5,23,4]
result=findmaxprice(price_stock)
print('The Maximum price in the stock',result)