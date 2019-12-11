def lambda_handler(event, context):
    """Add two numbers"""


    x = event['x']
    y = event['y']
    add = x +y
    print(f"The total of x:{x} and y:{y} =={add}")
    return{
         "Total" : add,
     }
