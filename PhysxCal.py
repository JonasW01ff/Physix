import tkinter as tk, PhysxSpeed, PhysxImg
from PIL import ImageTk, Image

class Main:

    def mainFrame(self):

        def Physics():
            print('[Physics Activated]')
            widget.pack_forget()
            widget1.pack_forget()
            label.pack_forget()

            def show_speed():
                global labelspe
                global widget_accspeed
                global widget_conspeed
                label_conspe.pack_forget()
                widget_speed.pack_forget()
                widget_velocity.pack_forget()
                widget_heat.pack_forget()
                widget_wave.pack_forget()
                widget_radioactivity.pack_forget()
                labelspe = tk.Label(top, text='What instance?')
                labelspe.pack()
                widget_conspeed = tk.Button(top, text='Constant speed', command=show_conspeed)
                widget_accspeed = tk.Button(top, text='Accelerating speed', command=show_accspeed)
                widget_conspeed.pack()
                widget_accspeed.pack()

            def show_conspeed():
                widget_conspeed.pack_forget()
                widget_accspeed.pack_forget()
                labelspe.pack_forget()
                label = tk.Label(top, text='What are the values?')
                label.pack()
                arg1_unit = tk.StringVar()
                arg2_unit = tk.StringVar()
                arg1 = tk.Entry(top)
                arg2 = tk.Entry(top)
                arg_menu1 = tk.OptionMenu(top, arg1_unit, 's', 'm', 'm/s', 'Kg', 'J')
                arg_menu2 = tk.OptionMenu(top, arg2_unit, 's', 'm', 'm/s', 'Kg', 'J')
                arg1.pack(side='top')
                arg_menu1.pack(side='top')
                arg_menu2.pack(side='bottom')
                arg2.pack(side='bottom')

                def done():
                    label.pack_forget()
                    arg1.pack_forget()
                    arg2.pack_forget()
                    arg_menu1.pack_forget()
                    arg_menu2.pack_forget()
                    doneB.pack_forget()
                    done_label = tk.Label(top, text='It is ' + str(PhysxSpeed.Speed.calSpeed(0, arg1.get(), arg2.get(), arg1_unit.get(), arg2_unit.get())))
                    done_label.pack()

                doneB = tk.Button(top, text='Done', command=done)
                doneB.pack(side='bottom')

            def show_accspeed():
                widget_conspeed.pack_forget()
                widget_accspeed.pack_forget()
                labelspe.pack_forget()
                label = tk.Label(top, text='What are the values?')
                label.pack()
                arg1_unit = tk.StringVar()
                arg2_unit = tk.StringVar()
                arg3_unit = tk.StringVar()
                arg1 = tk.Entry(top)
                arg2 = tk.Entry(top)
                arg3 = tk.Entry(top)
                arg_menu1 = tk.OptionMenu(top, arg1_unit, 's', 'm', 'N', 'Kg', 'm/s²', 'START- m/s', 'END- m/s')
                arg_menu2 = tk.OptionMenu(top, arg2_unit, 's', 'm', 'N', 'Kg', 'm/s²', 'START- m/s', 'END- m/s')
                arg_menu3 = tk.OptionMenu(top, arg3_unit, 's', 'm', 'N', 'Kg', 'm/s²', 'START- m/s', 'END- m/s')
                arg1.pack(side='top')
                arg_menu1.pack(side='top')
                arg_menu3.pack(side='bottom')
                arg3.pack(side='bottom')
                arg_menu2.pack(side='bottom')
                arg2.pack(side='bottom')

                def acc_done():
                    label.pack_forget()
                    arg1.pack_forget()
                    arg2.pack_forget()
                    arg3.pack_forget()
                    arg_menu1.pack_forget()
                    arg_menu2.pack_forget()
                    arg_menu3.pack_forget()
                    doneC.pack_forget()
                    done_label = tk.Label(top, text='It is ' + str(PhysxSpeed.Speed.calAccel(0, arg1.get(), arg2.get(), arg3.get(), arg1_unit.get(), arg2_unit.get(), arg3_unit.get())))
                    done_label.pack()

                doneC = tk.Button(top, text='Done', command=acc_done)
                doneC.pack(side='bottom')

            def show_vel():
                label_conspe.pack_forget()
                widget_speed.pack_forget()
                widget_velocity.pack_forget()
                widget_heat.pack_forget()
                widget_wave.pack_forget()
                widget_radioactivity.pack_forget()

                def force_angle():
                    vel_label.pack_forget()
                    widget_fall.pack_forget()
                    label = tk.Label(top, text='What are the values?')
                    label.pack()
                    arg1_unit = tk.StringVar()
                    arg2_unit = tk.StringVar()
                    arg1 = tk.Entry(top)
                    arg2 = tk.Entry(top)
                    arg_menu1 = tk.OptionMenu(top, arg1_unit, 'F- N', '°', 'Fy- N')
                    arg_menu2 = tk.OptionMenu(top, arg2_unit, 'F- N', '°', 'Fy- N')
                    arg1.pack(side='top')
                    arg_menu1.pack(side='top')
                    arg_menu2.pack(side='bottom')
                    arg2.pack(side='bottom')

                    def done_forceangle():
                        label.pack_forget()
                        arg1.pack_forget()
                        arg2.pack_forget()
                        arg_menu1.pack_forget()
                        arg_menu2.pack_forget()
                        doneB.pack_forget()
                        done_label = tk.Label(top, text='It is ' + str(PhysxSpeed.Velocity.calAngleforce(0, arg1.get(), arg2.get(), arg1_unit.get(), arg2_unit.get())))
                        done_label.pack()

                    doneB = tk.Button(top, text='Done', command=done_forceangle)
                    doneB.pack(side='bottom')

                vel_label = tk.Label(top, text='Choose the instance')
                vel_label.pack()
                widget_fall = tk.Button(top, text='Force at en angel', command=force_angle)
                widget_fall.pack()

            def show_heat():
                label_conspe.pack_forget()
                widget_speed.pack_forget()
                widget_velocity.pack_forget()
                widget_heat.pack_forget()
                widget_wave.pack_forget()
                widget_radioactivity.pack_forget()

                def mix_sub():
                    vel_label.pack_forget()
                    widget_mixture.pack_forget()
                    mix_label = tk.Label(top, text='How many substances')
                    mix_label.pack()
                    arg1_mix = tk.Entry(top)
                    arg1_mix.pack()

                    def mix_sub_val():
                        background_label.place_forget()
                        C.pack_forget()
                        mix_label.pack_forget()
                        arg1_mix.pack_forget()
                        doneA.pack_forget()
                        mixsub_label = tk.Label(top, text='What are the values?')
                        mixsub_label.pack()
                        unit_list = []
                        frame_value = top
                        for i in range(int(arg1_mix.get())):
                            unit_list.append('CUSTOM' + str(i) + '- Kg')
                            unit_list.append('CUSTOM' + str(i) + '- J*Kg⁻¹*K⁻¹(SOLID)')
                            unit_list.append('CUSTOM' + str(i) + '- J*Kg⁻¹*K⁻¹(LIQUID)')
                            unit_list.append('CUSTOM' + str(i) + '- J*Kg⁻¹*K⁻¹(GAS)')
                            unit_list.append('CUSTOM' + str(i) + '- K')
                            unit_list.append('CUSTOM' + str(i) + '- °C')
                            unit_list.append('CUSTOM' + str(i) + '- Kg*J⁻¹(MELT)')
                            unit_list.append('CUSTOM' + str(i) + '- Kg*J⁻¹(VAPORISE)')
                            unit_list.append('CUSTOM' + str(i) + '- °C (VAPORISE)')
                            unit_list.append('CUSTOM' + str(i) + '- °C (MELT)')

                        dict_mix = dict()
                        dict_mix['arg' + str(int(arg1_mix.get()) * 9 - 2) + '_unit'] = tk.StringVar()
                        dict_mix['arg' + str(int(arg1_mix.get()) * 9 - 1) + '_unit'] = tk.StringVar()
                        dict_mix['arg' + str(int(arg1_mix.get()) * 9 - 2)] = tk.Entry(frame_value)
                        dict_mix['arg' + str(int(arg1_mix.get()) * 9 - 1)] = tk.Entry(frame_value)
                        dict_mix['arg_menu' + str(int(arg1_mix.get()) * 9 - 2)] = tk.OptionMenu(frame_value, dict_mix['arg' + str(int(arg1_mix.get()) * 9 - 2) + '_unit'], *unit_list)
                        dict_mix['arg_menu' + str(int(arg1_mix.get()) * 9 - 1)] = tk.OptionMenu(frame_value, dict_mix['arg' + str(int(arg1_mix.get()) * 9 - 1) + '_unit'], *unit_list)
                        dict_mix['arg' + str(int(arg1_mix.get()) * 9 - 2)].pack(side='top')
                        dict_mix['arg_menu' + str(int(arg1_mix.get()) * 9 - 2)].pack(side='top')
                        dict_mix['arg_menu' + str(int(arg1_mix.get()) * 9 - 1)].pack(side='bottom')
                        dict_mix['arg' + str(int(arg1_mix.get()) * 9 - 1)].pack(side='bottom')
                        for num in range(int(arg1_mix.get()) * 9 - 2):
                            dict_mix['arg' + str(int(num)) + '_unit'] = tk.StringVar()
                            dict_mix['arg' + str(num)] = tk.Entry(frame_value)
                            dict_mix['arg_menu' + str(num)] = tk.OptionMenu(frame_value, dict_mix['arg' + str(int(num)) + '_unit'], *unit_list)
                            dict_mix['arg_menu' + str(num)].pack(side='bottom')
                            dict_mix['arg' + str(num)].pack(side='bottom')
                            countq = 1
                            window_dict = dict()
                            if num == 18:
                                top.pack(side='left')
                            if num % 18 == 0:
                                window_dict['window' + str(countq)] = tk.Frame()
                                window_dict['window' + str(countq)].pack(side='left')
                                frame_value = window_dict['window' + str(countq)]
                                countq += 1

                        def done_mix():
                            mixsub_label.pack_forget()
                            doneB.pack_forget()
                            for num1 in range(int(arg1_mix.get()) * 9):
                                dict_mix['arg_menu' + str(num1)].pack_forget()
                                dict_mix['arg' + str(num1)].pack_forget()

                            done_label = tk.Label(top, text='It is ' + str(PhysxSpeed.Calculation.thermodynamic_mix(0, arg1_mix.get(), **dict_mix)))
                            done_label.pack()

                        doneB = tk.Button(top, text='Done', command=done_mix)
                        doneB.pack(side='bottom')

                    doneA = tk.Button(top, text='Done', command=mix_sub_val)
                    doneA.pack()

                vel_label = tk.Label(top, text='Choose the instance')
                vel_label.pack()
                widget_mixture = tk.Button(top, text='Mixing substances', command=mix_sub)
                widget_mixture.pack()

            def show_wave():
                label_conspe.pack_forget()
                widget_speed.pack_forget()
                widget_velocity.pack_forget()
                widget_heat.pack_forget()
                widget_wave.pack_forget()
                widget_radioactivity.pack_forget()

                def harmonic_wave():
                    vel_label.pack_forget()
                    widget_harm.pack_forget()
                    label = tk.Label(top, text='What are the values?')
                    label.pack()
                    arg1_unit = tk.StringVar()
                    arg2_unit = tk.StringVar()
                    arg1 = tk.Entry(top)
                    arg2 = tk.Entry(top)
                    arg_menu1 = tk.OptionMenu(top, arg1_unit, 'Hz', 's', 'm/s', 'λ- m')
                    arg_menu2 = tk.OptionMenu(top, arg2_unit, 'Hz', 's', 'm/s', 'λ- m')
                    arg1.pack(side='top')
                    arg_menu1.pack(side='top')
                    arg_menu2.pack(side='bottom')
                    arg2.pack(side='bottom')

                    def done_harmonic_wave():
                        label.pack_forget()
                        arg1.pack_forget()
                        arg2.pack_forget()
                        arg_menu1.pack_forget()
                        arg_menu2.pack_forget()
                        doneB.pack_forget()
                        done_label = tk.Label(top, text=str(PhysxSpeed.Wave.harmonic_Wave(0, arg1.get(), arg2.get(), arg1_unit.get(), arg2_unit.get())))
                        done_label.pack()

                    doneB = tk.Button(top, text='Done', command=done_harmonic_wave)
                    doneB.pack(side='bottom')

                vel_label = tk.Label(top, text='Choose the instance')
                vel_label.pack()
                widget_harm = tk.Button(top, text='Harmonic wave', command=harmonic_wave)
                widget_harm.pack()

            def show_radioactivity():
                label_conspe.pack_forget()
                widget_speed.pack_forget()
                widget_velocity.pack_forget()
                widget_heat.pack_forget()
                widget_wave.pack_forget()
                widget_radioactivity.pack_forget()

                def radioactive_decay():
                    vel_label.pack_forget()
                    widget_radioact.pack_forget()
                    label = tk.Label(top, text='What are the values?')
                    label.pack()
                    arg1_unit = tk.StringVar()
                    arg2_unit = tk.StringVar()
                    arg1 = tk.Entry(top)
                    arg2 = tk.Entry(top)
                    arg_menu1 = tk.OptionMenu(top, arg1_unit, 'N', 'No', 'k', 't')
                    arg_menu2 = tk.OptionMenu(top, arg2_unit, 'N', 'No', 'k', 't')
                    arg1.pack(side='top')
                    arg_menu1.pack(side='top')
                    arg_menu2.pack(side='bottom')
                    arg2.pack(side='bottom')

                    def done_radioactive_decay():
                        label.pack_forget()
                        arg1.pack_forget()
                        arg2.pack_forget()
                        arg_menu1.pack_forget()
                        arg_menu2.pack_forget()
                        doneB.pack_forget()
                        done_label = tk.Label(top, text=str(PhysxSpeed.Wave.harmonic_Wave(0, arg1.get(), arg2.get(), arg1_unit.get(), arg2_unit.get())))
                        done_label.pack()

                    doneB = tk.Button(top, text='Done', command=done_radioactive_decay)
                    doneB.pack(side='bottom')

                vel_label = tk.Label(top, text='Choose the instance')
                vel_label.pack()
                widget_radioact = tk.Button(top, text='Radioactive decay', command=radioactive_decay)
                widget_radioact.pack()

            widget_speed = tk.Button(top, text='Speed', command=show_speed)
            widget_velocity = tk.Button(top, text='Velocity', command=show_vel)
            widget_heat = tk.Button(top, text='Thermodynamics', command=show_heat)
            widget_wave = tk.Button(top, text='Waves', command=show_wave)
            widget_radioactivity = tk.Button(top, text='Radioactivity', command=show_radioactivity)
            label_conspe = tk.Label(top, text='Choose the instance')
            label_conspe.pack()
            widget_speed.pack()
            widget_velocity.pack()
            widget_heat.pack()
            widget_wave.pack()
            widget_radioactivity.pack()

        def Chemisrtry():
            print('[CHEMISTRY ACTIVATED]')
            widget.pack_forget()
            widget1.pack_forget()
            label.pack_forget()

            def stuf_concentration():
                label_chemistry.pack_forget()
                widget_stuffconsentration.pack_forget()
                label_stuffconcentration = tk.Label(top, text='What are the values')
                label_stuffconcentration.pack()
                arg1_unit = tk.StringVar()
                arg2_unit = tk.StringVar()
                arg3_unit = tk.StringVar()
                arg4_unit = tk.StringVar()
                arg5_unit = tk.StringVar()
                arg1 = tk.Entry(top)
                arg2 = tk.Entry(top)
                arg3 = tk.Entry(top)
                arg4 = tk.Entry(top)
                arg5 = tk.Entry(top)
                arg_menu1 = tk.OptionMenu(top, arg1_unit, 'M0', 'mL0', 'coff0', 'M1', 'mL1', 'coff1')
                arg_menu2 = tk.OptionMenu(top, arg2_unit, 'M0', 'mL0', 'coff0', 'M1', 'mL1', 'coff1')
                arg_menu3 = tk.OptionMenu(top, arg3_unit, 'M0', 'mL0', 'coff0', 'M1', 'mL1', 'coff1')
                arg_menu4 = tk.OptionMenu(top, arg4_unit, 'M0', 'mL0', 'coff0', 'M1', 'mL1', 'coff1')
                arg_menu5 = tk.OptionMenu(top, arg5_unit, 'M0', 'mL0', 'coff0', 'M1', 'mL1', 'coff1')
                arg1.pack(side='top')
                arg_menu1.pack(side='top')
                arg_menu5.pack(side='bottom')
                arg5.pack(side='bottom')
                arg_menu4.pack(side='bottom')
                arg4.pack(side='bottom')
                arg_menu3.pack(side='bottom')
                arg3.pack(side='bottom')
                arg_menu2.pack(side='bottom')
                arg2.pack(side='bottom')

                def done_forceangle():
                    label_stuffconcentration.pack_forget()
                    arg1.pack_forget()
                    arg2.pack_forget()
                    arg3.pack_forget()
                    arg4.pack_forget()
                    arg5.pack_forget()
                    arg_menu1.pack_forget()
                    arg_menu2.pack_forget()
                    arg_menu3.pack_forget()
                    arg_menu4.pack_forget()
                    arg_menu5.pack_forget()
                    doneB.pack_forget()
                    done_label = tk.Label(top, text='It is ' + str(PhysxSpeed.stuffconsentration_cal(arg1.get(), arg2.get(), arg3.get(), arg1_unit.get(), arg2_unit.get(), arg3_unit.get())))
                    done_label.pack()

                doneB = tk.Button(top, text='Done', command=done_forceangle)
                doneB.pack(side='bottom')

            label_chemistry = tk.Label(top, text='Choose instance')
            label_chemistry.pack()
            widget_stuffconsentration = tk.Button(top, text='Stuff conentration', command=stuf_concentration)
            widget_stuffconsentration.pack()

        top = tk.Frame()
        top.pack()
        C = tk.Canvas(top, bg='blue', height=0, width=200)
        filename = tk.PhotoImage(file='C:\\Users\\Jonas\\code\\imageToSave1.png')
        background_label = tk.Label(top, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        label = tk.Label(top, text='Choose a subject')
        label.pack()
        widget = tk.Button(top, text='Physics', command=Physics)
        widget1 = tk.Button(top, text='Chemistry', command=Chemisrtry)
        widget.pack()
        widget1.pack()
        top.mainloop()
