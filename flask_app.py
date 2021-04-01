from flask import Flask, render_template, request, session
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os



app = Flask(__name__) # Creating our Flask Instance
app.secret_key = "randomly543tert443434"


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



@app.route('/operation_result/', methods=['POST', 'GET'])
def operation_result():
    """Route where we send calculator form input"""

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

        for filename in os.listdir('/home/gaviation/mysite/static/images/'):
            if filename.startswith('Payload'):  # not to remove other images
                os.remove('/home/gaviation/mysite/static/images/' + filename)

        im.save("/home/gaviation/mysite/static/images/" + new_graph_name)

        plt.figure(figsize=(20,40))



        # returning the template (Flask-part)
        return render_template(
            'index.html',
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

if __name__ == '__main__':
    app.debug = True
    app.run()