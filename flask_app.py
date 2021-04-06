from flask import Flask, render_template, request, session
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os



app = Flask(__name__) # Creating our Flask Instance
app.secret_key = "randomly543tert443434"

path_pycharm = ""
path_pythonanywhere = "/home/gaviation/mysite/"



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

@app.route('/instructions', methods=['GET', 'POST'])
def instructions():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))

    # show the form, it wasn't submitted
    return render_template('instructions.html')


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

    try:
        QNH = float(QNH_input)
        DOM = float(DOM_input)
        hover_height = float(hover_height_input)
        temp = float(temp_input)
        wind = float(wind_input)
        perf_benefit = float(perf_benefit_input)
        fuel_at_hho = float(fuel_at_hho_input)


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
        im = Image.open("/home/gaviation/mysite/static/images/Hover_ceiling_OGE_orig.png")
        d = ImageDraw.Draw(im)
        line_color = (255,0,0)

        #shift_on_x = 0  # strangely enough, all lines need to be shifted 28 pixel to the right to fit on the new image

        # 1- pressure altitude / y-axis intercept
        one = (1287, PA_pixel)

        # 2- pressure altitude / temperature intercept
        two = (zero_wind_mass_pixel, PA_pixel)

        # 3- 40knots at zero wind mass point
        three = (zero_wind_mass_pixel, 8270)

        # 4- acutal wind at 4400kg point
        four = (1287, wind_ref)

        # 5 - wind/mass intercept
        five = (max_mass_pixel, wind_ref)

        # 6 - full wind benefit mass
        six = (max_mass_pixel, 8270)

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

        # generate the image
        # printing the text on the image:
        font = ImageFont.truetype("/home/gaviation/mysite/static/fonts/SFNS.ttf", 130)

        #d.text((2860,3050),"Calculations provided by Stephan Goldberg",(255,0,0),font=font)

        d.text((5840,1500),"Date, Time (UTC)",(0,0,0),font=font)
        from datetime import datetime
        time = datetime.utcnow().strftime("%Y-%m-%d, %H%M")
        d.text((5840,1650),str(time),(0,0,255),font=font)

        d.text((5840,2050),'USER INPUT: ',(0,0,0),font=font)

        d.text((5840,2250),'DOM: ',(0,0,0),font=font)
        d.text((5840,2400),str(DOM) + ' kg' ,(0,0,255),font=font)

        d.text((5840,2600),"QNH:" ,(0,0,0),font=font)
        d.text((5840,2750),str(QNH) + ' mb' ,(0,0,255),font=font)

        d.text((5840,2950),"Hover Height above MSL:" ,(0,0,0),font=font)
        d.text((5840,3100),str(hover_height)+ ' ft' ,(0,0,255),font=font)

        d.text((5840,3300),"Temperature:" ,(0,0,0),font=font)
        d.text((5840,3450),str(temp) + ' C' ,(0,0,255),font=font)

        d.text((5840,3650),"Headwind:" ,(0,0,0),font=font)
        d.text((5840,3800),str(wind) + ' kt' ,(0,0,255),font=font)

        d.text((5840,4000),"Wind Benefit:" ,(0,0,0),font=font)
        d.text((5840,4150),str(perf_benefit) + ' %' ,(0,0,255),font=font)

        d.text((5840,4350),"Fuel at site:" ,(0,0,0),font=font)
        d.text((5840,4500),str(fuel_at_hho) + ' kg',(0,0,255),font=font)

        fontcolor = (255,0,0)
        d.text((5800,6150),"RESULT:" ,(0,0,0),font=font)

        d.text((5800,6350),"Pressure Altitude:" ,(0,0,0),font=font)
        d.text((5800,6500),str(result_PA) + ' ft' ,fontcolor,font=font)

        d.text((5800,6700),"Zero Wind Mass:" ,(0,0,0),font=font)
        d.text((5800,6850),str(result_no_wind) + ' kg' ,fontcolor,font=font)

        d.text((5800,7050),"Full Wind Mass:" ,(0,0,0),font=font)
        d.text((5800,7200),str(result_wind) + ' kg' ,fontcolor,font=font)

        d.text((5800,7400),"max ltd. Wind-benefit Mass:" ,(0,0,0),font=font)
        d.text((5800,7550),str(result_performance_limited) + ' kg' ,fontcolor,font=font)

        d.text((5800,7750),"max Useful Load:" ,(0,0,0),font=font)
        d.text((5800,7900),str(result_useful_load) + ' kg' ,fontcolor,font=font)

        d.text((5800,8150),"max Payload:" ,(0,0,0),font=font)
        d.text((5800,8300),str(result_payload) + ' kg' ,fontcolor,font=font)

        # # to create an output image
        new_graph_name = "Payload " + str(time) + " UTC.png"

        # removing previously generated images
        for filename in os.listdir('/home/gaviation/mysite/static/images/'):
            if filename.startswith('Payload'):  # not to remove other images
                os.remove('/home/gaviation/mysite/static/images/' + filename)

        im.save("/home/gaviation/mysite/static/images/" + new_graph_name)

        plt.figure(figsize=(20,40))



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

            result_PA = result_PA,
            result_no_wind = result_no_wind,
            result_wind = result_wind,
            result_performance_limited = result_performance_limited,
            result_useful_load = result_useful_load,
            result_payload = result_payload,
            result_png = new_graph_name,  # before: result_png = result_png,
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
    font = ImageFont.truetype("/home/gaviation/mysite/static/fonts/SFNS.ttf", 80)
    im = Image.open("/home/gaviation/mysite/static/images/baseline_images/AW139_dropdown_6800.png")


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

    try:
        QNH = float(QNH_input)
        gross_mass = float(gross_mass_input)
        hover_height = float(hover_height_input)
        temp = float(temp_input)
        wind = float(wind_input)

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


        # generating the image
        #im = Image.open("/home/gaviation/mysite/static/images/baseline_images/AW139_dropdown_6800.png")
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
        #font = ImageFont.truetype("/home/gaviation/mysite/static/fonts/SFNS.ttf", 80)
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
        d.text((vertical_align,650),str(time),(0,0,255),font=font)
        d.text((vertical_align,2050+horizontal_align),'USER INPUT: ',(0,0,0),font=font)
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


        # create an output image
        graph_name = "AW139_dropdown_6800_rendered " + str(time) + " UTC.png"

        for filename in os.listdir('/home/gaviation/mysite/static/images/'):
            if filename.startswith('AW139_dropdown_6800_rendered'):  # not to remove other images
                os.remove('/home/gaviation/mysite/static/images/' + filename)

        im.save("/home/gaviation/mysite/static/images/" + graph_name)

        plt.figure(figsize=(20,40))


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

            result_PA = result_PA,
            result_height_loss_feet = result_height_loss_feet,
            result_AW139_dropdown_6800 = graph_name,  # before: result_png = result_png,
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

if __name__ == '__main__':
    app.debug = True
    app.run()