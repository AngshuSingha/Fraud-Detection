from flask import Flask, request, render_template
import numpy as np
import pickle

# Load trained model
model_path = 'Xgb_pred_model.pkl'
model_load = pickle.load(open(model_path, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    step = int(request.form['step'])
    amount = float(request.form['amount'])
    old_org = float(request.form['oldbalanceOrg'])
    new_org = float(request.form['newbalanceOrig'])
    old_dest = float(request.form['oldbalanceDest'])
    new_dest = float(request.form['newbalanceDest'])
    trx_type = request.form['type']
    hour = int(request.form['hour'])
    day = int(request.form['day'])

    # Auto-generated features
    isFraud = 0
    merchant_sender = 0
    merchant_receiver = 0

    type_CASH_OUT = (trx_type == "CASH_OUT")
    type_DEBIT = (trx_type == "DEBIT")
    type_PAYMENT = (trx_type == "PAYMENT")
    type_TRANSFER = (trx_type == "TRANSFER")

    org_diff = old_org - new_org
    dest_diff = old_dest - new_dest

    org_no_change = 1 if old_org == new_org else 0
    dest_no_change = 1 if old_dest == new_dest else 0

    amount_ratio = amount / (old_org + 1)

    is_transfer = (trx_type == "TRANSFER")
    is_cashout = (trx_type == "CASH_OUT")

    final_features = np.array([[
        step, amount, old_org, new_org, old_dest, new_dest,
        merchant_sender, merchant_receiver,
        type_CASH_OUT, type_DEBIT, type_PAYMENT, type_TRANSFER,
        org_diff, dest_diff, org_no_change, dest_no_change,
        amount_ratio, hour, day, is_transfer, is_cashout
    ]])

    prediction = model_load.predict(final_features)[0]

    if prediction == 1:
        output = "Fraud Detected!"
    else:
        output = "Transaction is Safe"

    return render_template('index.html', prediction_text=output)


if __name__ == "__main__":
    app.run(debug=True)
