import pymysql
import cv2
from pyzbar.pyzbar import decode

db = pymysql.connect(
    host="mysql-ait.stud.idi.ntnu.no",
    user="jonasbl",
    passwd="kKjpnzGz",
    db="jonasbl")

# Method for scanning the five barcodes added.
def scannBarcodes(num):
    if (num == 0):
        path = "item_1554949.png"
    elif (num == 1):
        path = "item_1554950.png"
    elif (num == 2):
        path = "item_1554952.png"
    elif (num == 3):
        path = "item_1554953.png"
    else:
        path = "myBarcode.png"

    img = cv2.imread(path)
    decoded = decode(img)
    bytes = decoded[0].data
    res = bytes.decode("utf-8")  # Casting from bytes to string
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return res


cur = db.cursor()
welcome = "Welcome to myShop self-checkout!"
print('-'*80)
print(' '*(40-int(len(welcome)/2))+welcome)
print('-'*80)


num = 0
status = True
while status:
    print("Please scan an item: ")

    barcodeString = scannBarcodes(num)
    barcode = int(barcodeString)

    if barcode == "":
        continue

    # Ensure that barcode is an integer.
    if isinstance(barcode, int):
        if num >= 5:
            status = False

        num += 1
        numrows = 0
        print("Barcode id: ", barcode)

        # Set new price = 1,-
        newprice = 1
        setNewPrice = "UPDATE products SET price = %s WHERE id = %s" % (newprice, barcode)

        try:
            cur.execute(setNewPrice)
        except:
            print("+++ ERROR exception, Could not set new price")

        db.commit()

        # Fetch product
        getProduct = "SELECT price FROM products WHERE id = %s" % barcode
        try:
            numrows = cur.execute(getProduct)
        except:
            print("+++ ERROR exception, bad input")

        if numrows == 0:
            print("+++ ERROR product not found")
            print("+++ Adding new product to database")

            # Adding procuct with defualt price = barcode number.
            registerProduct = "INSERT INTO products VALUES (%s, %s)" % (barcode, barcode)
            try:
                cur.execute(registerProduct)
                db.commit()
            except:
                print("+++ ERROR exception, Could not register new price")

            continue

        for row in cur.fetchall():
            print("Price: %d,-" % row[0])

    else:
        break


    








