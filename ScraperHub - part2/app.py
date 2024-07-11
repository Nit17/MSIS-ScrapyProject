from flask import Flask, jsonify,render_template,request
from bs4 import BeautifulSoup
import requests
import csv
import json
from flask import Flask, send_file
import openpyxl
from io import BytesIO
import matplotlib.pyplot as plt
from fake_useragent import UserAgent


app = Flask(__name__)

@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/scrape', methods=['POST'])
def scrape_data():
    ua=UserAgent()
    header={'user-agent':ua.chrome}
    user_input = request.form.get('user_input')
    try:
       URL = "https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy,4io"
       values_list=[]
       tags_list=[]
       response = requests.get(URL,headers=header)
       soup = BeautifulSoup(response.content, 'html5lib')
       iphone=soup.find('div', attrs = {'class':'_2kHMtA'})
       for row in soup.findAll('div', attrs = {'class':'_2kHMtA'}):
        dictionary={}
        if 'name' in user_input.lower():
            name_color=row.find('div',attrs={'class':'_4rR01T'}).text
            name=name_color.split('(')[0]
            dictionary['Name']=name
            tags_list.append('Name')
        if 'price' in user_input.lower():
            priceValue=row.find('div',attrs={'class':'_1_WHN1'}).text
            price=int(priceValue.split('₹')[1].replace(',',''))
            dictionary['Price']=price
            tags_list.append('Price')
        if 'color' in user_input.lower():
            name_color=row.find('div',attrs={'class':'_4rR01T'}).text
            color=(name_color.split('(')[1]).split(',')[0]
            dictionary['Color']=color
            tags_list.append('Color')
        if 'ram' in user_input.lower():
            RAM=(((name_color.split('(')[1]).split(',')[1]).split(')')[0]).lstrip()
            dictionary['RAM']=RAM
            tags_list.append('RAM')
        if 'rating' in user_input.lower():
            rating=row.find('div',attrs={'class':'_3LWZlK'}).text
            dictionary["Rating"]=rating
            tags_list.append('Rating')
        if 'Ratings' in user_input.lower():
            ratingsReviews=row.find('span',attrs={'class':'_2_R_DZ'}).text
            ratings=int((ratingsReviews.split('Ratings\xa0&\xa0')[0]).replace(',',''))
            dictionary['Ratings']=ratings
            tags_list.append('Ratings')
        if 'Reviews' in user_input.lower():
            ratingsReviews=row.find('span',attrs={'class':'_2_R_DZ'}).text
            reviews=int(((ratingsReviews.split('Ratings\xa0&\xa0')[0]).split('Reviews')[0]).replace(',',''))
            dictionary['Reviews']=reviews
            tags_list.append('Reviews')
      
        
        else:
            if user_input==None or user_input=='' or user_input=='readonly':
                name_color=row.find('div',attrs={'class':'_4rR01T'}).text
                name=name_color.split('(')[0]
                dictionary['Name']=name
                priceValue=row.find('div',attrs={'class':'_1_WHN1'}).text
                price=int(priceValue.split('₹')[1].replace(',',''))
                dictionary['Price']=price
                name_color=row.find('div',attrs={'class':'_4rR01T'}).text
                color=(name_color.split('(')[1]).split(',')[0]
                dictionary['Color']=color
                RAM=(((name_color.split('(')[1]).split(',')[1]).split(')')[0]).lstrip()
                dictionary['RAM']=RAM
                rating=row.find('div',attrs={'class':'_3LWZlK'}).text
                dictionary["Rating"]=rating
                ratingsReviews=row.find('span',attrs={'class':'_2_R_DZ'}).text
                ratings=int((ratingsReviews.split('Ratings\xa0&\xa0')[0]).replace(',',''))
                dictionary['Ratings']=ratings
                reviews=int(((ratingsReviews.split('Ratings\xa0&\xa0')[0]).split('Reviews')[0]).replace(',',''))
                dictionary['Reviews']=reviews
                tags_list=['Name','Price','Color','RAM','Rating','Ratings','Reviews']
        values_list.append(dictionary)
       return render_template('scrape.html', scraped_data=values_list, user_input=user_input,tags=tags_list)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/scrape_CSV', methods=['POST'])
def scrape_data_CSV():
    user_input=request.form.get('user_input')
    value=request.form.get('action')
    ua=UserAgent()
    header={'user-agent':ua.chrome}
    try:
       URL = "https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy,4io"
       values_list=[]
       tags_list=[]
       response = requests.get(URL,headers=header)
       soup = BeautifulSoup(response.content, 'html5lib')
       iphone=soup.find('div', attrs = {'class':'_2kHMtA'})
       for row in soup.findAll('div', attrs = {'class':'_2kHMtA'}):
        dictionary={}
        if 'name' in user_input.lower():
            name_color=row.find('div',attrs={'class':'_4rR01T'}).text
            name=name_color.split('(')[0]
            dictionary['Name']=name
            tags_list.append('Name')
        if 'price' in user_input.lower():
            priceValue=row.find('div',attrs={'class':'_1_WHN1'}).text
            price=int(priceValue.split('₹')[1].replace(',',''))
            dictionary['Price']=price
            tags_list.append('Price')
        if 'color' in user_input.lower():
            name_color=row.find('div',attrs={'class':'_4rR01T'}).text
            color=(name_color.split('(')[1]).split(',')[0]
            dictionary['Color']=color
            tags_list.append('Color')
        if 'ram' in user_input.lower():
            RAM=(((name_color.split('(')[1]).split(',')[1]).split(')')[0]).lstrip()
            dictionary['RAM']=RAM
            tags_list.append('RAM')
        if 'rating' in user_input.lower():
            rating=row.find('div',attrs={'class':'_3LWZlK'}).text
            dictionary["Rating"]=rating
            tags_list.append('Rating')
        if 'Ratings' in user_input.lower():
            ratingsReviews=row.find('span',attrs={'class':'_2_R_DZ'}).text
            ratings=int((ratingsReviews.split('Ratings\xa0&\xa0')[0]).replace(',',''))
            dictionary['Ratings']=ratings
            tags_list.append('Ratings')
        if 'Reviews' in user_input.lower():
            ratingsReviews=row.find('span',attrs={'class':'_2_R_DZ'}).text
            reviews=int(((ratingsReviews.split('Ratings\xa0&\xa0')[0]).split('Reviews')[0]).replace(',',''))
            dictionary['Reviews']=reviews
            tags_list.append('Reviews')
      
        
        else:
            if user_input==None or user_input=='' or user_input=='readonly':
                name_color=row.find('div',attrs={'class':'_4rR01T'}).text
                name=name_color.split('(')[0]
                dictionary['Name']=name
                priceValue=row.find('div',attrs={'class':'_1_WHN1'}).text
                price=int(priceValue.split('₹')[1].replace(',',''))
                dictionary['Price']=price
                name_color=row.find('div',attrs={'class':'_4rR01T'}).text
                color=(name_color.split('(')[1]).split(',')[0]
                dictionary['Color']=color
                RAM=(((name_color.split('(')[1]).split(',')[1]).split(')')[0]).lstrip()
                dictionary['RAM']=RAM
                rating=row.find('div',attrs={'class':'_3LWZlK'}).text
                dictionary["Rating"]=rating
                ratingsReviews=row.find('span',attrs={'class':'_2_R_DZ'}).text
                ratings=int((ratingsReviews.split('Ratings\xa0&\xa0')[0]).replace(',',''))
                dictionary['Ratings']=ratings
                reviews=int(((ratingsReviews.split('Ratings\xa0&\xa0')[0]).split('Reviews')[0]).replace(',',''))
                dictionary['Reviews']=reviews
                tags_list=['Name','Price','Color','RAM','Rating','Ratings','Reviews']
        values_list.append(dictionary)
       if(value=='csv'):
        filename = 'iphones.csv'
        with open(filename, 'w', newline='') as f:
                w = csv.DictWriter(f,tags_list)
                w.writeheader()
                for quote in values_list:
                    w.writerow(quote)
        return send_file(filename, as_attachment=True, attachment_filename=filename, mimetype='text/csv')
       if(value=='json'):
        filename = 'iphones'
        with open(filename, 'w', newline='') as f:
                json.dump(values_list, f,indent=4)
        return send_file(filename, as_attachment=True, attachment_filename=filename, mimetype='application/json')
        
       if(value=='excel'):
           filename = 'iphones.xlsx'
           workbook = openpyxl.Workbook()
           worksheet = workbook.active
           header = list(values_list[0].keys())
           worksheet.append(header)
           for item in values_list:
            row = [item[field] for field in header]
            worksheet.append(row)
           output = BytesIO()
           workbook.save(output)
           output.seek(0)
           return send_file(output, as_attachment=True, attachment_filename=filename, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
       
       if(value=='visualization'):
           return render_template('visualization.html',tags=tags_list,scraped_data=values_list,user_input=user_input) 
           
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/visualize', methods=['POST'])
def scrapeVisualize():
    user_input=request.form.get('user_input')
    print(user_input)
    value=request.form.get('trigger')
    ua=UserAgent()
    header={'user-agent':ua.chrome}
    try:
       URL = "https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy,4io"
       values_list=[]
       tags_list=[]
       response = requests.get(URL,headers=header)
       soup = BeautifulSoup(response.content, 'html5lib')
       iphone=soup.find('div', attrs = {'class':'_2kHMtA'})
       for row in soup.findAll('div', attrs = {'class':'_2kHMtA'}):
        dictionary={}
        if 'name' in user_input.lower():
            name_color=row.find('div',attrs={'class':'_4rR01T'}).text
            name=name_color.split('(')[0]
            dictionary['Name']=name
            tags_list.append('Name')
        if 'price' in user_input.lower():
            priceValue=row.find('div',attrs={'class':'_1_WHN1'}).text
            price=int(priceValue.split('₹')[1].replace(',',''))
            dictionary['Price']=price
            tags_list.append('Price')
        if 'color' in user_input.lower():
            name_color=row.find('div',attrs={'class':'_4rR01T'}).text
            color=(name_color.split('(')[1]).split(',')[0]
            dictionary['Color']=color
            tags_list.append('Color')
        if 'ram' in user_input.lower():
            RAM=(((name_color.split('(')[1]).split(',')[1]).split(')')[0]).lstrip()
            dictionary['RAM']=RAM
            tags_list.append('RAM')
        if 'rating' in user_input.lower():
            rating=row.find('div',attrs={'class':'_3LWZlK'}).text
            dictionary["Rating"]=rating
            tags_list.append('Rating')
        if 'Ratings' in user_input.lower():
            ratingsReviews=row.find('span',attrs={'class':'_2_R_DZ'}).text
            ratings=int((ratingsReviews.split('Ratings\xa0&\xa0')[0]).replace(',',''))
            dictionary['Ratings']=ratings
            tags_list.append('Ratings')
        if 'Reviews' in user_input.lower():
            ratingsReviews=row.find('span',attrs={'class':'_2_R_DZ'}).text
            reviews=int(((ratingsReviews.split('Ratings\xa0&\xa0')[0]).split('Reviews')[0]).replace(',',''))
            dictionary['Reviews']=reviews
            tags_list.append('Reviews')
      
        
        else:
            if user_input==None or user_input=='' or user_input=='readonly':
                name_color=row.find('div',attrs={'class':'_4rR01T'}).text
                name=name_color.split('(')[0]
                dictionary['Name']=name
                priceValue=row.find('div',attrs={'class':'_1_WHN1'}).text
                price=int(priceValue.split('₹')[1].replace(',',''))
                dictionary['Price']=price
                name_color=row.find('div',attrs={'class':'_4rR01T'}).text
                color=(name_color.split('(')[1]).split(',')[0]
                dictionary['Color']=color
                RAM=(((name_color.split('(')[1]).split(',')[1]).split(')')[0]).lstrip()
                dictionary['RAM']=RAM
                rating=row.find('div',attrs={'class':'_3LWZlK'}).text
                dictionary["Rating"]=rating
                ratingsReviews=row.find('span',attrs={'class':'_2_R_DZ'}).text
                ratings=int((ratingsReviews.split('Ratings\xa0&\xa0')[0]).replace(',',''))
                dictionary['Ratings']=ratings
                reviews=int(((ratingsReviews.split('Ratings\xa0&\xa0')[0]).split('Reviews')[0]).replace(',',''))
                dictionary['Reviews']=reviews
                tags_list=['Name','Price','Color','RAM','Rating','Ratings','Reviews']
        values_list.append(dictionary)
        print(values_list)
        print(tags_list)
        if(value=='pie'):
            if 'Name' in tags_list:
               iphone_counts = {}
               for item in values_list:
                iphone = item.get("Name")
                if iphone in iphone_counts:
                 iphone_counts[iphone] =iphone_counts[iphone]+ int(1)
                else:
                  iphone_counts[iphone] = int(1)
               print(iphone_counts)
               plt.figure(figsize=(16, 16))
               plt.pie(iphone_counts.values(), labels=iphone_counts.keys(), autopct='%1.1f%%', startangle=90)
               plt.title("Count of iphones")
               plt.savefig('static/name_count_pie.jpg')
            if 'Name' in tags_list and 'Price' in tags_list:
               print("-------------------------------------------------------------name price")
               iphone_price_pie = {}
               for item in values_list:
                iphone = item.get("Name")
                if iphone not in iphone_price_pie:
                 iphone_price_pie[iphone] =int(item.get("Price"))
               print(iphone_price_pie)
               plt.figure(figsize=(16, 16))
               plt.pie(iphone_price_pie.values(), labels=iphone_price_pie.keys(), autopct='%1.1f%%', startangle=90)
               plt.title("Price of iphones")
               plt.savefig('static/name_price_pie.jpg')
            if 'Name' in tags_list and 'Ratings' in tags_list:
               print("-------------------------------------------------------------name Ratings")
               iphone_counts = {}
               for item in values_list:
                iphone = item.get("Name")
                if iphone not in iphone_counts:
                 iphone_counts[iphone] =item.get("Ratings")
               print(iphone_counts)
               plt.figure(figsize=(16, 16))
               plt.pie(iphone_counts.values(), labels=iphone_counts.keys(), autopct='%1.1f%%', startangle=90)
               plt.title("Ratings of iphones")
               plt.savefig('static/name_ratings_pie.jpg')
            if 'Name' in tags_list and 'Reviews' in tags_list:
               print("-------------------------------------------------------------name Reviews")
               iphone_counts = {}
               for item in values_list:
                iphone = item.get("Name")
                if iphone not in iphone_counts:
                 iphone_counts[iphone] =item.get("Reviews")
               print(iphone_counts)
               plt.figure(figsize=(16, 16))
               plt.pie(iphone_counts.values(), labels=iphone_counts.keys(), autopct='%1.1f%%', startangle=90)
               plt.title("Reviews of iphones")
               plt.savefig('static/name_reviews_pie.jpg')
        if(value=='column'):
            print("------------------------------column")
            if 'Name' in tags_list:
               print("---------------------------------name count")
               iphone_counts = {}
               for item in values_list:
                iphone = item.get("Name")
                if iphone in iphone_counts:
                 iphone_counts[iphone] =iphone_counts[iphone]+ int(1)
                else:
                  iphone_counts[iphone] = int(1)
               plt.figure(figsize=(16, 16))
               plt.bar(iphone_counts.keys(),iphone_counts.values(),color='#b37a00',width=0.5)
               plt.title("Count of iphones")
               plt.xlabel("Name")
               plt.xticks(rotation=45,ha='right')
               plt.ylabel("Count")
               plt.savefig('static/name_count_plot.jpg') 
            if 'Name' in tags_list and 'Price' in tags_list:
               print("---------------------------------price count")
               iphone_price = {}
               for item in values_list:
                iphone = item.get("Name")
                iphone_price[iphone]=item.get("Price")
               plt.figure(figsize=(16, 16))
               plt.bar(iphone_price.keys(),iphone_price.values(),color='#b37a00',width=0.5)
               plt.title("Price of Iphone")
               plt.xlabel("Name")
               plt.xticks(rotation=45,ha='right')
               plt.ylabel("Price")
               plt.savefig('static/name_price_plot.jpg') 
            if 'Color' in tags_list:
               print("---------------------------------color count")
               color_count = {}
               for item in values_list:
                iphone = item.get("Color")
                if iphone in color_count:
                 color_count[iphone] =color_count[iphone]+ int(1)
                else:
                  color_count[iphone] = int(1)
               plt.figure(figsize=(16, 16))
               plt.bar(color_count.keys(),color_count.values(),color='#b37a00',width=0.5)
               plt.title("Count of iphones for each color")
               plt.xlabel("Color")
               plt.xticks(rotation=45,ha='right')
               plt.ylabel("Count")
               plt.savefig('static/color_count_plot.jpg')  
            if 'RAM' in tags_list:
               Ram_counts = {}
               for item in values_list:
                iphone = item.get("RAM")
                if iphone in Ram_counts:
                 Ram_counts[iphone] =Ram_counts[iphone]+ int(1)
                else:
                  Ram_counts[iphone] = int(1)
               plt.figure(figsize=(16, 16))
               plt.bar(Ram_counts.keys(),Ram_counts.values(),color='#b37a00',width=0.5)
               plt.title("Count of iphones for each RAM")
               plt.xlabel("RAM")
               plt.xticks(rotation=45,ha='right')
               plt.ylabel("Count")
               plt.savefig('static/ram_count_plot.jpg') 
            if 'RAM' in tags_list and 'Price' in tags_list:
               print("---------------------------------RAM Price count")
               iphone_price = {}
               for item in values_list:
                iphone = item.get("RAM")
                iphone_price[iphone]=item.get("Price")
               plt.figure(figsize=(16, 16))
               plt.bar(iphone_price.keys(),iphone_price.values(),color='#b37a00',width=0.5)
               plt.title("Price of Iphone for each RAM")
               plt.xlabel("RAM")
               plt.xticks(rotation=45,ha='right')
               plt.ylabel("Price")
               plt.savefig('static/ram_price_plot.jpg') 
            if 'Name' in tags_list and 'Reviews' in tags_list:
               print("---------------------------------NAme reviews count")
               iphone_price = {}
               for item in values_list:
                iphone = item.get("Name")
                iphone_price[iphone]=item.get("Reviews")
               plt.figure(figsize=(16, 16))
               plt.bar(iphone_price.keys(),iphone_price.values(),color='#b37a00',width=0.5)
               plt.title("Reviews of Iphone")
               plt.xlabel("Name")
               plt.xticks(rotation=45,ha='right')
               plt.ylabel("Reviews")
               plt.savefig('static/name_reviews_plot.jpg')
            if 'Name' in tags_list and 'Ratings' in tags_list:
               print("-----------------------------------------name ratings")
               iphone_price = {}
               for item in values_list:
                iphone = item.get("Name")
                iphone_price[iphone]=item.get("Ratings")
               plt.figure(figsize=(16, 16))
               plt.bar(iphone_price.keys(),iphone_price.values(),color='#b37a00',width=0.5)
               plt.title("Ratings of Iphone")
               plt.xlabel("Name")
               plt.xticks(rotation=45,ha='right')
               plt.ylabel("Ratings")
               plt.savefig('static/name_ratings_plot.jpg')
    except Exception as e:
        return jsonify({"error": str(e)})
           
            
    return render_template('visualize.html',tags=user_input,chart=value)
               
   
if __name__ == '__main__':
    app.run(debug=True)
