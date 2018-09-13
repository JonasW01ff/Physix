import math
import sympy
import itertools

class Speed:

    def calSpeed(self, arg1, arg2, arg1_unit, arg2_unit):
        if arg1_unit == "m/s":
            if arg2_unit == "m":
                return str(float(arg2)/float(arg1)) + " seconds long"
            elif arg2_unit == "s":
                return str(float(arg1)*float(arg2)) + " meters far"
        elif arg2_unit == "m/s":
            if arg1_unit == "m":
                return str(float(arg1)/float(arg2)) + " seconds long"
            elif arg1_unit == "s":
                return str(float(arg2)*float(arg1)) + " meters far"
        elif arg1_unit == "m" or arg2_unit == "m" and arg1_unit == "s" or arg2_unit == "s":
            if arg1_unit == "m":
                return str(float(arg1)/float(arg2)) + " m/s fast"
            elif arg1_unit == "s":
                return str(float(arg2)/float(arg1)) + " m/s fast"
        if (arg1_unit == "J" or "Kg") or (arg2_unit == "J" or "Kg"):
            if arg1_unit == "Kg":
                if arg2_unit == "m/s":
                    return str(0.5*float(arg1)*float(arg2)**2) + " J strong"
                elif arg2_unit == "J":
                    return str(math.sqrt(float(arg2)/0.5/float(arg1))) + " m/s fast"
            elif arg1_unit == "m/s":
                if arg2_unit == "Kg":
                    return str(0.5 * float(arg2)*float(arg1)**2) + " J strong"
                elif arg2_unit == "J":
                    return str(float(arg2)/0.5/float(arg1)**2) + " Kg heavy"
            elif arg1_unit == "J":
                if arg2_unit == "Kg":
                    return str(math.sqrt(float(arg1)/0.5/float(arg2))) + " m/s fast"
                elif arg2_unit == "m/s":
                    return str(float(arg1)/0.5/float(arg2)**2) + " Kg heavy"

    def calAccel(self, arg1, arg2, arg3, arg1_unit, arg2_unit, arg3_unit):
        if arg1_unit == "Kg" or arg2_unit == "Kg" or arg3_unit == "Kg":
            m = None
            a = None
            if arg1_unit == "Kg":
                m = arg1
            elif arg2_unit == "Kg":
                m = arg2
            elif arg3_unit == "Kg":
                m = arg3
            if arg1_unit == u"m/s\N{SUPERSCRIPT TWO}":
                a = arg1
            elif arg2_unit == u"m/s\N{SUPERSCRIPT TWO}":
                a = arg2
            elif arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                a = arg3
            try:
                return str(float(m)*float(a)) + " N Strong"
            except:
                pass
        if arg1_unit == "N" or arg2_unit == "N" or arg3_unit == "N":
            m = None
            a = None
            F = None
            if arg1_unit == u"m/s\N{SUPERSCRIPT TWO}" or arg2_unit == u"m/s\N{SUPERSCRIPT TWO}" or arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                if arg1_unit == "N":
                    F = arg1
                elif arg2_unit == "N":
                    F = arg2
                elif arg3_unit == "N":
                    F = arg3
                if arg1_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    a = arg1
                elif arg2_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    a = arg2
                elif arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    a = arg3
                try:
                    return str(float(F)/float(a)) + " Kg heavy"
                except:
                    pass
            elif arg1_unit == "Kg" or arg2_unit == "Kg" or arg3_unit == "Kg":
                if arg1_unit == "Kg":
                    m = arg1
                elif arg2_unit == "Kg":
                    m = arg2
                elif arg3_unit == "Kg":
                    m = arg3
                if arg1_unit == "N":
                    F = arg1
                elif arg2_unit == "N":
                    F = arg2
                elif arg3_unit == "N":
                    F = arg3
                try:
                    return str(float(F)/float(m)) + u" m/s\N{SUPERSCRIPT TWO} in acceleration"
                except:
                    pass
        elif arg1_unit == u"m/s\N{SUPERSCRIPT TWO}":
            if arg2_unit == "s":
                if arg3_unit == "START- m/s":
                    return str(float(arg1)*float(arg2)+float(arg3)) + " m/s fast"
                elif arg3_unit == "END- m/s":
                    return str(float(arg3)-float(arg1)*float(arg2)) + " m/s fast to start with"
            elif arg2_unit == "START- m/s":
                if arg3_unit == "s":
                    return str(float(arg3)+float(arg2)*float(arg1)) + " m/s fast"
                elif arg3_unit == "END- m/s":
                    return str((float(arg3)-float(arg2))/float(arg1)) + " s to get that speed"
            elif arg2_unit == "END- m/s":
                if arg3_unit == "s":
                    return str(float(arg3)-float(arg2)*float(arg1)) + " m/s fast at the start"
                if arg3_unit == "START- m/s":
                    return str((float(arg2)-float(arg3))/float(arg1)) + " s to get that speed"
            elif arg2_unit == "m":
                if arg3_unit == "START- m/s":
                    d = float(arg3) ** 2 - 4 * (0.5 * float(arg1)) * (float(arg2) * -1)
                    if d == 0:
                        return str((float(arg3) * -1) / (2 * float(arg1))) + " s to get there"
                    elif d > 0:
                        return str(((float(arg3) * -1) + math.sqrt(d)) / (2 * (float(arg1) / 2))) + " s to get there or " + str(((float(arg3) * -1) - math.sqrt(d)) / (2 * (float(arg1) / 2))) + " s"
                    elif d < 0:
                        return "unsolvable"
        elif arg1_unit == "START- m/s":
            if arg2_unit == "END- m/s":
                if arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    return str((float(arg2)-float(arg1))/float(arg3)) + " s to get that speed"
                elif arg3_unit == "m":
                    return str((float(arg2)**2-float(arg1)**2)/float(arg3)*2) + u" m/s\N{SUPERSCRIPT TWO} in acceleration" # [Originates from "a = ( Vf - Vi ) / t" and "d = 0.5 (Vf + Vi ) * t" combined a.k.a. Uniform Acceleration]
                elif arg3_unit == "s":
                    return str((float(arg2)-float(arg1))/float(arg3)) + u" m/s\N{SUPERSCRIPT TWO} in acceleration over " + str((float(arg2)+float(arg1))/2*float(arg3)) + " m"
            elif arg2_unit == u"m/s\N{SUPERSCRIPT TWO}":
                if arg3_unit == "END- m/s":
                    return str((float(arg3) - float(arg1)) / float(arg2)) + " s to get that speed"
                elif arg3_unit == "m":
                    d = float(arg1)**2-4*(0.5*float(arg2))*(float(arg3)*-1)
                    if d == 0:
                        return str((float(arg1)*-1)/(2*float(arg2))) + " s to get there"
                    elif d > 0:
                        return str(((float(arg1)*-1)+math.sqrt(d))/(2*(float(arg2)/2))) + " s to get there or " + str(((float(arg1)*-1)-math.sqrt(d))/(2*(float(arg2)/2))) + " s"
                    elif d < 0:
                        return "unsolvable"
                elif arg3_unit == "s":
                    return str(float(arg2)*float(arg3)+float(arg1)) + " m/s fast"
            elif arg2_unit == "s":
                if arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    return str(float(arg3) * float(arg2) + float(arg1)) + " m/s fast"
                elif arg3_unit == "END- m/s":
                    return str((float(arg3) - float(arg1)) / float(arg2)) + u" m/s\N{SUPERSCRIPT TWO} in acceleration over " + str((float(arg3) + float(arg1)) / 2 * float(arg2)) + " m"
            elif arg2_unit == "m":
                if arg3_unit == "END- m/s":
                    return str((float(arg3) ** 2 - float(arg1) ** 2) / float(arg2) * 2) + u" m/s\N{SUPERSCRIPT TWO} in acceleration" # [UNIFORM ACCELERATION]
                if arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    d = float(arg1) ** 2 - 4 * (0.5 * float(arg3)) * (float(arg2) * -1)
                    if d == 0:
                        return str((float(arg1) * -1) / (2 * float(arg3))) + " s to get there"
                    elif d > 0:
                        return str(((float(arg1)*-1)+math.sqrt(d))/(2*(float(arg3)/2))) + " s to get there or " + str(((float(arg1)*-1)-math.sqrt(d))/(2*(float(arg3)/2))) + " s"
                    elif d < 0:
                        return "unsolvable"
        elif arg1_unit == "END- m/s":
            if arg2_unit == "START- m/s":
                if arg3_unit == "m":
                    return str((float(arg1) ** 2 - float(arg2) ** 2) / float(arg3) * 2) + u" m/s\N{SUPERSCRIPT TWO} in acceleration"
                elif arg3_unit == "s":
                    return str((float(arg1) - float(arg2)) / float(arg3)) + u" m/s\N{SUPERSCRIPT TWO} in acceleration over " + str((float(arg2) + float(arg1)) / 2 * float(arg3)) + " m"
                elif arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    return str((float(arg1) - float(arg2)) / float(arg3)) + " s to get that speed"
            elif arg2_unit == "m":
                if arg3_unit == "START- m/s":
                    return str((float(arg1) ** 2 - float(arg3) ** 2) / float(arg2) * 2) + u" m/s\N{SUPERSCRIPT TWO} in acceleration"
            elif arg2_unit == u"m/s\N{SUPERSCRIPT TWO}":
                if arg3_unit == "START- m/s":
                    return str((float(arg1) - float(arg3)) / float(arg2)) + " s to get that speed"
                elif arg3_unit == "s":
                    return str(float(arg1)-float(arg2)*float(arg3)) + " m/s fast at the start"
            elif arg2_unit == "s":
                if arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    return str(float(arg1)-float(arg3)*float(2)) + " m/s fast at the start"
                elif arg3_unit == "START- m/s":
                    return str((float(arg1) - float(arg3)) / float(arg2)) + u" m/s\N{SUPERSCRIPT TWO} in acceleration over " + str((float(arg3) + float(arg1)) / 2 * float(arg2)) + " m"
        elif arg1_unit == "m":
            if arg2_unit == "START- m/s":
                if arg3_unit == "END- m/s":
                    return str((float(arg3) ** 2 - float(arg2) ** 2) / float(arg1) * 2) + u" m/s\N{SUPERSCRIPT TWO} in acceleration"
                elif arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    d = float(arg2) ** 2 - 4 * (0.5 * float(arg3)) * (float(arg1) * -1)
                    if d == 0:
                        return str((float(arg2) * -1) / (2 * float(arg3))) + " s to get there"
                    elif d > 0:
                        return str(((float(arg2) * -1) + math.sqrt(d)) / (2 * (float(arg3) / 2))) + " s to get there or " + str(((float(arg2) * -1) - math.sqrt(d)) / (2 * (float(arg3) / 2))) + " s"
                    elif d < 0:
                        return "unsolvable"
            elif arg2_unit == "END- m/s":
                if arg3_unit == "START- m/s":
                    return str((float(arg2) ** 2 - float(arg3) ** 2) / float(arg1) * 2) + u" m/s\N{SUPERSCRIPT TWO} in acceleration"
            elif arg2_unit == u"m/s\N{SUPERSCRIPT TWO}":
                if arg3_unit == "START- m/s":
                    d = float(arg3) ** 2 - 4 * (0.5 * float(arg2)) * (float(arg1) * -1)
                    if d == 0:
                        return str((float(arg3) * -1) / (2 * float(arg2))) + " s to get there"
                    elif d > 0:
                        return str(((float(arg3) * -1) + math.sqrt(d)) / (2 * (float(arg2) / 2))) + " s to get there or " + str(((float(arg3) * -1) - math.sqrt(d)) / (2 * (float(arg2) / 2))) + " s"
                    elif d < 0:
                        return "unsolvable"
        elif arg1_unit == "s":
            if arg2_unit == u"m/s\N{SUPERSCRIPT TWO}":
                if arg3_unit == "START- m/s":
                    return str(float(arg2)*float(arg1)+float(arg3)) + " m/s fast"
                elif arg3_unit == "END- m/s":
                    return str(float(arg3)-float(arg2)*float(arg1)) + " m/s fast at the start"
            elif arg2_unit == "START- m/s":
                if arg3_unit == "END- m/s":
                    return str((float(arg3) - float(arg2)) / float(arg1)) + u" m/s\N{SUPERSCRIPT TWO} in acceleration over " + str((float(arg3) + float(arg2)) / 2 * float(arg1)) + " m"
                elif arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    return str(float(arg3) * float(arg1) + float(arg2)) + " m/s fast"
            elif arg2_unit == "END- m/s":
                if arg3_unit == "START- m/s":
                    return str((float(arg2) - float(arg3)) / float(arg1)) + u" m/s\N{SUPERSCRIPT TWO} in acceleration over " + str((float(arg2) + float(arg3)) / 2 * float(arg1)) + " m"
                elif arg3_unit == u"m/s\N{SUPERSCRIPT TWO}":
                    return str(float(arg2) - float(arg3) * float(arg1)) + " m/s fast at the start"





class Velocity:

    def calAngleforce(self, arg1, arg2, arg1_unit, arg2_unit):
        if arg1_unit == u"\N{DEGREE SIGN}":
            if arg2_unit == "F- N":
                return str(math.cos(math.radians(float(arg1)))*float(arg2)) + " N stong"
            elif arg2_unit == "Fy- N":
                return str(float(arg2)/math.cos(math.radians(float(arg1)))) + " N stong before the angle"
        elif arg1_unit == "F- N":
            if arg2_unit == u"\N{DEGREE SIGN}":
                return str(math.cos(math.radians(float(arg2)))*float(arg1)) + " N stong"
            elif arg2_unit == "Fy- N":
                return str(math.degrees(math.acos(float(arg2)/float(arg1)))) + u"\N{DEGREE SIGN} angled"
        elif arg1_unit == "Fy- N":
            if arg2_unit == "F- N":
                return str(math.degrees(math.acos(float(arg1)/float(arg2)))) + u"\N{DEGREE SIGN} angled"
            elif arg2_unit == u"\N{DEGREE SIGN}":
                return str(float(arg1)/math.cos(math.radians(float(arg2)))) + " N strong before the angle"

class Wave:

    def harmonic_Wave(self, arg1, arg2, arg1_unit, arg2_unit):
        if arg1_unit == "m/s":
            if arg2_unit == "Hz":
                return str(float(arg1)/float(arg2)) + " meter long wavelength and it's period -T- is " + str(1/float(arg2)) + " seconds"
            elif arg2_unit == "λ- m":
                return str(float(arg1)/float(arg2)) + " Hertz is the wave's frequency"
            elif arg2_unit == "s":
                return str(1/float(arg2)) + " Hertz is the frecuency and a wavelength of " + str(float(arg1)/(1/float(arg2))) + " meter"
        elif arg1_unit == "λ- m":
            if arg2_unit == "Hz":
                return str(float(arg1)*float(arg2)) + " m/s fast and a period -T- of " + str(1/float(arg2)) + " seconds"
            elif arg2_unit == "m/s":
                return str(float(arg2)/float(arg1)) + " Hertz is the wave and a period -T- of " + str(1/float(arg2)/float(arg1)) + " seconds"
            elif arg2_unit == "s":
                return str(1/float(arg2)) + " Hertz is the frequency and the speed is " + str((1/float(arg2))*float(arg1)) + " m/s"
        elif arg1_unit == "Hz":
            if arg2_unit == "λ- m":
                return str(float(arg2)*float(arg1)) + " m/s fast and a period -T- of " + str(1/float(arg1)) + " seconds"
            elif arg2_unit == "m/s":
                return str(float(arg2)/float(arg1)) + " meter long wavelength and it's period -T- is " + str(1/float(arg1)) + " seconds"
        elif arg1_unit == "s":
            if arg2_unit == "λ- m":
                return str(1/float(arg1)) + " Hertz is the frequency and the speed is " + str((1/float(arg1))*float(arg2)) + " m/s"
            elif arg2_unit == "m/s":
                return str(1/float(arg1)) + " Hertz is the frequency and a wavelength of " + str(float(arg2)/(1/float(arg1))) + " meter"
        

class Calculation:

    def thermodynamic_mix(self, num, **kwargs):

        equa_dict = dict()
        value_dict = dict()

        for numb in range(int(num)):
            equa_dict[str(numb)] = 1

        for i in kwargs:                                 # this loops sorts the values in to which part of the equations parts they represet
            for numb in range(int(num)):
                if i[-4:] == "unit":
                    if bool(str(numb) in str(kwargs[i].get())):
                        if bool("- Kg*J" in kwargs[i].get()) and bool("(MELT)" in kwargs[i].get()):
                            value_dict["MELT"+str(numb)] = float(kwargs["arg" + str(i[3:-5])].get())
                        elif bool("- Kg*J" in kwargs[i].get()) and bool("(VAPORISE)" in kwargs[i].get()):
                            value_dict["VAPORISE"+str(numb)] = float(kwargs["arg" + str(i[3:-5])].get())
                        elif bool("- Kg" in kwargs[i].get()):
                            equa_dict[str(numb)] *= float(kwargs["arg"+str(i[3:-5])].get())
                            value_dict["Kg"+str(numb)] = float(kwargs["arg" + str(i[3:-5])].get())
                        elif bool("- K" in kwargs[i].get()):
                            equa_dict[str(numb)] *= sympy.Symbol('X') - float(kwargs["arg"+str(i[3:-5])].get())-272.15
                            value_dict["DEGREE"+str(numb)] = float(kwargs["arg"+str(i[3:-5])].get())-272.15
                        elif bool("(SOLID)" in kwargs[i].get()):
                            value_dict["SOLID"+str(numb)] = float(kwargs["arg"+str(i[3:-5])].get())
                        elif bool("(LIQUID)" in kwargs[i].get()):
                            value_dict["LIQUID" + str(numb)] = float(kwargs["arg" + str(i[3:-5])].get())
                        elif bool("(GAS)" in kwargs[i].get()):
                            value_dict["GAS" + str(numb)] = float(kwargs["arg" + str(i[3:-5])].get())
                        elif bool("C" == kwargs[i].get()[-1]):
                            equa_dict[str(numb)] *= sympy.Symbol('X') - float(kwargs["arg" + str(i[3:-5])].get())
                            value_dict["DEGREE"+str(numb)] = float(kwargs["arg" + str(i[3:-5])].get())
                        elif bool("C (VAPORISE)" in kwargs[i].get()):
                            value_dict["DEGREE_VAPORISE"+str(numb)] = float(kwargs["arg" + str(i[3:-5])].get())
                        elif bool("C (MELT)" in kwargs[i].get()):
                            value_dict["DEGREE_MELT"+str(numb)] = float(kwargs["arg" + str(i[3:-5])].get())


        for numb in range(int(num)):             # checks which phase the substance is in
            if value_dict["DEGREE"+str(numb)] < value_dict["DEGREE_MELT"+str(numb)]:
                equa_dict[str(numb)] *= value_dict["SOLID"+str(numb)]
            elif value_dict["DEGREE_MELT"+str(numb)] <= value_dict["DEGREE"+str(numb)] < value_dict["DEGREE_VAPORISE"+str(numb)]:
                equa_dict[str(numb)] *= value_dict["LIQUID"+str(numb)]
            elif value_dict["DEGREE"+str(numb)] >= value_dict["DEGREE_VAPORISE"+str(numb)]:
                equa_dict[str(numb)] *= value_dict["GAS"+str(numb)]

        print(equa_dict)
        print(value_dict)

        equation = 0

        for i in equa_dict:        # this loop write an equation that can chenck which direction the temperature is going by an rough estimation of thw final temperature, this is though the wrong temperature and will be updated late now that it know whether the substance is being heated or cooled
#            if i == '0':
#                equation += equa_dict[i]*(int(num)-1)        # !!! I once wrote this but cant figure out why i wrote *(int(num)-1) the misteak seem too blatent to actualy be a misteak and thus i think it may have a purpose which i only knew of back then
#            else:
#                equation += equa_dict[i]
             equation += equa_dict[i]
        print(equation)
        end_temp = float(sympy.solve(equation, sympy.Symbol('X'))[0])
        print("end_temp done!")
        
        ref_point = end_temp    # this is used later on to check for invalidation

        # [CALCULATIONS FOR STATE TRANSFER STARTS HERE]

        # [BELOW TWO SECTION FINDS THE ORDER BY LOWEST MELT AND VAPORISE POINT]

        melt_list = [abs(value_dict["DEGREE_MELT0"] - end_temp)]
        melt_order = ['0']
        for numb in range(1, int(num)):
            melt_list_temp = melt_list[:]
            for i in melt_list_temp:
                if abs(value_dict["DEGREE_MELT"+str(numb)] - end_temp) <= i:
                    melt_list.insert(melt_list_temp.index(i), abs(value_dict["DEGREE_MELT"+str(numb)] - end_temp))
                    melt_order.insert(melt_list_temp.index(i), str(numb))
            if abs(value_dict["DEGREE_MELT"+str(numb)] - end_temp) > melt_list[-1]:
                melt_list.insert(-1, abs(value_dict["DEGREE_MELT"+str(numb)] - end_temp))
                melt_order.insert(-1, str(numb))

        vaporise_list = [abs(value_dict["VAPORISE0"] - end_temp)]
        vaporise_order = ['0']
        for numb in range(1, int(num)):
            vaporise_list_temp = vaporise_list[:]
            for i in vaporise_list_temp:
                if abs(value_dict["DEGREE_VAPORISE" + str(numb)] - end_temp) <= i:
                    vaporise_list.insert(vaporise_list_temp.index(i), abs(value_dict["DEGREE_VAPORISE" + str(numb)] - end_temp))
                    vaporise_order.insert(vaporise_list_temp.index(i), str(numb))
            if abs(value_dict["DEGREE_VAPORISE" + str(numb)] - end_temp) > melt_list[-1]:
                vaporise_list.insert(-1, abs(value_dict["DEGREE_VAPORISE" + str(numb)] - end_temp ))
                vaporise_order.insert(-1, str(numb))

        for melt_numb, vaporise_numb in itertools.zip_longest(melt_list, vaporise_list):
            if melt_numb != None and vaporise_numb != None:
                if melt_numb > vaporise_numb:
                    vaporise_list.insert(vaporise_list.index(vaporise_numb), None)
                elif melt_numb < vaporise_numb:
                    melt_list.insert(melt_list.index(melt_numb), None)

        print("list order done")

        crossed_release_dict = []
        crossed_absorb_dict = []

        for melt_numb,vaporise_numb in itertools.zip_longest(melt_order,vaporise_order):

            if melt_numb != None:
                print(sympy.solvers.solve(equation + value_dict["MELT"+str(melt_numb)] * value_dict["Kg"+str(melt_numb)], sympy.Symbol('X')))
                print(sympy.solvers.solve(equation - value_dict["MELT" + str(melt_numb)] * value_dict["Kg" + str(melt_numb)], sympy.Symbol('X')))
                if value_dict["DEGREE"+str(melt_numb)] > value_dict["DEGREE_MELT"+str(melt_numb)] > end_temp:
                    if value_dict["DEGREE_MELT"+str(melt_numb)] < sympy.solvers.solve(equation - value_dict["MELT"+str(melt_numb)] * value_dict["Kg"+str(melt_numb)], sympy.Symbol('X'))[0]:
                        # above checks if it has crossed back the melting point
                        energy_used = 0
                        energy_used -= value_dict["Kg" + str(melt_numb)] * value_dict["LIQUID" + str(melt_numb)] * (sympy.Symbol('X') - value_dict["DEGREE" + str(melt_numb)])
                        # ad energy the numb uses but temperature is now at melting point
                        energy_used -= value_dict["MELT" + str(melt_numb)] * value_dict["Kg" + str(melt_numb)]
                        # add energy used up to melt point
                        energy_used += value_dict["LIQUID" + str(melt_numb)] * value_dict["Kg" + str(melt_numb)] * (value_dict["DEGREE_MELT" + str(melt_numb)] - value_dict["DEGREE" + str(melt_numb)])
                        # remove the the the numb created
                        energy_used += value_dict["Kg" + str(melt_numb)] * value_dict["SOLID" + str(melt_numb)] * (sympy.Symbol('X') - value_dict["DEGREE_MELT" + str(melt_numb)])

                        crossed_release_dict.append([energy_used, value_dict["DEGREE_MELT" + str(melt_numb)], str(melt_numb)])
                        #return str(value_dict["DEGREE_MELT" + str(melt_numb)]) + u" C\N{DEGREE SIGN}"
                    else:
                        equation -= value_dict["Kg" + str(melt_numb)] * value_dict["LIQUID" + str(melt_numb)] * (sympy.Symbol('X') - value_dict["DEGREE" + str(melt_numb)])
                        # ad energy the numb uses but temperature is now at melting point
                        equation -= value_dict["MELT" + str(melt_numb)] * value_dict["Kg" + str(melt_numb)]
                        # add energy used up to melt point
                        equation += value_dict["LIQUID" + str(melt_numb)] * value_dict["Kg" + str(melt_numb)] * (value_dict["DEGREE_MELT" + str(melt_numb)] - value_dict["DEGREE" + str(melt_numb)])
                        # remove the the the numb created
                        equation += value_dict["Kg" + str(melt_numb)] * value_dict["SOLID" + str(melt_numb)] * (sympy.Symbol('X') - value_dict["DEGREE_MELT" + str(melt_numb)])
                        value_dict["DEGREE" + str(melt_numb)] = value_dict["DEGREE_MELT" + str(melt_numb)]
                        end_temp = float(sympy.solve(equation, sympy.Symbol('X'))[0])
                elif value_dict["DEGREE"+str(melt_numb)] < value_dict["DEGREE_MELT"+str(melt_numb)] < end_temp:
                    if value_dict["DEGREE_MELT"+str(melt_numb)] > sympy.solvers.solve(equation + value_dict["MELT"+str(melt_numb)] * value_dict["Kg"+str(melt_numb)], sympy.Symbol('X'))[0]:
                        energy_used = 0
                        energy_used -= value_dict["Kg" + str(melt_numb)] * value_dict["SOLID" + str(melt_numb)] * (sympy.Symbol('X') - value_dict["DEGREE" + str(melt_numb)])
                        # ad energy the numb uses but temperature is now at melting point
                        energy_used += value_dict["MELT" + str(melt_numb)] * value_dict["Kg" + str(melt_numb)]
                        # add energy used up to melt point
                        energy_used += value_dict["SOLID" + str(melt_numb)] * value_dict["Kg" + str(melt_numb)] * (value_dict["DEGREE_MELT" + str(melt_numb)] - value_dict["DEGREE" + str(melt_numb)])
                        # remove the the the numb created
                        energy_used += value_dict["Kg" + str(melt_numb)] * value_dict["LIQUID" + str(melt_numb)] * (sympy.Symbol('X') - value_dict["DEGREE_MELT" + str(melt_numb)])
                        # return str(value_dict["DEGREE_MELT" + str(melt_numb)]) + u" C\N{DEGREE SIGN}"

                        crossed_absorb_dict.append([energy_used, value_dict["DEGREE_MELT" + str(melt_numb)], str(melt_numb)])
                    else:
                        equation -= value_dict["Kg" + str(melt_numb)] * value_dict["SOLID" + str(melt_numb)] * (sympy.Symbol('X') - value_dict["DEGREE" + str(melt_numb)])
                        # ad energy the numb uses but temperature is now at melting point
                        equation += value_dict["MELT"+str(melt_numb)] * value_dict["Kg"+str(melt_numb)]
                        # add energy used up to melt point
                        equation += value_dict["SOLID"+str(melt_numb)]*value_dict["Kg"+str(melt_numb)]*(value_dict["DEGREE_MELT"+str(melt_numb)]-value_dict["DEGREE"+str(melt_numb)])
                        # remove the the the numb created
                        equation += value_dict["Kg"+str(melt_numb)] * value_dict["LIQUID"+str(melt_numb)] * (sympy.Symbol('X') - value_dict["DEGREE_MELT"+str(melt_numb)])
                        value_dict["DEGREE"+str(melt_numb)] = value_dict["DEGREE_MELT"+str(melt_numb)]
                        end_temp = float(sympy.solve(equation, sympy.Symbol('X'))[0])

            if vaporise_numb != None:
                print(sympy.solvers.solve(equation + value_dict["VAPORISE"+str(vaporise_numb)] * value_dict["Kg"+str(vaporise_numb)], sympy.Symbol('X')))
                print(sympy.solvers.solve(equation - value_dict["VAPORISE" + str(vaporise_numb)] * value_dict["Kg" + str(vaporise_numb)], sympy.Symbol('X')))
                if value_dict["DEGREE"+str(vaporise_numb)] > value_dict["DEGREE_VAPORISE"+str(vaporise_numb)] > end_temp:
                    if value_dict["DEGREE_VAPORISE"+str(vaporise_numb)] < sympy.solvers.solve(equation - value_dict["VAPORISE"+str(vaporise_numb)] * value_dict["Kg"+str(vaporise_numb)], sympy.Symbol('X'))[0]:
                        # above checks if it has crossed back the melting point
                        #return str(value_dict["DEGREE_VAPORISE" + str(vaporise_numb)]) + u" C\N{DEGREE SIGN}"
                        energy_used = 0
                        energy_used -= value_dict["Kg" + str(vaporise_numb)] * value_dict["GAS" + str(vaporise_numb)] * (sympy.Symbol('X') - value_dict["DEGREE" + str(vaporise_numb)])
                        # ad energy the numb uses but temperature is now at melting point
                        energy_used -= value_dict["VAPORISE" + str(vaporise_numb)] * value_dict["Kg" + str(vaporise_numb)]
                        # add energy used up to melt point
                        energy_used += value_dict["GAS" + str(vaporise_numb)] * value_dict["Kg" + str(vaporise_numb)] * (value_dict["DEGREE_VAPORISE" + str(vaporise_numb)] - value_dict["DEGREE" + str(vaporise_numb)])
                        # remove the the the numb created
                        energy_used += value_dict["Kg" + str(vaporise_numb)] * value_dict["LIQUID" + str(vaporise_numb)] * (sympy.Symbol('X') - value_dict["DEGREE_VAPORISE" + str(vaporise_numb)])

                        crossed_release_dict.append([energy_used, value_dict["DEGREE_VAPORISE" + str(vaporise_numb)], str(vaporise_numb)])
                    else:
                        equation -= value_dict["Kg" + str(vaporise_numb)] * value_dict["GAS" + str(vaporise_numb)] * (sympy.Symbol('X') - value_dict["DEGREE" + str(vaporise_numb)])
                        # ad energy the numb uses but temperature is now at melting point
                        equation -= value_dict["VAPORISE" + str(vaporise_numb)] * value_dict["Kg" + str(vaporise_numb)]
                        # add energy used up to melt point
                        equation += value_dict["GAS" + str(vaporise_numb)] * value_dict["Kg" + str(vaporise_numb)] * (value_dict["DEGREE_VAPORISE" + str(vaporise_numb)] - value_dict["DEGREE" + str(vaporise_numb)])
                        # remove the the the numb created
                        equation += value_dict["Kg" + str(vaporise_numb)] * value_dict["LIQUID" + str(vaporise_numb)] * (sympy.Symbol('X') - value_dict["DEGREE_VAPORISE" + str(vaporise_numb)])
                        value_dict["DEGREE" + str(vaporise_numb)] = value_dict["DEGREE_VAPORISE" + str(vaporise_numb)]
                        end_temp = float(sympy.solve(equation, sympy.Symbol('X'))[0])
                elif value_dict["DEGREE"+str(vaporise_numb)] < value_dict["DEGREE_VAPORISE"+str(vaporise_numb)] < end_temp:
                    if value_dict["DEGREE_VAPORISE"+str(vaporise_numb)] > sympy.solvers.solve(equation + value_dict["VAPORISE"+str(vaporise_numb)] * value_dict["Kg"+str(vaporise_numb)], sympy.Symbol('X'))[0]:
                        #return str(value_dict["DEGREE_VAPORISE" + str(vaporise_numb)]) + u" C\N{DEGREE SIGN}"
                        energy_used = 0
                        energy_used -= value_dict["Kg" + str(vaporise_numb)] * value_dict["LIQUID" + str(vaporise_numb)] * (sympy.Symbol('X') - value_dict["DEGREE" + str(vaporise_numb)])
                        # ad energy the numb uses but temperature is now at melting point
                        energy_used += value_dict["VAPORISE" + str(vaporise_numb)] * value_dict["Kg" + str(vaporise_numb)]
                        # add energy used up to melt point
                        energy_used += value_dict["LIQUID" + str(vaporise_numb)] * value_dict["Kg" + str(vaporise_numb)] * (value_dict["DEGREE_VAPORISE" + str(vaporise_numb)] - value_dict["DEGREE" + str(vaporise_numb)])
                        # remove the the the numb created
                        energy_used += value_dict["Kg" + str(vaporise_numb)] * value_dict["GAS" + str(vaporise_numb)] * (sympy.Symbol('X') - value_dict["DEGREE_VAPORISE" + str(vaporise_numb)])

                        crossed_absorb_dict.append([energy_used, value_dict["DEGREE_VAPORISE" + str(vaporise_numb)], str(vaporise_numb)])
                    else:
                        equation -= value_dict["Kg" + str(vaporise_numb)] * value_dict["LIQUID" + str(vaporise_numb)] * (sympy.Symbol('X') - value_dict["DEGREE" + str(vaporise_numb)])
                        # ad energy the numb uses but temperature is now at melting point
                        equation += value_dict["VAPORISE"+str(vaporise_numb)] * value_dict["Kg"+str(vaporise_numb)]
                        # add energy used up to melt point
                        equation += value_dict["LIQUID"+str(vaporise_numb)]*value_dict["Kg"+str(vaporise_numb)]*(value_dict["DEGREE_VAPORISE"+str(vaporise_numb)]-value_dict["DEGREE"+str(vaporise_numb)])
                        # remove the the the numb created
                        equation += value_dict["Kg"+str(vaporise_numb)] * value_dict["GAS"+str(vaporise_numb)] * (sympy.Symbol('X') - value_dict["DEGREE_VAPORISE"+str(vaporise_numb)])
                        value_dict["DEGREE"+str(vaporise_numb)] = value_dict["DEGREE_VAPORISE"+str(vaporise_numb)]
                        end_temp = float(sympy.solve(equation, sympy.Symbol('X'))[0])

            if len(crossed_release_dict) > 0 and len(crossed_absorb_dict) > 0:
                equation += crossed_release_dict[0][0]
                value_dict["DEGREE" + crossed_release_dict[0][2]] = crossed_release_dict[0][1]
                equation += crossed_absorb_dict[0][0]
                value_dict["DEGREE" + crossed_absorb_dict[0][2]] = crossed_absorb_dict[0][1]
                end_temp = float(sympy.solve(equation, sympy.Symbol('X'))[0])
                if end_temp > crossed_absorb_dict[0][1] > crossed_release_dict[0][1] or end_temp < crossed_absorb_dict[0][1] < crossed_release_dict[0][1]:
                    equation -= crossed_absorb_dict[0][0]
                    del (crossed_release_dict[0])
                elif end_temp > crossed_release_dict[0][1] > crossed_absorb_dict[0][1] or end_temp < crossed_release_dict[0][1] < crossed_absorb_dict[0][1]:
                    equation -= crossed_release_dict[0][0]
                    del (crossed_absorb_dict[0])

        print("melt and vaporise calculations done")
        print(sympy.solvers.solve(equation, sympy.Symbol('X')))
            

        if len(crossed_release_dict) == 0 and len(crossed_absorb_dict) == 0:
            return str(sympy.solvers.solve(equation, sympy.Symbol('X'))[0]) + u" C\N{DEGREE SIGN}"
        elif len(crossed_release_dict) == 0:
            return str(crossed_absorb_dict[0][1]) + u" C\N{DEGREE SIGN}"
        elif len(crossed_absorb_dict) == 0:
            return str(crossed_release_dict[0][1]) + u" C\N{DEGREE SIGN}"
"""
    i dont beleive this can calculate more than 2 substances if there is a phase transition which swap the directions of one of the substances is going (the middle ones) due to them by first estimation for exsample maybe
    being cooled but because of the hottes object's huge phase transition energy taking up so much energy that both of the two other now go get hotter instead og just the coldest, this is a problem that seem problematic
    because of this the result should be taken with a gram of salt. a check how ever can be made. That said if all the substances are the same and in the same phase then no problems can ocure. The only problems here that
    can happen are related to the transition bettween phases with more than 2 subtances pressent.
            
"""            
    
def stuffconsentration_cal(arg1, arg2, arg3, arg_unit1, arg_unit2, arg_unit3):

    arg1, arg2, arg3 = float(arg1), float(arg2), float(arg3)

    coff0, coff1, M0, M1, mL0, mL1 = sympy.symbol.Symbol('X'), sympy.symbol.Symbol('X'), sympy.symbol.Symbol('X'), sympy.symbol.Symbol('X'), sympy.symbol.Symbol('X'), sympy.symbol.Symbol('X')

    if arg_unit1 == "coff0":
        coff0 = arg1
    elif arg_unit2 == "coff0":
        coff0 = arg2
    elif arg_unit3 == "coff0":
        coff0 = arg3
    if arg_unit1 == "M0":
        M0 = arg1
    elif arg_unit2 == "M0":
        M0 = arg2
    elif arg_unit3 == "M0":
        M0 = arg3
    if arg_unit1 == "mL0":
        mL0 = arg1
    elif arg_unit2 == "mL0":
        mL0 = arg2
    elif arg_unit3 == "mL0":
        mL0 = arg3
    if arg_unit1 == "coff1":
        coff1 = arg1
    elif arg_unit2 == "coff1":
        coff1 = arg2
    elif arg_unit3 == "coff1":
        coff1 = arg3
    if arg_unit1 == "M1":
        M0 = arg1
    elif arg_unit2 == "M1":
        M1 = arg2
    elif arg_unit3 == "M1":
        M1 = arg3
    if arg_unit1 == "mL1":
        mL1 = arg1
    elif arg_unit2 == "mL1":
        mL1 = arg2
    elif arg_unit3 == "mL1":
        mL1 = arg3

    return sympy.solvers.solve(M0*mL0*coff0-M1*mL1*coff1, sympy.symbol.Symbol('X'))[0]