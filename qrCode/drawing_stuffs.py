import cv2 as cv
from pyzbar.pyzbar import decode
from playsound import playsound


def barcode_scanner():
    print("==Scan item barcode==")
    cap = cv.VideoCapture(1)

    while True:
        success, frame = cap.read()
        cv.imshow("Capture", frame)
        if cv.waitKey(1) == ord('q'):
            cap.release()
            cv.destroyAllWindows()
            return

        for code in decode(frame):
            cap.release()
            cv.destroyAllWindows()
            playsound("scanner_beep.mp3")
            print("..Item scanned")
            return code.data.decode('utf-8')


def add_item():
    print("==Store # Adding new items==")
    bar_code = barcode_scanner()
    item_name = input("item name: ")
    price = input("Price: ")
    qty = input("Quantity: ")
    bar_code = bar_code if bar_code else "No barcode"

    return {
        'name': item_name,
        'price': price,
        'qty': qty,
        'barcode': bar_code
    }


items = []
while True:
    print("=====    Isomero     ======")

    print("1. Add item(s)")
    print("2. Search item")
    print("3. All items")
    print("0. Exit")
    choice = input(">> ")

    if choice == '0':
        break
    if choice == '1':
        again = True
        while again:
            item_added = add_item()
            items.append(item_added)

            again_prompt = input("Add another? (y/n) ")
            again = True if again_prompt.casefold() == 'y' else False

    elif choice == '2':
        item_to_search = barcode_scanner()
        item_found = None
        for item in items:
            if item_to_search == item['barcode']:
                item_found = item
                break

        if item_found:
            print("== item found ==")
            for key, value in item_found.items():
                print(value)
            print()
        else:
            print("item not found!")
            print()

    elif choice == '3':
        print("=== items in Store ===")
        if len(items):
            for item in items:
                for key, value in item.items():
                    print(f"\t{value}")
                print("-" * 20)
        else:
            print("No items yet!")

print(items)


