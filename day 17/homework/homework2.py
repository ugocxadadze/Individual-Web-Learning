#შექმენი password ცვლადი სადაც შეინახავ შენთვის სასურველ პაროლს, შემდეგ მომხმარებელს შემოატანინე input()-ის მეშვეობით პაროლი და while loop-ის გამოყენებით სანამ მომხმარებლის შემოყვანილი პაროლი და შენი პაროლი არ დაემთხვევა ერთმანეთს, ტერმინალში დაბეჭდოს რომ password don't match(პაროლები არ ემთხვევა) , ხოლო როდესაც დაემთხვევა პაროლი , ტერმინალში დაპრინტოს რომ "You have successfully logged in."

my_password="Duck5835"
you_password=input(" შემოიტანე პაროლი: ")
while my_password!=you_password:
    you_password=input("შემოიტანე პაროლი ახლიდან")

print("you have successfully logged in")