try:
    with open('lietotajs.txt', 'a') as f:
        while True:
            vards = input("Ievadi savu vārdu vai 'iziet': ")

            if vards.lower() == "iziet":
                break

            try:
                f.write(vards + '\n')
                print(f"Vārds '{vards}' ir pievienots")
            except Exception as e:
                print(f"Errors: {str(e)}")

except Exception as e:
    print(f"Error atverot failu: {str(e)}")