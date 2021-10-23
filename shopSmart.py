def getPriceOfOrder(shop,orderlist):
    cost=0.0
    order=0
    for order in orderlist:
        value=orderlist[order]
        cost += shop[order]*value
    return cost
FruitShop={'shop1','shop2'}
def shopSmart(orderlist) :
    bestShop = shops[0]
    lowcost = getPriceOfOrder(shop1,orderlist)
    cost =getPriceOfOrder(shop2,orderlist)
    if cost < lowcost :
        bestShop = shops[1]
        lowcost = cost
    print("For orders " ,orders,"the best shop is ",bestShop)      
    return bestShop

dir1={'apples':2.0,'oranges':1.0}
shop1=dir1
dir2={'apples':1.0,'oranges':5.0}
shop2=dir2
shops=['shop1','shop2']

orders={'apples':1.0,'oranges':3.0}
s=shopSmart(orders)

orders={'apples':3.0}
s=shopSmart(orders)

orders={'oranges':2.0}
s=shopSmart(orders)
