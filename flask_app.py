from flask import Flask, render_template, request, session, redirect, url_for
# import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import numpy as np
import os
# test written in Pycharm

app = Flask(__name__) # Creating our Flask Instance
app.secret_key = "randomly543tert443434"

'''Paths for switching between Pycharm and Pythonanywere'''

path_pycharm = "/home/gaviation/mysite" # path for pythonanywere
#path_pycharm = ""                      # path for pycharm


'''Database'''
# from flask_sqlalchemy import SQLAlchemy
# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#     username="gaviation",
#     password="wq9IUEf4lX",
#     hostname="gaviation.mysql.pythonanywhere-services.com",
#     databasename="gaviation$comments",
# )
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
# db = SQLAlchemy(app)
#
# class Comment(db.Model):
#
#     __tablename__ = "comments"
#
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(4096))


'''Sites'''
@app.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))

    # show the form, it wasn't submitted
    return render_template('about.html')


@app.route('/AW139', methods=['GET', 'POST'])
def AW139():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))

    # show the form, it wasn't submitted
    return render_template('AW139.html')



@app.route('/AW169', methods=['GET', 'POST'])
def AW169():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))

    # show the form, it wasn't submitted
    return render_template('AW169.html')

@app.route('/AW139_OGE_OEI', methods=['GET', 'POST'])
def AW139_OGE_OEI():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))

    # show the form, it wasn't submitted
    return render_template('AW139_OGE_OEI.html')

@app.route('/operation_result/', methods=['POST', 'GET'])
def operation_result():
    """Route where we send calculator form input"""

    # linear function parameters
    # function 0 - left side upper chart
    x_1,y_1 = 2364,5684           # about 2000ft PA on 30C line
    x_2,y_2 = 2956, 6290          # about 200ft PA on 30C line
    m_0 = (y_1 - y_2)/(x_1 - x_2) #slope
    b_0 = -m_0*x_1 + y_1          #intercept
    b_0 = b_0 - (30 +273.15)*43.1 #finding the intercept of the -273C line, 43.1 pixel shift
    # function 0 - left side upper chart
    x_1,y_1 = 3011,5685            # about 2000ft PA on 10C line
    x_2,y_2 = 3265,6676            # about -1000ft PA on 10C line
    m_1 = (y_1 - y_2)/(x_1 - x_2)  #slope
    b_1 = -m_1*x_1 + y_1           #intercept
    b_1 = b_1 - (10 +273.15)*31    #finding the intercept of the -273C line
    # function 2:   0-5kts (lower chart)
    x_1, y_1 = 1317,6716          # (0,0)
    x_2, y_2 = 1449,6878          # (4480,5)
    m_2 = (y_1 - y_2)/(x_1 - x_2) # slope
    b_2 = -m_2*x_1 + y_1          # intercept
    # function 3: 5-10knts
    x_1, y_1 = 1449,6878          # (4480,5)
    x_2, y_2 = 1702,7044          # (4635,10)
    m_3 = (y_1 - y_2)/(x_1 - x_2) # slope
    b_3 = -m_3*x_1 + y_1          # intercept
    # function 4: 25-30kts
    x_1, y_1 = 3456,7538          # (5705,25)
    x_2, y_2 = 4219,7702          # (6169,30)
    m_4 = (y_1 - y_2)/(x_1 - x_2) # slope
    b_4 = -m_4*x_1 + y_1          # intercept
    # function 5: 30-40kts
    x_1, y_1 = 4219,7702          # (6169,30)
    x_2, y_2 = 5231,8034          # (6785,40)
    m_5 = (y_1 - y_2)/(x_1 - x_2) # slope
    b_5 = -m_5*x_1 + y_1          # intercept

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    QNH_input = request.form['QNH']
    session['QNH_SV'] = QNH_input

    DOM_input = request.form['DOM']
    session['DOM_SV'] = DOM_input

    hover_height_input = request.form['hover_height']
    session['hover_height_SV'] = hover_height_input

    temp_input = request.form['temp']
    session['temp_SV'] = temp_input

    wind_input = request.form['wind']
    session['wind_SV'] = wind_input

    perf_benefit_input = request.form['perf_benefit']
    session['perf_benefit_SV'] = perf_benefit_input

    fuel_at_hho_input = request.form['fuel_at_hho']
    session['fuel_at_hho_SV'] = fuel_at_hho_input

    PIC_input = request.form['PIC']
    session['PIC_SV'] = PIC_input
    # db.session.add(PIC_input)
    # db.session.commit()

    flight_ID_input = request.form['flight_ID']
    session['flight_ID_SV'] = flight_ID_input

    try:
        QNH = float(QNH_input)
        DOM = float(DOM_input)
        hover_height = float(hover_height_input)
        temp = float(temp_input)
        wind = float(wind_input)
        perf_benefit = float(perf_benefit_input)
        fuel_at_hho = float(fuel_at_hho_input)
        PIC = str(PIC_input)
        flight_ID = str(flight_ID_input)


        # linking all functions together:
        #  pressure difference between QNH and standard pressure
        difference = (1013.2 - QNH) * 27

        # pressure difference added to hover height.
        PA = hover_height + difference
        # converting to PA on chart
        # 0ft: 6347,   1000ft: 6016, diff = 331 pixel
        PA_pixel = round(6347 - PA * (331/1000))

        # function 0 (left upper chart)
        zero_wind_mass_left = (PA_pixel - b_0 - (43.1*(temp+273.15)))/m_0
        # function 1 (right upper chart)
        zero_wind_mass_right = (PA_pixel - b_1 - (31*(temp+273.15)))/m_1

        # selecting the correct zero wind mass
        if zero_wind_mass_left < zero_wind_mass_right:
            zero_wind_mass_pixel = zero_wind_mass_left
        else:
            zero_wind_mass_pixel = zero_wind_mass_right

        # converting to zero_wind_mass_pixel to kg for output
        # 5000kg = 2272 pixels , 6000kg = 3915 pixels
        # difference = 3915 - 2272 = 1643 pixels
        # 1kg = 1.643 pixel
        zero_wind_mass = 5000 + (zero_wind_mass_pixel-2272)/1.643


        # converting wind scale of lower table for pixel output
        # 0 = 6713, 10 = 7043, difference = 330, 1 knot = 33 pixel
        wind_ref = 6713 + wind*33

        # calculating max mass in lower part graph
        #import numpy as np
        if wind < 5:
            max_mass_pixel = ((wind_ref - b_2)/m_2) + zero_wind_mass_pixel - 1315 # function 2

        if 5 <= wind < 10:
            max_mass_pixel = ((wind_ref - b_3)/m_3) + zero_wind_mass_pixel  - 1315 # function 3
        if 10 <= wind < 25:
            zero_ref_root = (zero_wind_mass -5000)/100
            # converting wind scale of lower table
            wind_ref_root = -1*(wind/10)

            a= 0.550  #before: 0.5
            b= 0.430  #before: 0.438
            c= 0.570  #before: 0.57
            max_mass_root =  ( c- wind_ref_root)**(1/b)-a+zero_ref_root  # function 6 (root function)
            # converting root result to kg
            full_wind_mass = 5000 + (max_mass_root * 100)
            # converting kg to pixel
            max_mass_pixel = ((full_wind_mass-5000)*1.643)+2272
        if 25 <= wind < 30:
            max_mass_pixel = ((wind_ref - b_4)/m_4) + zero_wind_mass_pixel  - 1315 # function 4
        if wind >= 30:
            max_mass_pixel = ((wind_ref - b_5)/m_5)  + zero_wind_mass_pixel  - 1315 # function 5

        if max_mass_pixel > (5257):
            max_mass_pixel = (5257)
        else:
            pass

        # converting pixel to kg:
        full_wind_mass =  5000 + (max_mass_pixel-2272)/1.643

        if full_wind_mass > 6800:
            full_wind_mass = 6800
        else:
            pass

        # calculate maximum mass for customer
        performance_limited_mass = zero_wind_mass + (full_wind_mass - zero_wind_mass) * (perf_benefit/100)

        # rounding
        result_PA = round(PA)
        result_no_wind = round(zero_wind_mass)
        result_wind = round(full_wind_mass)
        result_performance_limited = round (performance_limited_mass)
        result_useful_load = round(performance_limited_mass - DOM)
        result_payload = round(performance_limited_mass - DOM - fuel_at_hho)

        # drawing the new image
        im = Image.open(path_pycharm + "/static/images/Hover_ceiling_OGE_orig.png")
        d = ImageDraw.Draw(im)
        line_color = (255,0,0)

        #shift_on_x = 0  # strangely enough, all lines need to be shifted 28 pixel to the right to fit on the new image

        # 1- pressure altitude / y-axis intercept
        one = (120, PA_pixel)

        # 2- pressure altitude / temperature intercept
        two = (zero_wind_mass_pixel, PA_pixel)

        # 3- 40knots at zero wind mass point
        three = (zero_wind_mass_pixel, 8720)

        # 4- acutal wind at 4400kg point
        four = (120, wind_ref)

        # 5 - wind/mass intercept
        five = (max_mass_pixel, wind_ref)

        # 6 - full wind benefit mass
        six = (max_mass_pixel, 8720)

        # drawing the lines:
        d.line([one, two], fill=line_color, width=15)
        d.line([two,three], fill=line_color, width=15)
        d.line([four,five], fill=line_color, width=15)
        d.line([five,six], fill=line_color, width=15)

        # drawing the approximate connection line between zero wind and max wind
        dot_list = []
        correction = 5  # to draw the line all the way to the end
        for wind_ref in range (6713, int(wind_ref+correction),20):
            if wind_ref < (6713 + 5*33):
                max_mass_pixel = ((wind_ref - b_2)/m_2) + zero_wind_mass_pixel - 1315 # function 2
            elif (6713 + 5*33) <= wind_ref < (6713 + 10*33):
                max_mass_pixel = ((wind_ref - b_3)/m_3) + zero_wind_mass_pixel - 1315# function 3
            elif (6713 + 10*33) <= wind_ref < (6713 + 25*33):
                zero_ref_root = (zero_wind_mass -5000)/100
                # converting wind scale of lower table
                wind_root =((wind_ref - 6713)/33)
                wind_ref_root = -1*(wind_root/10)

                a= 0.550  #before: 0.5
                b= 0.430  #before: 0.438
                c= 0.570  #before: 0.57
                max_mass_root =  ( c- wind_ref_root)**(1/b)-a+zero_ref_root  # function 6 (root function)
                # converting root result to kg
                full_wind_mass = 5000 + (max_mass_root * 100)
                # converting kg to pixel
                max_mass_pixel = ((full_wind_mass-5000)*1.643)+2272
            elif (6713 + 25*33) <= wind_ref < (6713 + 30*33):
                max_mass_pixel = ((wind_ref - b_4)/m_4) + zero_wind_mass_pixel - 1315 # function 4
            elif wind_ref >= (6713 + 25*33):
                max_mass_pixel = ((wind_ref - b_5)/m_5) + zero_wind_mass_pixel - 1315 # function 5
            if max_mass_pixel >= 5257:
                max_mass_pixel = 5257
            else:
                pass
            x_y = (int(max_mass_pixel),int(wind_ref))
            dot_list.append(x_y)
        d.line(dot_list, fill=line_color, width=15)

        # results
        QNH = int(QNH)
        DOM = int(DOM)
        hover_height = int(hover_height)
        temp = int(temp)
        wind = int(wind)
        perf_benefit = int(perf_benefit)
        fuel_at_hho = int(fuel_at_hho)


        # generate the image
        # printing the text on the image:
        font = ImageFont.truetype(path_pycharm + "/static/fonts/SFNS.ttf", 130)

        #d.text((2860,3050),"Calculations provided by Stephan Goldberg",(255,0,0),font=font)

        d.text((5840,1500),"Date, Time (UTC)",(0,0,0),font=font)
        from datetime import datetime
        time = datetime.utcnow().strftime("%Y-%m-%d, %H%M")
        d.text((5840,1650),str(time),(0,0,255),font=font)

        d.text((5840,1850),"Flight ID:" ,(0,0,0),font=font)
        d.text((5840,2000),str(flight_ID_input),(0,0,255),font=font)

        d.text((5840,2200),"PIC/SIC:" ,(0,0,0),font=font)
        d.text((5840,2350),str(PIC_input),(0,0,255),font=font)

        #d.text((5840,2550),'INPUT: ',(0,0,0),font=font)

        d.text((5840,2750),'DOM: ',(0,0,0),font=font)
        d.text((5840,2900),str(DOM) + ' kg' ,(0,0,255),font=font)

        d.text((5840,3100),"QNH:" ,(0,0,0),font=font)
        d.text((5840,3250),str(QNH) + ' mb' ,(0,0,255),font=font)

        d.text((5840,3450),"Height above MSL:" ,(0,0,0),font=font)
        d.text((5840,3600),str(hover_height)+ ' ft' ,(0,0,255),font=font)

        d.text((5840,3800),"Temperature:" ,(0,0,0),font=font)
        d.text((5840,3950),str(temp) + ' C' ,(0,0,255),font=font)

        d.text((5840,4150),"Headwind:" ,(0,0,0),font=font)
        d.text((5840,4300),str(wind) + ' kt' ,(0,0,255),font=font)

        d.text((5840,4500),"Wind Benefit:" ,(0,0,0),font=font)
        d.text((5840,4650),str(perf_benefit) + ' %' ,(0,0,255),font=font)

        d.text((5840,4850),"Fuel at site:" ,(0,0,0),font=font)
        d.text((5840,5000),str(fuel_at_hho) + ' kg',(0,0,255),font=font)



        fontcolor = (255,0,0)
        d.text((5800,6150),"RESULT:" ,(0,0,0),font=font)
        d.text((5800,6350),"Pressure Altitude:" ,(0,0,0),font=font)
        d.text((5800,6500),str(result_PA) + ' ft' ,fontcolor,font=font)
        d.text((5800,6700),"Mass, 0 kt Wind:" ,(0,0,0),font=font)
        d.text((5800,6850),str(result_no_wind) + ' kg' ,fontcolor,font=font)
        d.text((5800,7050),"Mass, "+str(wind) + ' kt Wind:' ,(0,0,0),font=font)
        d.text((5800,7200),str(result_wind) + ' kg' ,fontcolor,font=font)
        d.text((5800,7400),"Mass, "+str(perf_benefit) + ' %'  " Wind:" ,(0,0,0),font=font)
        d.text((5800,7550),str(result_performance_limited) + ' kg' ,fontcolor,font=font)
        d.text((5800,7750),"Useful Load:" ,(0,0,0),font=font)
        d.text((5800,7900),str(result_useful_load) + ' kg' ,fontcolor,font=font)
        d.text((5800,8150),"Payload:" ,(0,0,0),font=font)
        d.text((5800,8300),str(result_payload) + ' kg' ,fontcolor,font=font)


        # figures on chart margin
        d.text((120, PA_pixel-160),str(result_PA) + ' ft' ,fontcolor,font=font)
        d.text((zero_wind_mass_pixel, PA_pixel-160),str(temp) + ' C' ,(0,0,255),font=font)
        d.text((zero_wind_mass_pixel-480, 8652-80),str(result_no_wind) + ' kg' ,fontcolor,font=font)
        d.text((120, wind_ref-160),str(wind) + ' kt' ,(0,0,255),font=font)
        d.text((max_mass_pixel+30,8652-80),str(result_wind) + ' kg' ,fontcolor,font=font)

        # removing previously generated images
        for filename in os.listdir('/home/gaviation/mysite/static/images/'):
            if filename.startswith('139_HOGE_OEI_rendered'):  # not to remove other images
                os.remove('/home/gaviation/mysite/static/images/' + filename)

        # create png
        graph_png = "139_HOGE_OEI_rendered " + str(time) + " UTC.png"
        im.save(path_pycharm + "/static/images/" + graph_png)

        # create pdf
        graph_pdf = "139_HOGE_OEI_rendered " + str(time) + " UTC.pdf"
        rgb = Image.new('RGB', im.size, (255, 255, 255))  # white background
        rgb.paste(im, mask=im.split()[3])                 # paste using alpha channel as mask
        rgb.save(path_pycharm + "/static/images/" + graph_pdf)



        # returning the template (Flask-part)
        return render_template(
            'AW139_OGE_OEI.html',
            QNH = QNH,
            QNH_SV = session['QNH_SV'],

            DOM = DOM,
            DOM_SV = session['DOM_SV'],

            hover_height = hover_height,
            hover_height_SV = session['hover_height_SV'],

            temp = temp,
            temp_SV = session['temp_SV'],

            wind = wind,
            wind_SV = session['wind_SV'],

            perf_benefit = perf_benefit,
            perf_benefit_SV = session['perf_benefit_SV'],

            fuel_at_hho = fuel_at_hho,
            fuel_at_hho_SV = session['fuel_at_hho_SV'],

            PIC = PIC,
            PIC_SV = session['PIC_SV'],

            flight_ID = flight_ID,
            flight_ID_SV = session['flight_ID_SV'],

            result_PA = result_PA,
            result_no_wind = result_no_wind,
            result_wind = result_wind,
            result_performance_limited = result_performance_limited,
            result_useful_load = result_useful_load,
            result_payload = result_payload,
            result_png = graph_png,
            result_pdf = graph_pdf,

            calculation_success = True,
        )

    except ZeroDivisionError:
        return render_template(
            'index.html',
            QNH = QNH,
            DOM = DOM,
            hover_height = hover_height,
            temp = temp,
            wind = wind,
            perf_benefit = perf_benefit,
            fuel_at_hho = fuel_at_hho,
            result="Bad Input",
            calculation_success = False,
            error = "You cannot divide by zero"
        )

    except ValueError:
        return render_template(
            'index.html',
            QNH = QNH,
            DOM = DOM,
            hover_height = hover_height,
            temp = temp,
            wind = wind,
            perf_benefit = perf_benefit,
            fuel_at_hho = fuel_at_hho,
            result="Bad Input",
            calculation_success = False,
            error = "Cannot perform numeric operations with provided input"
        )

@app.route('/AW139_dropdown_6800', methods=['GET', 'POST'])
def AW139_dropdown_6800():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))

    # show the form, it wasn't submitted
    return render_template('AW139_dropdown_6800.html')

@app.route('/AW139_dropdown_6800_result/', methods=['POST', 'GET'])
def AW139_dropdown_6800_result():

    error = None
    result = None

    # paths
    font = ImageFont.truetype(path_pycharm + "/static/fonts/SFNS.ttf", 80)
    im = Image.open(path_pycharm + "/static/images/baseline_images/AW139_dropdown_6800.png")

    # request.form looks for:
    # html tags with matching "name= "
    QNH_input = request.form['QNH']
    session['QNH_SV'] = QNH_input

    gross_mass_input = request.form['gross_mass']
    session['gross_mass_SV'] = gross_mass_input

    hover_height_input = request.form['hover_height']
    session['hover_height_SV'] = hover_height_input

    temp_input = request.form['temp']
    session['temp_SV'] = temp_input

    wind_input = request.form['wind']
    session['wind_SV'] = wind_input

    PIC_input = request.form['PIC']
    session['PIC_SV'] = PIC_input

    flight_ID_input = request.form['flight_ID']
    session['flight_ID_SV'] = flight_ID_input
    try:
        QNH = float(QNH_input)
        gross_mass = float(gross_mass_input)
        hover_height = float(hover_height_input)
        temp = float(temp_input)
        wind = float(wind_input)
        PIC = str(PIC_input)
        flight_ID = str(flight_ID_input)

        # Calulating pixel_PA:
        #  pressure difference between QNH and standard pressure
        difference = (1013.2 - QNH) * 27

        # pressure difference added to hover height.
        PA = hover_height + difference
        # converting to PA on chart
        zero_feet = 3852
        sixthousand_feet = 1501
        # input PA_pixel (vertical line)
        PA_pixel = round(zero_feet + PA * ((sixthousand_feet - zero_feet) / 6000))
        # x = PA_pixel  # vertical line


        # function 0 - temperature line at 10C
        x_1,y_1 = 1115,1942          # about 7000, 0.45 (10C)
        x_2,y_2 = 4242,3168          # about -1000, 0.175  (10C)
        m_0 = (y_1 - y_2)/(x_1 - x_2) #slope
        b_0 = -m_0*x_1 + y_1          #intercept

        # # equation for 10C line (273.15K + 10K):
        # y_pixel = m_0*x_pixel + b_0

        # # equation for -273.15C (0 Kelvin) line:
        # y_pixel = m_0*x_pixel + b_0 + (283.15+10)*15

        # # equation for 'temp'C line ( 273.15K + 'temp'K)
        # y_pixel = m_0*x_pixel + b_0 + (283.15+10)*15 - (283.15+temp)*15

        # substituting x_pixel for PA_pixel we obtain the equation for y_pixel value
        PA_temp_pixel = m_0 * PA_pixel + b_0 + (283.15+10)*15 - (283.15+temp)*15


        # # finding the equation for 6400kg line
        # we reverse x and y, because y is the input and x is the output here
        # point_4 = (4055, 4533)
        # point_5 = (3560,4870)
        # point_6 = (3311, 5056)
        # point_7 = (3062,5257)
        # point_8 = (2814,5472)
        # point_9 = (2562, 5707)
        # point_10 = (2016, 6282)
        # # fitting with polynomial regression (2 degrees) results in:
        # out_pixel = 0.000123437*in_pixel**2 - 1.60415*in_pixel + 9011.4

        # next we find out how much the line shifts for every kg:
        # for every kg above 6400kg and up to 6800kg the line shifts by 260/400 pixel down (in the positive direction)
        above6400 = gross_mass - 6400
        above6400_pixel = above6400 * 260/400

        mass_pixel = 0.000123437*(PA_temp_pixel - above6400_pixel)**2 - 1.60415*(PA_temp_pixel - above6400_pixel )+ 9011.4

        # # finding the equation for 0kt wind line
        # point_11 = (4844,1798)
        # point_12 = (5132,1736)
        # point_13 = (5420,1613)
        # point_14 = (5707,1427)
        # point_15 = (5996,1179)
        # point_16 = (6283,870)
        # # fitting with polynomial regression (2 degrees) results in:
        # out_pixel = -0.000374156*in_pixel**2 + 3.5184*in_pixel - 6465.88

        d1 = 5862 - 5804 # from 0 to 10 knots right shift
        d2 = 5936 - 5862 # from 10 to 20 knots right shift
        d3 = 6052 -5936  # from 20 to 30 knots right shift
        d4 =6208 - 6052  # from 30 to 40 knots right shift

        if wind <= 10:
            height_loss_pixel = (-0.000374156)*(mass_pixel-(wind*(d1)/10))**2 + 3.5184*(mass_pixel-(wind*(d1)/10))-6465.88
        elif 10 < wind <=20:
            height_loss_pixel = (-0.000374156)*(mass_pixel-d1-     ((wind-10)*d2/10)   )**2 + 3.5184*(mass_pixel-d1-      ((wind-10)*d2/10) )-6465.88
        elif 20 < wind <=30:
            height_loss_pixel = (-0.000374156)*(mass_pixel-d1-d2-  ((wind-20)*d3/10)   )**2 + 3.5184*(mass_pixel-d1-d2-  ((wind-20)*d3/10) )-6465.88
        elif 30 < wind <=40:
            height_loss_pixel = (-0.000374156)*(mass_pixel-d1-d2-d3-  ((wind-30)*d4/10)   )**2 + 3.5184*(mass_pixel-d1-d2-d3-  ((wind-30)*d4/10) )-6465.88

        # convert pixel to feet and preparing for html variables:
        zero_feet = 1916        #pixel
        two_hundret_feet = 788  #pixel
        one_foot = (two_hundret_feet - zero_feet)/200  #pixel per foot
        height_loss_feet =  (height_loss_pixel - zero_feet)/one_foot
        result_height_loss_feet = round(height_loss_feet)
        result_PA = round(PA)
        QNH = int(QNH)
        gross_mass = int(gross_mass)
        hover_height = int(hover_height)
        temp = int(temp)
        wind = int(wind)

        # generating the image
        #im = Image.open(path_pycharm + "/static/images/baseline_images/AW139_dropdown_6800.png")
        d = ImageDraw.Draw(im)
        line_color = (255, 0, 0)

        # defining the points:
        point_1 = (PA_pixel, 4184)    # pressure altitude on x-axis
        point_2 = (PA_pixel, PA_temp_pixel) # pressure altitude intersect with temp line
        point_3 = (mass_pixel, PA_temp_pixel)     # mass intersection
        point_4 = (mass_pixel, height_loss_pixel) # wind intersection
        point_5 = (4112, height_loss_pixel)  # height loss (ft) on y-axis

        # drawing the lines between points:
        d.line([point_1,point_2], fill=line_color, width=10)
        d.line([point_2,point_3], fill=line_color, width=10)
        d.line([point_3,point_4], fill=line_color, width=10)
        d.line([point_4,point_5], fill=line_color, width=10)
        #font = ImageFont.truetype(path_pycharm + "/static/fonts/SFNS.ttf", 80)
        d.text((3820,height_loss_pixel-40),str(result_height_loss_feet) + ' ft' ,(255,0,0),font=font)

        # #testbed to draw functions on graph
        # shift = -(58 + 74 + 116 + 156)
        # dot_list = []
        # for x_pixel in range (4844,6283, 5):
        #     y_pixel = -0.000374156*(x_pixel+shift)**2 + 3.5184*(x_pixel+shift) - 6465.88
        #     x_y = (x_pixel,int(y_pixel))
        #     dot_list.append(x_y)
        # d.line(dot_list, fill=line_color, width=5)

        # text on image:
        vertical_align = 100
        horizontal_align = -730
        d.text((vertical_align,500),"Date, Time (UTC)",(0,0,0),font=font)
        time = datetime.utcnow().strftime("%Y-%m-%d, %H:%M")
        d.text((vertical_align,580),str(time),(0,0,255),font=font)

        d.text((vertical_align,700),"Flight ID:" ,(0,0,0),font=font)
        d.text((vertical_align,780),str(flight_ID_input),(0,0,255),font=font)
        d.text((vertical_align,900),"PIC/SIC:" ,(0,0,0),font=font)
        d.text((vertical_align,980),str(PIC_input),(0,0,255),font=font)

        #d.text((vertical_align,2050+horizontal_align),'USER INPUT: ',(0,0,0),font=font)
        d.text((vertical_align,2250+horizontal_align),'Gross Mass: ',(0,0,0),font=font)
        d.text((vertical_align,2400+horizontal_align),str(gross_mass) + ' kg' ,(0,0,255),font=font)
        d.text((vertical_align,2600+horizontal_align),"QNH:" ,(0,0,0),font=font)
        d.text((vertical_align,2750+horizontal_align),str(QNH) + ' mb' ,(0,0,255),font=font)
        d.text((vertical_align,2950+horizontal_align),"Hover Height:" ,(0,0,0),font=font)
        d.text((vertical_align,3100+horizontal_align),str(hover_height)+ ' ft' ,(0,0,255),font=font)
        d.text((vertical_align,3300+horizontal_align),"Temperature:" ,(0,0,0),font=font)
        d.text((vertical_align,3450+horizontal_align),str(temp) + ' C' ,(0,0,255),font=font)
        d.text((vertical_align,3650+horizontal_align),"Wind:" ,(0,0,0),font=font)
        d.text((vertical_align,3800+horizontal_align),str(wind) + ' kt' ,(0,0,255),font=font)

        fontcolor = (255,0,0)
        d.text((vertical_align,4150+horizontal_align),"RESULT:" ,(0,0,0),font=font)
        d.text((vertical_align,4350+horizontal_align),"Pressure Altitude:" ,(0,0,0),font=font)
        d.text((vertical_align,4500+horizontal_align),str(result_PA) + ' ft' , fontcolor,font=font)
        d.text((vertical_align,4700+horizontal_align),"Height loss:" ,(0,0,0),font=font)
        d.text((vertical_align,4850+horizontal_align),str(result_height_loss_feet) + ' ft' , fontcolor,font=font)

        # removing previously generated images
        for filename in os.listdir('/home/gaviation/mysite/static/images/'):
            if filename.startswith('AW139_dropdown_6800_rendered'):  # not to remove other images
                os.remove('/home/gaviation/mysite/static/images/' + filename)

        # create png
        graph_png = "AW139_dropdown_6800_rendered " + str(time) + " UTC.png"
        im.save(path_pycharm + "/static/images/" + graph_png)

        # create pdf
        graph_pdf = "AW139_dropdown_6800_rendered " + str(time) + " UTC.pdf"
        rgb = Image.new('RGB', im.size, (255, 255, 255))  # white background
        rgb.paste(im, mask=im.split()[3])                 # paste using alpha channel as mask
        rgb.save(path_pycharm + "/static/images/" + graph_pdf)


        # returning the template (Flask-part)
        return render_template(
            'AW139_dropdown_6800.html',
            QNH = QNH,
            QNH_SV = session['QNH_SV'],
            gross_mass = gross_mass,
            gross_mass_SV = session['gross_mass_SV'],
            hover_height = hover_height,
            hover_height_SV = session['hover_height_SV'],
            temp = temp,
            temp_SV = session['temp_SV'],
            wind = wind,
            wind_SV = session['wind_SV'],
            PIC = PIC,
            PIC_SV = session['PIC_SV'],
            flight_ID = flight_ID,
            flight_ID_SV = session['flight_ID_SV'],

            result_PA = result_PA,
            result_height_loss_feet = result_height_loss_feet,
            result_png = graph_png,
            result_pdf = graph_pdf,
            calculation_success = True,
        )

    except ZeroDivisionError:
        return render_template(
            'index.html',
            QNH = QNH,
            hover_height = hover_height,
            temp = temp,
            wind = wind,
            result="Bad Input",
            calculation_success = False,
            error = "You cannot divide by zero"
        )

    except ValueError:
        return render_template(
            'index.html',
            QNH = QNH,
            hover_height = hover_height,
            temp = temp,
            wind = wind,
            result="Bad Input",
            calculation_success = False,
            error = "Cannot perform numeric operations with provided input"
        )

@app.route('/AW169_OGE_OEI', methods=['GET', 'POST'])
def AW169_OGE_OEI():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))

    # show the form, it wasn't submitted
    return render_template('AW169_OGE_OEI.html')

@app.route('/AW169_OGE_OEI_result/', methods=['POST', 'GET'])
def AW169_OGE_OEI_result():

    error = None
    result = None

    # flask
    font = ImageFont.truetype(path_pycharm + "/static/fonts/SFNS.ttf", 60)
    im = Image.open(path_pycharm + "/static/images/baseline_images/AW169_HOGE_OEI_600.png")


    # # jupyter
    # im = Image.open("charts/AW169/OEI_hover/modified/AW169_HOGE_OEI_600.png")
    # font = ImageFont.truetype("SFNS.ttf", 50)
    # from datetime import date, datetime

    # flask
    # request.form looks for:
    # html tags with matching "name= "
    QNH_input = request.form['QNH']
    session['QNH_SV'] = QNH_input

    DOM_input = request.form['DOM']
    session['DOM_SV'] = DOM_input

    hover_height_input = request.form['hover_height']
    session['hover_height_SV'] = hover_height_input

    temp_input = request.form['temp']
    session['temp_SV'] = temp_input

    wind_input = request.form['wind']
    session['wind_SV'] = wind_input

    perf_benefit_input = request.form['perf_benefit']
    session['perf_benefit_SV'] = perf_benefit_input

    fuel_at_hho_input = request.form['fuel_at_hho']
    session['fuel_at_hho_SV'] = fuel_at_hho_input

    PIC_input = request.form['PIC']
    session['PIC_SV'] = PIC_input

    flight_ID_input = request.form['flight_ID']
    session['flight_ID_SV'] = flight_ID_input

    # # jupyter
    # # User input:
    # DOM = 3000
    # QNH = 1013.2                # mb (min 971, max 1044)
    # hover_height = 1000          # feet (min 0, max 350)
    # temp = 10                   # degrees celcius (min: -10, max: 30)
    # wind = 26               # knots (min: 0, max: 40)
    # perf_benefit = 100          # percent
    # fuel_at_hho = 439           # kg


    # flask
    try:
        QNH = float(QNH_input)
        DOM = float(DOM_input)
        hover_height = float(hover_height_input)
        temp = float(temp_input)
        wind = float(wind_input)
        perf_benefit = float(perf_benefit_input)
        fuel_at_hho = float(fuel_at_hho_input)
        PIC = str(PIC_input)
        flight_ID = str(flight_ID_input)

        # Calulating pixel_PA:
        #  pressure difference between QNH and standard pressure
        difference = (1013.2 - QNH) * 27

        # pressure difference added to hover height.
        PA = hover_height + difference
        result_PA = round(PA)
        # converting to PA on chart in pixel

        #scaling the PA line
        lower_feet = 3307  # here: 0 feet
        upper_feet = 2528  # here 6000 feet
        diff_feet = 6000 - 0
        # input PA_pixel (vertical line)
        PA_pixel = round(lower_feet + PA * ((upper_feet - lower_feet) / diff_feet))

        # we pick the 30C line
        line = 30

        # function 0 - temperature line at 30C
        x_1,y_1 = 589,2653          # about 5000ft, 30C
        x_2,y_2 = 1521,3329          # about 4025kg, 30C
        m_0 = (y_1 - y_2)/(x_1 - x_2) #slope
        b_0 = -m_0*x_1 + y_1          #intercept

        # # equation for 30C line (273.15K + 30K = 303.15K) line:
        # y_pixel = m_0*x_pixel + b_0

        # for each degree above 0K we move (3394 - 3218)/10 = 16.8px in the positive(+) pixel direction
        change_per_degree = +(3394 - 3218)/10
        absolute_zero = 273.15
        # # equation for -273.15C (0 Kelvin) line:
        # y_pixel = m_0*x_pixel + b_0 - (273.15 + 30)*change_per_degree

        # # equation for 'temp'C line ( 273.15K + 'temp'K)
        # y_pixel = m_0*x_pixel + b_0 - (273.15 + 30)*change_per_degree + (273.15+temp)*change_per_degree

        # # solving for x_pixel:
        # x_pixel =  (y_pixel - (b_0 - (273.15 + 30)*change_per_degree + (273.15+temp)*change_per_degree) )/m_0

        # # substituting the variables
        PA_temp_pixel =  (PA_pixel - (b_0 - (absolute_zero + line)*change_per_degree + (absolute_zero+temp)*change_per_degree) )/m_0


        # use different line if past the 4025kg-line on x-axis:
        if PA_temp_pixel > 1520:
            # we pick the 20C line
            line = 20

            # function 0 - temperature line at 30C
            x_1,y_1 = 1520,3157          # about 4025kg, 20C
            x_2,y_2 = 1719,3280 # about 4180kg, 20C
            m_0 = (y_1 - y_2)/(x_1 - x_2) #slope
            b_0 = -m_0*x_1 + y_1          #intercept

            PA_temp_pixel =  (PA_pixel - (b_0 - (absolute_zero + line)*change_per_degree + (absolute_zero+temp)*change_per_degree) )/m_0

        # x = PA_temp_pixel
        # y = PA_pixel

        # checking if result is of right side of divisor line (blue):
        x_1,y_1 = 1681,2751          # about 4150kg, -10C
        x_2,y_2 = 1746,3437          # about 4200kg, -1000ft
        slope = (y_1 - y_2)/(x_1 - x_2) #slope
        intercept = -slope*x_1 + y_1    #intercept

        result_a = PA_pixel
        result_b = PA_temp_pixel * slope + intercept

        if result_b > result_a:
            # we pick the 0C line
            line = 0

            # function 0 - temperature line at 30C
            x_1,y_1 = 1700,2923          # about 3000ft, 0C
            x_2,y_2 = 1818,3362          # about 4265kg, 0C
            m_0 = (y_1 - y_2)/(x_1 - x_2) #slope
            b_0 = -m_0*x_1 + y_1          #intercept

            # # equation for 30C line (273.15K + 30K = 303.15K) line:
            # y_pixel = m_0*x_pixel + b_0

            # for each degree above 0K we move (3394 - 3218)/10 = 16.8px in the positive(+) pixel direction
            change_per_degree = +(3440 - 3308)/10
            absolute_zero = 273.15
            # # equation for -273.15C (0 Kelvin) line:
            # y_pixel = m_0*x_pixel + b_0 - (273.15 + 30)*change_per_degree

            # # equation for 'temp'C line ( 273.15K + 'temp'K)
            # y_pixel = m_0*x_pixel + b_0 - (273.15 + 30)*change_per_degree + (273.15+temp)*change_per_degree

            # # solving for x_pixel:
            # x_pixel =  (y_pixel - (b_0 - (273.15 + 30)*change_per_degree + (273.15+temp)*change_per_degree) )/m_0

            # # substituting the variables
            PA_temp_pixel =  (PA_pixel - (b_0 - (absolute_zero + line)*change_per_degree + (absolute_zero+temp)*change_per_degree) )/m_0


        # use different line if past the 4025kg-line on x-axis:
        if PA_temp_pixel > 1818:
            # we pick the -10C line
            line = -10

            # function 0 - temperature line at 30C
            x_1,y_1 = 1818,3230          # about 4265kg, -10C
            x_2,y_2 = 1864,3433          # about 4290kg, -10C
            m_0 = (y_1 - y_2)/(x_1 - x_2) #slope
            b_0 = -m_0*x_1 + y_1          #intercept

            change_per_degree = +(3433 - 3298)/10

            PA_temp_pixel =  (PA_pixel - (b_0 - (absolute_zero + line)*change_per_degree + (absolute_zero+temp)*change_per_degree) )/m_0

        PA_temp_pixel = round(PA_temp_pixel)

        # convert pixel output to chart value
        lower_pixel = 712   # here: 3400kg
        upper_pixel = 2004  # here: 4400kg
        diff_value_kg =  4400 - 3400
        diff_value_pixel = upper_pixel  - lower_pixel

        pixel_per_kg = diff_value_pixel / diff_value_kg

        zero_wind_mass = 3400 + ( PA_temp_pixel - lower_pixel )/pixel_per_kg

        divisor = 5
        wind_mod = wind%divisor
        wind_table ={0:0,
                     5:62,
                    10:218,
                    15:398,
                    20:618,
                    25:849,
                    30:1045,
                    35:1259,
                    40:1499,
                    45:1723,
                    50:1959}

        if wind_mod == 0:
            result = wind_table.get(wind)

        else:
            wind_floor = wind//divisor
            wind_mod = wind%divisor
            table_value = wind_floor * divisor
            result1 = wind_table.get(table_value)
            result2 = (wind_mod/divisor)*((wind_table.get(table_value+divisor))-wind_table.get(table_value))
            result = round(result1 + result2)

        result_full_wind_mass = round (zero_wind_mass + result)
        result_full_wind_mass_customer = result_full_wind_mass
        if result_full_wind_mass > 4800:
            result_full_wind_mass = 4800
        result_zero_wind_mass = round(zero_wind_mass)
        result_customer_mass = round(result_zero_wind_mass + (result_full_wind_mass_customer - result_zero_wind_mass)* perf_benefit/100)
        if result_customer_mass > 4800:
            result_customer_mass = 4800
        result_useful_load = round(result_customer_mass - DOM)
        result_payload = round(result_useful_load - fuel_at_hho)

# double, can be removed if block above work
        # result_full_wind_mass = round (zero_wind_mass + result)
        # if result_full_wind_mass > 4800:
        #     result_full_wind_mass = 4800
        # result_zero_wind_mass = round(zero_wind_mass)
        # result_customer_mass = round(result_zero_wind_mass + (result_full_wind_mass - result_zero_wind_mass)* perf_benefit/100)
        # if result_customer_mass > 4800:
        #     result_customer_mass = 4800
        # result_useful_load = round(result_customer_mass - DOM)
        # result_payload = round(result_useful_load - fuel_at_hho)

        QNH = int(QNH)
        DOM = int(DOM)
        hover_height = int(hover_height)
        temp = int(temp)
        wind = int(wind)
        perf_benefit = int(perf_benefit)
        fuel_at_hho = int(fuel_at_hho)


        # generating the image
        d = ImageDraw.Draw(im)
        line_color = (255, 0, 0)

        # defining the points:
        point_1 = (70, PA_pixel)           # pressure altitude on y-axis
        point_2 = (PA_temp_pixel, PA_pixel) # pressure altitude intersect with temp line
        point_3 = (PA_temp_pixel, 3520)     # zero wind mass on x-axis

        # drawing the lines between points:
        d.line([point_1,point_2], fill=line_color, width=10)
        d.line([point_2,point_3], fill=line_color, width=10)

        # text on image:
        vertical_align = 2931
        horizontal_align = -730
        d.text((vertical_align,580),"Date, Time (UTC)",(0,0,0),font=font)
        time = datetime.utcnow().strftime("%Y-%m-%d, %H:%M")
        d.text((vertical_align,650),str(time),(0,0,255),font=font)
        d.text((vertical_align,800),"Flight ID:" ,(0,0,0),font=font)
        d.text((vertical_align,870),str(flight_ID_input),(0,0,255),font=font)
        d.text((vertical_align,1000),"PIC/SIC:" ,(0,0,0),font=font)
        d.text((vertical_align,1070),str(PIC_input),(0,0,255),font=font)
        d.text((vertical_align,2100+horizontal_align),'USER INPUT: ',(0,0,0),font=font)
        d.text((vertical_align,2200+horizontal_align),'Dry Ops Mass: ',(0,0,0),font=font)
        d.text((vertical_align,2270+horizontal_align),str(DOM) + ' kg' ,(0,0,255),font=font)
        d.text((vertical_align,2400+horizontal_align),"QNH:" ,(0,0,0),font=font)
        d.text((vertical_align,2470+horizontal_align),str(QNH) + ' mb' ,(0,0,255),font=font)
        d.text((vertical_align,2600+horizontal_align),"Hover Height:" ,(0,0,0),font=font)
        d.text((vertical_align,2670+horizontal_align),str(hover_height)+ ' ft' ,(0,0,255),font=font)
        d.text((vertical_align,2800+horizontal_align),"Temperature:" ,(0,0,0),font=font)
        d.text((vertical_align,2870+horizontal_align),str(temp) + ' C' ,(0,0,255),font=font)
        d.text((vertical_align,3000+horizontal_align),"Wind:" ,(0,0,0),font=font)
        d.text((vertical_align,3070+horizontal_align),str(wind) + ' kt' ,(0,0,255),font=font)
        d.text((vertical_align,3200+horizontal_align),"Wind benefit:" ,(0,0,0),font=font)
        d.text((vertical_align,3270+horizontal_align),str(perf_benefit) + ' %' ,(0,0,255),font=font)
        d.text((vertical_align,3400+horizontal_align),"Fuel at HHO:" ,(0,0,0),font=font)
        d.text((vertical_align,3470+horizontal_align),str(fuel_at_hho) + ' kg' ,(0,0,255),font=font)

        fontcolor = (255,0,0)
        d.text((vertical_align,3900+horizontal_align),"RESULT:" ,(0,0,0),font=font)
        d.text((vertical_align,4000+horizontal_align),"Pressure Altitude:" ,(0,0,0),font=font)
        d.text((vertical_align,4070+horizontal_align),str(result_PA) + ' ft' , fontcolor,font=font)

        d.text((vertical_align,4200+horizontal_align),"Mass, 0 kt Wind:" ,(0,0,0),font=font)
        d.text((vertical_align,4270+horizontal_align),str(result_zero_wind_mass) + ' kg' , fontcolor,font=font)
        d.text((vertical_align,4400+horizontal_align),"Mass, "+str(wind) + ' kt Wind' ,(0,0,0),font=font)
        d.text((vertical_align,4470+horizontal_align),str(result_full_wind_mass) + ' kg' , fontcolor,font=font)
        d.text((vertical_align,4600+horizontal_align),"Mass, "+str(perf_benefit) + ' %'  " Wind:" ,(0,0,0),font=font)
        d.text((vertical_align,4670+horizontal_align),str(result_customer_mass) + ' kg' , fontcolor,font=font)
        d.text((vertical_align,4800+horizontal_align),"Useful Load at site:" ,(0,0,0),font=font)
        d.text((vertical_align,4870+horizontal_align),str(result_useful_load) + ' kg' , fontcolor,font=font)
        d.text((vertical_align,5000+horizontal_align),"Payload at site:" ,(0,0,0),font=font)
        d.text((vertical_align,5070+horizontal_align),str(result_payload) + ' kg' , fontcolor,font=font)

        d.text((60, PA_pixel-80),str(result_PA) + ' ft' , fontcolor,font=font)
        d.text((PA_temp_pixel, PA_pixel-80),str(temp) + ' C' ,(0,0,255),font=font)
        d.text((PA_temp_pixel, 3520),str(result_zero_wind_mass) + ' kg' , fontcolor,font=font)

        # wind box
        begin = 1050
        end = 2732
        fieldlength = (end - begin)/9
        zeroknots = begin - fieldlength
        pix_per_knot = fieldlength / 5
        windpix = zeroknots + (pix_per_knot * wind)
        top = 3724
        bottom = 4288
        linetop_pt = (windpix,top)
        linebottom_pt = (windpix, bottom)
        linetop_left = (windpix-50,top )
        linetop_right = (windpix +50, top)
        linebottom_left = (windpix-50,bottom )
        linebottom_right = (windpix +50, bottom)
        #draw lines
        d.line([linetop_pt,linebottom_pt], fill=line_color, width=5)
        d.line([linetop_left,linetop_right], fill=line_color, width=10)
        d.line([linebottom_left,linebottom_right], fill=line_color, width=10)
        #text
        d.text((windpix-50,top -80),str(wind) + ' kt' ,(0,0,255),font=font)
        d.text((windpix-80,bottom +10),str(result) + ' kg' ,(255,0,0),font=font)

        # removing previously generated images
        for filename in os.listdir('/home/gaviation/mysite/static/images/'):
            if filename.startswith('AW169_HOGE_OEI_rendered'):  # not to remove other images
                os.remove('/home/gaviation/mysite/static/images/' + filename)

        # create png
        graph_png = "AW169_HOGE_OEI_rendered " + str(time) + " UTC.png"
        im.save(path_pycharm + "/static/images/" + graph_png)

        # create pdf
        graph_pdf = "AW169_HOGE_OEI_rendered " + str(time) + " UTC.pdf"
        rgb = Image.new('RGB', im.size, (255, 255, 255))  # white background
        rgb.paste(im, mask=im.split()[3])                 # paste using alpha channel as mask
        rgb.save(path_pycharm + "/static/images/" + graph_pdf)


        # returning the template (Flask-part)
        return render_template(
            'AW169_OGE_OEI.html',
            QNH = QNH,
            QNH_SV = session['QNH_SV'],
            DOM = DOM,
            DOM_SV = session['DOM_SV'],
            hover_height = hover_height,
            hover_height_SV = session['hover_height_SV'],
            temp = temp,
            temp_SV = session['temp_SV'],
            wind = wind,
            wind_SV = session['wind_SV'],
            perf_benefit = perf_benefit,
            perf_benefit_SV = session['perf_benefit_SV'],
            fuel_at_hho = fuel_at_hho,
            fuel_at_hho_SV = session['fuel_at_hho_SV'],
            PIC = PIC,
            PIC_SV = session['PIC_SV'],
            flight_ID = flight_ID,
            flight_ID_SV = session['flight_ID_SV'],
            result_PA = result_PA,
            result_zero_wind_mass = result_zero_wind_mass,
            result_full_wind_mass = result_full_wind_mass,
            result_customer_mass = result_customer_mass,
            result_useful_load = result_useful_load,
            result_payload = result_payload,
            result_png = graph_png,
            result_pdf = graph_pdf,
            calculation_success = True,
        )

    except ZeroDivisionError:
        return render_template(
            'index.html',
            QNH = QNH,
            DOM = DOM,
            hover_height = hover_height,
            temp = temp,
            wind = wind,
            perf_benefit = perf_benefit,
            fuel_at_hho = fuel_at_hho,
            result="Bad Input",
            calculation_success = False,
            error = "You cannot divide by zero"
        )

    except ValueError:
        return render_template(
            'index.html',
            QNH = QNH,
            DOM = DOM,
            hover_height = hover_height,
            temp = temp,
            wind = wind,
            perf_benefit = perf_benefit,
            fuel_at_hho = fuel_at_hho,
            result="Bad Input",
            calculation_success = False,
            error = "Cannot perform numeric operations with provided input"
        )

@app.route('/AW169_dropdown_4200', methods=['GET', 'POST'])
def AW169_dropdown_4200():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))

    # show the form, it wasn't submitted
    return render_template('AW169_dropdown_4200.html')

@app.route('/AW169_dropdown_4200_result/', methods=['POST', 'GET'])
def AW169_dropdown_4200_result():

    error = None
    result = None

    # flask
    font = ImageFont.truetype(path_pycharm + "/static/fonts/SFNS.ttf", 50)
    im = Image.open(path_pycharm + "/static/images/baseline_images/AW169_drowdown_4200_600.png")


    # # jupyter
    # im = Image.open("charts/AW169/OEI_hover/modified/AW169_HOGE_OEI_600.png")
    # font = ImageFont.truetype("SFNS.ttf", 50)
    # from datetime import date, datetime

    # flask
    # request.form looks for:
    # html tags with matching "name= "
    QNH_input = request.form['QNH']
    session['QNH_SV'] = QNH_input


    hover_height_input = request.form['hover_height']
    session['hover_height_SV'] = hover_height_input

    temp_input = request.form['temp']
    session['temp_SV'] = temp_input

    wind_input = request.form['wind']
    session['wind_SV'] = wind_input

    PIC_input = request.form['PIC']
    session['PIC_SV'] = PIC_input

    flight_ID_input = request.form['flight_ID']
    session['flight_ID_SV'] = flight_ID_input

    # flask
    try:
        QNH = float(QNH_input)
        hover_height = float(hover_height_input)
        temp = float(temp_input)
        wind = float(wind_input)
        PIC = str(PIC_input)
        flight_ID = str(flight_ID_input)
        # Calulating pixel_PA:
        #  pressure difference between QNH and standard pressure
        difference = (1013.2 - QNH) * 27

        # pressure difference added to hover height.
        PA = hover_height + difference
        result_PA = round(PA)
        print("PA: " + str(PA))
        # converting to PA on chart in pixel

        #scaling the PA line
        lower_feet = 3035  # here: 0 feet
        upper_feet = 1346  # here 5000 feet
        diff_feet = 5000 - (0)
        # input PA_pixel (vertical line)
        PA_pixel = round(lower_feet + PA * ((upper_feet - lower_feet) / diff_feet))


        #X  = [-1000, 0 ,1000,2000,3000,4000,5000]  # chart values
        y   = [3372,3035,2697,2360,2022,1684,1346]  # pixel values

        x_neg10 = [ 758, 762, 766, 773, 782, 794,823]  # -10 deg line
        x_0   =   [ 763, 768, 774, 783, 795, 826,873]
        x_10  =   [ 768, 772, 782, 797, 832, 882,958]
        x_20  =   [ 772, 782, 806, 841, 896, 977,1089]
        x_30  =   [ 784, 811, 849, 907, 990,1101,1278]
        x_40  =   [ 823, 866, 934,1028,1174,1400,1695]
        x_45  =   [836,912,1031,1225,1538,1954,2478]
        x_50  =   [900,1001,1189,1482,1880,2393,3079]  # 50 deg line

        # dictionary of temperature lines
        temp_dict ={-10:x_neg10,
                     0:x_0,
                    10:x_10,
                    20:x_20,
                    30:x_30,
                    40:x_40,
                    45:x_45,
                    50:x_50}

        # switched x and y here, since for this particular case y is the input and x is the output
        if temp in temp_dict.keys():
            x = temp_dict.get(temp)
            model = np.poly1d(np.polyfit(y, x, len(y)-1)) # polynomial regression of degree (len(y)-1)
            # r2_score(x, model(y)) # r-score   # check the r2 score
            ft_pixel = round(model(PA_pixel))   # make prediction
            print("Pixel feet: "+ str(ft_pixel))
        else:
            lower_temp_key = max(k for k in temp_dict if k <= temp) # finding the adjacent lower value in the dictionary
            upper_temp_key = min(k for k in temp_dict if k >= temp) # finding the adjacent higher value in the dictionary
            x_1 = temp_dict.get(lower_temp_key)  # getting the pixel table
            x_2 = temp_dict.get(upper_temp_key)  # getting the pixel table
            model_1 = np.poly1d(np.polyfit(y, x_1, len(y)-1))
            model_2 = np.poly1d(np.polyfit(y, x_2, len(y)-1))
            intersect1 = model_1(PA_pixel)  # prediction
            intersect2 = model_2(PA_pixel)  # prediction
            interpolated = intersect1 + ((temp-lower_temp_key)/(upper_temp_key - lower_temp_key)*(intersect2-intersect1))
            ft_pixel = round(interpolated)
            print("Pixel feet: "+ str(ft_pixel))

        # convert pixel output to chart value
        lower_pixel = 747   # here: 0   ft
        upper_pixel = 2529  # here: 170 ft
        diff_value_pixel = upper_pixel  - lower_pixel # number of pixel in whole range
        diff_value_unit =  170 - 0   # number of units in whole range

        pixel_per_unit = diff_value_pixel / diff_value_unit

        feet = 0 + ( ft_pixel - lower_pixel )/pixel_per_unit
        print('Feet: '+ str(feet))

        # wind correction table
        divisor = 5
        wind_mod = wind%divisor
        wind_table ={0:0,
                     5:2,
                    10:7,
                    15:12,
                    20:17,
                    25:22,
                    30:27,
                    35:32,
                    40:37,
                    45:42,
                    50:47}
        if wind_mod == 0:
            wind_correction = wind_table.get(wind)
        else:
            wind_floor = wind//divisor
            wind_mod = wind%divisor
            table_value = wind_floor * divisor
            wind_correction1 = wind_table.get(table_value)
            wind_correction2 = (wind_mod/divisor)*((wind_table.get(table_value+divisor))-wind_table.get(table_value))
            wind_correction = wind_correction1 + wind_correction2
        print("wind correction: "+ str(wind_correction))

        result_PA
        result_feet = int(round (feet))
        result_wind_correction = round(wind_correction)
        result_total_dropdown = int(round(feet - wind_correction))
        if result_total_dropdown <0:
            result_total_dropdown = 0

        wind = int(wind)
        temp = int(temp)
        hover_height = int(hover_height)
        QNH = int(QNH)

        # generating the image
        d = ImageDraw.Draw(im)
        line_color = (255, 0, 0)

        # defining the points:
        point_1 = (728, PA_pixel)           # pressure altitude on y-axis
        point_2 = (ft_pixel, PA_pixel) # pressure altitude intersect with temp line
        point_3 = (ft_pixel, 3400)     # zero wind mass on x-axis

        # drawing the lines between points:
        d.line([point_1,point_2], fill=line_color, width=10)
        d.line([point_2,point_3], fill=line_color, width=10)

        # text on image:
        vertical_align = 2931
        horizontal_align = -730
        d.text((vertical_align,500),"Date, Time (UTC)",(0,0,0),font=font)
        time = datetime.utcnow().strftime("%Y-%m-%d, %H:%M")
        d.text((vertical_align,580),str(time),(0,0,255),font=font)

        d.text((vertical_align,700),"Flight ID:" ,(0,0,0),font=font)
        d.text((vertical_align,780),str(flight_ID_input),(0,0,255),font=font)
        d.text((vertical_align,900),"PIC/SIC:" ,(0,0,0),font=font)
        d.text((vertical_align,980),str(PIC_input),(0,0,255),font=font)

        # d.text((vertical_align,2050+horizontal_align),'USER INPUT: ',(0,0,0),font=font)
        d.text((vertical_align,2400+horizontal_align),"QNH:" ,(0,0,0),font=font)
        d.text((vertical_align,2450+horizontal_align),str(QNH) + ' mb' ,(0,0,255),font=font)
        d.text((vertical_align,2600+horizontal_align),"Hover Height:" ,(0,0,0),font=font)
        d.text((vertical_align,2650+horizontal_align),str(hover_height)+ ' ft' ,(0,0,255),font=font)
        d.text((vertical_align,2800+horizontal_align),"Temperature:" ,(0,0,0),font=font)
        d.text((vertical_align,2850+horizontal_align),str(temp) + ' C' ,(0,0,255),font=font)
        d.text((vertical_align,3000+horizontal_align),"Wind:" ,(0,0,0),font=font)
        d.text((vertical_align,3050+horizontal_align),str(wind) + ' kt' ,(0,0,255),font=font)

        fontcolor = (255,0,0)
        d.text((vertical_align,3800+horizontal_align),"RESULT:" ,(0,0,0),font=font)
        d.text((vertical_align,4000+horizontal_align),"Pressure Altitude:" ,(0,0,0),font=font)
        d.text((vertical_align,4050+horizontal_align),str(result_PA) + ' ft' , fontcolor,font=font)

        d.text((vertical_align,4200+horizontal_align),"Dropdown with 0kt Wind:" ,(0,0,0),font=font)
        d.text((vertical_align,4250+horizontal_align),str(result_feet) + ' ft' , fontcolor,font=font)
        d.text((vertical_align,4400+horizontal_align),"Wind-benefit:" ,(0,0,0),font=font)
        d.text((vertical_align,4450+horizontal_align),str(result_wind_correction) + ' ft' , fontcolor,font=font)
        d.text((vertical_align,4600+horizontal_align),"Total Dropdown:" ,(0,0,0),font=font)
        d.text((vertical_align,4650+horizontal_align),str(result_total_dropdown) + ' ft' , fontcolor,font=font)

        # wind box
        begin = 1300
        end = 2437
        fieldlength = (end - begin)/9
        zeroknots = begin - fieldlength
        pix_per_knot = fieldlength / 5
        windpix = zeroknots + (pix_per_knot * wind)
        top = 3674
        bottom = 3960
        linetop_pt = (windpix,top)
        linebottom_pt = (windpix, bottom)
        linetop_left = (windpix-50,top )
        linetop_right = (windpix +50, top)
        linebottom_left = (windpix-50,bottom )
        linebottom_right = (windpix +50, bottom)
        #draw lines
        d.line([linetop_pt,linebottom_pt], fill=line_color, width=5)
        d.line([linetop_left,linetop_right], fill=line_color, width=10)
        d.line([linebottom_left,linebottom_right], fill=line_color, width=10)
        #text
        d.text((windpix-35,top -80),str(wind) + ' kt' ,(0,0,255),font=font)
        d.text((windpix-35,bottom +20),str(result_wind_correction) + ' ft' ,(255,0,0),font=font)

        # removing previously generated images
        for filename in os.listdir('/home/gaviation/mysite/static/images/'):
            if filename.startswith('AW169_dropdown_4200_rendered'):  # not to remove other images
                os.remove('/home/gaviation/mysite/static/images/' + filename)

        # create png
        graph_png = "AW169_dropdown_4200_rendered " + str(time) + " UTC.png"
        im.save(path_pycharm + "/static/images/" + graph_png)

        # create pdf
        graph_pdf = "AW169_dropdown_4200_rendered " + str(time) + " UTC.pdf"
        rgb = Image.new('RGB', im.size, (255, 255, 255))  # white background
        rgb.paste(im, mask=im.split()[3])                 # paste using alpha channel as mask
        rgb.save(path_pycharm + "/static/images/" + graph_pdf)


        # returning the template (Flask-part)
        return render_template(
            'AW169_dropdown_4200.html',
            QNH = QNH,
            QNH_SV = session['QNH_SV'],
            hover_height = hover_height,
            hover_height_SV = session['hover_height_SV'],
            temp = temp,
            temp_SV = session['temp_SV'],
            wind = wind,
            wind_SV = session['wind_SV'],
            PIC = PIC,
            PIC_SV = session['PIC_SV'],
            flight_ID = flight_ID,
            flight_ID_SV = session['flight_ID_SV'],
            result_PA = result_PA,
            result_feet = result_feet,
            result_wind_correction = result_wind_correction,
            result_total_dropdown = result_total_dropdown,
            result_png = graph_png,
            result_pdf = graph_pdf,
            calculation_success = True,
        )

    except ZeroDivisionError:
        return render_template(
            'index.html',
            QNH = QNH,
            hover_height = hover_height,
            temp = temp,
            wind = wind,
            result="Bad Input",
            calculation_success = False,
            error = "You cannot divide by zero"
        )

    except ValueError:
        return render_template(
            'index.html',
            QNH = QNH,
            hover_height = hover_height,
            temp = temp,
            wind = wind,
            result="Bad Input",
            calculation_success = False,
            error = "Cannot perform numeric operations with provided input"
        )

@app.route('/AW139_dropdown_enhanced', methods=['GET', 'POST'])
def AW139_dropdown_enhanced():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))

    # show the form, it wasn't submitted
    return render_template('AW139_dropdown_enhanced.html')

@app.route('/AW139_dropdown_enhanced_result/', methods=['POST', 'GET'])
def AW139_dropdown_enhanced_result():

    error = None
    result = None

    # flask
    im = Image.open(path_pycharm + "/static/images/baseline_images/AW139_dropdown_enhanced.png")
    font = ImageFont.truetype(path_pycharm + "/static/fonts/SFNS.ttf", 70)



    # # jupyter
    # im = Image.open("charts/AW139/dropdown_enhanced/modified/AW139_dropdown_enhanced.png")
    # font = ImageFont.truetype("SFNS.ttf", 80)
    # from datetime import date, datetime

    # flask
    # request.form looks for:
    # html tags with matching "name= "
    QNH_input = request.form['QNH']
    session['QNH_SV'] = QNH_input

    gross_mass_input = request.form['gross_mass']
    session['gross_mass_SV'] = gross_mass_input

    hover_height_input = request.form['hover_height']
    session['hover_height_SV'] = hover_height_input

    temp_input = request.form['temp']
    session['temp_SV'] = temp_input

    wind_input = request.form['wind']
    session['wind_SV'] = wind_input

    perf_benefit_input = request.form['perf_benefit']
    session['perf_benefit_SV'] = perf_benefit_input

    PIC_input = request.form['PIC']
    session['PIC_SV'] = PIC_input

    flight_ID_input = request.form['flight_ID']
    session['flight_ID_SV'] = flight_ID_input


    # # jupyter
    # # User input:
    # gross_mass = 7000           # 6600 to 7000kg
    # QNH = 1013.2                # mb (min 971, max 1044)
    # hover_height = 200          # feet (min 0, max 350)
    # temp = 25                   # degrees celcius (min: -10, max: 30)
    # wind = 7               # knots (min: 0, max: 40)
    # flight_ID = 'HSO41A'
    # PIC =  'SGO'

    # flask
    try:
        QNH = float(QNH_input)
        gross_mass = float(gross_mass_input)
        hover_height = float(hover_height_input)
        temp = float(temp_input)
        wind = float(wind_input)
        perf_benefit = float(perf_benefit_input)
        PIC = str(PIC_input)
        flight_ID = str(flight_ID_input)

        '''The left chart area:'''
        # Calulating pixel_PA:
        #  pressure difference between QNH and standard pressure
        difference = (1013.2 - QNH) * 27

        # pressure altitude at hover height.
        PA = hover_height + difference
        result_PA = round(PA)

        # converting PA to pixel
        pixel_per_ft = (2496 - 841)/2000
        PA_pixel = 1668 + (result_PA * pixel_per_ft)

        # Define the known points
        x = [841, 2495]  # 0ftPA, 1000ftPA
        y_1 = [3744,3226] #-30 deg
        y_2 = [3452,2942] #-20 deg
        y_3 = [3178,2670] #-10 deg
        y_4 = [2916,2412]   #0 deg
        y_5 = [2664, 2165] #10 deg
        y_6 = [2422,1926]  #20 deg
        y_7 = [2192,1702]  #30 deg
        y_8 = [1970,1480]  #40 deg
        y_9 = [1756,1256]  #50 deg

        # reference dictionary
        temp_dict ={-30:y_1,-20:y_2,-10:y_3,0:y_4,10:y_5,20:y_6,30:y_7,40:y_8,50:y_9}

        # assign the input
        pixel_in = PA_pixel

        if temp in temp_dict.keys():
            y = temp_dict.get(temp)
            model = np.poly1d(np.polyfit(x,y, len(y)-1)) # polynomial regression of degree (len(y)-1)
            # r2_score(x, model(y)) # r-score   # check the r2 score
            pixel_out_left = round(model(pixel_in))   # make prediction
        else:
            lower_temp_key = max(k for k in temp_dict if k <= temp) # finding the adjacent lower value in the dictionary
            upper_temp_key = min(k for k in temp_dict if k >= temp) # finding the adjacent higher value in the dictionary
            y_lower = temp_dict.get(lower_temp_key)  # getting the pixel table
            y_upper = temp_dict.get(upper_temp_key)  # getting the pixel table
            model_1 = np.poly1d(np.polyfit(x, y_lower, len(y_lower)-1))
            model_2 = np.poly1d(np.polyfit(x, y_upper, len(y_upper)-1))
            intersect1 = model_1(pixel_in)  # prediction
            intersect2 = model_2(pixel_in)  # prediction
            interpolated = intersect1 + ((temp-lower_temp_key)/(upper_temp_key - lower_temp_key)*(intersect2-intersect1))
            pixel_out_left = round(interpolated)

        # assign the output
        pixel_in_middle = pixel_out_left

        '''The middle chart area:'''
        # line for pixel_in starts on y-axis at 1503 (top left corner)
        x=[2520,2762,2992,3233,3465,3697,3937,4173,4411]
        y=[1503,1585,1684,1831,1988,2155,2332,2532,2739]

        # shift line for different input values
        correction = pixel_in_middle - 1503
        y = [i+correction for i in y]

        # fit polynomial regression
        coef = np.polyfit(x, y, 5)

        # create model to be used for other input values
        model = np.poly1d(coef)

        '''Analysis of model for middle chart'''
        # print ('coef1 =', coef[0])
        # print ('coef2 =', coef[1])
        # from sklearn.metrics import r2_score
        # y_pred = model(x)
        # print(r2_score(y, y_pred)) # r-score   # check the r2 score
        # x_axis = np.linspace(min(x),max(x),100)
        # y_axis = model(x_axis)  # the prediction
        # plt.plot(x_axis, y_axis)
        # plt.plot( x, y, 'go' )
        # plt.grid('on')
        # plt.show()

        # wind pixel
        pixel_per_knot = (4411-2520)/40
        wind_pixel = round(2520 +  (pixel_per_knot * wind))
        zero_wind_pixel = 2520

        # plotting the line
        x_pixel = np.linspace(min(x),wind_pixel,100) # full wind
        x_zero_pixel = np.linspace(min(x),zero_wind_pixel,100) # zero wind
        y_pixel = model(x_pixel) #the prediction for full wind
        y_zero_pixel = model(x_zero_pixel) #the prediction for zero wind

        # pixle out
        pixel_out_middle = round(model(wind_pixel)) # full wind
        pixel_zero_out_middle = round(model(zero_wind_pixel)) # zero wind

        # assigning pixel_in:
        pixel_in_right = pixel_out_middle # full wind
        pixel_zero_in_right = pixel_zero_out_middle # zero wind


        '''Right chart area'''
        # pixel values on x- and y-axis
        y_7000=[4435,4509,4709,4980,5336,5556,5774,6098,6444]
        x_7000=[2811,2697,2494,2293,2089,1989,1889,1769,1647]
        y_6800=[4436,4509,4705,4980,5339,5781,6325,6443]
        x_6800=[2609,2495,2297,2093,1890,1689,1488,1452]
        y_6600=[4435,4504,4703,4987,5151,5331]
        x_6600=[2401,2294,2091,1890,1793,1692]
        y_6400=[4435,4496,4694,4831,4966]
        x_6400=[2187,2091,1892,1789,1690]
        y_6200=[4435,4484,4679,4951,5127]
        x_6200=[1970,1891,1689,1485,1387]
        y_6000=[4435,4470,4658,4789]
        x_6000=[1747,1690,1487,1388]
        y_5800=[4434,4450,4539]
        x_5800=[1515,1486,1389]

        # dictionary for mass lines
        mass_dict ={7000:[x_7000,y_7000],
                    6800:[x_6800,y_6800],
                    6600:[x_6600,y_6600],
                    6400:[x_6400,y_6400],
                    6200:[x_6200,y_6200],
                    6000:[x_6000,y_6000],
                    5800:[x_5800,y_5800]}

        # finding the output value
        if gross_mass in mass_dict.keys():
            x_and_y = mass_dict.get(gross_mass)
            model = np.poly1d(np.polyfit(x_and_y[0], x_and_y[1], len(x_and_y[0])-1)) # polynomial regression of degree (len(x_y[0])-1)
            # r2_score(x, model(y)) # r-score   # check the r2 score
            height_loss_pixel = round(model(pixel_in_right))   # make prediction full wind
            height_loss_pixel_zero = round(model(pixel_zero_in_right))   # make prediction zero wind
        #    print("Pixel height loss: "+ str(height_loss_pixel))
        else:
            lower_key = max(k for k in mass_dict if k <= gross_mass) # finding the adjacent lower value in the dictionary
            upper_key = min(k for k in mass_dict if k >= gross_mass) # finding the adjacent higher value in the dictionary
            x_and_y_1 = mass_dict.get(lower_key)  # getting the pixel table
            x_and_y_2 = mass_dict.get(upper_key)  # getting the pixel table
            model_1 = np.poly1d(np.polyfit(x_and_y_1[0],x_and_y_1[1], len(x_and_y_1[0])-1))
            model_2 = np.poly1d(np.polyfit(x_and_y_2[0],x_and_y_2[1], len(x_and_y_2[0])-1))
            intersect1 = model_1(pixel_in_right)  # prediction full wind
            intersect2 = model_2(pixel_in_right)  # prediction full wind
            intersect1_zero = model_1(pixel_zero_in_right)  # prediction full wind
            intersect2_zero = model_2(pixel_zero_in_right)  # prediction full wind

            interpolated = intersect1 + ((gross_mass-lower_key)/(upper_key - lower_key)*(intersect2-intersect1)) # full wind
            interpolated_zero = intersect1_zero + ((gross_mass-lower_key)/(upper_key - lower_key)*(intersect2_zero-intersect1_zero)) # zero wind

            height_loss_pixel = round(interpolated) # full wind
            height_loss_pixel_zero = round(interpolated_zero) # zero wind
        #     print("Pixel height loss: "+ str(height_loss_pixel))
        # print(pixel_in_right)

        # convert pixel output to chart value
        lower_pixel = 4434   # here: 0ft
        upper_pixel = 6443  # here: 150ft
        diff_value_pixel = upper_pixel  - lower_pixel # number of pixel in whole range
        diff_value_unit =  150 - 0   # number of units in whole range

        pixel_per_unit = diff_value_pixel / diff_value_unit

        result_height_loss_feet = int(0 + ( height_loss_pixel - lower_pixel )/pixel_per_unit) # full wind
        result_height_loss_feet_zero = int(0 + ( height_loss_pixel_zero - lower_pixel )/pixel_per_unit) # zero wind
        result_height_loss_perf_benefit = int(result_height_loss_feet_zero + (perf_benefit/100 * (result_height_loss_feet - result_height_loss_feet_zero)))
        # print(' Height Loss Feet: '+ str(result_height_loss_feet))


        '''Preparing for print '''
        QNH = int(QNH)
        gross_mass = int(gross_mass)
        hover_height = int(hover_height)
        temp = int(temp)
        wind = int(wind)

        # generating the image
        d = ImageDraw.Draw(im)
        line_color = (255, 0, 0)





        # defining the points:
        point_1 = (PA_pixel, 4450)           # pressure altitude on x-axis
        point_2 = (PA_pixel, pixel_out_left) # pressure altitude intersect with temp line
        point_3 = (zero_wind_pixel, pixel_out_left)     # entry point in middle chart

        point_4 = (wind_pixel, 4450)       # full wind start point
        point_4_zero = (zero_wind_pixel, 4450)       # zero wind start point

        point_5 = (wind_pixel, pixel_out_middle) # full wind
        point_5_zero = (zero_wind_pixel, pixel_zero_out_middle) # zero wind

        point_6 = (height_loss_pixel, pixel_out_middle) # between middle and right chart
        point_6_zero = (height_loss_pixel_zero, pixel_zero_out_middle) # between middle and right chart zero wind

        point_7 = (height_loss_pixel, 4450)  # height loss point
        point_7_zero = (height_loss_pixel_zero, 4450)  # height loss point zero wind

        # drawing the lines between points:
        d.line([point_1,point_2], fill=line_color, width=10)
        d.line([point_2,point_3], fill=line_color, width=10)

        #x_y = (x_pixel,y_pixel)
        x_y = zip(x_pixel,y_pixel)
        x_y = list(x_y)
        x_y_zero = zip (x_zero_pixel, y_zero_pixel)
        x_y_zero = list(x_y_zero)
        # dot_list.append(x_y)
        d.line(x_y, fill=line_color, width=10)
        d.line(x_y_zero, fill=line_color, width=10)
        # here following full wind curve
        d.line([point_4,point_5], fill=line_color, width=10)
        d.line([point_5,point_6], fill=line_color, width=10)
        d.line([point_6,point_7], fill=line_color, width=10)
        # zero wind curve
        d.line([point_4_zero,point_5_zero], fill=line_color, width=10)
        d.line([point_5_zero,point_6_zero], fill=line_color, width=10)
        d.line([point_6_zero,point_7_zero], fill=line_color, width=10)
        # zero wind curve



        # text on image:
        vertical_align = 100
        horizontal_align = -730
        d.text((vertical_align,500),"Date, Time (UTC)",(0,0,0),font=font)
        time = datetime.utcnow().strftime("%Y-%m-%d, %H:%M")
        d.text((vertical_align,600),str(time),(0,0,255),font=font)

        d.text((vertical_align,750),"Flight ID:" ,(0,0,0),font=font)
        d.text((vertical_align,850),str(flight_ID_input),(0,0,255),font=font)

        d.text((vertical_align,950),"PIC/SIC:" ,(0,0,0),font=font)
        d.text((vertical_align,1050),str(PIC_input),(0,0,255),font=font)

        d.text((vertical_align,2050+horizontal_align),'USER INPUT: ',(0,0,0),font=font)
        d.text((vertical_align,2150+horizontal_align),'Gross Mass: ',(0,0,0),font=font)
        d.text((vertical_align,2250+horizontal_align),str(gross_mass) + ' kg' ,(0,0,255),font=font)
        d.text((vertical_align,2350+horizontal_align),"QNH:" ,(0,0,0),font=font)
        d.text((vertical_align,2450+horizontal_align),str(QNH) + ' mb' ,(0,0,255),font=font)
        d.text((vertical_align,2550+horizontal_align),"TDP (above MSL):" ,(0,0,0),font=font)
        d.text((vertical_align,2650+horizontal_align),str(hover_height)+ ' ft' ,(0,0,255),font=font)
        d.text((vertical_align,2750+horizontal_align),"Temperature:" ,(0,0,0),font=font)
        d.text((vertical_align,2850+horizontal_align),str(temp) + ' C' ,(0,0,255),font=font)
        d.text((vertical_align,2950+horizontal_align),"Actual Wind:" ,(0,0,0),font=font)
        d.text((vertical_align,3050+horizontal_align),str(wind) + ' kt' ,(0,0,255),font=font)
        d.text((vertical_align,3150+horizontal_align),"Performance Benefit:" ,(0,0,0),font=font)
        d.text((vertical_align,3250+horizontal_align),str(int(perf_benefit)) + ' %' ,(0,0,255),font=font)

        fontcolor = (255,0,0)
        d.text((vertical_align,3500+horizontal_align),"RESULT:" ,(0,0,0),font=font)
        d.text((vertical_align,3600+horizontal_align),"Pressure Altitude:" ,(0,0,0),font=font)
        d.text((vertical_align,3700+horizontal_align),str(result_PA) + ' ft' , fontcolor,font=font)
        d.text((vertical_align,3800+horizontal_align),"Height loss zero wind:" ,(0,0,0),font=font)
        d.text((vertical_align,3900+horizontal_align),str(result_height_loss_feet_zero) + ' ft' , fontcolor,font=font)
        d.text((vertical_align,4000+horizontal_align),"Height loss full wind:" ,(0,0,0),font=font)
        d.text((vertical_align,4100+horizontal_align),str(result_height_loss_feet) + ' ft' , fontcolor,font=font)
        d.text((vertical_align,4300+horizontal_align),"Height loss " +  str(int(perf_benefit)) + ' % perf.benefit: ',(0,0,0),font=font)
        d.text((vertical_align,4400+horizontal_align),str(result_height_loss_perf_benefit) + ' ft' , fontcolor,font=font)

        d.text((PA_pixel-200, 4450-80),str(result_PA) + ' ft' , fontcolor,font=font)
        d.text((zero_wind_pixel-150, 4450-80),'0 kt' ,(0,0,255),font=font)
        d.text((wind_pixel+50, 4450-80),str(wind) + ' kt' ,(0,0,255),font=font)
        d.text((height_loss_pixel-200, 4450-80),str(result_height_loss_feet) + ' ft' , fontcolor,font=font)
        d.text((height_loss_pixel_zero+50, 4450-80),str(result_height_loss_feet_zero) + ' ft' , fontcolor,font=font) # here
        d.text((PA_pixel-200, pixel_out_left-80),str(temp) + ' C' ,(0,0,255),font=font)
        d.text((height_loss_pixel_zero+30, pixel_zero_out_middle-80),str(gross_mass) + ' kg' ,(0,0,255),font=font)

        # flask
        # removing previously generated images
        for filename in os.listdir('/home/gaviation/mysite/static/images/'):
            if filename.startswith('AW139_dropdown_enhanced_rendered'):  # not to remove other images
                os.remove('/home/gaviation/mysite/static/images/' + filename)

        # create png
        graph_png = "AW139_dropdown_enhanced_rendered " + str(time) + " UTC.png"
        im.save(path_pycharm + "/static/images/" + graph_png)

        # create pdf
        graph_pdf = "AW139_dropdown_enhanced_rendered " + str(time) + " UTC.pdf"
        rgb = Image.new('RGB', im.size, (255, 255, 255))  # white background
        rgb.paste(im, mask=im.split()[3])                 # paste using alpha channel as mask
        rgb.save(path_pycharm + "/static/images/" + graph_pdf)

        # likely nothing
        # im.save("AW139_dropdown_enhanced_rendered.png")


        # returning the template (Flask-part)
        return render_template(
            'AW139_dropdown_enhanced.html',
            gross_mass = gross_mass,
            gross_mass_SV = session['gross_mass_SV'],
            QNH = QNH,
            QNH_SV = session['QNH_SV'],
            hover_height = hover_height,
            hover_height_SV = session['hover_height_SV'],
            temp = temp,
            temp_SV = session['temp_SV'],
            wind = wind,
            wind_SV = session['wind_SV'],
            perf_benefit = perf_benefit,
            perf_benefit_SV = session['perf_benefit_SV'],
            PIC = PIC,
            PIC_SV = session['PIC_SV'],
            flight_ID = flight_ID,
            flight_ID_SV = session['flight_ID_SV'],
            result_PA = result_PA,
            result_height_loss_feet = result_height_loss_feet,
            result_height_loss_perf_benefit = result_height_loss_perf_benefit,
            # result_feet = result_feet,
            # result_wind_correction = result_wind_correction,
            # result_total_dropdown = result_total_dropdown,
            result_png = graph_png,
            result_pdf = graph_pdf,
            calculation_success = True,
        )

    except ZeroDivisionError:
        return render_template(
            'index.html',
            QNH = QNH,
            hover_height = hover_height,
            temp = temp,
            wind = wind,
            perf_benefit = perf_benefit,
            result="Bad Input",
            calculation_success = False,
            error = "You cannot divide by zero"
        )

    except ValueError:
        return render_template(
            'index.html',
            QNH = QNH,
            hover_height = hover_height,
            temp = temp,
            wind = wind,
            perf_benefit = perf_benefit,
            result="Bad Input",
            calculation_success = False,
            error = "Cannot perform numeric operations with provided input"
        )

@app.route('/AW139_rejected_tod_clear_area', methods=['GET', 'POST'])
def AW139_rejected_tod_clear_area():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))

    # show the form, it wasn't submitted
    return render_template('AW139_rejected_tod_clear_area.html')

@app.route('/AW139_rejected_tod_clear_area_result/', methods=['POST', 'GET'])
def AW139_rejected_tod_clear_area_result():

    error = None
    result = None

    fontcolor = (255,0,0)
    line_color = (255, 0, 0)

    #flask
    QNH_input = request.form['QNH']
    session['QNH_SV'] = QNH_input

    height_input = request.form['height']
    session['height_SV'] = height_input

    gross_mass_input = request.form['gross_mass']
    session['gross_mass_SV'] = gross_mass_input

    temp_input = request.form['temp']
    session['temp_SV'] = temp_input

    wind_input = request.form['wind']
    session['wind_SV'] = wind_input

    PIC_input = request.form['PIC']
    session['PIC_SV'] = PIC_input

    flight_ID_input = request.form['flight_ID']
    session['flight_ID_SV'] = flight_ID_input

    # flask
    QNH = int(QNH_input)
    height = int(height_input)
    gross_mass = int(gross_mass_input)
    temp = int(temp_input)
    wind = int(wind_input)
    PIC = PIC_input
    flight_ID = flight_ID_input



    # # jupyter
    # im = Image.open("charts/AW139/dropdown_enhanced/modified/AW139_dropdown_enhanced.png")
    # font = ImageFont.truetype("SFNS.ttf", 80)
    # from datetime import date, datetime

    # flask
    # request.form looks for:
    # html tags with matching "name= "



    # # jupyter
    # # User input:
    # gross_mass = 7000           # 6600 to 7000kg
    # QNH = 1013.2                # mb (min 971, max 1044)
    # hover_height = 200          # feet (min 0, max 350)
    # temp = 25                   # degrees celcius (min: -10, max: 30)
    # wind = 7               # knots (min: 0, max: 40)
    # flight_ID = 'HSO41A'
    # PIC =  'SGO'


    '''Forking three charts:'''
    if gross_mass <= 6400:

        # # jupyter
        # font = ImageFont.truetype("SFNS.ttf", 60)
        # im = Image.open("charts/AW139/rejected_tod_clear_area/modified/AW139_rejected_tod_clear_area_6400.png")

        # flask
        font = ImageFont.truetype(path_pycharm + "/static/fonts/SFNS.ttf", 60)
        im = Image.open(path_pycharm + "/static/images/baseline_images/AW139_rejected_tod_clear_area_6400.png")

        d = ImageDraw.Draw(im) # generating the image

        '''Left chart area:'''
        # Calulating Pressure Altitude and pixel_PA:
        difference = (1013.2 - QNH) * 27 #  pressure difference between QNH and standard pressure
        result_PA = round(height + difference) # pressure altitude at hover height.
        lower_PA_pixel = 2211 # here: 0ft
        upper_PA_pixel = 555  # here: 14000ft
        diff_upper_lower_PA = 14000 # difference between upper and lower PA on chart
        pixel_per_ft = (upper_PA_pixel - lower_PA_pixel)/diff_upper_lower_PA # converting PA to pixel
        PA_pixel = lower_PA_pixel + (result_PA * pixel_per_ft) # converting PA to pixel

        input_output_row_pixel = 2800
        point_1 = (PA_pixel, input_output_row_pixel)              # defining starting point on chart
        d.text((PA_pixel+80, input_output_row_pixel-80),str(result_PA) + ' ft' , fontcolor,font=font) # labeling the point

        # pixel values on x- and y-axis
        x_1=[ 555, 792,1028,1265] #-40
        y_1=[1721,1929,2150,2387]
        x_2=[ 555, 792,1028,1265,1502] #-30
        y_2=[1622,1823,2039,2270,2516]
        x_3=[ 555, 792,1028,1265,1502] #-20
        y_3=[1528,1722,1929,2151,2386]
        x_4=[ 555, 792,1028,1265,1502,1738] #-10
        y_4=[1443,1628,1827,2043,2271,2511]
        x_5=[ 555, 792,1028,1265,1502,1738] # 0
        y_5=[1359,1539,1731,1937,2157,2388]
        x_6=[ 555, 792,1028,1265,1502,1738,1975] # +10
        y_6=[1280,1450,1635,1834,2046,2269,2508]
        x_7=[ 555, 792,1028,1265,1502,1738,1975,2102] # +20
        y_7=[1188,1351,1529,1722,1925,2143,2370,2498]
        x_8=[          1028,1265,1502,1738,1975,2211] # +30
        y_8=[          1416,1599,1793,1999,2217,2448]
        x_9=[                         1738,1975,2211,2330] # +40
        y_9=[                         1864,2073,2289,2399]
        x_10=[                                  2211,2330] # +50
        y_10=[                                  2095,2201]

        # dictionary for lines
        dictionary ={-40:[x_1,y_1],
                     -30:[x_2,y_2],
                     -20:[x_3,y_3],
                     -10:[x_4,y_4],
                       0:[x_5,y_5],
                      10:[x_6,y_6],
                      20:[x_7,y_7],
                      30:[x_8,y_8],
                      40:[x_9,y_9],
                      50:[x_10,y_10]}

        # finding the output value
        input_real = temp
        input_pixel = PA_pixel
        if input_real in dictionary.keys():
            x_and_y = dictionary.get(input_real)
            model = np.poly1d(np.polyfit(x_and_y[0], x_and_y[1], len(x_and_y[0])-1)) # polynomial regression of degree (len(x_y[0])-1)
            # r2_score(x, model(y)) # r-score   # check the r2 score
            output_pixel = round(model(input_pixel))   #  prediction
        else:
            lower_key = max(k for k in dictionary if k <= input_real) # finding the adjacent lower value in the dictionary
            upper_key = min(k for k in dictionary if k >= input_real) # finding the adjacent higher value in the dictionary
            x_and_y_1 = dictionary.get(lower_key)  # getting the pixel table for the lower line
            x_and_y_2 = dictionary.get(upper_key)  # getting the pixel table for the upper line
            model_1 = np.poly1d(np.polyfit(x_and_y_1[0],x_and_y_1[1], len(x_and_y_1[0])-1)) # model the lower line
            model_2 = np.poly1d(np.polyfit(x_and_y_2[0],x_and_y_2[1], len(x_and_y_2[0])-1)) # model the upper line
            intersect1 = model_1(input_pixel)  # prediction upper line
            intersect2 = model_2(input_pixel)  # prediction lower line
            interpolated = intersect1 + ((input_real-lower_key)/(upper_key - lower_key)*(intersect2-intersect1)) # interpolate between lower and upper line
            output_pixel = round(interpolated)
        pixel_limit = 2501
        if output_pixel > pixel_limit:
            output_pixel = pixel_limit
        # # restricting the chart output
        # if output_pixel > 2501:
        #     output_pixel = 2501
        output_pixel_left = output_pixel
        point_2 = (PA_pixel, output_pixel_left) # defining second point on chart
        d.text((PA_pixel-150, output_pixel_left-80),str(temp) + ' C' ,(0,0,255),font=font) # point label

        # #  sanity check: plotting the model
        # # define plot range
        # input_is_x = 0 # set to 1 if input is x
        # output_is_y = 1 # set to 0 if output is y
        # chart_lower_value = 555 # choose x- or y- values
        # chart_upper_value = 2331  # choose x- or y- values
        # for key in dictionary.keys():
        #     x_and_y = dictionary.get(key)
        #     model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1))
        #     point_list = []
        #     for i in np.arange(chart_lower_value,chart_upper_value,10):
        #         output_pixel = round(model(i))
        #         point = (i, output_pixel)  # make sure x and y have correct position here!!
        #         point_list.append(point)
        #     d.line(point_list, fill=line_color, width=10)

        '''Middle chart area:'''
        # pixel values on x- and y-axis
        x_1=[2424,2414,2419,2421,2425,2435,2449,2454,2456,2502,2533,2597,2721,2847,3036,3098,3224,3287,3350,3429,3475] # 6400kg
        y_1=[2398,2471,2439,2419,2399,2385,2367,2363,2358,2299,2259,2179,2019,1859,1617,1536,1376,1295,1216,1113,1055]
        x_2=[2409,3385] # 6000kg
        y_2=[2222,1055]
        x_3=[2409,3288] #5600kg
        y_3=[2039,1055]
        x_4=[2409,3171] # 5200kg
        y_4=[1841,1055]
        x_5=[2409,3027] # 4800kg
        y_5=[1653,1055]
        x_6=[2409,2865] # 4400kg
        y_6=[1461,1055]

        # dictionary for lines
        dictionary ={6400:[x_1,y_1],
                     6000:[x_2,y_2],
                     5600:[x_3,y_3],
                     5200:[x_4,y_4],
                     4800:[x_5,y_5],
                     4400:[x_6,y_6]}

        # finding the output value
        input_real = gross_mass
        input_pixel = output_pixel_left

        # defining input and output variable
        input_is_x = 1 # set to 1 if input is x, set to 0 if input is y
        output_is_y = 0 # set to 0 if output is y, set to 1 if output is x

        if input_real in dictionary.keys():
            x_and_y = dictionary.get(input_real)
            model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1)) # polynomial regression of degree (len(x_y[0])-1)
            # r2_score(x, model(y)) # r-score   # check the r2 score
            output_pixel = round(model(input_pixel))   #  prediction
        else:
            lower_key = max(k for k in dictionary if k <= input_real) # finding the adjacent lower value in the dictionary
            upper_key = min(k for k in dictionary if k >= input_real) # finding the adjacent higher value in the dictionary
            x_and_y_1 = dictionary.get(lower_key)  # getting the pixel table for the lower line
            x_and_y_2 = dictionary.get(upper_key)  # getting the pixel table for the upper line
            model_1 = np.poly1d(np.polyfit(x_and_y_1[input_is_x],x_and_y_1[output_is_y], len(x_and_y_1[0])-1)) # model the lower line
            model_2 = np.poly1d(np.polyfit(x_and_y_2[input_is_x],x_and_y_2[output_is_y], len(x_and_y_2[0])-1)) # model the upper line
            intersect1 = model_1(input_pixel)  # prediction upper line
            intersect2 = model_2(input_pixel)  # prediction lower line
            interpolated = intersect1 + ((input_real-lower_key)/(upper_key - lower_key)*(intersect2-intersect1)) # interpolate between lower and upper line
            output_pixel = round(interpolated)
        pixel_limit = 2409
        if output_pixel < pixel_limit:
            output_pixel = pixel_limit


        output_pixel_middle = output_pixel
        point_3 = (output_pixel_middle, output_pixel_left)     # entry point in middle chart
        d.text((output_pixel_middle+40, output_pixel_left-80),str(gross_mass) + ' kg' ,(0,0,255),font=font) # point label

        # # sanity check: plotting the model
        # # define plot range
        # input_is_x = 0 # set to 1 if input is x
        # output_is_y = 1 # set to 0 if output is y
        # chart_lower_value = 2403 # choose x- or y- values
        # chart_upper_value = 3471  # choose x- or y- values
        # for key in dictionary.keys():
        #     x_and_y = dictionary.get(key)
        #     model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1))
        #     point_list = []
        #     for i in np.arange(chart_lower_value,chart_upper_value,10):
        #         output_pixel = round(model(i))
        #         point = (i, output_pixel)  # make sure x and y have correct position here!!
        #         point_list.append(point)
        #     d.line(point_list, fill=line_color, width=10)

        point_4 = (output_pixel_middle, input_output_row_pixel)      # bottom exit point middle chart

        # convert pixel output to chart value
        lower_pixel = 2346   # here: 0   m
        upper_pixel = 3475  # here: 1800 m
        diff_value_pixel = upper_pixel  - lower_pixel # number of pixel in whole range
        diff_value_unit =  1800 - 0   # number of units in whole range
        pixel_per_unit = diff_value_pixel / diff_value_unit

        result_distance = round(0 + ( output_pixel_middle - lower_pixel )/pixel_per_unit)
        print('Meter: '+ str(result_distance))

        d.text((output_pixel_middle+80, input_output_row_pixel-80),str(result_distance) + ' m' , fontcolor,font=font) # point label

        '''Right chart area:'''
        input_pixel_right = output_pixel_left  #beware
        input_pixel = output_pixel_left

        # defining the curve by points
        x_1=[3492,3543,3651,3734,3814,3975,4136,4198]
        y_1=[2500,2420,2242,2101,1955,1635,1241,1055]
        x_and_y = [x_1,y_1]

        # defining input and output variable
        input_is_x = 1 # set to 1 if input is x, set to 0 if input is y
        output_is_y = 0 # set to 0 if output is y, set to 1 if output is x

        # fitting the model to the data
        model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1))
        output_pixel = round(model(input_pixel))   #  prediction
        output_pixel_right = output_pixel

        point_5 = (output_pixel_right, input_pixel_right)  # intersection point right chart
        point_6 = (output_pixel_right, input_output_row_pixel)  # bottom exit point right chart

        # convert pixel output to chart value
        lower_pixel = 3491   # here: 0 m
        upper_pixel = 4298  # here: -25 m
        diff_value_pixel = upper_pixel  - lower_pixel # number of pixel in whole range
        diff_value_unit =  -25 - 0   # number of units in whole range
        pixel_per_unit = diff_value_pixel / diff_value_unit

        result_correction = round(0 + ( output_pixel_right - lower_pixel )/pixel_per_unit,2)
        print('Correction factor: '+ str(result_correction))

        d.text((output_pixel_right+80, input_output_row_pixel-80),str(result_correction) + ' m' ,fontcolor,font=font) # point label

        # # sanity check: plotting the model
        # point_list = []
        # chart_lower_value = 1053 # can be x- or y- values
        # chart_upper_value = 2499  # can be x- or y- values
        # for i in np.arange(chart_lower_value,chart_upper_value,10):
        #     output_pixel = round(model(i))
        #     point = (output_pixel,i)  # make sure x and y have correct position here!!
        #     point_list.append(point)
        # d.line(point_list, fill=line_color, width=10)

        # endresult
        result_rejected_takeoff_distance = round(result_distance + wind * result_correction)

    elif 6400 < gross_mass <= 6800:
        # # jupyter
        # font = ImageFont.truetype("SFNS.ttf", 60)
        # im = Image.open("charts/AW139/rejected_tod_clear_area/modified/AW139_rejected_tod_clear_area_6800.png")

        # flask
        font = ImageFont.truetype(path_pycharm + "/static/fonts/SFNS.ttf", 60)
        im = Image.open(path_pycharm + "/static/images/baseline_images/AW139_rejected_tod_clear_area_6800.png")

        d = ImageDraw.Draw(im) # generating the image

        '''Left chart area:'''
        # Calulating Pressure Altitude and pixel_PA:
        difference = (1013.2 - QNH) * 27 #  pressure difference between QNH and standard pressure
        result_PA = round(height + difference) # pressure altitude at hover height.
        lower_PA_pixel = 1960 # here: 0ft
        upper_PA_pixel = 562  # here: 14000ft
        diff_upper_lower_PA = 8000 # difference between upper and lower PA on chart
        pixel_per_ft = (upper_PA_pixel - lower_PA_pixel)/diff_upper_lower_PA # converting PA to pixel
        PA_pixel = lower_PA_pixel + (result_PA * pixel_per_ft) # converting PA to pixel

        input_output_row_pixel = 2800
        point_1 = (PA_pixel, input_output_row_pixel)              # defining starting point on chart
        d.text((PA_pixel+40, input_output_row_pixel-80),str(result_PA) + ' ft' , fontcolor,font=font) # labeling the point

        # pixel values on x- and y-axis
        # x_1=[ 562, 792,1028,1265] #-40
        # y_1=[1721,1929,2150,2387]
        x_2=[ 562, 737, 912,1087,1262,1436,1611,1776] #-30
        y_2=[1767,1874,1984,2098,2214,2334,2455,2573]
        x_3=[ 562, 737, 912,1087,1262,1436,1611,1785] #-20
        y_3=[1658,1763,1871,1981,2093,2210,2328,2449]
        x_4=[ 562, 737, 912,1087,1262,1436,1611,1785,1960] #-10
        y_4=[1562,1663,1767,1873,1983,2095,2210,2327,2446]
        x_5=[ 562, 737, 912,1087,1262,1436,1611,1785,1960,2135] # 0
        y_5=[1469,1565,1665,1768,1875,1984,2095,2209,2326,2441]
        x_6=[ 562, 737, 912,1087,1262,1436,1611,1785,1960,2135] # +10
        y_6=[1377,1470,1566,1665,1768,1872,1980,2091,2205,2317]
        x_7=[ 562, 602, 737, 912,1087,1262,1436,1611,1785,1960,2090,2135] # +20
        y_7=[1275,1296,1366,1457,1553,1653,1753,1859,1965,2074,2156,2184]
        x_8=[ 562, 737, 912,1087,1262,1436,1611,1785,1960,2135] # +30
        y_8=[1169,1254,1340,1431,1524,1621,1721,1824,1928,2034]
        x_9=[               912,1087,1262,1436,1611,1785,1960,2135] # +40
        y_9=[               1220,1316,1406,1497,1591,1688,1787,1887]
        x_10=[                                       1960,2135] # +50
        y_10=[                                       1615,1710]

        # dictionary for lines
        dictionary ={-30:[x_2,y_2],
                     -20:[x_3,y_3],
                     -10:[x_4,y_4],
                     0:[x_5,y_5],
                     10:[x_6,y_6],
                     20:[x_7,y_7],
                     30:[x_8,y_8],
                     40:[x_9,y_9],
                     50:[x_10,y_10]}

        # finding the output value
        input_real = temp
        input_pixel = PA_pixel
        if input_real in dictionary.keys():
            x_and_y = dictionary.get(input_real)
            model = np.poly1d(np.polyfit(x_and_y[0], x_and_y[1], len(x_and_y[0])-1)) # polynomial regression of degree (len(x_y[0])-1)
            # r2_score(x, model(y)) # r-score   # check the r2 score
            output_pixel = round(model(input_pixel))   #  prediction
        else:
            lower_key = max(k for k in dictionary if k <= input_real) # finding the adjacent lower value in the dictionary
            upper_key = min(k for k in dictionary if k >= input_real) # finding the adjacent higher value in the dictionary
            x_and_y_1 = dictionary.get(lower_key)  # getting the pixel table for the lower line
            x_and_y_2 = dictionary.get(upper_key)  # getting the pixel table for the upper line
            model_1 = np.poly1d(np.polyfit(x_and_y_1[0],x_and_y_1[1], len(x_and_y_1[0])-1)) # model the lower line
            model_2 = np.poly1d(np.polyfit(x_and_y_2[0],x_and_y_2[1], len(x_and_y_2[0])-1)) # model the upper line
            intersect1 = model_1(input_pixel)  # prediction upper line
            intersect2 = model_2(input_pixel)  # prediction lower line
            interpolated = intersect1 + ((input_real-lower_key)/(upper_key - lower_key)*(intersect2-intersect1)) # interpolate between lower and upper line
            output_pixel = round(interpolated)

        # restricting the chart output
        pixel_limit = 2461
        if output_pixel > pixel_limit:
            output_pixel = pixel_limit

        output_pixel_left = output_pixel

        point_2 = (PA_pixel, output_pixel_left) # defining second point on chart
        d.text((PA_pixel-150, output_pixel_left-80),str(temp) + ' C' ,(0,0,255),font=font) # point label

        # #  sanity check: plotting the model
        # # define plot range
        # input_is_x = 0 # set to 1 if input is x
        # output_is_y = 1 # set to 0 if output is y
        # chart_lower_value = 555 # choose x- or y- values
        # chart_upper_value = 2135  # choose x- or y- values
        # for key in dictionary.keys():
        #     x_and_y = dictionary.get(key)
        #     model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1))
        #     point_list = []
        #     for i in np.arange(chart_lower_value,chart_upper_value,10):
        #         output_pixel = round(model(i))
        #         point = (i, output_pixel)  # make sure x and y have correct position here!!
        #         point_list.append(point)
        #     d.line(point_list, fill=line_color, width=10)

        '''Middle chart area:'''
        # pixel values on x- and y-axis
        x_1=[2217,2238,2250,2260,2270,2282,  2347,2413,2479,2544,2610,2675,2741,2806,2872,2938,3003,3068,3134,3200,3265,3315,3331] # 6800
        y_1=[2432,2385,2357,2334,2322,2308,  2232,2156,2080,2003,1927,1851,1774,1698,1621,1545,1469,1393,1316,1240,1163,1106,1087]
        x_2=[2217,3148] # 6600kg
        y_2=[2140,1088]
        x_3=[2217,2232,2242,2265,2292,2309,2342,2380,2397,2473,2541,2609,2675,2740,2807,2871,2938,2962] #6400kg
        y_3=[1930,1889,1874,1850,1821,1806,1764,1724,1709,1621,1545,1469,1400,1329,1256,1183,1112,1087]

        # dictionary for lines
        dictionary ={6800:[x_1,y_1],
                     6600:[x_2,y_2],
                     6400:[x_3,y_3]}


        # finding the output value
        input_real = gross_mass
        input_pixel = output_pixel_left

        # defining input and output variable
        input_is_x = 1 # set to 1 if input is x, set to 0 if input is y
        output_is_y = 0 # set to 0 if output is y, set to 1 if output is x

        if input_real in dictionary.keys():
            x_and_y = dictionary.get(input_real)
            model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1)) # polynomial regression of degree (len(x_y[0])-1)
            # r2_score(x, model(y)) # r-score   # check the r2 score
            output_pixel = round(model(input_pixel))   #  prediction
        else:
            lower_key = max(k for k in dictionary if k <= input_real) # finding the adjacent lower value in the dictionary
            upper_key = min(k for k in dictionary if k >= input_real) # finding the adjacent higher value in the dictionary
            x_and_y_1 = dictionary.get(lower_key)  # getting the pixel table for the lower line
            x_and_y_2 = dictionary.get(upper_key)  # getting the pixel table for the upper line
            model_1 = np.poly1d(np.polyfit(x_and_y_1[input_is_x],x_and_y_1[output_is_y], len(x_and_y_1[0])-1)) # model the lower line
            model_2 = np.poly1d(np.polyfit(x_and_y_2[input_is_x],x_and_y_2[output_is_y], len(x_and_y_2[0])-1)) # model the upper line
            intersect1 = model_1(input_pixel)  # prediction upper line
            intersect2 = model_2(input_pixel)  # prediction lower line
            interpolated = intersect1 + ((input_real-lower_key)/(upper_key - lower_key)*(intersect2-intersect1)) # interpolate between lower and upper line
            output_pixel = round(interpolated)
        pixel_limit = 2409
        if output_pixel < pixel_limit:
            output_pixel = pixel_limit


        output_pixel_middle = output_pixel
        point_3 = (output_pixel_middle, output_pixel_left)     # entry point in middle chart
        d.text((output_pixel_middle+40, output_pixel_left-80),str(gross_mass) + ' kg' ,(0,0,255),font=font) # point label

        # # sanity check: plotting the model
        # # define plot range
        # input_is_x = 0 # set to 1 if input is x
        # output_is_y = 1 # set to 0 if output is y
        # chart_lower_value = 2210 # choose x- or y- values
        # chart_upper_value = 3331  # choose x- or y- values
        # for key in dictionary.keys():
        #     x_and_y = dictionary.get(key)
        #     model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1))
        #     point_list = []
        #     for i in np.arange(chart_lower_value,chart_upper_value,10):
        #         output_pixel = round(model(i))
        #         point = (i, output_pixel)  # make sure x and y have correct position here!!
        #         point_list.append(point)
        #     d.line(point_list, fill=line_color, width=10)

        point_4 = (output_pixel_middle, input_output_row_pixel)      # bottom exit point middle chart

        # convert pixel output to chart value
        lower_pixel = 2151  # here: 0   m
        upper_pixel = 3331  # here: 1800 m
        diff_value_pixel = upper_pixel  - lower_pixel # number of pixel in whole range
        diff_value_unit =  1800 - 0   # number of units in whole range
        pixel_per_unit = diff_value_pixel / diff_value_unit

        result_distance = round(0 + ( output_pixel_middle - lower_pixel )/pixel_per_unit)
        print('Meter: '+ str(result_distance))

        d.text((output_pixel_middle+40, input_output_row_pixel-80),str(int(result_distance)) + ' m' , fontcolor,font=font) # point label

        '''Right chart area:'''
        input_pixel_right = output_pixel_left  #beware
        input_pixel = output_pixel_left

        # defining the curve by points
        x_1=[3346,3519,3693,3866,4039,4212]
        y_1=[2462,2258,2039,1798,1524,1185]
        x_and_y = [x_1,y_1]

        # defining input and output variable
        input_is_x = 1 # set to 1 if input is x, set to 0 if input is y
        output_is_y = 0 # set to 0 if output is y, set to 1 if output is x

        # fitting the model to the data
        model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1))
        output_pixel = round(model(input_pixel))   #  prediction
        output_pixel_right = output_pixel

        point_5 = (output_pixel_right, input_pixel_right)  # intersection point right chart
        point_6 = (output_pixel_right, input_output_row_pixel)  # bottom exit point right chart

        # convert pixel output to chart value
        lower_pixel = 3346   # here: 0 m
        upper_pixel = 4212  # here: -25 m
        diff_value_pixel = upper_pixel  - lower_pixel # number of pixel in whole range
        diff_value_unit =  -25 - 0   # number of units in whole range
        pixel_per_unit = diff_value_pixel / diff_value_unit

        result_correction = round(0 + ( output_pixel_right - lower_pixel )/pixel_per_unit,2)
        print('Correction factor: '+ str(result_correction))

        d.text((output_pixel_right+40, input_output_row_pixel-80),str(result_correction) + ' m' ,fontcolor,font=font) # point label

        # # sanity check: plotting the model
        # point_list = []
        # chart_lower_value = 1087 # can be x- or y- values
        # chart_upper_value = 2461  # can be x- or y- values
        # for i in np.arange(chart_lower_value,chart_upper_value,10):
        #     output_pixel = round(model(i))
        #     point = (output_pixel,i)  # make sure x and y have correct position here!!
        #     point_list.append(point)
        # d.line(point_list, fill=line_color, width=10)

        # endresult
        result_rejected_takeoff_distance = round(result_distance + wind * result_correction)


    elif 6800 < gross_mass <= 7000:
        # # jupyter
        # font = ImageFont.truetype("SFNS.ttf", 60)
        # im = Image.open("charts/AW139/rejected_tod_clear_area/modified/AW139_rejected_tod_clear_area_7000.png")

        # flask
        font = ImageFont.truetype(path_pycharm + "/static/fonts/SFNS.ttf", 60)
        im = Image.open(path_pycharm + "/static/images/baseline_images/AW139_rejected_tod_clear_area_7000.png")

        d = ImageDraw.Draw(im) # generating the image

        '''Left chart area:'''
        # Calulating Pressure Altitude and pixel_PA:
        difference = (1013.2 - QNH) * 27 #  pressure difference between QNH and standard pressure
        result_PA = round(height + difference) # pressure altitude at hover height.
        lower_PA_pixel = 1957 # here: 0ft
        upper_PA_pixel = 559  # here: 8000ft
        diff_upper_lower_PA = 8000 # difference between upper and lower PA on chart
        pixel_per_ft = (upper_PA_pixel - lower_PA_pixel)/diff_upper_lower_PA # converting PA to pixel
        PA_pixel = lower_PA_pixel + (result_PA * pixel_per_ft) # converting PA to pixel

        input_output_row_pixel = 2800
        point_1 = (PA_pixel, input_output_row_pixel)              # defining starting point on chart
        d.text((PA_pixel+40, input_output_row_pixel-80),str(result_PA) + ' ft' , fontcolor,font=font) # labeling the point

        # pixel values on x- and y-axis
        x_1=[ 559, 908,1258,1607,1791] #-40
        y_1=[1459,1723,2001,2290,2446]
        x_2=[ 559, 908,1258,1607,1957] #-30
        y_2=[1335,1590,1860,2142,2436]
        x_3=[ 559, 908,1258,1607,1957,2132] #-20
        y_3=[1210,1456,1718,1992,2279,2422]
        x_4=[ 559, 908,1258,1607,1957,2132] #-10
        y_4=[1098,1334,1587,1853,2133,2273]
        x_5=[ 690, 908,1258,1607,1957,2132] # 0
        y_5=[1071,1217,1461,1719,1990,2127]
        x_6=[ 863, 908,1258,1607,1957,2132] # +10
        y_6=[1071,1101,1335,1585,1848,1981]
        x_7=[1057,1258,1607,1957,2132] # +20
        y_7=[1071,1203,1442,1696,1824]
        x_8=[1286,1433,1607,1957,2132] # +30
        y_8=[1071,1167,1284,1525,1649]
        x_9=[1510,1782,2131] # +40
        y_9=[1071,1245,1478]
        x_10=[564,3938] # +50
        y_10=[282,2414]

        # dictionary for lines
        dictionary ={-40:[x_1,y_1],
                     -30:[x_2,y_2],
                     -20:[x_3,y_3],
                     -10:[x_4,y_4],
                     0:[x_5,y_5],
                     10:[x_6,y_6],
                     20:[x_7,y_7],
                     30:[x_8,y_8],
                     40:[x_9,y_9],
                     50:[x_10,y_10]}

        # finding the output value
        input_real = temp
        input_pixel = PA_pixel
        if input_real in dictionary.keys():
            x_and_y = dictionary.get(input_real)
            model = np.poly1d(np.polyfit(x_and_y[0], x_and_y[1], len(x_and_y[0])-1)) # polynomial regression of degree (len(x_y[0])-1)
            # r2_score(x, model(y)) # r-score   # check the r2 score
            output_pixel = round(model(input_pixel))   #  prediction
        else:
            lower_key = max(k for k in dictionary if k <= input_real) # finding the adjacent lower value in the dictionary
            upper_key = min(k for k in dictionary if k >= input_real) # finding the adjacent higher value in the dictionary
            x_and_y_1 = dictionary.get(lower_key)  # getting the pixel table for the lower line
            x_and_y_2 = dictionary.get(upper_key)  # getting the pixel table for the upper line
            model_1 = np.poly1d(np.polyfit(x_and_y_1[0],x_and_y_1[1], len(x_and_y_1[0])-1)) # model the lower line
            model_2 = np.poly1d(np.polyfit(x_and_y_2[0],x_and_y_2[1], len(x_and_y_2[0])-1)) # model the upper line
            intersect1 = model_1(input_pixel)  # prediction upper line
            intersect2 = model_2(input_pixel)  # prediction lower line
            interpolated = intersect1 + ((input_real-lower_key)/(upper_key - lower_key)*(intersect2-intersect1)) # interpolate between lower and upper line
            output_pixel = round(interpolated)

        pixel_limit = 2446     # restricting the chart output
        if output_pixel > pixel_limit:
            output_pixel = pixel_limit

        output_pixel_left = output_pixel

        point_2 = (PA_pixel, output_pixel_left) # defining second point on chart
        d.text((PA_pixel-150, output_pixel_left-80),str(temp) + ' C' ,(0,0,255),font=font) # point label

        # #  sanity check: plotting the model
        # # define plot range
        # input_is_x = 0 # set to 1 if input is x
        # output_is_y = 1 # set to 0 if output is y
        # chart_lower_value = 555 # choose x- or y- values
        # chart_upper_value = 2135  # choose x- or y- values
        # for key in dictionary.keys():
        #     x_and_y = dictionary.get(key)
        #     model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1))
        #     point_list = []
        #     for i in np.arange(chart_lower_value,chart_upper_value,10):
        #         output_pixel = round(model(i))
        #         point = (i, output_pixel)  # make sure x and y have correct position here!!
        #         point_list.append(point)
        #     d.line(point_list, fill=line_color, width=10)

        '''Middle chart area:'''
        # pixel values on x- and y-axis
        x_1=[2226,2243,2253,2262,2270,2279,2292,2305,2339,2384,2463,2541,2619,2698,2776,2855,2934,3012,3054,3081,3099] # 6800
        y_1=[2116,2080,2057,2036,2019,2000,1984,1970,1932,1881,1792,1701,1614,1524,1434,1344,1256,1168,1120,1089,1071]
        x_2=[2226,2240,2252,2263,2273,2282,2295,2309,2322,2345,2364,2383,2462,2541,2619,2698,2777,2856,2934,3013,3091,3170,3249,3289,3327] # 7000kg
        y_2=[2413,2383,2357,2331,2309,2289,2274,2257,2243,2215,2194,2172,2079,1987,1897,1804,1712,1621,1530,1438,1347,1255,1163,1116,1071]


        # dictionary for lines
        dictionary ={6800:[x_1,y_1],
                     7000:[x_2,y_2]}


        # finding the output value
        input_real = gross_mass
        input_pixel = output_pixel_left

        # defining input and output variable
        input_is_x = 1 # set to 1 if input is x, set to 0 if input is y
        output_is_y = 0 # set to 0 if output is y, set to 1 if output is x

        if input_real in dictionary.keys():
            x_and_y = dictionary.get(input_real)
            model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1)) # polynomial regression of degree (len(x_y[0])-1)
            # r2_score(x, model(y)) # r-score   # check the r2 score
            output_pixel = round(model(input_pixel))   #  prediction
        else:
            lower_key = max(k for k in dictionary if k <= input_real) # finding the adjacent lower value in the dictionary
            upper_key = min(k for k in dictionary if k >= input_real) # finding the adjacent higher value in the dictionary
            x_and_y_1 = dictionary.get(lower_key)  # getting the pixel table for the lower line
            x_and_y_2 = dictionary.get(upper_key)  # getting the pixel table for the upper line
            model_1 = np.poly1d(np.polyfit(x_and_y_1[input_is_x],x_and_y_1[output_is_y], len(x_and_y_1[0])-1)) # model the lower line
            model_2 = np.poly1d(np.polyfit(x_and_y_2[input_is_x],x_and_y_2[output_is_y], len(x_and_y_2[0])-1)) # model the upper line
            intersect1 = model_1(input_pixel)  # prediction upper line
            intersect2 = model_2(input_pixel)  # prediction lower line
            interpolated = intersect1 + ((input_real-lower_key)/(upper_key - lower_key)*(intersect2-intersect1)) # interpolate between lower and upper line
            output_pixel = round(interpolated)
        pixel_limit = 2226
        if output_pixel < pixel_limit:
            output_pixel = pixel_limit


        output_pixel_middle = output_pixel
        point_3 = (output_pixel_middle, output_pixel_left)     # entry point in middle chart
        d.text((output_pixel_middle+40, output_pixel_left-80),str(gross_mass) + ' kg' ,(0,0,255),font=font) # point label

        # # sanity check: plotting the model
        # # define plot range
        # input_is_x = 0 # set to 1 if input is x
        # output_is_y = 1 # set to 0 if output is y
        # chart_lower_value = 2226 # choose x- or y- values
        # chart_upper_value = 3327  # choose x- or y- values
        # for key in dictionary.keys():
        #     x_and_y = dictionary.get(key)
        #     model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1))
        #     point_list = []
        #     for i in np.arange(chart_lower_value,chart_upper_value,10):
        #         output_pixel = round(model(i))
        #         point = (i, output_pixel)  # make sure x and y have correct position here!!
        #         point_list.append(point)
        #     d.line(point_list, fill=line_color, width=10)

        point_4 = (output_pixel_middle, input_output_row_pixel)      # bottom exit point middle chart

        # convert pixel output to chart value
        lower_pixel = 2147  # here: 0   m
        upper_pixel = 3328  # here: 1800 m
        diff_value_pixel = upper_pixel  - lower_pixel # number of pixel in whole range
        diff_value_unit =  1500 - 0   # number of units in whole range
        pixel_per_unit = diff_value_pixel / diff_value_unit

        result_distance = round(0 + ( output_pixel_middle - lower_pixel )/pixel_per_unit)
        print('Meter: '+ str(result_distance))

        d.text((output_pixel_middle+40, input_output_row_pixel-80),str(int(result_distance)) + ' m' , fontcolor,font=font) # point label

        '''Right chart area:'''
        input_pixel_right = output_pixel_left  #beware
        input_pixel = output_pixel_left

        # defining the curve by points
        x_1=[3343,3516,3689,3862,4035,4147]
        y_1=[2446,2201,1938,1650,1321,1070]
        x_and_y = [x_1,y_1]

        # defining input and output variable
        input_is_x = 1 # set to 1 if input is x, set to 0 if input is y
        output_is_y = 0 # set to 0 if output is y, set to 1 if output is x

        # fitting the model to the data
        model = np.poly1d(np.polyfit(x_and_y[input_is_x], x_and_y[output_is_y], len(x_and_y[0])-1))
        output_pixel = round(model(input_pixel))   #  prediction
        output_pixel_right = output_pixel

        point_5 = (output_pixel_right, input_pixel_right)  # intersection point right chart
        point_6 = (output_pixel_right, input_output_row_pixel)  # bottom exit point right chart

        # convert pixel output to chart value
        lower_pixel = 3346   # here: 0 m
        upper_pixel = 4212  # here: -25 m
        diff_value_pixel = upper_pixel  - lower_pixel # number of pixel in whole range
        diff_value_unit =  -25 - 0   # number of units in whole range
        pixel_per_unit = diff_value_pixel / diff_value_unit

        result_correction = round(0 + ( output_pixel_right - lower_pixel )/pixel_per_unit,2)
        print('Correction factor: '+ str(result_correction))

        d.text((output_pixel_right+40, input_output_row_pixel-80),str(result_correction) + ' m' ,fontcolor,font=font) # point label

        # # sanity check: plotting the model
        # point_list = []
        # chart_lower_value = 1087 # can be x- or y- values
        # chart_upper_value = 2461  # can be x- or y- values
        # for i in np.arange(chart_lower_value,chart_upper_value,10):
        #     output_pixel = round(model(i))
        #     point = (output_pixel,i)  # make sure x and y have correct position here!!
        #     point_list.append(point)
        # d.line(point_list, fill=line_color, width=10)

        # endresult
        result_rejected_takeoff_distance = round(result_distance + wind * result_correction)


        # # Sanity check: printing calculated values
        # print('Height: ' + str(height))
        # print('QNH: ' + str(QNH))
        # print('Temperature: '+ str(temp))
        # print('PA: ' + str(result_PA))
        # print('Gross mass: ' + str(gross_mass))
        # print('Wind: ' + str(wind))
        # print("Pixel output left: "+ str(output_pixel_left))
        # print("Pixel output middle: "+ str(output_pixel_middle))
        # print("Pixel input right: "+ str(input_pixel_right))
        # print("Pixel output right: "+ str(output_pixel_right))
        # print("Rejected takeoff distance:" + str(result_rejected_takeoff_distance))


    '''Preparing for print '''
    QNH = int(QNH)
    gross_mass = int(gross_mass)
    height = int(height)
    temp = int(temp)
    wind = int(wind)
    result_distance = int(result_distance)
    result_rejected_takeoff_distance = int(result_rejected_takeoff_distance)

    # drawing the lines between points:
    d.line([point_1,point_2,point_3,point_4], fill=line_color, width=10)
    d.line([point_3,point_5,point_6], fill=line_color, width=10)

    # adding text to chart:
    vertical_align = 100
    horizontal_align = -730
    d.text((vertical_align,400),"Date, Time (UTC)",(0,0,0),font=font)
    time = datetime.utcnow().strftime("%Y-%m-%d, %H:%M")
    d.text((vertical_align,500),str(time),(0,0,255),font=font)

    d.text((vertical_align,750),"Flight ID:" ,(0,0,0),font=font)
    d.text((vertical_align,850),str(flight_ID),(0,0,255),font=font)

    d.text((vertical_align,950),"PIC/SIC:" ,(0,0,0),font=font)
    d.text((vertical_align,1050),str(PIC),(0,0,255),font=font)

    #d.text((vertical_align,2050+horizontal_align),'USER INPUT: ',(0,0,0),font=font)
    d.text((vertical_align,2000+horizontal_align),'Gross Mass: ',(0,0,0),font=font)
    d.text((vertical_align,2100+horizontal_align),str(gross_mass) + ' kg' ,(0,0,255),font=font)
    d.text((vertical_align,2200+horizontal_align),"QNH:" ,(0,0,0),font=font)
    d.text((vertical_align,2300+horizontal_align),str(QNH) + ' mb' ,(0,0,255),font=font)
    d.text((vertical_align,2400+horizontal_align),"Height above MSL:" ,(0,0,0),font=font)
    d.text((vertical_align,2500+horizontal_align),str(height)+ ' ft' ,(0,0,255),font=font)
    d.text((vertical_align,2600+horizontal_align),"Temperature:" ,(0,0,0),font=font)
    d.text((vertical_align,2700+horizontal_align),str(temp) + ' C' ,(0,0,255),font=font)
    d.text((vertical_align,2800+horizontal_align),"Headwind component:" ,(0,0,0),font=font)
    d.text((vertical_align,2900+horizontal_align),str(wind) + ' kt' ,(0,0,255),font=font)


    d.text((vertical_align,3050+horizontal_align),"RESULT:" ,(0,0,0),font=font)
    d.text((vertical_align,3150+horizontal_align),"Pressure Altitude:" ,(0,0,0),font=font)
    d.text((vertical_align,3250+horizontal_align),str(result_PA) + ' ft' , fontcolor,font=font)
    d.text((vertical_align,3350+horizontal_align),"Rejected Takeoff Distance:" ,(0,0,0),font=font)
    d.text((vertical_align,3450+horizontal_align),str(result_distance) + ' m - (' + str(-1*result_correction) + ' m * '+ str(wind) +' kt)', fontcolor,font=font)
    d.text((vertical_align-45,3550+horizontal_align),'≈ '+ str(result_distance) + ' m - ' + str(int(-1*result_correction*wind)) + ' m', fontcolor,font=font)
    d.text((vertical_align-45,3650+horizontal_align),'= '+ str(result_rejected_takeoff_distance) + ' m', fontcolor,font=font)
    # # jupyter
    # plt.figure(figsize=(160,80))
    # imgplot = plt.imshow(im)
    # plt.show()

    # flask
    # removing previously generated images
    for filename in os.listdir(path_pycharm + '/static/images/'):
        if filename.startswith('AW139_rejected_tod_clear_area_rendered'):  # not to remove other images
            os.remove(path_pycharm + '/static/images/' + filename)

    # create png
    graph_png = "AW139_rejected_tod_clear_area_rendered " + str(time) + " UTC.png"
    im.save(path_pycharm + '/static/images/' + graph_png)

    # create pdf
    graph_pdf = "AW139_rejected_tod_clear_area_rendered " + str(time) + " UTC.pdf"
    rgb = Image.new('RGB', im.size, (255, 255, 255))  # white background
    rgb.paste(im, mask=im.split()[3])                 # paste using alpha channel as mask
    rgb.save(path_pycharm + '/static/images/' + graph_pdf)


    # returning the html template with filled values(Flask-part)
    return render_template(
        'AW139_rejected_tod_clear_area.html',
        gross_mass = gross_mass,
        gross_mass_SV = session['gross_mass_SV'],
        QNH = QNH,
        QNH_SV = session['QNH_SV'],
        height = height,
        height_SV = session['height_SV'],
        temp = temp,
        temp_SV = session['temp_SV'],
        wind = wind,
        wind_SV = session['wind_SV'],
        PIC = PIC,
        PIC_SV = session['PIC_SV'],
        flight_ID = flight_ID,
        flight_ID_SV = session['flight_ID_SV'],
        result_png = graph_png,
        result_pdf = graph_pdf,
        result_PA = result_PA,
        result_distance = result_distance,
        result_correction = result_correction,
        result_rejected_takeoff_distance = result_rejected_takeoff_distance,
        # result_height_loss_feet = result_height_loss_feet,
        # result_height_loss_perf_benefit = result_height_loss_perf_benefit,
        # result_feet = result_feet,
        # result_wind_correction = result_wind_correction,
        # result_total_dropdown = result_total_dropdown,
        #perf_benefit = perf_benefit,
        #perf_benefit_SV = session['perf_benefit_SV'],

        calculation_success = True,
    )



if __name__ == '__main__':
    app.debug = True
    app.run()