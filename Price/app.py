from flask import Flask,render_template,request
import pickle

app = Flask(__name__)  # here we are creating the instance




with open('gbr.pkl','rb') as file:
    model1 = pickle.load(file)


with open('grid_search_results.pkl','rb') as file1:
    best_model, best_params, best_score = pickle.load(file1)


@app.route('/') 
def hello():    
    return render_template('1.html')

@app.route('/predict', methods=['GET', 'POST'])

def predict():

    if request.method == 'POST':

        qty = int(request.form.get('qty'))
        unit_price = float(request.form.get('unit_price'))
        lag_price = float(request.form.get('lag_price'))
        Volume = int(request.form.get('volume'))
        Customers = int(request.form.get('customers'))
        s = float(request.form.get('s'))

        prediction = model1.predict([[qty,unit_price,lag_price,Volume,Customers,s]])

        print(prediction)

        return render_template('result.html', prediction = round(float(prediction[0]), 2))
    return render_template('predict_price.html')


@app.route('/pred1', methods=['GET', 'POST'])
def pred1():

    if request.method== 'POST':
        comp_2 = float(request.form['comp_2'])
        product_name_length = float(request.form['product_name_lenght'])
        comp_3 = float(request.form['comp_3'])
        product_weight_g = float(request.form['product_weight_g'])
        freight_price = float(request.form['freight_price'])
        product_description_length = float(request.form['product_description_lenght'])
        comp_1 = float(request.form['comp_1'])
        product_score = float(request.form['product_score'])
        volume = float(request.form['volume'])
        product_id = float(request.form['product_id'])
        fp1 = float(request.form['fp1'])

        input_data = [[comp_2,product_name_length,comp_3,product_weight_g,freight_price,product_description_length,comp_1,product_score,volume,product_id,fp1]]
        pred2 = best_model.predict(input_data)

        print(pred2)
        return render_template('result1.html',pred2 = round(float(pred2),2))

    return render_template('predict1.html')
if __name__=='__main__':
    app.run()