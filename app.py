from flask import Flask , render_template , request, jsonify
from bs4 import BeautifulSoup
import requests



app = Flask(__name__)
def my_func(url):
        
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36' }
        
        res = requests.get(url, headers = headers)
        lst = []
        if res :
                print(res.status_code)
                soup = BeautifulSoup(res.text,'html.parser')
                all_links = soup.select("#containerid a")
                        # print(type(all_links))
                
                for i in all_links:
                        link_dict = {}
                        dt_name = i.text  
                        link_dict['dt_name'] = dt_name
                        links = i.get('href') 
                        link_dict['links'] = links
                        
                        lst.append(link_dict)
                # dt_lst.append(dt_name)
        else:
                print("website down")     

        return lst
     
       
@app.route('/')

def index ():
    return render_template ("index.html")



@app.route('/the_hindu')

def the_hindu():
         
    my_lst = my_func("https://newspaperpdf.online/the-hindu-pdf-download.php")
    if request.method == 'GET':
         if len(my_lst) > 0:
            return jsonify(my_lst)
#     print(lst)
    return render_template ('the_hindu.html', all_linkss = my_lst)


@app.route('/fin_exp')

def fin_exp():
        
        my_lst = my_func("https://newspaperpdf.online/download-financial-express.php")
        if request.method == 'GET':
         if len(my_lst) > 0:
            return jsonify(my_lst)
        return render_template('fin_exp.html', all_linkss = my_lst )


@app.route('/ind_exp')

def ind_exp():
  my_lst = my_func("https://newspaperpdf.online/download-indian-express.php")
  if request.method == 'GET':
         if len(my_lst) > 0:
            return jsonify(my_lst)     
  return render_template('ind_exp.html', all_linkss = my_lst )


@app.route('/dain_jag')

def dainik():
  my_lst = my_func("https://newspaperpdf.online/download-dainik-jagran.php")          
  if request.method == 'GET':
         if len(my_lst) > 0:
            return jsonify(my_lst)
  return render_template('dain_jag.html', all_linkss = my_lst)
 


@app.route('/eco_tim')

def eco():
  my_lst = my_func("https://newspaperpdf.online/download-economic-times.php")
  if request.method == 'GET':
         if len(my_lst) > 0:
            return jsonify(my_lst)
  return render_template('eco_tim.html', all_linkss = my_lst)


@app.route('/dec_chro')

def deccan():
  my_lst = my_func("https://newspaperpdf.online/download-deccan-chronicle.php")
  if request.method == 'GET':
         if len(my_lst) > 0:
            return jsonify(my_lst)
  return render_template('dec_chro.html', all_linkss = my_lst)


@app.route('/jan')

def jansata():
  my_lst = my_func("https://newspaperpdf.online/download-jansatta.php")
  if request.method == 'GET':
         if len(my_lst) > 0:
            return jsonify(my_lst)
  return render_template('jan.html', all_linkss = my_lst)


@app.route('/hind_tim')

def hin_tim():
  my_lst = my_func("https://newspaperpdf.online/download-hindustan-times.php")  
  if request.method == 'GET':
         if len(my_lst) > 0:
            return jsonify(my_lst)
  return render_template('hind_tim.html', all_linkss = my_lst)


@app.route('/toi')

def toi():
  my_lst = my_func("https://newspaperpdf.online/download-times-of-india.php")
  if request.method == 'GET':
         if len(my_lst) > 0:
            return jsonify(my_lst)
  return render_template('toi.html', all_linkss = my_lst)
   
      
if __name__=="__main__" :   
    app.run(debug= True)             