fruit = {'apples':2.0,'orange':3.0,'limes':4.0}
def buyLotsOfFruit(orderlist):
    cost=0.0
    order=0
    for order in orderlist:
        value=orderlist[order]
        cost += fruit[order]*value
    print("cost of ", fruit ," is ",cost)
    return cost

orderlist = {'apples':1.5,'orange':1.75,'limes':1.0}
buyLotsOfFruit(orderlist)
