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
            # print(f"count is {count}")
            return price[count]

        count += 1
    if count > len(name):
        print("item not found")


def price_finder(address, no, item_name):
    #tpath = int(input(
    #    'Please input the local address of the web store you want to find the price separetely\n (Type 1 for Store 1, type 2 for Store 2, and type 3 for Store 3)\n'))
    #tpath = request.form.get('address')
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
        #count = (input('Please input the no. of item you want to find\n'))
        #count = request.form.get('no')
        count = no
        try:
            count = int(count)
        except ValueError:
            print('Wrong input, please input another value')
        else:
            t = 1

    result = []
    for temp in range(count):
        x = sWeb(path)  # name is 0 price is 1
        name = x[0]
        price = x[1]
        #item = input('input the item name that you want to get the price\n')
        #item = request.form.get('item_name')
        item = item_name
        result.append(find_price_by_item(item, name, price))  # change the first parameter to change the item which you want to get the price
    if count > 1:
        return result
    else:
        result = result[0]
        return result


def compare(noOfS, item_name, store):
    #count = int(input(
        #'Please input the no. of store you want to find (type "0" if you want to compare with all store that default to be compare)\n'))
    #count = request.form.get('noOfS')
    count = noOfS
    #item = input('And please input the name of the item that you want to do the price comparison\n')
    #item = request.form.get('item_name')
    item = item_name
    name = []
    price = []
    result = []
    if count == 0:
        for temp in range(3):
            x = sWeb(dp[temp])
            name.append(x[0])
            price.append(x[1])
            result.append(find_price_by_item(item, name[temp], price[temp]))

        #new_result = []  # for remove the '$' sign
        new_result = [float(i[1:]) for i in result]  # fk this shxx
        result = new_result

        result_price = min(result)
        result_no = []
        for temp in range(3):
            if result_price == result[temp]:
                y = temp + 1
                result_no.append(y)
        if len(result_no) == 1:
            print(
                f'The lowest price of {item} amoung Store 1, Store 2 and Store 3 is ${result_price} in Store{result_no}')
        elif len(result_no) > 1:
            # print(f'The lowest price of {item} amoung Store 1, Store 2 and Store 3 is Store')
            # for i in range(len(result_no)):
            #    print(f'{result_no[i]}')
            #    if (i+1) < len(result_no):
            #        print(f'& Store ')
            # print(f', the price is ${result_price}')

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
            print(
                f'The lowest price of {item} amoung Store 1, Store 2 and Store 3 is ${result_price} in Store{result_no}')

    elif count > 0:
        print(
            f'Please input the local address of the web store you want to compare separetely\n (Type 1 for Store 1, type 2 for Store 2, and type 3 for Store 3)\n')
        for temp in range(count):

            if temp != 0:
                print(
                    f'Please type another web address\n (Type 1 for Store 1, type 2 for Store 2, and type 3 for Store 3)\n')

            #tpath = int(input())
            #tpath = request.form.get('store')
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

            # if path == 1:         It's not work
            #    path = dp1
            # if path == 2:
            #     path == dp2
            #  if path == 3:
            #      path == dp3
            #  print(f'alsdjlkb {path}')

            x = sWeb(path)
            name.append(x[0])
            price.append(x[1])
            result.append(find_price_by_item(item, name[temp], price[temp]))

        new_result = []  # for remove the '$' sign
        new_result = [float(i[1:]) for i in result]  # fk this shxx
        result = new_result  # end of remove the '$' sign

        result_price = min(result)
        result_no = []
        for temp in range(count):
            if result_price == result[temp]:
                y = temp + 1
                result_no.append(y)
        # temp = ''
        # for i in range(len(result_no)):
        # temp = temp + str(result_no[i])
        # if (i + 1) < len(result_no):
        # temp = temp + ' and' + ' Store'
        # print(f'{result_no[i]}')
        # if (i+1) < len(result_no):
        #    print(f'& Store ')
        # store = temp

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


#def main():
#    x = input('type 1 for find price, type 2 for compare\n')
#    if x == '1':
#        price_finder()
#    else:
#        if x == '2':
#            compare()
#        else:
 #           print('ERROR: wrong input')


#main()