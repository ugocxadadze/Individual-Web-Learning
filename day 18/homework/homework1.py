# შექმენი ცვლადი სადაც შეინახავ შენს სახელს ,  შემდეგ if ის გამოყენებით შეამოწმე თუ ეს სახელი ტოლია "ugo"-ანუ შენი სახელის , მაშინ დაპრინტოს "Hello "+name , ხოლო სხვა შემთხვევაში დაპრინტოს "Hello Guest"


name=input("რა არის შენი სახელი: ")
if name == "ugo":
    print("Hello "+name )
else: 
    print("HELLO Guest ")