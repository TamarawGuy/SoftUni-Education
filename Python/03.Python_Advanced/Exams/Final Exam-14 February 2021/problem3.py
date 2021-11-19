def stock_availability(boxes, command, *args):

    if command == "delivery":
        cupcakes = list(args)
        boxes.extend(cupcakes)
        return boxes
    
    elif command == 'sell':
        if not args:
            boxes.pop(0)
            return boxes
        
        elif len(args) == 1:
            argument = args[0]
            if isinstance(argument, int):
                return boxes[argument:]
            
            elif isinstance(argument, str):
                if argument in boxes:
                    return [x for x in boxes if x != argument]
                else:
                    return boxes

        elif len(args) > 1:
            return [x for x in boxes if x not in args]
            

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

