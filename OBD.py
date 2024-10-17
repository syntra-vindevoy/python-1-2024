### Eerst een dictionary maken met alle elementen
#nested dict opzoeken
my_dict_obd = {
    "P0001": {
        "Description:": "Fuel Volume Regulator Control Circuit/Open",
        "Causes:": "1. Faulty fuel volume regulator: The fuel volume regulator may be malfunctioning, causing the system to throw the error. \n" "2. Wiring issues: There could be a problem in the electrical wiring or connectors related to the fuel volume regulator. \n" "3. Damaged fuel pump: If the fuel pump is not operating correctly, it can cause this code to appear. \n" "4. ECU (Engine Control Unit) malfunction: The ECU may have a fault, causing it to incorrectly detect an issue with the fuel regulator.",
        "Symptoms:": "1. Engine stalling or hesitation. \n" "2. Difficulty starting the vehicle. \n" "3. Poor fuel efficiency. \n" "4. The engine running rough or erratically.",
        "Recommended Actions:": "1. Inspect the wiring: Check the wiring and connections around the fuel volume regulator for any loose or damaged components. \n" "2. Test the fuel volume regulator: Use a multimeter to test the regulator for proper voltage and operation. \n" "3. Check the fuel pump: Ensure the fuel pump is working correctly, as it could be related to the issue. \n" "4. Clear the code: After making repairs, use an OBD-II scanner to clear the code and see if it reappears."

    }




}


print(my_dict_obd["P0001"]["Symptoms:"])
#----------------------------------------------------------------------------

### Opvragen bepaald obd code

obdcode = input("Enter OBD Code: ")


#----------------------------------------------------------------------------

### Controleren of de code wel in de lijst staat

if obdcode in my_dict_obd:
    print(my_dict_obd[obdcode])
else:
    print("Invalid OBD Code")

#----------------------------------------------------------------------------





