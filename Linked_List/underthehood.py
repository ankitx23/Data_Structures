# lets say the linked list is {2,3,45,67,8}

head= {
    "value" : 2,
    "next": {
        "value" : 3,
        "next" : {
            "value" : 45,
            "next" :{
                "value" : 67,
                "next" : {
                    "value" : 8,
                    "next" : None
                }

            }
        }

    }
}

print (head)

print(head ["next"]["value"])