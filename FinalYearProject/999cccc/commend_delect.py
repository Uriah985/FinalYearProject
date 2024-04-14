from bs4 import BeautifulSoup
from flask import request

# path = input('Please input the path of the web you want to get the price:\n')
dp1 = 'web.html'
dp2 = 'web2.html'
dp3 = 'web3.html'
dp = [dp1, dp2, dp3]

# path = 'web.html' # here's the path of the web


def sWeb(path):  # the output list name is 0 price is 1
    r = open(path, "r")
    html = r.read()

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table")
    headings = [th.get_text().strip() for th in table.find("tr").find_all("th")]

    datasets = []
    for row in table.find_all("tr")[1:]:
        dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
        datasets.append(dataset)

    name = []
    price = []
    for x in range(len(datasets)):
        z = datasets[x]
        name.append(z.get("Item Name"))
        price.append(z.get("Price"))
    result = []
    result.append(name)
    result.append(price)
    return result


def find_price_by_item(Iname, name, price):
    count = 0
    for x in name:
        if x == Iname:
            print(f"The price of {x} is {price[count]}")
            return price[count]

        count += 1
    if count > len(name):
        print("item not found")


def price_finder(address, item_name):
    print(item_name)
    tpath = address
    if tpath == (1):
        path = dp1
    else:
        if tpath == (2):
            path = dp2
        else:
            if tpath == (3):
                path = dp3
            else:
                path = tpath
            print(f"The path is {path}\n")

    t = 0
    while t == 0:
        count = len(item_name)
        try:
            count = int(count)
        except ValueError:
            print('Wrong input, please input another value')
        else:
            t = 1

    result = []
    #for temp in range(count):
    x = sWeb(path)  # name is 0 price is 1
    name = x[0]
    price = x[1]

    item = item_name
    result.append(find_price_by_item(item, name, price))  # change the first parameter to change the item which you want to get the price

    Nresult = []
    c = 0
    print(type(item_name))
    if type(item_name) == str:
        a = f"The price of {item_name} in {address} is {result}"
        result = ''.join(map(str, a))
    else:
        a = f"The price of {item_name[c]} in {address} is {result}"
        result = ''.join(map(str, a))
    #if count > 1:
    #NNresult = '\n'.join(map(str, Nresult))
    return result
    #else:
        #result = result[0]
        #return result


def compare(noOfS, item_name, store):

    count = noOfS

    item = item_name
    name = []
    price = []
    result = []
    if count == '0':
        for temp in range(3):
            x = sWeb(dp[temp])
            name.append(x[0])
            price.append(x[1])
            result.append(find_price_by_item(item, name[temp], price[temp]))

        #new_result = [float(i[1:]) for i in result]  # fk this shxx
        #result = new_result
        result_price = min(result)
        #return result_price
        result_no = []
        for temp in range(3):
            if result_price == result[temp]:
                y = temp + 1
                result_no.append(y)
        if len(result_no) == 1:
            return f'The lowest price of {item} amoung Store 1, Store 2 and Store 3 is {result_price} in Store{result_no}'
        elif len(result_no) > 1:
            temp = ''  # Start(change the result no. to the format of Store X and Store Y and Stoe Z that can be printed directly)
            count = 2
            for i in result_no:
                if count == len(result_no):
                    temp = str(i)
                elif count != 0:
                    temp = temp + ' and Store ' + str(i)
                elif count == 0:
                    temp = temp + i
                count -= 1
            result_no = temp  # End of the change
            print(f'The lowest price of {item} amoung Store 1, Store 2 and Store 3 is {result_price} in Store{result_no}')
            return f'The lowest price of {item} amoung Store 1, Store 2 and Store 3 is {result_price} in Store{result_no}'

    else:
        nStore = []
        temp = 0
        for i in store:
            tpath = i
            if tpath == (1):
                path = dp1
            else:
                if tpath == (2):
                    path = dp2
                else:
                    if tpath == (3):
                        path = dp3
                    else:
                        path = tpath
            print(f"The path is {path}\n")

            x = sWeb(path)
            name.append(x[0])
            price.append(x[1])
            result.append(find_price_by_item(item, name[temp], price[temp]))
            temp += 1

        #new_result = [float(i[1:]) for i in result]  # fk this shxx
        #result = new_result  # end of remove the '$' sign

        result_price = min(result)
        result_no = []
        for temp in range(count):
            if result_price == result[temp]:
                y = temp + 1
                result_no.append(y)

        if len(result_no) == 1:
            print(f'The lowest price of {item} amoung those Store is ${result_price} in Store{result_no[0]}')
        elif len(result_no) > 1:

            temp = ''  # Start(change the result no. to the format of Store X and Store Y and Stoe Z that can be printed directly)
            count = len(result_no)
            for i in result_no:
                if count == len(result_no):
                    temp = str(i)
                elif count != 0:
                    temp = temp + ' and Store ' + str(i)
                elif count == 0:
                    temp = temp + i
                count -= 1
            result_no = temp  # End of the change

            a = str(item_name)
            b = str(result_price)
            c = str(result_no)
            print(f"The lowest price of {a} amoung those Store is ${b} in Store {c}")
            return f"The lowest price of {a} amoung those Store is ${b} in Store {c}"



        print(
            f'Please input the local address of the web store you want to compare separetely\n (Type 1 for Store 1, type 2 for Store 2, and type 3 for Store 3)\n')
        for temp in range(count):

            if temp != 0:
                print(
                    f'Please type another web address\n (Type 1 for Store 1, type 2 for Store 2, and type 3 for Store 3)\n')

            tpath = store

            if tpath == (1):
                path = dp1
            else:
                if tpath == (2):
                    path = dp2
                else:
                    if tpath == (3):
                        path = dp3
                    else:
                        path = tpath
            print(f"The path is {path}\n")

            x = sWeb(path)
            name.append(x[0])
            price.append(x[1])
            result.append(find_price_by_item(item, name[temp], price[temp]))

        new_result = [float(i[1:]) for i in result]  # fk this shxx
        result = new_result  # end of remove the '$' sign

        result_price = min(result)
        result_no = []
        for temp in range(count):
            if result_price == result[temp]:
                y = temp + 1
                result_no.append(y)

        if len(result_no) == 1:
            print(f'The lowest price of {item} amoung those Store is ${result_price} in Store{result_no[0]}')
        elif len(result_no) > 1:

            temp = ''  # Start(change the result no. to the format of Store X and Store Y and Stoe Z that can be printed directly)
            count = len(result_no)
            for i in result_no:
                if count == len(result_no):
                    temp = str(i)
                elif count != 0:
                    temp = temp + ' and Store ' + str(i)
                elif count == 0:
                    temp = temp + i
                count -= 1
            result_no = temp  # End of the change

            print(f'The lowest price of {item} amoung those Store is ${result_price} in Store{result_no}')