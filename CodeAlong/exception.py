import time
import traceback
while True:
    try: 
        print("DAB")
        time.sleep(0.1)
    except Exception as e:
       traceback.print_exc()