from flask import Flask, request
from config import API_KEY, API_SECRET, PASSWORD
from binance.cm_futures import CMFutures

app = Flask(__name__)

cm_futures_client = CMFutures()

# get server time
print(cm_futures_client.time())

cm_futures_client = CMFutures(key= API_KEY, secret= API_SECRET)

# Get account information
print(cm_futures_client.account())


@app.route("/alert", methods=['POST'])

def alerta():
    msg = request.json
    if msg['password'] != PASSWORD:
        return { 'code': 'error',
                'message': 'User not authorized'
        }
    print(msg)

   
 

    response = msg
    print(response)   
    
    return {
        'code' : 'Success',
        'msg': msg  


    }



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)





 


 